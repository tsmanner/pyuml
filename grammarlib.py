# grammarlib.py
#   Object Heirarchy:
#                 Object
#                  |  | 
#            +-----+  +----+-------+-------+---------+-----------+
#            |             |       |       |         |           |
#            V             |       |       |         |           |
#          Member          V       V       V         V           V
#           |  |         Class   Struct   Enum   EnumValue   Namespace
#       +---+  +-----+
#       |            |
#       V            V
#    Method       Variable


# We need some Abstract Base Classes(ABCs) here
from abc import ABC

class Grammar:
    def __init__(self):
        pass

class Object(ABC):
    def __init__(self):
        self.name = None

class Class(Object):
    def __init__(self):
        pass

class Struct(Object):
    def __init__(self):
        pass

class Enum(Object):
    def __init__(self):
        # Enum::name is None if there isn't one given
        # Enum::values is a list of EnumValues
        self.values = []

class EnumValue(Object):
    def __init__(self):
        # EnumValue::value is None if it is not defined(left up to compiler)
        self.value = None

class Namespace(Object):
    def __init__(self):
        pass

class Member(Object,ABC):
    def __init__(self):
        self.type             = None
        self.access_specifier = None

class Variable(Member):
    def __init__(self):
        pass

class Method(Member):
    def __init__(self):
        pass
