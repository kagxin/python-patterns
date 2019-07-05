#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
*What is this pattern about?
It decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects from the same
family.
This is useful when you must separate the specification of an object
from its actual representation (generally for abstraction).

它解耦了复杂对象的创建及其表示，因此可以重用相同的流程来构建来自相同家族的对象。
当您必须将对象的规范与其实际表示(通常用于抽象)分离时，这是非常有用的。

*What does this example do?

The first example achieves this by using an abstract base
class for a building, where the initializer (__init__ method) specifies the
steps needed, and the concrete subclasses implement these steps.

In other programming languages, a more complex arrangement is sometimes
necessary. In particular, you cannot have polymorphic behaviour in a constructor in C++ -
see https://stackoverflow.com/questions/1453131/how-can-i-get-polymorphic-behavior-in-a-c-constructor
- which means this Python technique will not work. The polymorphism
required has to be provided by an external, already constructed
instance of a different class.

In general, in Python this won't be necessary, but a second example showing
this kind of arrangement is also included.

第一个示例通过使用一个抽象基类来实现这一点，其中初始化器(__init__方法)指定了所需的步骤，具体的子类实现了这些步骤。
在其他编程语言中，有时需要更复杂的安排。特别是，您不能在c++的构造函数中有多态行为——请参见
https://stackoverflow.com/questions/1453131/how-can-i-get-polymorphic-behavior-in-a-c-constructor
-这意味着这种Python技术将不起作用。所需的多态性必须由一个外部的、已构造的不同类的实例提供。

一般来说，在Python中，这不是必需的，但是还包含了展示这种安排的第二个示例。

*Where is the pattern used practically?

*References:
https://sourcemaking.com/design_patterns/builder

*TL;DR
Decouples the creation of a complex object and its representation.
解耦复杂对象的创建及其表示。
"""


# Abstract Building
class Building(object):
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


# Concrete Buildings
class House(Building):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big'


class Flat(Building):
    def build_floor(self):
        self.floor = 'More than One'

    def build_size(self):
        self.size = 'Small'


# In some very complex cases, it might be desirable to pull out the building
# logic into another function (or a method on another class), rather than being
# in the base class '__init__'. (This leaves you in the strange situation where
# a concrete class does not have a useful constructor)
'''
在一些非常复杂的情况下，将构建逻辑提取到另一个函数(或另一个类上的方法)中，而不是放在基类“_init__”中，可能是可取的。
(这会让您陷入一种奇怪的情况，具体类没有一个有用的构造函数)
'''


class ComplexBuilding(object):
    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big and fancy'


def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building


# Client
if __name__ == "__main__":
    house = House()
    print(house)
    flat = Flat()
    print(flat)

    # Using an external constructor function:
    complex_house = construct_building(ComplexHouse)
    print(complex_house)

### OUTPUT ###
# Floor: One | Size: Big
# Floor: More than One | Size: Small
# Floor: One | Size: Big and fancy
