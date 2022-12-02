# Topic: Behaviour Design Patterns

### Course: TMPS
### Author: Tincu Catalin FAF-201

----
## OVERVIEW:
1. Iterator method is a Behavioral Design Pattern that allows us to traverse the elements of the collections without taking the exposure of in-depth details of the elements.
2. Mediator Method is a Behavioral Design Pattern that allows us to reduce the unordered dependencies between the objects. In a mediator environment, objects take the help of mediator objects to communicate with each other.
3. Observer method is a Behavioral design Pattern which allows you to define or create a subscription mechanism to send the notification to the multiple objects about any new event that happens to the object that they are observing. The subject is basically observed by multiple objects. 
4. Strategy method is Behavioral Design pattern that allows you to define the complete family of algorithms, encapsulates each one and putting each of them into separate classes and also allows to interchange there objects.
5. Visitor Method is a Behavioral Design Pattern which allows us to separate the algorithm from an object structure on which it operates. It helps us to add new features to an existing class hierarchy dynamically without changing it.
## Iterator Method
1. To demonstrate how Iterator works, I will need 2 functions iterators that will generate some data
```
def DogCounting():
    alphabets = [chr(i) for i in range(49, 58)]

    """using in-built iterator"""
    for alpha in alphabets:
        print(alpha, end=" ")
    print()
    
def LetterAssigning():
    alphabets = [chr(i) for i in range(65, 74)]

    """using in-built iterator"""
    for alpha in alphabets:
        print(alpha, end=" ")
    print()
```
2. After that I will call in main the inbuiltIterators
```
    DogCounting()
    LetterAssigning()
```
## Mediator Method
1. For this method I need to create 2 classes, one that will serve as a mediator class, second one that will have instances that want to interact with each other.
```
class CompanyType(object):
    def displayComapnyType(self, user, type_name):
        print("[{}'s course ]: {}".format(user, type_name))


class PetStore(object):
    def __init__(self, name):
        self.name = name
        self.course = CompanyType()

    def sendType(self, type_name):
        self.course.displayComapnyType(self, type_name)

    def __str__(self):
        return self.name
```
2. Afterwords will execute PetStore class
```
first = MediatorMethod.PetStore('Pet Shop Labrador')  # petstore object
second = MediatorMethod.PetStore('Mister Dog')  # petstore object
third = MediatorMethod.PetStore('Global Pet Store')  # petstore object

first.sendType("It's a specific shop for a type of dog")
second.sendType("It's a generic shop for dogs")
third.sendType("It's a shop for any kind of pet")
```
## Observer Method
1. First class indicates what is being observed
```
class SubjectYears:
    def __init__(self):
        """create an empty observer list"""

        self._observers = []

    def notify(self, modifier=None):
        """Alert the observers"""

        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        """If the observer is not in the list,
        append it into the list"""

        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove the observer from the observer list"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
```
2. Next, I need a class that will monitor the object
```
class Data(SubjectYears):
    def __init__(self, name=''):
        SubjectYears.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()
```
3. Therefore, the last thing that I need in order to implement Observer Method is some updates or events that will trigger the monitor. Decided to create 3 classes for this purpose and the input of the method is visible in main.py
```
class HexViewer:
    """updates the Hexviewer"""

    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))
class OctalViewer:
    """updates the Octal viewer"""

    def update(self, subject):
        print('OctalViewer: Subject' + str(subject.name) + 'has data ' + str(oct(subject.data)))
class DecimalViewer:
    """updates the Decimal viewer"""

    def update(self, subject):
        print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))
```
## Strategy Method
1. Firstly I created a constructor function with price and discount
```
class PetCost:
    def __init__(self, price, discount_strategy=None):

        """take price and discount strategy"""
        self.price = price
        self.discount_strategy = discount_strategy

    """A separate function for price after discount"""
    def price_after_discount(self):

        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self):

        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_discount())

"""function dedicated to On Sale Discount"""
def on_sale_discount(order):
    return order.price * 0.25 + 20

"""function dedicated to 20 % discount"""
def twenty_percent_discount(order):
    return order.price * 0.20
```
2. The input of costs
```
print(StratagyMethod.PetCost(20000))
"""with discount strategy as 20 % discount"""
print(StratagyMethod.PetCost(20000, discount_strategy=StratagyMethod.twenty_percent_discount))
"""with discount strategy as On Sale Discount"""
print(StratagyMethod.PetCost(20000, discount_strategy=StratagyMethod.on_sale_discount))
```
## Visitor Method
1. First step is to create a class for courses and after that 3 more classes that will represent the courses for animal care
```
class Courses_For_PetCare:
    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(self, "Taught by ", visitor)

    def studying(self, visitor):
        print(self, "studied by ", visitor)

    def __str__(self):
        return self.__class__.__name__

class AnimalAdoption(Courses_For_PetCare): pass
class PuppyMills(Courses_For_PetCare): pass
class VeterinaryCare(Courses_For_PetCare): pass
```
2. Second step is to create class Visitor that will be used by other two classes that represents types of visitors that can attend the courses. 
```
class Visitor:
    def __str__(self):
        return self.__class__.__name__

class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)

class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)
```
## The Output of the program
```
-------------------Iterator Method------------------------
Count the dogs in the house
1 2 3 4 5 6 7 8 9 
Give them tag letters
A B C D E F G H I 
-------------------Mediator Method------------------------
[Pet Shop Labrador's course ]: It's a specific shop for a type of dog
[Mister Dog's course ]: It's a generic shop for dogs
[Global Pet Store's course ]: It's a shop for any kind of pet
-------------------Observer Method------------------------
DecimalViewer: Subject Cody Young Labrador has data  3
HexViewer: Subject Cody Young Labrador has data 0x3
OctalViewer: SubjectCody Young Labradorhas data 0o3
DecimalViewer: Subject Zuko Elder Husky has data  12
HexViewer: Subject Zuko Elder Husky has data 0xc
OctalViewer: SubjectZuko Elder Huskyhas data 0o14
-------------------Strategy Method------------------------
Price: 20000, price after discount: 20000
Price: 20000, price after discount: 16000.0
Price: 20000, price after discount: 14980.0
-------------------Visitor Method------------------------
AnimalAdoption Taught by  Instructor
AnimalAdoption studied by  Student
PuppyMills Taught by  Instructor
PuppyMills studied by  Student
VeterinaryCare Taught by  Instructor
VeterinaryCare studied by  Student
```


