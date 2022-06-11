import os.path
import math

def main():
    import bord
    import Pionnen

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
            running = False

        if ronde == 11 and running == True:
            running = False
            bord.tekenBord(geraad, wit, zwart)
            #print('Je hebt helaas niet de juiste kleurencombinatie geraden')


if __name__ == '__main__':
    main()