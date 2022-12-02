class SimpleDog:
    """Represents a Dog """

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


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
