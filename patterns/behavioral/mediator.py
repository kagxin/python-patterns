#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://www.djangospin.com/design-patterns-python/mediator/

Objects in a system communicate through a Mediator instead of directly with each other.
This reduces the dependencies between communicating objects, thereby reducing coupling.
系统中的对象通过中介进行通信，而不是彼此直接通信。
这减少了通信对象之间的依赖关系，从而减少了耦合。
*TL;DR
Encapsulates how a set of objects interact.
封装一组对象如何交互。
"""


class ChatRoom(object):
    """Mediator class
        中介者
    """

    def display_message(self, user, message):
        print("[{} says]: {}".format(user, message))


class User(object):
    """A class whose instances want to interact with each other
        实例希望彼此交互的类
    """

    def __init__(self, name):
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message):
        self.chat_room.display_message(self, message)

    def __str__(self):
        return self.name


def main():
    """
    >>> molly = User('Molly')
    >>> mark = User('Mark')
    >>> ethan = User('Ethan')

    >>> molly.say("Hi Team! Meeting at 3 PM today.")
    [Molly says]: Hi Team! Meeting at 3 PM today.
    >>> mark.say("Roger that!")
    [Mark says]: Roger that!
    >>> ethan.say("Alright.")
    [Ethan says]: Alright.
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
