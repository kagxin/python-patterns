#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
目录？
A class that uses different static function depending of a parameter passed in
init. Note the use of a single dictionary instead of multiple conditions

一个类更具传入的参数使用不同的静态函数。
注意使用单个字典而不是多个条件语句
"""

__author__ = "Ibrahim Diop <ibrahim@sikilabs.com>"


class Catalog(object):
    """catalog of multiple static methods that are executed depending on an init
        根据初始化函数执行的多个静态方法的catalog
    parameter
    """

    def __init__(self, param):

        # dictionary that will be used to determine which static method is
        # to be executed but that will be also used to store possible param
        # value
        """
            字典_static_method_choices，用于确定要执行哪个静态方法，也将用于存储可能的参数值
        """
        self._static_method_choices = {'param_value_1': self._static_method_1, 'param_value_2': self._static_method_2}

        # simple test to validate param value 对参数的有效性进行简单测试
        if param in self._static_method_choices.keys():
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("executed method 1!")

    @staticmethod
    def _static_method_2():
        print("executed method 2!")

    def main_method(self):
        """will execute either _static_method_1 or _static_method_2

        depending on self.param value
            - 更具self.param 的值，将会执行_static_method_1或者_static_method_2
        """
        self._static_method_choices[self.param]()


# Alternative implementation for different levels of methods 不同级别方法的另外一种实现
class CatalogInstance(object):

    """catalog of multiple methods that are executed depending on an init
        根据初始化函数执行的多个静态方法的catalog
    parameter
    """

    def __init__(self, param):
        self.x1 = 'x1'
        self.x2 = 'x2'
        # simple test to validate param value
        if param in self._instance_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    def _instance_method_1(self):
        print("Value {}".format(self.x1))

    def _instance_method_2(self):
        print("Value {}".format(self.x2))

    _instance_method_choices = {'param_value_1': _instance_method_1, 'param_value_2': _instance_method_2}

    def main_method(self):
        """will execute either _instance_method_1 or _instance_method_2

        depending on self.param value
        """
        self._instance_method_choices[self.param].__get__(self)()


class CatalogClass(object):

    """catalog of multiple class methods that are executed depending on an init

    parameter
    """

    x1 = 'x1'
    x2 = 'x2'

    def __init__(self, param):
        # simple test to validate param value
        if param in self._class_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @classmethod
    def _class_method_1(cls):
        print("Value {}".format(cls.x1))

    @classmethod
    def _class_method_2(cls):
        print("Value {}".format(cls.x2))

    _class_method_choices = {'param_value_1': _class_method_1, 'param_value_2': _class_method_2}

    def main_method(self):
        """will execute either _class_method_1 or _class_method_2

        depending on self.param value
        """
        self._class_method_choices[self.param].__get__(None, self.__class__)()


class CatalogStatic(object):

    """catalog of multiple static methods that are executed depending on an init

    parameter
    """

    def __init__(self, param):
        # simple test to validate param value
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("executed method 1!")

    @staticmethod
    def _static_method_2():
        print("executed method 2!")

    _static_method_choices = {'param_value_1': _static_method_1, 'param_value_2': _static_method_2}

    def main_method(self):
        """will execute either _static_method_1 or _static_method_2

        depending on self.param value
        """
        self._static_method_choices[self.param].__get__(None, self.__class__)()


def main():
    """
    >>> test = Catalog('param_value_2')
    >>> test.main_method()
    executed method 2!

    >>> test = CatalogInstance('param_value_1')
    >>> test.main_method()
    Value x1

    >>> test = CatalogClass('param_value_2')
    >>> test.main_method()
    Value x2

    >>> test = CatalogStatic('param_value_1')
    >>> test.main_method()
    executed method 1!
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
