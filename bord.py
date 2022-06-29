class Bord():
    def __init__(self): # startwaarden
        self.ronde = 0

        self.r1k1 = '_'
        self.r1k2 = '_'
        self.r1k3 = '_'
        self.r1k4 = '_'
        self.r2k1 = '_'
        self.r2k2 = '_'
        self.r2k3 = '_'
        self.r2k4 = '_'
        self.r3k1 = '_'
        self.r3k2 = '_'
        self.r3k3 = '_'
        self.r3k4 = '_'
        self.r4k1 = '_'
        self.r4k2 = '_'
        self.r4k3 = '_'
        self.r4k4 = '_'
        self.r5k1 = '_'
        self.r5k2 = '_'
        self.r5k3 = '_'
        self.r5k4 = '_'
        self.r6k1 = '_'
        self.r6k2 = '_'
        self.r6k3 = '_'
        self.r6k4 = '_'
        self.r7k1 = '_'
        self.r7k2 = '_'
        self.r7k3 = '_'
        self.r7k4 = '_'
        self.r8k1 = '_'
        self.r8k2 = '_'
        self.r8k3 = '_'
        self.r8k4 = '_'
        self.r9k1 = '_'
        self.r9k2 = '_'
        self.r9k3 = '_'
        self.r9k4 = '_'
        self.r10k1 = '_'
        self.r10k2 = '_'
        self.r10k3 = '_'
        self.r10k4 = '_'
        self.r11k1 = '_'
        self.r11k2 = '_'
        self.r11k3 = '_'
        self.r11k4 = '_'

        self.r0w = 0
        self.r0z = 0
        self.r1w = 0
        self.r1z = 0
        self.r2w = 0
        self.r2z = 0
        self.r3w = 0
        self.r3z = 0
        self.r4w = 0
        self.r4z = 0
        self.r5w = 0
        self.r5z = 0
        self.r6w = 0
        self.r6z = 0
        self.r7w = 0
        self.r7z = 0
        self.r8w = 0
        self.r8z = 0
        self.r9w = 0
        self.r9z = 0
        self.r10w = 0
        self.r10z = 0
        self.r11w = 0
        self.r11z = 0

    def get1gok(self):
        self.goki = [self.r0k1, self.r0k2, self.r0k3, self.r0k4]
        return self.goki

    def tekenBord(self, invoer, wit, zwart):
        if self.ronde == 0: # kijkt bij ronde en verandert het bord daardoor
            self.r0k1 = invoer[0]
            self.r0k2 = invoer[1]
            self.r0k3 = invoer[2]
            self.r0k4 = invoer[3]
            self.r0w = wit
            self.r0z = zwart
        elif self.ronde == 1:
            self.r1k1 = invoer[0]
            self.r1k2 = invoer[1]
            self.r1k3 = invoer[2]
            self.r1k4 = invoer[3]
            self.r1w = wit
            self.r1z = zwart
        elif self.ronde == 2:
            self.r2k1 = invoer[0]
            self.r2k2 = invoer[1]
            self.r2k3 = invoer[2]
            self.r2k4 = invoer[3]
            self.r2w = wit
            self.r2z = zwart
        elif self.ronde == 3:
            self.r3k1 = invoer[0]
            self.r3k2 = invoer[1]
            self.r3k3 = invoer[2]
            self.r3k4 = invoer[3]
            self.r3w = wit
            self.r3z = zwart
        elif self.ronde == 4:
            self.r4k1 = invoer[0]
            self.r4k2 = invoer[1]
            self.r4k3 = invoer[2]
            self.r4k4 = invoer[3]
            self.r4w = wit
            self.r4z = zwart
        elif self.ronde == 5:
            self.r5k1 = invoer[0]
            self.r5k2 = invoer[1]
            self.r5k3 = invoer[2]
            self.r5k4 = invoer[3]
            self.r5w = wit
            self.r5z = zwart
        elif self.ronde == 6:
            self.r6k1 = invoer[0]
            self.r6k2 = invoer[1]
            self.r6k3 = invoer[2]
            self.r6k4 = invoer[3]
            self.r6w = wit
            self.r6z = zwart
        elif self.ronde == 7:
            self.r7k1 = invoer[0]
            self.r7k2 = invoer[1]
            self.r7k3 = invoer[2]
            self.r7k4 = invoer[3]
            self.r7w = wit
            self.r7z = zwart
        elif self.ronde == 8:
            self.r8k1 = invoer[0]
            self.r8k2 = invoer[1]
            self.r8k3 = invoer[2]
            self.r8k4 = invoer[3]
            self.r8w = wit
            self.r8z = zwart
        elif self.ronde == 9:
            self.r9k1 = invoer[0]
            self.r9k2 = invoer[1]
            self.r9k3 = invoer[2]
            self.r9k4 = invoer[3]
            self.r9w = wit
            self.r9z = zwart
        elif self.ronde == 10:
            self.r10k1 = invoer[0]
            self.r10k2 = invoer[1]
            self.r10k3 = invoer[2]
            self.r10k4 = invoer[3]
            self.r10w = wit
            self.r10z = zwart
        elif self.ronde == 11:
            self.r11k1 = invoer[0]
            self.r11k2 = invoer[1]
            self.r11k3 = invoer[2]
            self.r11k4 = invoer[3]
            self.r11w = wit
            self.r11z = zwart
        # het tekenen van het bord
        print('\n-------------------------------------------')
        print('|', self.r11w, 'W', self.r11z, 'Z|    ', self.r11k1, '    ', self.r11k2, '    ', self.r11k3, '    ', self.r11k4, '    |')
        print('-------------------------------------------')
        print('|', self.r10w, 'W', self.r10z, 'Z|    ', self.r10k1, '    ', self.r10k2, '    ', self.r10k3, '    ', self.r10k4, '    |')
        print('-------------------------------------------')
        print('|', self.r9w, 'W', self.r9z, 'Z|    ', self.r9k1, '    ', self.r9k2, '    ', self.r9k3, '    ', self.r9k4, '    |')
        print('-------------------------------------------')
        print('|', self.r8w, 'W', self.r8z, 'Z|    ', self.r8k1, '    ', self.r8k2, '    ', self.r8k3, '    ', self.r8k4, '    |')
        print('-------------------------------------------')
        print('|', self.r7w, 'W', self.r7z, 'Z|    ', self.r7k1, '    ', self.r7k2, '    ', self.r7k3, '    ', self.r7k4, '    |')
        print('-------------------------------------------')
        print('|', self.r6w, 'W', self.r6z, 'Z|    ', self.r6k1, '    ', self.r6k2, '    ', self.r6k3, '    ', self.r6k4, '    |')
        print('-------------------------------------------')
        print('|', self.r5w, 'W', self.r5z, 'Z|    ', self.r5k1, '    ', self.r5k2, '    ', self.r5k3, '    ', self.r5k4, '    |')
        print('-------------------------------------------')
        print('|', self.r4w, 'W', self.r4z, 'Z|    ', self.r4k1, '    ', self.r4k2, '    ', self.r4k3, '    ', self.r4k4, '    |')
        print('-------------------------------------------')
        print('|', self.r3w, 'W', self.r3z, 'Z|    ', self.r3k1, '    ', self.r3k2, '    ', self.r3k3, '    ', self.r3k4, '    |')
        print('-------------------------------------------')
        print('|', self.r2w, 'W', self.r2z, 'Z|    ', self.r2k1, '    ', self.r2k2, '    ', self.r2k3, '    ', self.r2k4, '    |')
        print('-------------------------------------------')
        print('|', self.r1w, 'W', self.r1z, 'Z|    ', self.r1k1, '    ', self.r1k2, '    ', self.r1k3, '    ', self.r1k4, '    |')
        print('-------------------------------------------')
        print('|', self.r0w, 'W', self.r0z, 'Z|    ', self.r0k1, '    ', self.r0k2, '    ', self.r0k3, '    ', self.r0k4, '    |')
        print('-------------------------------------------\n')

        self.ronde += 1
        return self.ronde # geeft de ronde
