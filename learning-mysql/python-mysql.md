# Python Mysql


## 使用with语句

```
conn = MySQLdb.connect()

with conn as cur:
	cur.execute(sql)
	...
```

connect的__enter__方法返回了游标，在with中执行结束，它会决断当前是否有错误， 有错误就回滚，
没有则进行事务提交。相当于无须和上书来写正面这样的异常处理：
```
try:
    cur = conn.cursor()
	cur.execute("")
	conn.commit()
except MySQLdb.Error as e:
    conn.rollback()
```

## 使用sqlalchemy

```
engine = create_engine('mysql+mysqldb://user:passwd@host/db')
with engine.connect()as conn:
    rs = conn.execute("")
	for row in rs:
	    print row
```