import pygame

pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./image/background.jpeg")
screen.blit(bg, (0,0))

#绘制英雄的飞机
hero = pygame.image.load("./image/me1.png")
screen.blit(hero, (200, 500))

pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()

#游戏循环
i = 0

while True:
    pass


pygame.quit()