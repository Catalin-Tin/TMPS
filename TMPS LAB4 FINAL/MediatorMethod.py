class CompanyType(object):
    """Mediator class."""

    def displayComapnyType(self, user, type_name):
        print("[{}'s course ]: {}".format(user, type_name))


class PetStore(object):
    '''A class whose instances want to interact with each other.'''

    def __init__(self, name):
        self.name = name
        self.course = CompanyType()

    def sendType(self, type_name):
        self.course.displayComapnyType(self, type_name)

    def __str__(self):
        return self.name