
class Agent():
    def __init__(self):
        self.fitness = 0
        self.mogelijkheden = 4 ** 6

    def addFitness(self, fitness):
        self.fitness += fitness

    def BerekenFitness(self, lijst):
        wit = lijst[1]

        if wit == 4:
            self.fitness += 10

    def gok(self):
        pass
    #TODO: Alle antwoord mogelijkheden genereren, dan antwoorden elimineren, hierdoor antwoord vinden

