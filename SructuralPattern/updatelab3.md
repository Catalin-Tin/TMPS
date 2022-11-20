# Topic: Structural Design Patterns

### Course: TMPS
### Author: Tincu Catalin FAF-201

----
## OVERVIEW:
1. Adapter method is a Structural Design Pattern which helps us in making the incompatible objects adaptable to each other. The Adapter method is one of the easiest methods to understand because we have a lot of real-life examples that show the analogy with it. The main purpose of this method is to create a bridge between two incompatible interfaces. 
2. Composite Method is a Structural Design Pattern which describes a group of objects that is treated the same way as a single instance of the same type of the objects. The purpose of the Composite Method is to Compose objects into Tree type structures to represent the whole-partial hierarchies.
3. Decorator Method is a Structural Design Pattern which allows you to dynamically attach new behaviors to objects without changing their implementation by placing these objects inside the wrapper objects that contains the behaviors.
## Adapter Method
1. First step is to create some classes that will be created by some Adapter class
```
class High:

    def __init__(self):
        self.name = "High Energy dogs"

    def HighEnergy(self):
        return "likes to play a lot"


class Medium:

    def __init__(self):
        self.name = "Medium Energy dogs"

    def MediumEnergy(self):
        return "search for some attention"


class Low:

    def __init__(self):
        self.name = "Low Energy dogs"

    def LowEnergy(self):
        return "don't botter you that much"
```
2. Next Step is to create that specific Adapter class that will adapt the object by replacing methods
```
class Adapter:
    """
    Adapts an object by replacing methods.
    """

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
HighEnergyDog = High()
objects.append(Adapter(HighEnergyDog, type=HighEnergyDog.HighEnergy))

MediumEnergyDog = Medium()
objects.append(Adapter(MediumEnergyDog, type=MediumEnergyDog.MediumEnergy))

LowEnergyDog = Low()
objects.append(Adapter(LowEnergyDog, type=LowEnergyDog.LowEnergy))
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
class SimpleDog:
    """Represents a Dog """

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text
```
2. Next step is adding feature classes that will boost the initial object, I will add for instance some tuning properties
```
class DogSize(SimpleDog):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<Giant>{}".format(self._wrapped.render())


class DogEnergy(SimpleDog):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<High>{}".format(self._wrapped.render())


class DogShedding(SimpleDog):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<Heavy>{}".format(self._wrapped.render())
```
3. And this is how you call this method
```
 before_gfg = SimpleDog("Husky")
    after_gfg = DogSize(DogEnergy(DogShedding(before_gfg)))
```
## The Output of the program
```
-------------------Adapter Method------------------------
A High Energy dogs likes to play a lot
A Medium Energy dogs search for some attention
A Low Energy dogs don't botter you that much
-------------------Composite Method------------------------
Dogs
	Long
		Labrador
		Akita
		Harrier
	Short
		Mops
		Bulldog
		Beagle
-------------------Decorator Method------------------------
before tuning : Husky
after tuning : <Giant><High><Heavy>Husky
```


