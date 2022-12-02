class Courses_For_PetCare:

    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(self, "Taught by ", visitor)

    def studying(self, visitor):
        print(self, "studied by ", visitor)

    def __str__(self):
        return self.__class__.__name__


"""Concrete Courses_For_PetCare: Classes being visited."""


class AnimalAdoption(Courses_For_PetCare): pass


class PuppyMills(Courses_For_PetCare): pass


class VeterinaryCare(Courses_For_PetCare): pass


""" Abstract Visitor class for Concrete Visitor classes:
 method defined in this class will be inherited by all
 Concrete Visitor classes."""


class Visitor:

    def __str__(self):
        return self.__class__.__name__


""" Concrete Visitors: Classes visiting Concrete Course objects.
 These classes have a visit() method which is called by the
 accept() method of the Concrete Courses_For_PetCare."""


class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)


class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)