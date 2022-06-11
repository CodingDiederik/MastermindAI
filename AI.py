import random


def aantalWit(raden, antwoord):
    wit = 0
    gebruikt1 = 0
    gebruikt2 = 0
    gebruikt3 = 0
    gebruikt4 = 0

    for i in range(0, 4):
        if raden[i] == antwoord[0] and gebruikt1 == 0:
            gebruikt1 += 1
            wit += 1
        elif raden[i] == antwoord[1] and gebruikt2 == 0:
            gebruikt2 += 1
            wit += 1
        elif raden[i] == antwoord[2] and gebruikt3 == 0:
            gebruikt3 += 1
            wit += 1
        elif raden[i] == antwoord[3] and gebruikt4 == 0:
            gebruikt4 += 1
            wit += 1

    return wit


def aantalZwart(raden, antwoord, wit):
    zwart = 0
    for i in range(0, 4):
        if raden[i] == antwoord[i]:
            wit -= 1
            zwart += 1

    return zwart, wit


def witenzwart(gok, wit, zwart, antwoord):
    zwart = aantalZwart(gok, antwoord, aantalWit(gok, antwoord))
    wit = zwart[1]
    zwart = zwart[0]
    return zwart, wit


class Agent():
    def __init__(self):
        import itertools

        mogelijkheden = ['o', 'p', 'g', 'l', 'b', 'r']
        self.mogelijkheden = [''.join(i) for i in itertools.product(mogelijkheden, repeat = 4)]
        #print(self.mogelijkheden)

        kleur1 = random.choice(['o', 'p', 'g', 'l', 'b', 'r'])
        kleur2 = random.choice(['o', 'p', 'g', 'l', 'b', 'r'])
        self.kleur1 = kleur1
        self.kleur2 = kleur2
        self.gok1 = [kleur1, kleur1, kleur2, kleur2]


    def gokken(self, ronde, wit, zwart, antwoord): # Gebruik van Donald Knuth's algoritme: https://en.wikipedia.org/wiki/Mastermind_(board_game)
        if ronde == 0:
            return self.gok1
        else:
            kan = []
            for i in S:
                if witenzwart(gok, wit, zwart, antwoord) == [zwart, wit]:
                    kan.append(i)
            self.mogelijkheden == kan
            if len(self.mogelijkheden == 1):
                print('Het antwoord is: ', self.mogelijkheden[0])
            else:
                print('Er zijn nog', len(self.mogelijkheden, 'mogelijkheden over.'))

                #TODO: Van de opties die kunnen, de beste selecteren

