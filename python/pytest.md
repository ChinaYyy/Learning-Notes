# Learning Pytest

`pip install -U pytest`

```python
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

```bash
$ pytest
========= test session starts =========
platform linux -- Python 3.x.y, pytest-3.x.y, py-1.x.y, pluggy-0.x.y
rootdir: $REGENDOC_TMPDIR, inifile:
collected 1 item

test_sample.py F                                                     [100%]

======== FAILURES =========
________ test_answer ______

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:5: AssertionError
======= 1 failed in 0.12 seconds ===========
```

`pytest` will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.

断言引起异常

```python
# content of test_sysexit.py
import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```

每次调用创建临时目录

```python
# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print (tmpdir)
    assert 0
```
