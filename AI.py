import random

def pinnetjes(code, antwoord_spel, goki):
    "Gaat langs elke code, als dit de code was, kreeg het dan dezelfde aantal pinnetjes wit en zwart als je dit zou verglijken met de eerdere gok?"
    code = code.split() # maakt van de code losse elementen: 'c' 'c' 'c' 'c' ipv 'c c c c'
    zwart = 0
    wit = 0
    #print(code)

    pin1 = 'niet gebruikt'
    pin2 = 'niet gebruikt'
    pin3 = 'niet gebruikt'
    pin0 = 'niet gebruikt'

    if goki[0] == code[0]: #checken of zwart overeenkomt
        pin0 = 'gebruikt'
        zwart += 1
    if goki[1] == code[1]:
        pin1 = 'gebruikt'
        zwart += 1
    if goki[2] == code[2]:
        pin2 = 'gebruikt'
        zwart += 1
    if goki[3] == code[3]:
        pin3 = 'gebruikt'
        zwart += 1

    if goki[0] == code[1] and pin1 == 'niet gebruikt': # checken of wit overeenkomt
        wit += 1
        pin1 = 'gebruikt'
    elif goki[0] == code[2] and pin2 == 'niet gebruikt':
        wit += 1
        pin2 = 'gebruikt'
    elif goki[0] == code[3] and pin3 == 'niet gebruikt':
        wit += 1
        pin3 = 'gebruikt'

    if goki[1] == code[0] and pin0 == 'niet gebruikt':
        wit += 1
        pin0 = 'gebruikt'
    elif goki[1] == code[2] and pin2 == 'niet gebruikt':
        wit += 1
        pin2 = 'gebruikt'
    elif goki[1] == code[3] and pin3 == 'niet gebruikt':
        wit += 1
        pin3 = 'gebruikt'

    if goki[2] == code[1] and pin1 == 'niet gebruikt':
        wit += 1
        pin1 = 'gebruikt'
    elif goki[2] == code[0] and pin0 == 'niet gebruikt':
        wit += 1
        pin0 = 'gebruikt'
    elif goki[2] == code[3] and pin3 == 'niet gebruikt':
        wit += 1
        pin3 = 'gebruikt'

    if goki[3] == code[1] and pin1 == 'niet gebruikt':
        wit += 1
        pin1 = 'gebruikt'
    elif goki[3] == code[0] and pin0 == 'niet gebruikt':
        wit += 1
        pin0 = 'gebruikt'
    elif goki[3] == code[2] and pin2 == 'niet gebruikt':
        wit += 1
        pin2 = 'gebruikt'

    #print('wit: ', wit)
    #print('zwart: ', zwart)

    if zwart == antwoord_spel[0]: # komt het overeen met zwart
        if wit == antwoord_spel[1]: # komt het overeen met wit
            return True
        else:
            return False
    else:
        return False


def scoreberekenen(code, mogelijkheden):
    "Berekent een score voor elke code hoeveel hij minimaal elimineert, de hoogste wordt geraden. (Als ze evenhoog zijn, dan willekeurig eentje daarvan pakken."
    # Mogelijke antwoorden die we terugkrijgen van een code
    worstcase = 0
    wit = 0
    zwart = 0
    score = False
    eindscore = 0
    scores = []

    for wit in range(0, 4):
        for zwart in range(0, 4):
            if zwart + wit > 4:
                pass
            else:
                antwoord = [zwart, wit]
                for i in range(len(mogelijkheden)): # voor alle mogelijkheden kijken hoeveel mogelijkheden hij combineert
                    i -= 1
                    score = pinnetjes(code, antwoord, mogelijkheden[i])
                    if score == True:
                        eindscore+= 1
                        score = False
                scores.append(eindscore)

    return min(scores) # pakt de minimale score (worstcase scenario)




class Agent(): # computer
    def __init__(self, eerstegok):
        import itertools

        mogelijkheden = ['o', 'p', 'g', 'l', 'b', 'r']
        self.mogelijkheden = [' '.join(i) for i in itertools.product(mogelijkheden, repeat = 4)]
        print('Totaal aantal mogelijkheden: ', len(self.mogelijkheden)) # alle mogelijkheden aanmaken

        self.goki = eerstegok # willekeurige gok, 2 van dezelfde kleuren

    def gokken(self, ronde, antwoord_speler, pogingen, hoeveelheid): # Gebruik van Donald Knuth's algoritme: https://en.wikipedia.org/wiki/Mastermind_(board_game)

        remove = self.goki[0] + ' ' +self.goki[1] + ' ' + self.goki[2] + ' ' + self.goki[3]

        if ronde == 0: # dan de standaard gok

            return self.goki
        else:
            zoeken = 0

            self.mogelijkheden.remove(remove)

            niet_mogelijk = []
            import time
            for i in range(len(self.mogelijkheden)):
                code = self.mogelijkheden[i]
                #print(code)

                pinnen = pinnetjes(code, antwoord_speler, self.goki) # gaat kijken of bij die code,  ook dezelfde aantal witte en zwarte pinnetjes krijgt

                if pinnen == False:
                    #print('niet mogelijk')
                    niet_mogelijk.append(self.mogelijkheden[i])


            for i in range (len(niet_mogelijk)):
                self.mogelijkheden.remove(niet_mogelijk[i])

            if len(self.mogelijkheden) == 1:
                print('Er is nog 1 mogelijkheid over.')
                gok = self.mogelijkheden[0]
                self.goki = gok.split()
                return self.goki

            elif len(self.mogelijkheden) == 2:
                print('Er zijn nog 2 mogelijkheden over.')
                gok = self.mogelijkheden[0]
                self.goki = gok.split()
                return self.goki

            else:
                print('Er zijn nog', len(self.mogelijkheden), 'mogelijkheden over.')
                print('Op', round(len(pogingen) / hoeveelheid2 * 100, 1), 'procent\n')

                score_lijst = []
                for i in range(len(self.mogelijkheden)):
                    mogelijkheid  = self.mogelijkheden[i]
                    score_lijst.append(scoreberekenen(mogelijkheid, self.mogelijkheden)) # score algoritme

                #print(score_lijst)
                max_waarde = max(score_lijst)
                max_index = score_lijst.index(max_waarde)

                self.goki = self.mogelijkheden[max_index]
                self.goki = self.goki.split() # Hetgeen wat geraden gaat worden
                return self.goki
