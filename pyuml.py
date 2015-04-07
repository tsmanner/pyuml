from grammarlib import Variable, Method, Class
# Base UML Object class.  All data classes derive from this!
class UmlObject:
    def __init__(self):

# Basic entity to display in the uml diagram(contains function and member information etc)
class UmlEntity(UmlObject):
    def __init__(self):
        pass

# Classes representing different types of object relationship.
class UmlRelationship(UmlObject):
    def __init__(self,lhs,rhs):
        pass

class RelationshipPeer(UmlRelationship):
    def __init__(self,lhs,rhs):
        pass

class RelationshipOwnerOwned(UmlRelationship):
    def __init__(self,lhs,rhs):
        pass

class UmlOneToMany(RelationshipOwnerOwned):
    def __init__(self,lhs,rhs):
        pass

class UmlOneToOne(RelationshipOwnerOwned):
    def __init__(self,lhs,rhs):
        pass

class UmlOneToOne(RelationshipPeer):
    def __init__(self,lhs,rhs):
        pass

# Entry point class, contains and manages application.
class PyUML:
    def __init__(self,source_dir):
        self.source_dir = source_dir

# Entry point to program, only invoked this way if module called stand alone
if __name__ == "__main__":
    source_dir = "E:\Documents\Projects\zMidas\L2LsuDrvr\"
    pyuml = PyUML(source_dir)
