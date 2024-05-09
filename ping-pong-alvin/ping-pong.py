from random import randint
from pygame import *
from time import time as timer

win_width  = 700
win_height = 500
window = display.set_mode((700,500))
display.set_caption('Ping Pong')
back = (255,255,255)
background = transform.scale(image.load('pool.jpg'),(win_width,win_height))
font.init()
font1 = font.SysFont('Arial',80)
font2 = font.SysFont('Arial',36)
win = font1.render('YOU WON!',True,(255,215,0))
lose = font1.render('YOU LOSE!',True,(180,0,0))


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s]and self.rect.y < win_height-5:
            self.rect.y +=self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_DOWN]and self.rect.y < win_height-5:
            self.rect.y +=self.speed

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



player_L = Player('table_tennis_racket.png',30, 200,10)
player_R = Player('table_tennis_racket.png',win_width-100,200,10)
ball = GameSprite('football.png',200,200,50)

clock = time.Clock()
FPS = 60
game = True
game_over = False




font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSES',True,(180, 0, 0))
font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSES',True,(180,0 ,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if game_over !=True:
        window.fill(back)
        window.blit(background,(0,0))
        player_L.update_l()
        player_R.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        
        if sprite.collide_rect(player_L,ball)or sprite.collide_rect(player_R,ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y> win_height -50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            game_over = True
            window.blit(lose1, (200,200))
        if ball.rect.x > win_width:
            game_over = True
            window.blit(lose2, (350,200))




    player_L.reset()
    player_R.reset()
    ball.reset()


    display.update()
    clock.tick(FPS)
