#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
This pattern aims to minimise the number of objects that are needed by
a program at run-time. A Flyweight is an object shared by multiple
contexts, and is indistinguishable from an object that is not shared.

The state of a Flyweight should not be affected by it's context, this
is known as its intrinsic state. The decoupling of the objects state
from the object's context, allows the Flyweight to be shared.

这种模式的目的是最小化程序在运行时所需的对象数量。
Flyweight是由多个上下文共享的对象，与不共享的对象没有什么区别。

Flyweight的状态不应该受到它的上下文的影响，这就是它的固有状态。
对象状态与对象上下文的解耦允许共享Flyweight。

*What does this example do?
The example below sets-up an 'object pool' which stores initialised
objects. When a 'Card' is created it first checks to see if it already
exists instead of creating a new one. This aims to reduce the number of
objects initialised by the program.

下面的例子设置了一个“对象池”，它存储初始化的对象。
当一个“卡片”被创建时，它首先检查它是否已经存在，而不是创建一个新的。
这旨在减少程序初始化的对象数量。

*References:
http://codesnipers.com/?q=python-flyweights
https://python-patterns.guide/gang-of-four/flyweight/

*Examples in Python ecosystem:
https://docs.python.org/3/library/sys.html#sys.intern

*TL;DR
Minimizes memory usage by sharing data with other similar objects.
通过与其他类似对象共享数据，最小化内存使用。
"""

import weakref


class Card(object):
    """The Flyweight"""

    # Could be a simple dict.
    # With WeakValueDictionary garbage collection can reclaim the object
    # when there are no other references to it.
    _pool = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        # If the object exists in the pool - just return it
        obj = cls._pool.get(value + suit)
        # otherwise - create new one (and add it to the pool)
        if obj is None:
            obj = object.__new__(Card)
            cls._pool[value + suit] = obj
            # This row does the part we usually see in `__init__`
            obj.value, obj.suit = value, suit
        return obj

    # If you uncomment `__init__` and comment-out `__new__` -
    #   Card becomes normal (non-flyweight).
    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


def main():
    """
    >>> c1 = Card('9', 'h')
    >>> c2 = Card('9', 'h')
    >>> c1, c2
    (<Card: 9h>, <Card: 9h>)
    >>> c1 == c2
    True
    >>> c1 is c2
    True

    >>> c1.new_attr = 'temp'
    >>> c3 = Card('9', 'h')
    >>> hasattr(c3, 'new_attr')
    True

    >>> Card._pool.clear()
    >>> c4 = Card('9', 'h')
    >>> hasattr(c4, 'new_attr')
    False
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
