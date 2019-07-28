# Aggregation

## Distinct

```mongodb
db.singer_metadata.distinct('source')
```

## Groupby Count

```mongodb
db.singer_metadata.aggregate([
    {"$group" : {_id:"$source", count:{$sum:1}}}
])
```

## Random Select

```mongodb
db.mycoll.aggregate([{ $sample: { size: 1 } }])
```

## Foreign Association

```mongodb
pipeline = [
    {'$match': where},
    {'$skip': skip},
    {'$limit': limit},
    {"$lookup": {
        "localField": "task_id",
        "from": "task",
        "foreignField": "task_id",
        "as": "task"
    }},
    {'$unwind': '$task'},
    {'$project': {
        '_id': 0,
        'origin_insert_time': 0,
        'task._id': 0,
        'task.task_log': 0,
        'log': 0
    }},
]
data = self.db[module].aggregate(pipeline=pipeline)
```
