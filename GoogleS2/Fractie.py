class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, other):
        numa = self.numarator*other.numitor+other.numarator*self.numitor
        numi = self.numitor*other.numitor
        return Fractie(numa, numi)

    def __sub__(self, other):
        numa = self.numarator * other.numitor - other.numarator * self.numitor
        numi = self.numitor * other.numitor
        return Fractie(numa, numi)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)


a = Fractie(1, 2)
b = Fractie(4, 7)
print(a)
print(a+b)
print(a-b)
print(a.inverse())
