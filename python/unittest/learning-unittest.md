# Learning Unittest

[document](https://docs.python.org/3.6/library/unittest.html)

## Concepts

- test fixture  测试的准备工作
- test case  单元测试的独立单元
- test suite  test case的集合
- test runner  编排执行，并输出结果

## Example

```python
import unittest


@unittest.skip("skip reason...")
class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


if __name__ == '__main__':
    unittest.main()

```

- `assertRaises()` 来验证引发了某个异常
- `unittest.main()` 是命令行接口，来运行测试脚本

    ```shell
    python -m unittest test_module1 test_module2
    python -m unittest test_module.TestClass
    python -m unittest test_module.TestClass.test_method
    ```

- `setUp`, 在每个测试函数前执行
- `tearDown`, 在每个测试函数后执行， 只要setUp运行成功， 该方法就会运行，无论测试函数是否异常

    带setUp和tearDown方法这样环境的测试用例，称之为`test_fixture`

    TestCase下每个测试函数运行，`__init__`, setUp, tearDown 都要执行一次！！

- `skip`, `skipIf`, `skipUnless` 会跳过测试函数运行， 但`init`, `setUp`, `tearDown`还是会执行
- TestCase类 也可以被skip
- `expectedFailure` 期望测试失败

## Test Discovery

- `-s`, `--start-directory` directory,  Directory to start discovery (. default)
- `-p`, `--pattern` pattern, Pattern to match test files (test*.py default)

```shell
cd project_directory
python -m unittest discover -p "*_test.py"
```

## Run

```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```
