class Mastermind():
    def spel():
        import bord
        import Pionnen
        import AI

        running = True
        random = 'ja'

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

            geraad = pionnen.raden()

            wit = pionnen.aantalWit(geraad)
            zwart = pionnen.aantalZwart(geraad)
            wit = zwart[1]
            zwart = zwart[0]

            ronde = bord.tekenBord(geraad, wit, zwart)

            if zwart == 4:
                #print('Je hebt de juiste kleurencombinatie geraden!')
                beloning = 10
                running = False

            if ronde == 11 and running == True:
                running = False
                beloning = -10
                bord.tekenBord(geraad, wit, zwart)
                #print('Je hebt helaas niet de juiste kleurencombinatie geraden')

Mastermind.spel()