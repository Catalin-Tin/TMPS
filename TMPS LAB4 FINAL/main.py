import AbstractMethod
import Builder
import PrototypeMethod
import SingletonMethod
import AdapterMethod
import CompositeMethod
import DecoratorMethod
import ProxyMethod
import FlyweightMethod
import IteratorMethod
import MediatorMethod
import ObserverMethod
import StratagyMethod
import VisitorMethod

""" main method """
if __name__ == "__main__":
    print("-------------------Factory and Abstract Method------------------------")
dog1Class = AbstractMethod.petfactory('purebread')
AbstractMethod.petStore(dog1Class).show_pet()

dog2Class = AbstractMethod.petfactory('stray')
AbstractMethod.petStore(dog2Class).show_pet()

print("-------------------Builder Method------------------------")
pet_obj = Builder.pet()
petBuilder = Builder.hair_builder(pet_obj)
build_pet = Builder.director(petBuilder)
build_pet.get_pet_without_hair()
pet_built = build_pet.get_pet()
print(pet_built)

pet_obj_hair = Builder.pet()
petBuilder = Builder.hair_builder(pet_obj_hair)
build_pet = Builder.director(petBuilder)
build_pet.get_pet_with_hair()
pet_built = build_pet.get_pet()
print(pet_built)

print("-------------------Prototype Method------------------------")
identity = PrototypeMethod.identity()
proto_1 = PrototypeMethod.prototype()
proto_1.register_class('sandy', identity)
dog_cloned = proto_1.clone('sandy', color='yellow', voice='low')
print(dog_cloned)

print("-------------------Singleton Method------------------------")
x = SingletonMethod.singleton(Kingdom="Animalia")
print(f"The current version is {x}")

y = SingletonMethod.singleton(Subkingdom="Bilateria")
print(f"The current version is {x}")

z = SingletonMethod.singleton(Infrakingdom="Deuterostomia")
print(f"The current version is {x}")

print("-------------------Adapter Method------------------------")
"""list to store objects"""
objects = []

HighEnergyDog = AdapterMethod.High()
objects.append(AdapterMethod.Adapter(HighEnergyDog, type=HighEnergyDog.HighEnergy))

MediumEnergyDog = AdapterMethod.Medium()
objects.append(AdapterMethod.Adapter(MediumEnergyDog, type=MediumEnergyDog.MediumEnergy))

LowEnergyDog = AdapterMethod.Low()
objects.append(AdapterMethod.Adapter(LowEnergyDog, type=LowEnergyDog.LowEnergy))

for obj in objects:
    print("{0} {1}".format(obj.name, obj.type()))

print("-------------------Composite Method------------------------")
topLevelMenu = CompositeMethod.CompositeElement("Dogs")
subMenuItem1 = CompositeMethod.CompositeElement("Long")
subMenuItem2 = CompositeMethod.CompositeElement("Short")
subMenuItem11 = CompositeMethod.LeafElement("Labrador")
subMenuItem12 = CompositeMethod.LeafElement("Akita")
subMenuItem13 = CompositeMethod.LeafElement("Harrier")
subMenuItem21 = CompositeMethod.LeafElement("Mops")
subMenuItem22 = CompositeMethod.LeafElement("Bulldog")
subMenuItem23 = CompositeMethod.LeafElement("Beagle")
subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)
subMenuItem1.add(subMenuItem13)
subMenuItem2.add(subMenuItem22)
subMenuItem2.add(subMenuItem22)
subMenuItem2.add(subMenuItem23)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2)
topLevelMenu.showDetails()

print("-------------------Decorator Method------------------------")
before_gfg = DecoratorMethod.SimpleDog("Husky")
after_gfg = DecoratorMethod.DogSize(DecoratorMethod.DogEnergy(DecoratorMethod.DogShedding(before_gfg)))

print("before changing :", before_gfg.render())
print("after changing :", after_gfg.render())

print("-------------------Proxy Method------------------------")
puppyProxy = ProxyMethod.PuppyEnergyProxy()
puppyProxy.enjoyPlaying()
puppyProxy.energyLeft = 100
puppyProxy.enjoyPlaying()

print("-------------------Flyweight Method------------------------")
dog_data = (('a', 1, 'Golden'), ('a', 2, 'Labrador'), ('b', 1, 'Golden'))
dog_family_objects = []
for i in dog_data:
    obj = FlyweightMethod.RetriverFamilies(i[0], i[1])
    obj.set_dog_info(i[2])
    dog_family_objects.append(obj)
for i in dog_family_objects:
    print("id = " + str(id(i)))
    print(i.get_dog_info())

print("-------------------Iterator Method------------------------")
print("Count the dogs in the house")
IteratorMethod.DogCounting()
print("Give them tag letters")
IteratorMethod.LetterAssigning()

print("-------------------Mediator Method------------------------")
first = MediatorMethod.PetStore('Pet Shop Labrador')  # petstore object
second = MediatorMethod.PetStore('Mister Dog')  # petstore object
third = MediatorMethod.PetStore('Global Pet Store')  # petstore object

first.sendType("It's a specific shop for a type of dog")
second.sendType("It's a generic shop for dogs")
third.sendType("It's a shop for any kind of pet")

print("-------------------Observer Method------------------------")
obj1 = ObserverMethod.Data('Cody Young Labrador')
obj2 = ObserverMethod.Data('Zuko Elder Husky')
view1 = ObserverMethod.DecimalViewer()
view2 = ObserverMethod.HexViewer()
view3 = ObserverMethod.OctalViewer()
obj1.attach(view1)
obj1.attach(view2)
obj1.attach(view3)
obj2.attach(view1)
obj2.attach(view2)
obj2.attach(view3)
obj1.data = 3
obj2.data = 12

print("-------------------Strategy Method------------------------")
print(StratagyMethod.PetCost(20000))
"""with discount strategy as 20 % discount"""
print(StratagyMethod.PetCost(20000, discount_strategy=StratagyMethod.twenty_percent_discount))
"""with discount strategy as On Sale Discount"""
print(StratagyMethod.PetCost(20000, discount_strategy=StratagyMethod.on_sale_discount))

print("-------------------Visitor Method------------------------")
"""creating objects for concrete classes"""
stCourse = VisitorMethod.AnimalAdoption()
ndCourse = VisitorMethod.PuppyMills()
rdCourse = VisitorMethod.VeterinaryCare()
"""Creating Visitors"""
instructor = VisitorMethod.Instructor()
student = VisitorMethod.Student()
"""Visitors visiting courses"""
stCourse.accept(instructor)
stCourse.accept(student)
ndCourse.accept(instructor)
ndCourse.accept(student)
rdCourse.accept(instructor)
rdCourse.accept(student)