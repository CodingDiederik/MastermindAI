class Mastermind():
    def spel():
        global gewonnen, verloren, pogingen
        import bord
        import Pionnen
        import AI

        running = True
        agent = AI.Agent()
        random = 'ja'
        antwoord_speler = [0, 0]
        ronde = 0

        #random = str(input('Wilt u de getallen willekeurig laten genereren? '))
        if random == 'ja':
            random = True
        else:
            random = False

        pionnen = Pionnen.pion()
        bord = bord.Bord()

        if random == False:
            pionnen.antwoord()
        else:
            pionnen.willekeurigantwoord()

        #print('Instructie voor het raden: Er zijn 6 kleuren aanwezig: paars, oranje, geel, lichtgroen, blauw en rood.')
        #print('Je raadt in één keer alle kleuren, dit doe je door de eerste letter van de kleur te noteren.')
        #print('Je krijgt dan bijvoorbeeld l o g p, dit staat dan voor lichtgroen, oranje, geel en paars.\n')

        while running == True:

            #geraad = pionnen.raden()
            geraad = agent.gokken(ronde, antwoord_speler)
            print('Antwoord is: ', pionnen.getantwoord())

            zwartenwit = pionnen.witenzwart(geraad)
            antwoord_speler = zwartenwit
            wit = zwartenwit[1]
            zwart = zwartenwit[0]

            ronde = bord.tekenBord(geraad, wit, zwart)

            if zwart == 4:
                gewonnen += 1
                print('Ik heb de juiste kleurencombinatie geraden!\n')
                running = False

            if ronde == 11 and running == True:
                verloren += 1
                running = False
                bord.tekenBord(geraad, wit, zwart)
                #print('Je hebt helaas niet de juiste kleurencombinatie geraden')
        pogingen.append(ronde + 1)

import time

gewonnen = 0
verloren = 0
pogingen = []
start = time.time()
hoeveelheid = int(input('Hoe vaak wilt u de computer een willekeurige code laten raden? '))
for i in range(0, hoeveelheid):
    Mastermind.spel()
eind = time.time()

print('\nDe computer heeft', gewonnen, 'gewonnen en', verloren, 'keer verloren.')
print('De computer deed gemiddeld', sum(pogingen) / len(pogingen), 'aantal pogingen over het gokken van een code.')
print('Dit alles is voltooid in', round(eind-start), 'seconden.')
