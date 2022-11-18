# Topic: Structural Design Patterns

### Course: TMPS
### Author: Tincu Catalin FAF-201

----
## OVERVIEW:
1. Adapter method is a Structural Design Pattern which helps us in making the incompatible objects adaptable to each other. The Adapter method is one of the easiest methods to understand because we have a lot of real-life examples that show the analogy with it. The main purpose of this method is to create a bridge between two incompatible interfaces. 
2. Composite Method is a Structural Design Pattern which describes a group of objects that is treated the same way as a single instance of the same type of the objects. The purpose of the Composite Method is to Compose objects into Tree type structures to represent the whole-partial hierarchies.
3. Decorator Method is a Structural Design Pattern which allows you to dynamically attach new behaviors to objects without changing their implementation by placing these objects inside the wrapper objects that contains the behaviors. 
4. Proxy method is Structural design pattern that allows you to provide the replacement for an another object. 
5. Flyweight method is a Structural Design Pattern that focus on minimizing the number of objects that are required by the program at the run-time. Basically, it creates a Flyweight object which is shared by multiple contexts. It is created in such a fashion that you can not distinguish between an object and a Flyweight Object.

## Adapter Method
1. First step is to create some classes that will be created by some Adapter class
```
class Hybrid:

    def __init__(self):
        self.name = "Hybrid Car"

    def BatteryEngine(self):
        return "Battery and Engine"


class Standard:

    def __init__(self):
        self.name = "Engine Car"

    def Engine(self):
        return "Engine"


class Electric:

    def __init__(self):
        self.name = "Electric Car"

    def Battery(self):
        return "Battery"
```
2. Next Step is to create that specific Adapter class that will adapt the object by replacing methods
```
class Adapter:
    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__
```
3. This is how objects are called
```
 HybridCar = Hybrid()
    objects.append(Adapter(HybridCar, wheels=HybridCar.BatteryEngine))

    StandardCar = Standard()
    objects.append(Adapter(StandardCar, wheels=StandardCar.Engine))

    ElectricCar = Electric()
    objects.append(Adapter(ElectricCar, wheels=ElectricCar.Battery))
```
## Composite Method
1. To be able to implement this method we need only two classes, one of it will represent objects at the bottom or Leaf of the hierarchy tree
```
class LeafElement:
    def __init__(self, *args):
        """'Takes the first positional argument and assigns to member variable "position"."""
        self.position = args[0]

    def showDetails(self):
        """Prints the position of the child element."""
        print("\t", end="")
        print(self.position)
```
2. While the second one will represent objects at any level of the hierarchy
     tree except for the bottom or leaf level.
```
class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()
```
## Decorator Method
1. First step we need an object, such as car, that will be our default setting and then we will create some of them more, that will boost our initial object
```
class BasicCar:
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text
```
2. Next step is adding feature classes that will boost the initial object, I will add for instance some tuning properties
```
class EngineTuning(BasicCar):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<200horsepowers+>{}".format(self._wrapped.render())


class BodyTuning(BasicCar):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<yellow color with golden rims>{}".format(self._wrapped.render())


class InteriorTuning(BasicCar):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<Alcantara Wrap>{}".format(self._wrapped.render())
```
3. And this is how you call this method
```
before_gfg = BasicCar("Honda Civic Type R")
    after_gfg = EngineTuning(BodyTuning(InteriorTuning(before_gfg)))
```
## Proxy Method
1. I need to simulate the replacement an object with another and different classes should present the functionality of another class, for this I will need 2 objects. First one should be resource intensive object. 
```
class Highway:

    def drivingOnHighway(self):
        print("You may go....")
```
2. When the second one is less resource intensive proxy
```
class HighwayProxy:
    def __init__(self):

        self.timeLeft = 500
        self.highway = None

    def drivingOnHighway(self):

        print("Proxy in action. Checking to see if time of payment has passed...")
        if self.timeLeft >= 200:
            # If the balance is greater than 500, let him drive.
            self.highway = Highway()
            self.highway.drivingOnHighway()
        else:

            # Otherwise, don't instantiate the highway object.
            print("Your fee balance is smaller than 200, first pay the fee")
```
## Flyweight Method
1. The goal with this method is to minimize the number of objects that are required by the program at the run-time, this class will be distinctive for complex cars
```
class ComplexCars(object):

    def __init__(self):
        pass

    def cars(self, car_name):
        return "ComplexPattern[% s]" % (car_name)
```
2. Next class will serve as dictionary for the car's ids, also I will add here functions for set the car information and return the same information
```
class CarFamilies(object):

    car_family = {}

    def __new__(cls, name, car_family_id):
        try:
            id = cls.car_family[car_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.car_family[car_family_id] = id
        return id

    def set_car_info(self, car_info):

        cg = ComplexCars()
        self.car_info = cg.cars(car_info)

    def get_car_info(self):

        return (self.car_info)
```
## The Output of the program
```
-------------------Adapter Method------------------------
A Hybrid Car is a Battery and Engine vehicle
A Engine Car is a Engine vehicle
A Electric Car is a Battery vehicle
-------------------Composite Method------------------------
Toyota Group
	Toyota
		Corola Hybrid
		Rav4 Hybrid
		Prado Engine
	Lexus
		NX Engine
		RX Hybrid
		RZ 450e Electric
-------------------Decorator Method------------------------
before tuning : Toyota Corola Hybrid
after tuning : <200horsepowers+><yellow color with golden rims><Alcantara Wrap>Toyota Corola Hybrid
-------------------Proxy Method------------------------
Proxy in action. Checking to see if time of payment has passed...
You may go....
Proxy in action. Checking to see if time of payment has passed...
Your fee balance is smaller than 200, first pay the fee
-------------------Flyweight Method------------------------
id = 2046437182384
ComplexPattern[Toyota]
id = 2046437182336
ComplexPattern[Porsche]
id = 2046437182384
ComplexPattern[Toyota]
```


