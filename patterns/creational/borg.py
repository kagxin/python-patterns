#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
单态模式
*What is this pattern about?
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.

Borg 模式（也称单态模式）是一种方法实现单例行为，而不是只有一个实例对于一个类，
有多个共享相同状态的实例。在换句话说，
重点是共享状态而不是共享实例的身份。

*What does this example do?
To understand the implementation of this pattern in Python, it is
important to know that, in Python, instance attributes are stored in a
attribute dictionary called __dict__. Usually, each instance will have
its own dictionary, but the Borg pattern modifies this so that all
instances have the same dictionary.
In this example, the __shared_state attribute will be the dictionary
shared between all instances, and this is ensured by assigining
__shared_state to the __dict__ variable when initializing a new
instance (i.e., in the __init__ method). Other attributes are usually
added to the instance's attribute dictionary, but, since the attribute
dictionary itself is shared (which is __shared_state), all other
attributes will also be shared.
For this reason, when the attribute self.state is modified using
instance rm2, the value of self.state in instance rm1 also changes. The
same happens if self.state is modified using rm3, which is an
instance from a subclass.
Notice that even though they share attributes, the instances are not
the same, as seen by their ids.

要理解这个模式在Python中的实现，它是重要的是要知道，
在Python中，实例属性存储在属性字典称为__dict__。
通常，每个实例都有它有自己的字典，
但博格模式修改了这一切实例具有相同的字典。
在本例中，_shared_state属性将是字典
在所有实例之间共享，这是通过分配来确保的
初始化一个新变量时，将_shared_state赋给_dict__变量
实例(即。，用……init__方法)。其他属性通常是
添加到实例的属性字典中，但是，由于属性
dictionary本身是共享的(它是_shared_state)，其他的都是共享的
属性也将被共享。
因此，当属性为self时。使用以下命令修改状态实例rm2, self的值。
实例rm1中的状态也发生了变化。的self也是一样。状态使用rm3修改，rm3是一个
子类的实例。
注意，即使它们共享属性，实例也不是
从他们的身份证上看，是一样的。

*Where is the pattern used practically?
Sharing state is useful in applications like managing database connections:
https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py
共享状态是有用的对于像数据库连接这样的应用。


*References:
https://fkromer.github.io/python-pattern-references/design/#singleton

*TL;DR
Provides singleton-like behavior sharing state between instances.
提供在实例之间共享状态，类似于单例的行为。
"""


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))

### OUTPUT ###
# rm1: Running
# rm2: Running
# rm1: Zombie
# rm2: Zombie
# rm1 id: 140732837899224
# rm2 id: 140732837899296
# rm1: Init
# rm2: Init
# rm3: Init
