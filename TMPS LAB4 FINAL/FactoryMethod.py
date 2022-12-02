
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


def get_pet(pet="purebread dog"):
    """the factory method"""
    pets = dict(purebread=purebread("lucky"), stray=stray("poor"))
    return pets[pet]
