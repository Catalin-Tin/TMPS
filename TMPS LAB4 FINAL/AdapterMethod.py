class High:

    def __init__(self):
        self.name = "High Energy dogs"

    def HighEnergy(self):
        return "likes to play a lot"


class Medium:

    def __init__(self):
        self.name = "Medium Energy dog"

    def MediumEnergy(self):
        return "pray for some attention"


class Low:

    def __init__(self):
        self.name = "Low Energy dogs"

    def LowEnergy(self):
        return "don't bother you that much"


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



