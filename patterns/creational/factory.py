#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""*What is this pattern about?
A Factory is an object for creating other objects.
工厂是用于创建其他对象的对象。

*What does this example do?
The code shows a way to localize words in two languages: English and
Greek. "get_localizer" is the factory function that constructs a
localizer depending on the language chosen. The localizer object will
be an instance from a different class according to the language
localized. However, the main code does not have to worry about which
localizer will be instantiated, since the method "localize" will be called
in the same way independently of the language.

该代码显示了一种用两种语言本地化单词的方法:英语和希腊语。
“get_localizer”是工厂函数，它根据选择的语言构造本地化器。
localizer对象将根据本地化的语言是来自不同类的实例。
但是，主代码不必担心实例化哪个本地化器，因为方法“localalize”将以独立于语言的相同方式调用。

*Where can the pattern be used practically?
The Factory Method can be seen in the popular web framework Django:
http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns For
example, in a contact form of a web page, the subject and the message
fields are created using the same form factory (CharField()), even
though they have different implementations according to their
purposes.
工厂方法中可以看到流行的web框架
http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns为例,在接触的一个网页形式,
主题和消息字段是使用相同的形式创建工厂(CharField()),即使他们有不同的实现根据他们的目的
*References:
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR
Creates objects without having to specify the exact class.
创建对象而不必指定确切的类。
"""

from __future__ import unicode_literals
from __future__ import print_function


class GreekLocalizer(object):
    """A simple localizer a la gettext"""

    def __init__(self):
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg):
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer(object):
    """Simply echoes the message"""

    def localize(self, msg):
        return msg


def get_localizer(language="English"):
    """Factory"""
    localizers = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }
    return localizers[language]()


def main():
    """
    # Create our localizers
    >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")

    # Localize some text
    >>> for msg in "dog parrot cat bear".split():
    ...     print(e.localize(msg), g.localize(msg))
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
