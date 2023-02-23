import pygame
import random
g = 0
pole = []
for qwe in range(13):
    sps = []
    for spss in range(8):
        sps.append(0)
    pole.append(sps)
print(pole)
class Board:
    def __init__(self, w, h, size=40):
        self.w = w
        self.h = h
        self.s = size
    def render(self, screen):
        for q in range(self.w):
            for j in range(self.h):
                hqh = 55 + (j * 15)
                if pole[j][q] == 0:
                    pygame.draw.rect(screen, (155, 155, 155), (20 + self.s * (q), 20 + self.s * (j), self.s, self.s), 1)
                if pole[j][q] == 1:
                    pygame.draw.rect(screen, (hqh, hqh, hqh), (20 + self.s * (q), 20 + self.s * (j), self.s, self.s))
                if pole[j][q] == 2:
                    pygame.draw.rect(screen, (255, 0, 0), (20 + self.s * (q), 20 + self.s * (j), self.s, self.s))

ww = 8
hh = 13
g = 1
kpd = 0
nsp = 0
funf = 0
fp = [-1, 0]
a = Board(ww, hh)
file = open('set.txt', encoding='utf-8')
file1 = file.readlines()
nfn = [int(i) for i in file1[0].split()]
const = nfn[0]
rate = nfn[1]
file.close()
qwe = 0
fsp = [[]]

if __name__ == '__main__':
    pygame.init()
    font = pygame.font.Font(None, 30)
    size = width, height = 700, 560
    screen = pygame.display.set_mode(size)
    img = pygame.image.load('enter.png')
    running = True
    run = 0
    while running:
        if run == 0:
            screen.blit(img, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = 1
            if run != 1:
                continue
        screen.fill((0, 0, 0))
        a.render(screen)
        text1 = font.render(f'Скорость Падения = {100 - const}', True, [255, 255, 255])
        text11 = font.render(f'LEFT and RIGHT button', True, [255, 255, 255])
        text2 = font.render(f'Вероятность Античастицы = {rate} к 1', True, [255, 255, 255])
        text22 = font.render(f'UP and DOWN button', True, [255, 255, 255])
        screen.blit(text1, (350, 200))
        screen.blit(text2, (350, 300))
        screen.blit(text11, (350, 230))
        screen.blit(text22, (350, 330))
        if kpd == const and qwe < 3:
            if fp[0] != 12 and pole[fp[0] + 1][fp[1]] == 0:
                if fp[0] != -1:
                    pole[fp[0]][fp[1]] = 0
                fp[0] += 1
                pole[fp[0]][fp[1]] = 1
                kpd = 0
            if fp[0] == 12 or pole[fp[0] + 1][fp[1]] != 0:
                if fp[0] != 12:
                    if pole[fp[0] + 1][fp[1]] != 0:
                        if fp[0] < 2:
                            pole[fp[0]][fp[1]] = 0
                aa = random.randint(0, 7)
                while pole[0][aa] != 0:
                    aa = random.randint(0, 7)
                fp = [-1, aa]
                qwe = random.randint(1, 4 + ((rate - 1) * 2))
        if kpd == const and qwe >= 3:
            if fp[0] == 12 or pole[fp[0] + 1][fp[1]] == 1:
                if fp[0] == 12:
                    pole[fp[0]][fp[1]] = 0
                    aa = random.randint(0, 7)
                    while pole[0][aa] != 0:
                        aa = random.randint(0, 7)
                    fp = [-1, aa]
                elif pole[fp[0] + 1][fp[1]] == 1:
                    pole[fp[0] + 1][fp[1]] = 0
                    pole[fp[0]][fp[1]] = 0
                    aa = random.randint(0, 7)
                    while pole[0][aa] != 0:
                        aa = random.randint(0, 7)
                    fp = [-1, aa]
                qwe = random.randint(1, 4 + ((rate - 1) * 2))
                kpd = 0
            if fp[0] != 12 and pole[fp[0] + 1][fp[1]] == 0:
                if fp[0] != -1:
                    pole[fp[0]][fp[1]] = 0
                fp[0] += 1
                pole[fp[0]][fp[1]] = 2
                kpd = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if const < 91:
                        const += 10
                        kpd = 0
                        print(const)
                        file = open('set.txt', 'w')
                        file.write(f'{str(const)} {str(rate)}')
                        file.close()
                if event.key == pygame.K_RIGHT:
                    if const != 1:
                        const -= 10
                        kpd = 0
                        print(const)
                        file = open('set.txt', 'w')
                        file.write(f'{str(const)} {str(rate)}')
                        file.close()
                if event.key == pygame.K_UP:
                    rate += 1
                    kpd = 0
                    print(rate)
                    file = open('set.txt', 'w')
                    file.write(f'{str(const)} {str(rate)}')
                    file.close()
                if event.key == pygame.K_DOWN:
                    if rate > 1:
                        rate -= 1
                        kpd = 0
                        print(rate)
                        file = open('set.txt', 'w')
                        file.write(f'{str(const)} {str(rate)}')
                        file.close()
        kpd += 1
        pygame.display.flip()
    pygame.quit()
