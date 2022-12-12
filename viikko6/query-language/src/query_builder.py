from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And, Or

class QueryBuilder:
    def __init__(self, build = All()):
        self.build_olio = build

    def build(self):
        return self.build_olio

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.build_olio))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value,attr), self.build_olio))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr),self.build_olio))

    def oneOf(self, build1, build2):
        return QueryBuilder(Or(build1, build2))
