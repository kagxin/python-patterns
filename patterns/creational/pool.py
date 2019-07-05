#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
This pattern is used when creating an object is costly (and they are
created frequently) but only a few are used at a time. With a Pool we
can manage those instances we have as of now by caching them. Now it
is possible to skip the costly creation of an object if one is
available in the pool.
A pool allows to 'check out' an inactive object and then to return it.
If none are available the pool creates one to provide without wait.

当创建一个对象很昂贵(而且经常创建)，但一次只使用几个对象时，就会使用这种模式。
使用池，我们可以通过缓存这些实例来管理我们目前拥有的实例。
现在，如果池中有对象可用，就可以跳过昂贵的对象创建。
池允许“检出”不活动的对象，然后返回它。
如果没有可用的线程池，则创建一个线程池来提供，而不需要等待。

*What does this example do?
In this example queue.Queue is used to create the pool (wrapped in a
custom ObjectPool object to use with the with statement), and it is
populated with strings.
As we can see, the first string object put in "yam" is USED by the
with statement. But because it is released back into the pool
afterwards it is reused by the explicit call to sample_queue.get().
Same thing happens with "sam", when the ObjectPool created insided the
function is deleted (by the GC) and the object is returned.

在这个示例队列中。Queue用于创建池(包装在与with语句一起使用的自定义ObjectPool对象中)，并用字符串填充它。
正如我们所看到的，放在“yam”中的第一个字符串对象由with语句使用。但是因为它在之后被释放回池中，所以会被显式调用sample_queue.get()重用。
同样的事情也发生在“sam”上，当内部创建的ObjectPool函数被删除(由GC创建)并返回对象时。

*Where is the pattern used practically?

*References:
http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern
https://sourcemaking.com/design_patterns/object_pool

*TL;DR
Stores a set of initialized objects kept ready to use.
存储一组初始化的对象，以备使用。
"""


class ObjectPool(object):
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    try:
        import queue
    except ImportError:  # python 2.x compatibility
        import Queue as queue

    def test_object(queue):
        pool = ObjectPool(queue, True)
        print('Inside func: {}'.format(pool.item))

    sample_queue = queue.Queue()

    sample_queue.put('yam')
    with ObjectPool(sample_queue) as obj:
        print('Inside with: {}'.format(obj))
    print('Outside with: {}'.format(sample_queue.get()))

    sample_queue.put('sam')
    test_object(sample_queue)
    print('Outside func: {}'.format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())


if __name__ == '__main__':
    main()

### OUTPUT ###
# Inside with: yam
# Outside with: yam
# Inside func: sam
# Outside func: sam
