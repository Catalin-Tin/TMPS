import FactoryMethod


class petfactory:
    def __init__(self, name):
        self.name = name

    def get_pet_obj(self):
        return FactoryMethod.get_pet(self.name)

    def get_food(self):
        return FactoryMethod.get_pet(self.name).food()


class petStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet_obj()
        food = self._pet_factory.get_food()

        print(f"The pet is {pet} and the food is {food}, and the price is {pet.price()}")
