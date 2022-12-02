class PuppyEnergy:

    def enjoyPlaying(self):
        print("You may go....")


class PuppyEnergyProxy:
    def __init__(self):

        self.energyLeft = 500
        self.puppy = None

    def enjoyPlaying(self):

        print("Proxy in action. Checking to see if puppy is tired...")
        if self.energyLeft >= 200:
            # If the energy is lower or equal to 200, give him threats.
            self.puppy = PuppyEnergy()
            self.puppy.enjoyPlaying()
        else:

            # Otherwise, don't instantiate the PuppyEnergy object.
            print("Your are out of energy, time to get some treats")