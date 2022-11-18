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


class LeafElement:
    """Class representing objects at the bottom or Leaf of the hierarchy tree."""

    def __init__(self, *args):
        """'Takes the first positional argument and assigns to member variable "position"."""
        self.position = args[0]

    def showDetails(self):
        """Prints the position of the child element."""
        print("\t", end="")
        print(self.position)


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


class CompositeElement:
    """Class representing objects at any level of the hierarchy
     tree except for the bottom or leaf level. Maintains the child
      objects by adding and removing them from the tree structure."""

    def __init__(self, *args):
        """Takes the first positional argument and assigns to member
         variable "position". Initializes a list of children elements."""
        self.position = args[0]
        self.children = []

    def add(self, child):
        """Adds the supplied child element to the list of children
         elements "children"."""
        self.children.append(child)

    def remove(self, child):
        """Removes the supplied child element from the list of
        children elements "children"."""
        self.children.remove(child)

    def showDetails(self):
        """Prints the details of the component element first. Then,
        iterates over each of its children, prints their details by
        calling their showDetails() method."""
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()


class BasicCar:
    """Represents a Mark of Car """

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


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


class Highway:

    def drivingOnHighway(self):
        print("You may go....")


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


class ComplexCars(object):

    def __init__(self):
        pass

    def cars(self, car_name):
        return "ComplexPattern[% s]" % (car_name)


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


""" main method """
if __name__ == "__main__":
    print("-------------------Adapter Method------------------------")
    """list to store objects"""
    objects = []

    HybridCar = Hybrid()
    objects.append(Adapter(HybridCar, type=HybridCar.BatteryEngine))

    StandardCar = Standard()
    objects.append(Adapter(StandardCar, type=StandardCar.Engine))

    ElectricCar = Electric()
    objects.append(Adapter(ElectricCar, type=ElectricCar.Battery))

    for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.type()))

    print("-------------------Composite Method------------------------")

    topLevelMenu = CompositeElement("Toyota Group")
    subMenuItem1 = CompositeElement("Toyota")
    subMenuItem2 = CompositeElement("Lexus")
    subMenuItem11 = LeafElement("Corola Hybrid")
    subMenuItem12 = LeafElement("Rav4 Hybrid")
    subMenuItem13 = LeafElement("Prado Engine")
    subMenuItem21 = LeafElement("NX Engine")
    subMenuItem22 = LeafElement("RX Hybrid")
    subMenuItem23 = LeafElement("RZ 450e Electric")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem1.add(subMenuItem13)
    subMenuItem2.add(subMenuItem21)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem23)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()

    print("-------------------Decorator Method------------------------")
    before_gfg = BasicCar("Toyota Corola Hybrid")
    after_gfg = EngineTuning(BodyTuning(InteriorTuning(before_gfg)))

    print("before tuning :", before_gfg.render())
    print("after tuning :", after_gfg.render())

    print("-------------------Proxy Method------------------------")
    highwayProxy = HighwayProxy()
    highwayProxy.drivingOnHighway()
    highwayProxy.timeLeft = 100
    highwayProxy.drivingOnHighway()

    print("-------------------Flyweight Method------------------------")
    car_data = (('a', 1, 'Toyota'), ('a', 2, 'Porsche'), ('b', 1, 'Toyota'))
    car_family_objects = []
    for i in car_data:
        obj = CarFamilies(i[0], i[1])
        obj.set_car_info(i[2])
        car_family_objects.append(obj)
    for i in car_family_objects:
        print("id = " + str(id(i)))
        print(i.get_car_info())
