#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example from https://en.wikipedia.org/wiki/Facade_pattern#Python


*What is this pattern about?
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This kind of abstraction is seen in many real life situations. For
example, we can turn on a computer by just pressing a button, but in
fact there are many procedures and operations done when that happens
(e.g., loading programs from disk to memory). In this case, the button
serves as an unified interface to all the underlying procedures to
turn on a computer.

Facade模式是一种为更复杂的系统提供更简单的统一接口的方法。
通过提供一个入口点，它提供了访问底层系统功能的更简单的方法。
这种抽象出现在许多实际的情况中。
例如，我们只需按下一个按钮就可以打开一台计算机，
但实际上，当这种情况发生时，有许多过程和操作要做(例如，将程序从磁盘加载到内存)。
在本例中，该按钮作为所有打开计算机的底层过程的统一接口。

*Where is the pattern used practically?
This pattern can be seen in the Python standard library when we use
the isdir function. Although a user simply uses this function to know
whether a path refers to a directory, the system makes a few
operations and calls other modules (e.g., os.stat) to give the result.

当我们使用isdir函数时，可以在Python标准库中看到这种模式。
虽然用户只是使用这个函数来知道路径是否引用目录，但是系统会执行一些操作并调用其他模块(例如os.stat)来给出结果。

*References:
https://sourcemaking.com/design_patterns/facade
https://fkromer.github.io/python-pattern-references/design/#facade
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#facade

*TL;DR
Provides a simpler unified interface to a complex system.
为复杂系统提供更简单的统一接口。
"""

from __future__ import print_function


# Complex computer parts
class CPU(object):
    """
    Simple CPU representation.
    """
    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Executing.")


class Memory(object):
    """
    Simple memory representation.
    """
    def load(self, position, data):
        print("Loading from {0} data: '{1}'.".format(position, data))


class SolidStateDrive(object):
    """
    Simple solid state drive representation.
    """
    def read(self, lba, size):
        return "Some data from sector {0} with size {1}".format(lba, size)


class ComputerFacade(object):
    """
    Represents a facade for various computer parts.
    """
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


def main():
    """
    >>> computer_facade = ComputerFacade()
    >>> computer_facade.start()
    Freezing processor.
    Loading from 0x00 data: 'Some data from sector 100 with size 1024'.
    Jumping to: 0x00
    Executing.
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
