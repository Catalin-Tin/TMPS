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
