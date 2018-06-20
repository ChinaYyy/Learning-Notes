# Celery


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

