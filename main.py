import pygame
import sys
from pygame.locals import QUIT

pygame.init()

win_width = 700
win_height = 500
DISPLAYSURF = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Maze')

background = pygame.transform.scale(pygame.image.load("background.jpg"),
                                    (win_width, win_height))


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(player_image), (40, 40))
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        DISPLAYSURF.blit(self.image, (self.rect.x, self.rect.y))

    def refresh(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.player_speed
        if keys[pygame.K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.player_speed
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.player_speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.player_speed



class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width-85:
            self.side = "left"

        if self.side == "left":
            self.rect.x -= self.player_speed
        else:
            self.rect.x += self.player_speed


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        DISPLAYSURF.blit(self.image, (self.rect.x, self.rect.y))


player = Player("hero.png", 10, win_height-80, 5)
monster = Enemy("cyborg.png", win_width-80, 280, 2)
final = GameSprite("treasure.png", win_width-120, win_height-80, 0)

w1 = Wall((22, 201, 187), 100, 20, 580, 10)
w2 = Wall((22, 201, 187), 100, 20, 10, 350)
w3 = Wall((22, 201, 187), 200, 20, 10, 150)
w4 = Wall((22, 201, 187), 200, 160, 240, 10)
w5 = Wall((22, 201, 187), 200, 250, 100, 10)
w6 = Wall((22, 201, 187), 200, 250, 10, 350)
w7 = Wall((22, 201, 187), 300, 250, 10, 350)
w8 = Wall((22, 201, 187), 430, 169, 10, 250)
w9 = Wall((22, 201, 187), 550, 350, 10, 250)
w10 = Wall((22, 201, 187), 550, 130, 10, 145)

pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play()

kick = pygame.mixer.Sound("kick.ogg")
money = pygame.mixer.Sound("money.ogg")

pygame.font.init()
text = pygame.font.Font(None, 70)
win = text.render("YOU WIN!", True, (255,215,0))
lose = text.render("YOU LOSE!", True, (180,0,0))

clock = pygame.time.Clock()
FPS = 60

finish = False
lose_life = False
level = 1
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if finish != True:
            
        DISPLAYSURF.blit(background, (0, 0))
        player.reset()
        player.update()
        monster.reset()
        monster.update()
        final.reset()


        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        
        if (pygame.sprite.collide_rect(player, monster) or
            pygame.sprite.collide_rect(player, w1) or
            pygame.sprite.collide_rect(player, w2) or
            pygame.sprite.collide_rect(player, w3) or
            pygame.sprite.collide_rect(player, w4) or
            pygame.sprite.collide_rect(player, w5) or
            pygame.sprite.collide_rect(player, w6) or
            pygame.sprite.collide_rect(player, w7) or
            pygame.sprite.collide_rect(player, w8) or
            pygame.sprite.collide_rect(player, w9) or
            pygame.sprite.collide_rect(player, w10)):
            #pygame.sprite.collide_rect(player, w?)) or Для нових стінок
            finish = True
            DISPLAYSURF.blit(lose, (200,200))
            lose_life = True
            kick.play()

        if pygame.sprite.collide_rect(player, final):
            finish = True
            DISPLAYSURF.blit(win, (200,200))
            money.play()
    else:
        w1.kill()
        w2.kill()
        w3.kill()
        w4.kill()
        w5.kill()
        w6.kill()
        w7.kill()
        w8.kill()
        w9.kill()
        w10.kill()        
        pygame.time.delay(1000)
        if lose_life != True:
            level += 1
        if level == 1:
            player.refresh(10, win_height-80)
            w1 = Wall((22, 201, 187), 100, 20, 580, 10)
            w2 = Wall((22, 201, 187), 100, 20, 10, 350)
            w3 = Wall((22, 201, 187), 200, 20, 10, 150)
            w4 = Wall((22, 201, 187), 200, 160, 240, 10)
            w5 = Wall((22, 201, 187), 200, 250, 100, 10)
            w6 = Wall((22, 201, 187), 200, 250, 10, 350)
            w7 = Wall((22, 201, 187), 300, 250, 10, 350)
            w8 = Wall((22, 201, 187), 430, 169, 10, 250)
            w9 = Wall((22, 201, 187), 550, 350, 10, 250)
            w10 = Wall((22, 201, 187), 550, 130, 10, 145)
            finish = False
            lose_life = False
        elif level == 2:
            player.refresh(10, win_height-80)
            w1 = Wall((22, 201, 187), 10, 2, 58, 10)
            w2 = Wall((22, 201, 187), 10, 20, 10, 35)
            w3 = Wall((22, 201, 187), 20, 2, 10, 15)
            w4 = Wall((22, 201, 187), 20, 16, 24, 10)
            w5 = Wall((22, 201, 187), 20, 25, 10, 10)
            w6 = Wall((22, 201, 187), 20, 250, 10, 35)
            w7 = Wall((22, 201, 187), 30, 250, 10, 35)
            w8 = Wall((22, 201, 187), 43, 16, 10, 25)
            w9 = Wall((22, 201, 187), 55, 35, 10, 25)
            w10 = Wall((22, 201, 187), 55, 13, 10, 14)
            finish = False
            lose_life = False
        elif level == 3:
            player.refresh(50, 450)
            w1 = Wall((22, 201, 187), 10, 2, 58, 10)
            w2 = Wall((22, 201, 187), 10, 20, 10, 35)
            w3 = Wall((22, 201, 187), 20, 2, 10, 15)
            w4 = Wall((22, 201, 187), 20, 16, 24, 10)
            w5 = Wall((22, 201, 187), 20, 25, 10, 10)
            w6 = Wall((22, 201, 187), 20, 250, 10, 35)
            w7 = Wall((22, 201, 187), 30, 250, 10, 35)
            w8 = Wall((22, 201, 187), 43, 16, 10, 25)
            w9 = Wall((22, 201, 187), 55, 35, 10, 25)
            w10 = Wall((22, 201, 187), 55, 13, 10, 14)
            finish = False
            lose_life = False

            


    clock.tick(FPS)
    pygame.display.update()
