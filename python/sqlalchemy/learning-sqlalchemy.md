# Learning Sqlalchemy

## Operate

#### Update

``` python
session.query(User).filter(User.id == 25).update({'password': 'pppp'})
```



