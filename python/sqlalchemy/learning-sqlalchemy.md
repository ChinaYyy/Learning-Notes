# Learning Sqlalchemy

## Base Code

```python
from sqlalchemy import Column, String, Integer, Float, Text, TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER, FLOAT, BIGINT, DECIMAL, TEXT, DATETIME
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


def to_json_dict(self):
    # 将数据转化为可json化的数据
    data = to_dict(self)
    for k, v in data.items():
        data[k] = v
    return data


Base = declarative_base()
Base.to_dict = to_dict
Base.to_json_dict = to_json_dict


mysl_dialect_object = mysql.dialect()


def query_to_sql(query, dialect=mysl_dialect_object):
    sql = query.statement.compile(dialect=dialect, compile_kwargs={"literal_binds": True})
    return str(sql)
```

## Operate

### Query

- is not `session.query(User).filter(User.id.isnot(None))`

### Update

``` python
session.query(User).filter(User.id == 25).update({'password': 'pppp'})
```

## Query to SQL

```python
from sqlalchemy.dialects import mysql

def query_to_sql(query, dialect=mysl_dialect_onject):
    sql = query.statement.compile(dialect=dialect, compile_kwargs={"literal_binds": True})
    return str(sql)

query = Session().query(MusicAlbum.albumid).filter_by(source='aiting')
sql = query_to_sql(query)

## Code


model

```python
def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Base = declarative_base()
Base.to_dict = to_dict
```
