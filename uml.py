# Base UML Object class.  All data classes derive from this!
class Object:
    def __init__(self):
        pass


# Basic entity to display in the uml diagram(contains function and member information etc)
class Entity(Object):
    def __init__(self):
        super().__init__()


# Classes representing different types of object relationship.
class Relationship(Object):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.lhs = lhs
        self.rhs = rhs


class RelationshipPeer(Relationship):
    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs)
        super().__init__(lhs, rhs)


class RelationshipOwnerOwned(Relationship):
    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs)


class OneToMany(Relationship):
    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs)


class OneToOne(Relationship):
    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs)


# Entry point class, contains and manages application.
class PyUML:
    def __init__(self, source_dir):
        self.source_dir = source_dir


# Entry point to program, only invoked this way if module called stand alone
if __name__ == '__main__':
    pyuml = PyUML('.')
