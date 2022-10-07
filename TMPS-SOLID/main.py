class Cylinder:
    def __init__(self, race: int, high: int):
        self.race = race
        self.high = high

    def increase(self):
        self.race += 1

    def decrease(self):
        self.race -= 1

    def multiply(self, value):
        self.high *= value

    def __str__(self):
        return f'{self.race}-{self.high}'


class Aria(Cylinder):

    def __init__(self, race: int, high: int, pi: float, arial: float, ariab: float, ariat: float):
        super().__init__(race, high)
        self.pi = pi
        self.arial = arial
        self.ariab = ariab
        self.ariat = ariat

    def laterala(self):
        self.arial = 2 * self.pi * self.race * self.high

    def baza(self):
        self.ariab = self.pi * (self.race*self.race)

    def totala(self):
        self.ariat = 2 * self.ariab + self.arial

    def __str__(self):
        return f'{self.race}cm  {self.high}cm  {self.pi} = Aria Laterala: {self.arial}, Aria Bazei: {self.ariab}, Aria Totala: {self.ariat}'


my_form = Aria(3, 4, 3.14, 0, 0, 0)

print(my_form)

my_form.laterala()
my_form.baza()
my_form.totala()

print(my_form)

