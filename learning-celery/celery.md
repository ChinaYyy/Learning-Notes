# Celery

## Command

重要的命令

```text
-d --destination 指定worker
-B beat， 开启scheduler
```

```shell
# 启动celery
$ celery -A tasks worker --loglevel=info

# restart
$ celery multi start -A proj -l info -c4 --pidfile=/var/run/celery/%n.pid
$ celery multi restart -B -A tasks worker -l info -c 2 --logfile='../logs/celery_task.log' --pidfile=../pids/celery_%n.pid

# 查看正在运行的任务
$ celery -A proj inspect active

# 关半所有的worker
app.control.broadcast('shutdown') # shutdown all workers

# 集群节点数, 机器数，非worker数
$ celery -A proj status
```

[Monitor and Manager](http://docs.celeryproject.org/en/latest/userguide/monitoring.html#monitoring-and-management-guide)

## Code

### log

```python
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y
```

### retry

```python
@app.task(bind=True)
def send_twitter_status(self, oauth, tweet):
    try:
        twitter = Twitter(oauth)
        twitter.update_status(tweet)
    except (Twitter.FailWhaleError, Twitter.LoginError) as exc:
        raise self.retry(exc=exc)
```

### ETA & Countdown & Expiration

ETA: estimated time of arrival（预计到达时间）

```python
add.apply_async((2, 2), countdown=3)

from datetime import datetime, timedelta

tomorrow = datetime.utcnow() + timedelta(days=1)
add.apply_async((2, 2), eta=tomorrow)

add.apply_async((10, 10), expires=60)
```

### Group

```python
>>> from celery import group

>>> numbers = [(2, 2), (4, 4), (8, 8), (16, 16)]
>>> res = group(add.s(i, j) for i, j in numbers).apply_async()

>>> res.get()
[4, 8, 16, 32]
```

### OnMessageChange

```python
# http://docs.celeryproject.org/en/latest/userguide/calling.html#on-message

@app.task(bind=True)
def hello(self, a, b):
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(1)
    return 'hello world: %i' % (a+b)

def on_raw_message(body):
    print(body)

r = hello.apply_async()
print(r.get(on_message=on_raw_message, propagate=False))

{'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
 'result': {'progress': 50},
 'children': [],
 'status': 'PROGRESS',
 'traceback': None}
{'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
 'result': {'progress': 90},
 'children': [],
 'status': 'PROGRESS',
 'traceback': None}
{'task_id': '5660d3a3-92b8-40df-8ccc-33a5d1d680d7',
 'result': 'hello world: 10',
 'children': [],
 'status': 'SUCCESS',
 'traceback': None}
hello world: 10
```

## Tutorial

[Tutorial](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#id9)

```
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
```

redis: `redis://localhost:6379`

#### Running the celery worker server

```
$ celery -A tasks worker --loglevel=info
```

`celery worker --help` or `celery help`

#### Calling the task

```
>>> from tasks import add
>>> add.delay(4, 4)
```

Returns an `AsyncResult` instance.

