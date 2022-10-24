# Topic: Creational Design Patterns

### Course: TMPS
### Author: Tincu Catalin FAF-201

----
## OVERVIEW:
1. The factory method is a creational design pattern that provides an interface for a superclass to call and create an object with the type of the object created can be controlled and determined by the subclass.
2. Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.
3. Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.
4. Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.
5. Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.
   
## Factory Method
1. First I created 2 main classes called purebread and stray, these classes describe two different dogs which I will use later on
```
class purebread:
    def __init__(self, name):
        self.name = name

    def price(self):
        return "Expensive!"

    def food(self):
        return "Good meat and dog food"

    def __str__(self):
        return "Purebread dog"
```
```
class stray:
    def __init__(self, name):
        self.name = name

    def price(self):
        return "Free!"

    def food(self):
        return "Everything"

    def __str__(self):
        return "Stray dog"
```
2. After that, I create a function called get_pet which allows us to interchange the types of dogs in our case between classes without any big changes, in other words it allows me to call 2 different classes from my factory class.
```
def get_pet(pet="purebread dog"):
    """the factory method"""
    pets = dict(purebread=purebread("lucky"), stray=stray("poor"))
    return pets[pet]
```
## Abstract Method
To make an abstract method to my project it's enough to add two more classes, petfactory and petstore 
```
class petfactory:
    def __init__(self, name):
        self.name = name

    def get_pet_obj(self):
        return get_pet(self.name)

    def get_food(self):
        return get_pet(self.name).food()
```
```
class petStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet_obj()
        food = self._pet_factory.get_food()

        print(f"The pet is {pet} and the food is {food}, and the price is {pet.price()}")
```
## Builder
1. Builder is the most complex method from all fo them, in order to make it work I need a class called director that manages the dogs with hair and dogs without hair, or less hair let's say it like that
```
class director():
    def __init__(self, name):
        self.name = name

    def get_pet_without_hair(self):
        # one config
        self.name.get_pet()
        self.name.add_type()
        self.name.add_color()
        self.name.add_length()

    def get_pet_with_hair(self):
        # another config
        self.name.get_pet()
        self.name.add_type()
        self.name.add_color()
        self.name.add_length()
        self.name.add_hair()

    def get_pet(self):
        return self.name.pet
```
2. Next we should have a class builder, that will generate class pet and hand it over to hair_builder
```
class builder():
    # generate the class pet and hand it over to hair_builder
    def __init__(self, pet=None):
        self.pet = pet

    def get_pet(self):
        self.pet = pet()
```
3. The second builder, that uses the information from the first one and initialise the attributes of the class, such as type, color, length and hair
```
class hair_builder(builder):
    # this initialise the attributes of the class
    def add_type(self):
        self.pet.type = 'Retriever'

    def add_color(self):
        self.pet.color = "Golden"

    def add_length(self):
        self.pet.length = '25cm'

    def add_hair(self):
        self.pet.hair = 'Straight Hair'
```
4. And the last step for builder method is creating a core class which will output all the results from the program
```
class pet():
    # this is the core class to be initialised
    def __init__(self):
        self.type = None
        self.color = None
        self.length = None
        self.hair = None

    def __str__(self):
        if self.hair:
            return f"This is TYPE: {self.type}, COLOR: {self.color}, LENGTH: {self.length} WITH HAIR: {self.hair}"
        else:
            return f"This is TYPE: {self.type}, COLOR: {self.color}, LENGTH: {self.length} WITH NO HORN"
```
## Prototype
1. For being able to clone a dog from another existing dog, I need a class prototype
```
class prototype:

    def __init__(self):
        self.obj_dict = {}

    def register_class(self, name, obj):
        self.obj_dict[name] = obj

    def unregister_class(self, name):
        del self.obj_dict[name]

    def clone(self, name, **attr):
        obj_aux = copy.deepcopy(self.obj_dict.get(name))
        obj_aux.__dict__.update(attr)

        return obj_aux
```
2. After that we need a specific class from which we will clone the dog identity
```
class identity:

    def __init__(self):
        self.name = 'sandy'
        self.color = 'red'
        self.voice = 'high'

    def __str__(self):
        return 'The obj attributes {} | {} | {}'.format(self.name, self.color, self.voice)
```
## Singleton
1. In my example I describe the canide family writing it in a specific dictionary that may easily be updated by adding a new line of text to it, for that we need 2 classes, one called canide and another one as method itself 
```
class canide:
    _attr_dict = {}

    def __init__(self):
        self.__dict__ = self._attr_dict
```
```
class singleton(canide):
    def __init__(self, **kwargs):
        canide.__init__(self)
        self._attr_dict.update(kwargs)

    def __str__(self):
        return str(self._attr_dict)
```
## The Output of the program
```
The pet is Purebread dog and the food is Good meat and dog food, and the price is Expensive!
The pet is Stray dog and the food is Everything, and the price is Free!
This is TYPE: Retriever, COLOR: Golden, LENGTH: 25cm WITH NO HORN
This is TYPE: Retriever, COLOR: Golden, LENGTH: 25cm WITH HAIR: Straight Hair
The obj attributes cloned are: sandy | yellow | low
The current version is {'Kingdom': 'Animalia'}
The current version is {'Kingdom': 'Animalia', 'Subkingdom': 'Bilateria'}
The current version is {'Kingdom': 'Animalia', 'Subkingdom': 'Bilateria', 'Infrakingdom': 'Deuterostomia'}
```



