class ComplexRetriver(object):

    def __init__(self):
        pass

    def dogs(self, dog_name):
        return "ComplexPattern[% s]" % dog_name


class RetriverFamilies(object):

    dog_family = {}

    def __new__(cls, name, dog_family_id):
        try:
            id = cls.dog_family[dog_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.dog_family[dog_family_id] = id
        return id

    def set_dog_info(self, dog_info):

        cg = ComplexRetriver()
        self.dog_info = cg.dogs(dog_info)

    def get_dog_info(self):

        return self.dog_info