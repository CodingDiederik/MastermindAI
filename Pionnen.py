
class pion():
    def __init__ (self):
        import random
        self.random = random
        self.paars = 'paars'
        self.oranje = 'oranje'
        self.roze = 'geel'
        self.groen = 'lichtgroen'
        self.blauw = 'blauw'
        self.rood = 'rood'

    def antwoord(self):
        print('De kleuren zijn: paars, oranje, geel, lichtgroen, blauw en rood')
        print('Voer de eerste letter van de kleur in, bij lichtgroen is dit bijvoorbeeld dus l')
        kleur1 = str(input('Wat is kleur 1? '))
        kleur2 = str(input('Wat is kleur 2? '))
        kleur3 = str(input('Wat is kleur 3? '))
        kleur4 = str(input('Wat is kleur 4? '))
        #kleur1 = 'o'
        #kleur2 = 'o'
        #kleur3 = 'o'
        #kleur4 = 'o'
        self.antwoord = [kleur1, kleur2, kleur3, kleur4]

    def getantwoord(self):
        return self.antwoord

    def willekeurigantwoord(self):
        #print('Een willekeurige kleurenset wordt gegenereerd.')

        kleur1 = self.random.choice(['o', 'p', 'g', 'l', 'b', 'r'])
        kleur2 = self.random.choice(['o', 'p', 'g', 'l', 'b', 'r'])
        kleur3 = self.random.choice(['o', 'p', 'g', 'l', 'b', 'r'])
        kleur4 = self.random.choice(['o', 'p', 'g', 'l', 'b', 'r'])

        self.antwoord = [kleur1, kleur2, kleur3, kleur4]
        #print(self.antwoord)

    def raden(self):
        print('De kleuren zijn: paars, oranje, geel, lichtgroen, blauw en rood.')
        raden = str(input('Welke kleuren wilt u raden? '))
        raden = raden.split()
        return raden

    def witenzwart(self, geraad):
        wit = 0
        zwart = 0
        pin1 = 'niet gebruikt'
        pin2 = 'niet gebruikt'
        pin3 = 'niet gebruikt'
        pin0 = 'niet gebruikt'
        code = self.antwoord

        if geraad[0] == code[0]:
            pin0 = 'gebruikt'
            zwart += 1
        if geraad[1] == code[1]:
            pin1 = 'gebruikt'
            zwart += 1
        if geraad[2] == code[2]:
            pin2 = 'gebruikt'
            zwart += 1
        if geraad[3] == code[3]:
            pin3 = 'gebruikt'
            zwart += 1

        if geraad[0] == code[1] and pin1 == 'niet gebruikt':
            wit += 1
            pin1 = 'gebruikt'
        elif geraad[0] == code[2] and pin2 == 'niet gebruikt':
            wit += 1
            pin2 = 'gebruikt'
        elif geraad[0] == code[3] and pin3 == 'niet gebruikt':
            wit += 1
            pin3 = 'gebruikt'

        if geraad[1] == code[0] and pin0 == 'niet gebruikt':
            wit += 1
            pin0 = 'gebruikt'
        elif geraad[1] == code[2] and pin2 == 'niet gebruikt':
            wit += 1
            pin2 = 'gebruikt'
        elif geraad[1] == code[3] and pin3 == 'niet gebruikt':
            wit += 1
            pin3 = 'gebruikt'

        if geraad[2] == code[1] and pin1 == 'niet gebruikt':
            wit += 1
            pin1 = 'gebruikt'
        elif geraad[2] == code[0] and pin0 == 'niet gebruikt':
            wit += 1
            pin0 = 'gebruikt'
        elif geraad[2] == code[3] and pin3 == 'niet gebruikt':
            wit += 1
            pin3 = 'gebruikt'

        if geraad[3] == code[1] and pin1 == 'niet gebruikt':
            wit += 1
            pin1 = 'gebruikt'
        elif geraad[3] == code[0] and pin0 == 'niet gebruikt':
            wit += 1
            pin0 = 'gebruikt'
        elif geraad[3] == code[2] and pin2 == 'niet gebruikt':
            wit += 1
            pin2 = 'gebruikt'

        return zwart, wit
