import copy


class purebread:
    def __init__(self, name):
        self.name = name

    def price(self):
        return "Expensive!"

    def food(self):
        return "Good meat and dog food"

    def __str__(self):
        return "Purebread dog"


class stray:
    def __init__(self, name):
        self.name = name

    def price(self):
        return "Free!"

    def food(self):
        return "Everything"

    def __str__(self):
        return "Stray dog"


class identity:

    def __init__(self):
        self.name = 'sandy'
        self.color = 'red'
        self.voice = 'high'

    def __str__(self):
        return 'The obj attributes cloned are: {} | {} | {}'.format(self.name, self.color, self.voice)


class canide:
    _attr_dict = {}

    def __init__(self):
        self.__dict__ = self._attr_dict


class singleton(canide):
    def __init__(self, **kwargs):
        canide.__init__(self)
        self._attr_dict.update(kwargs)

    def __str__(self):
        return str(self._attr_dict)


def get_pet(pet="purebread dog"):
    """the factory method"""
    pets = dict(purebread=purebread("lucky"), stray=stray("poor"))
    return pets[pet]


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


class builder():
    # generate the class pet and hand it over to hair_builder
    def __init__(self, pet=None):
        self.pet = pet

    def get_pet(self):
        self.pet = pet()


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


class petfactory:
    def __init__(self, name):
        self.name = name

    def get_pet_obj(self):
        return get_pet(self.name)

    def get_food(self):
        return get_pet(self.name).food()


class petStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet_obj()
        food = self._pet_factory.get_food()

        print(f"The pet is {pet} and the food is {food}, and the price is {pet.price()}")


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


dog1Class = petfactory('purebread')
petStore(dog1Class).show_pet()

dog2Class = petfactory('stray')
petStore(dog2Class).show_pet()

pet_obj = pet()
petBuilder = hair_builder(pet_obj)
build_pet = director(petBuilder)
build_pet.get_pet_without_hair()
pet_built = build_pet.get_pet()
print(pet_built)

pet_obj_hair = pet()
petBuilder = hair_builder(pet_obj_hair)
build_pet = director(petBuilder)
build_pet.get_pet_with_hair()
pet_built = build_pet.get_pet()
print(pet_built)

identity = identity()
proto_1 = prototype()
proto_1.register_class('sandy', identity)
dog_cloned = proto_1.clone('sandy', color='yellow', voice='low')
print(dog_cloned)

x = singleton(Kingdom="Animalia")
print(f"The current version is {x}")

y = singleton(Subkingdom="Bilateria")
print(f"The current version is {x}")

z = singleton(Infrakingdom="Deuterostomia")
print(f"The current version is {x}")