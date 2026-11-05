
import random
import math

class Boson:
    isFermion = False

    def __init__(self, name, spin, momentum):
        self.name = name
        self.spin = spin
        self.momentum = momentum

    def PrintInfo(self):
        print("Name:", self.name)
        print("Spin:", self.spin)
        print("Momentum:", self.momentum)
        print("Is Fermion:", self.isFermion)


class Higgs(Boson):
    MassSigma = 1

    def __init__(self, name, spin, momentum, MassMean):
        super().__init__(name, spin, momentum)
        self.MassMean = MassMean

    def PrintInfo(self):
        super().PrintInfo()
        print("Mass Mean:", self.MassMean)
        print("Mass Sigma:", self.MassSigma)

    def Energy(self):
        mass = random.gauss(self.MassMean, self.MassSigma)
        energy = math.sqrt(mass**2 + self.momentum**2)
        return energy
