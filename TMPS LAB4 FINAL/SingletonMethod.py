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
