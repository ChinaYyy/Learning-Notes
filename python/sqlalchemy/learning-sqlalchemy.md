# Learning Sqlalchemy

## Operate

#### Update

``` python
session.query(User).filter(User.id == 25).update({'password': 'pppp'})
```

## Code

model

```python
def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Base = declarative_base()
Base.to_dict = to_dict
```

