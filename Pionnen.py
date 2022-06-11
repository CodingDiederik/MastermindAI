
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

    def willekeurigantwoord(self):
        print('Een willekeurige kleurenset wordt gegenereerd.')

        kleur1 = self.random.choice(['o', 'p', 'g', 'l', 'b', 'r'])
        kleur2 = self.random.choice(['o', 'p', 'g', 'l', 'b', 'r'])
        kleur3 = self.random.choice(['o', 'p', 'g', 'l', 'b', 'r'])
        kleur4 = self.random.choice(['o', 'p', 'g', 'l', 'b', 'r'])

        self.antwoord = [kleur1, kleur2, kleur3, kleur4]
        #print(self.antwoord)

    def raden(self):
        print('De kleuren zijn: paars, oranje, geel, lichtgroen, blauw en rood.')
        raden = str(input('Welke kleuren wilt u raden? '))
        #raden = 'l o g p'
        raden = raden.split()
        return raden

    def aantalWit(self, raden):
        self.wit = 0
        self.gebruikt1 = 0
        self.gebruikt2 = 0
        self.gebruikt3 = 0
        self.gebruikt4 = 0

        for i in range(0, 4):
            if raden[i] == self.antwoord[0] and self.gebruikt1 == 0:
                self.gebruikt1 += 1
                self.wit += 1
            elif raden[i] == self.antwoord[1] and self.gebruikt2 == 0:
                self.gebruikt2 += 1
                self.wit += 1
            elif raden[i] == self.antwoord[2] and self.gebruikt3 == 0:
                self.gebruikt3 += 1
                self.wit += 1
            elif raden[i] == self.antwoord[3] and self.gebruikt4 == 0:
                self.gebruikt4 += 1
                self.wit += 1

        return self.wit

    def aantalZwart(self, raden):
        self.zwart = 0
        for i in range(0,4):
            if raden[i] == self.antwoord[i]:
                self.wit -= 1
                self.zwart += 1

        return self.zwart, self.wit
