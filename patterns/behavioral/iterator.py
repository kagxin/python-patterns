#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
Implementation of the iterator pattern with a generator
用生成器实现迭代器模式

*TL;DR
Traverses a container and accesses the container's elements.
遍历容器并访问容器的元素。
"""

from __future__ import print_function


def count_to(count):
    """Counts by word numbers, up to a maximum of five
        按单词数计数，最多5个
    """
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number


# Test the generator
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)


def main():
    """
    # Counting to two...
    >>> for number in count_to_two():
    ...     print(number)
    one
    two

    # Counting to five...
    >>> for number in count_to_five():
    ...     print(number)
    one
    two
    three
    four
    five
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
