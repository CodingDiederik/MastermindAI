class Mastermind():
    def spel():
        global gewonnen, verloren, pogingen, hoeveelheid, eerstegok, highscore, bestegok
        import bord
        import Pionnen
        import AI

        running = True
        agent = AI.Agent(eerstegok)
        random = 'ja'
        antwoord_speler = [0, 0]
        ronde = 0

        if random == 'ja': # Random code generen ja of nee
            random = True
        else:
            random = False

        pionnen = Pionnen.pion() # intialiseer pionnen
        bord = bord.Bord() # intialiseer bord

        if random == False:
            pionnen.antwoord()
        else:
            pionnen.willekeurigantwoord() # willekeurig antwoord laten genereren

        while running == True: # game lus

            #geraad = pionnen.raden()
            geraad = agent.gokken(ronde, antwoord_speler, pogingen, hoeveelheid) # computer gaat een gok maken
            print('Antwoord is: ', pionnen.getantwoord()) # print het antwoord

            zwartenwit = pionnen.witenzwart(geraad)
            antwoord_speler = zwartenwit
            wit = zwartenwit[1]
            zwart = zwartenwit[0]

            ronde = bord.tekenBord(geraad, wit, zwart) # tekenen van het bord

            if zwart == 4: # eindigt de code
                gewonnen += 1
                print('Ik heb de juiste kleurencombinatie geraden in', ronde + 1, 'stappen')
                running = False
                #print(highscore)
                #print(ronde)
                if ronde < highscore:
                    highscore = ronde
                    print('Nieuwe highscore!!')
                    bestegok = bord.get1gok()

            if ronde == 11 and running == True: # eindigt de code
                verloren += 1
                running = False
                bord.tekenBord(geraad, wit, zwart)
                print('Ik heb helaas na 12 rondes niet de juiste kleurcombinatie kunnen raden.')
        pogingen.append(ronde + 1)

def main():
    global gewonnen, verloren, pogingen, hoeveelheid, eerstegok, highscore, bestegok
    import time
    import random

    gewonnen = 0
    verloren = 0
    highscore = 999
    pogingen = []

    mogelijkheden = ['o', 'p', 'g', 'l', 'b', 'r']
    print('De kleuren zijn: paars, oranje, geel, lichtgroen, blauw en rood.')

    kleur1 = random.choice(mogelijkheden)
    kleur2 = random.choice(mogelijkheden)
    kleur3 = random.choice(mogelijkheden)
    kleur4 = random.choice(mogelijkheden)

    eerstegok = [kleur1, kleur2, kleur3, kleur4]

    hoeveelheid = int(input('Hoe vaak wilt u de computer een willekeurige code laten raden om de beste eerste gok te vinden?')) # hoe vaak de computer de code oplost

    start = time.time() # start de klok

    for i in range(0, hoeveelheid): # voert het zo vaak uit als bij mogelijkheden is aangegeven
        print('\n-------------------------------------------')
        print('Spel', i + 1)

        kleur1 = random.choice(mogelijkheden)
        kleur2 = random.choice(mogelijkheden)
        kleur3 = random.choice(mogelijkheden)
        kleur4 = random.choice(mogelijkheden)

        eerstegok = [kleur1, kleur2, kleur3, kleur4]

        Mastermind.spel()

    eind = time.time() # tijd van het einde


    print('De best code is ', bestegok)
    print('De computer deed er', round(eind - start, 1), 'seconden over.')
    print('Bij deze gok deed hij er ', highscore, ' zetten over.')

    eerstegok = bestegok

    hoeveelheid = int(input('Hoe vaak wilt u de computer een code laten raden?'))
    start = time.time()
    for i in range(0, hoeveelheid):
        print('\n-------------------------------------------')
        print('Spel', i + 1)
        Mastermind.spel()

    eind = time.time()

    print('\nDe computer heeft', gewonnen, 'keer gewonnen en', verloren, 'keer verloren.')  # informatie weergeven
    print('De computer deed er', round(eind - start, 1), 'seconden over.')
    print('De computer deed gemiddeld', round(sum(pogingen) / len(pogingen), 1), 'aantal pogingen over het gokken van een code.')

if __name__ == '__main__': # hoofdscript
    main()
