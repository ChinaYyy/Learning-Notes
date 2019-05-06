# MongoEngine

## QuerySet

### Query

- Raw query `__raw__`

    `Page.objects(__raw__={'tags': 'coding'})`

- Projection 获取部分字段数据， `only`, `exclude`

    ```python
    Film.objects.only('title', 'date').first()
    Film.objects.exclude('title', 'date').first()
    ```

- Advanced queries, `and`, `or`

    ```python
    from mongoengine.queryset.visitor import Q

    # Get published posts
    Post.objects(Q(published=True) | Q(publish_date__lte=datetime.now()))

    # Get top posts
    Post.objects((Q(featured=True) & Q(hits__gte=1000)) | Q(hits__gte=5000))
    ```

- EmbededDocument 使用双下划线 `__`

    `uk_pages = Page.objects(author__country='uk')`

- Retrieving unique results 使用 `get()`

    raise `DoesNotExist` or `MultipleObjectsReturned`

- like objects

    ```python
    class BlogPost(Document):
    title = StringField()
    published = BooleanField()

    @queryset_manager
    def live_posts(doc_cls, queryset):
        return queryset.filter(published=True)

    BlogPost(title='test1', published=False).save()
    BlogPost(title='test2', published=True).save()
    assert len(BlogPost.objects) == 2
    assert len(BlogPost.live_posts()) == 1
    ```

- `no_dereference` 不提取引用数据

    ```python
    post = Post.objects.no_dereference().first()
    assert(isinstance(post.author, DBRef))

    with no_dereference(Post) as Post:
        post = Post.objects.first()
        assert(isinstance(post.author, DBRef))
    # Outside the context manager dereferencing occurs.
    assert(isinstance(post.author, User))

    ```

- DatetimeField Query

    ```python
    User.objects(Q(c_time__gt=datetime.datetime(2019, 5, 6)) & Q(c_time__lt=datetime.datetime(2019, 5, 7))).first()
    ```

### Aggregation

- item_frequencies

    ```python
    class Article(Document):
    tag = ListField(StringField())

    # After adding some tagged articles...
    tag_freqs = Article.objects.item_frequencies('tag', normalize=True)

    from operator import itemgetter
    top_tags = sorted(tag_freqs.items(), key=itemgetter(1), reverse=True)[:10]
    ```

## Functions

- [Pre save data validation and cleaning](http://docs.mongoengine.org/guide/document-instances.html#pre-save-data-validation-and-cleaning)

    ```python
    class Essay(Document):
    status = StringField(choices=('Published', 'Draft'), required=True)
    pub_date = DateTimeField()

    def clean(self):
        """Ensures that only published essays have a `pub_date` and
        automatically sets `pub_date` if essay is published and `pub_date`
        is not set"""
        if self.status == 'Draft' and self.pub_date is not None:
            msg = 'Draft entries should not have a publication date.'
            raise ValidationError(msg)
        # Set the pub_date for published items if not set.
        if self.status == 'Published' and self.pub_date is None:
            self.pub_date = datetime.now()
    ```

- [ManageContext](http://docs.mongoengine.org/guide/connecting.html#context-managers) 切换col， db

    ```python
    from mongoengine.context_managers import switch_db

    class User(Document):
        name = StringField()

        meta = {'db_alias': 'user-db'}

    with switch_db(User, 'archive-user-db') as User:
        User(name='Ross').save()  # Saves the 'archive-user-db'

    with switch_collection(User, 'user2000') as User:
        User(name='hello Group 2000 collection!').save()  # Saves in user2000 collection
    ```

## Errors

- validate:

    save保存时， 引用的数据不存在时 `mongoengine.errors.ValidationError`

    ```plain
    mongoengine.errors.ValidationError: ValidationError (Car:None) (value should be `User` document, LazyReference or DBRef on `User` or `User`'s primary key (i.e. `ObjectIdField`): ['user'])
    ```

## Intention

- Validation

    只有在save时，会进行validate， 不通过报错`ValidationError`； 取数据model.objects不会进行验证。

- model定义的额外字段

    当mongodb保存的model有额外字段时， 保存时额外字段会丢弃； 取数据时，model.objects会报错`FieldDoesNotExist`。

    解决办法：
        1. 使用`DynamicDocument`, 这样可以保存额外的字段
        2. 单纯解决取数据，有额外字段报错问题，可以`meta = {'strict': False}`

- DatetimeField 时区问题

    1. mongodb保存在数据库里为UTC时间， 所以定义的时候`DateTimeField(default=datetime.datetime.utcnow)`
    2. 取数据的时候为了保证取出来的数据，是带0时区的， 在连接时需要指定tz_aware=True, `connect('tumblelog', tz_aware=True)`
    3. 需要自行转换

- ReferenceField 保存时， 只能引用已保存过的文档

    `mongoengine.errors.ValidationError: ValidationError (Post.TextPost:None) (You can only reference documents once they have been saved to the database: ['author'])`

## Question

[reverse_delete_rule](http://docs.mongoengine.org/tutorial.html#handling-deletions-of-references)