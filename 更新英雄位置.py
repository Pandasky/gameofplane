import pygame

pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./image/background.jpeg")
screen.blit(bg, (0,0))

#绘制英雄的飞机
hero = pygame.image.load("./image/me1.png")
screen.blit(hero, (150, 300))

pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()

#1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

#游戏循环
while True:
    clock.tick(60)

    hero_rect.y -= 5

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    pygame.display.update()


pygame.quit()