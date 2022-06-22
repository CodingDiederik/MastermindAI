class Mastermind():
    def spel():
        global gewonnen, verloren, pogingen, hoeveelheid
        import bord
        import Pionnen
        import AI

        running = True
        agent = AI.Agent()
        random = 'ja'
        antwoord_speler = [0, 0]
        ronde = 0

        #random = str(input('Wilt u de getallen willekeurig laten genereren? '))
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

        #print('Instructie voor het raden: Er zijn 6 kleuren aanwezig: paars, oranje, geel, lichtgroen, blauw en rood.')
        #print('Je raadt in één keer alle kleuren, dit doe je door de eerste letter van de kleur te noteren.')
        #print('Je krijgt dan bijvoorbeeld l o g p, dit staat dan voor lichtgroen, oranje, geel en paars.\n')

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

            if ronde == 11 and running == True: # eindigt de code
                verloren += 1
                running = False
                bord.tekenBord(geraad, wit, zwart)
                print('Ik heb helaas na 12 rondes niet de juiste kleurcombinatie kunnen raden.')
        pogingen.append(ronde + 1)
def main():
    global gewonnen, verloren, pogingen, hoeveelheid
    import time

    gewonnen = 0
    verloren = 0
    pogingen = []

    start = time.time() # start de klok

    hoeveelheid = int(input('Hoe vaak wilt u de computer een willekeurige code laten raden? ')) # hoe vaak de computer de code oplost

    for i in range(0, hoeveelheid): # voert het zo vaak uit als bij mogelijkheden is aangegeven
        print('\n-------------------------------------------')
        print('Spel', i + 1)
        Mastermind.spel()
    eind = time.time() # tijd van het einde

    print('\nDe computer heeft', gewonnen, 'keer gewonnen en', verloren, 'keer verloren.') # informatie weergeven
    print('De computer deed gemiddeld', round(sum(pogingen) / len(pogingen), 1), 'aantal pogingen over het gokken van een code.')
    print('De computer deed er', round(eind-start, 1), 'seconden over.')


if __name__ == '__main__': # hoofdscript
    main()
