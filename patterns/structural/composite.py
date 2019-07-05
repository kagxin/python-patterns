#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
The composite pattern describes a group of objects that is treated the
same way as a single instance of the same type of object. The intent of
a composite is to "compose" objects into tree structures to represent
part-whole hierarchies. Implementing the composite pattern lets clients
treat individual objects and compositions uniformly.

复合模式描述一组对象，这些对象被当作同一类型对象的单个实例来处理。
组合的目的是将对象“组合”到树结构中，以表示部分整体层次结构。
实现组合模式允许客户端统一地处理单个对象和组合。

*What does this example do?
The example implements a graphic class，which can be either an ellipse
or a composition of several graphics. Every graphic can be printed.

这个例子实现了一个图形类,它可以是一个椭圆或几个图形的组合。每个图形都可以打印。

*Where is the pattern used practically?
In graphics editors a shape can be basic or complex. An example of a
simple shape is a line, where a complex shape is a rectangle which is
made of four line objects. Since shapes have many operations in common
such as rendering the shape to screen, and since shapes follow a
part-whole hierarchy, composite pattern can be used to enable the
program to deal with all shapes uniformly.

在图形编辑器中，形状可以是基本的，也可以是复杂的。
一个简单形状的例子是一条线，其中一个复杂形状是由四个线对象组成的矩形。
由于形状有许多共同的操作，例如将形状呈现到屏幕上，而且形状遵循部分-整体层次结构，
因此可以使用组合模式使程序能够一致地处理所有形状。

*References:
https://en.wikipedia.org/wiki/Composite_pattern
https://infinitescript.com/2014/10/the-23-gang-of-three-design-patterns/

*TL;DR
Describes a group of objects that is treated as a single instance.
描述一组被视为单个实例的对象。
"""


class Graphic:
    def render(self):
        raise NotImplementedError("You should implement this.")


class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name):
        self.name = name

    def render(self):
        print("Ellipse: {}".format(self.name))


if __name__ == '__main__':
    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    ellipse3 = Ellipse("3")
    ellipse4 = Ellipse("4")

    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()

    graphic1.add(ellipse1)
    graphic1.add(ellipse2)
    graphic1.add(ellipse3)
    graphic2.add(ellipse4)

    graphic = CompositeGraphic()

    graphic.add(graphic1)
    graphic.add(graphic2)

    graphic.render()

### OUTPUT ###
# Ellipse: 1
# Ellipse: 2
# Ellipse: 3
# Ellipse: 4
