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
import abc


class Grammar:
    def __init__(self):
        pass


class Object(abc.ABC):
    def __init__(self):
        self.name = None


class Class(Object):
    def __init__(self):
        super().__init__()


class Struct(Object):
    def __init__(self):
        super().__init__()


class Enum(Object):
    def __init__(self):
        # Enum.name is None if there isn't one given
        # Enum.values is a list of EnumValues
        super().__init__()
        self.values = []


class EnumValue(Object):
    def __init__(self):
        # EnumValue::value is None if it is not defined(left up to compiler)
        super().__init__()
        self.value = None


class Namespace(Object):
    def __init__(self):
        super().__init__()


class Member(Object, ABC):
    def __init__(self):
        super().__init__()
        self.type = None
        self.access_specifier = None


class Variable(Member):
    def __init__(self):
        super().__init__()


class Method(Member):
    def __init__(self):
        super().__init__()
