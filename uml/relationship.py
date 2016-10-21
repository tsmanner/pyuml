from uml import Element


class Relationship(Element):
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
