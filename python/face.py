# !!! 单例设计模式

# 使用__new__方法
class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Myclass(Singleton):
    pass


# 装饰器方法
def singleton(cls, *args, **kwargs):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class MyClass2:
    pass


# import 方法


def linefunc(a, b):
    def calc(x):
        value = a*x+b
        return value
    return calc


# !!! 二分查找
def binarySearch(l, t):
    low, high = 0, len(l) - 1

    while low <= high:
        mid = (low+high)/2
        if l[mid] > t:
            high = mid-1
        elif l[mid] < t:
            low = mid+1
        else:
            return mid
    return -1

def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists