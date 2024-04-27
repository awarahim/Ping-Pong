from random import randint
from pygame import *
from time import time as timer

start = timer()


end = timer()

win_width  = 700
win_height = 500
window = display.set_mode((700,500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('pool.jpg'),(win_width,win_height))
font.init()
font1 = font.SysFont('Arial',80)
font2 = font.SysFont('Arial',36)
win = font1.render('YOU WON!',True,(255,215,0))
lose = font1.render('YOU LOSE!',True,(180,0,0))
goal = 10


FPS = 60
clock = time.Clock()

lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80,win_width- 80)
            self.rect.y = 0
            lost = lost + 1




class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s]and self.rect.y > 5:
            self.rect.y +=self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_DOWN]and self.rect.y< 5:
            self.rect.y +=self.speed

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



player = Player('racket.png',5,win_height -100,4)
enemy = Enemy('ufo.png',randint(0,200),0,randint(1,3))



monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy('ufo.png',randint(0,200),0,randint(1,3))
    monsters.add(monster)



finish = False   
run = True
life = 3
score  = 0
rel_time = False
num_fire = 0
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type ==  KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play( )
                player.fire()

                if num_fire >= 5 and rel_time == False:

                    last_time = timer()
                    rel_time = True


    if not finish:
        window.blit(background,(0,0))
        player.reset()
        player.update()
        monsters.update()
        bullets.update()
        asteriods.update()
        asteriods.draw(window)

        
        monsters.draw(window)
        bullets.draw(window)

        Score = font2.render("Score:"+str(score),1,(255,255,255))
        window.blit(Score,(10,20))

        text_lose = font2.render("Missed:"+str(lost),1,(255,255,255))
        window.blit(text_lose,(10,50))

        text_life =font2.render("Life:"+str(life),1,(255,0,0))
        window.blit(text_life,(10,80))

        collides = sprite.groupcollide(monsters,bullets,True,True)
        for i in collides:
            score = score + 1
            enemy = Enemy('ufo.png',randint(0,200),0,randint(1,3))
            monsters.add(monster)

        if sprite.spritecollide(player,monsters,False)or sprite.spritecollide(player,asteriods,False):
            sprite.spritecollide(player,monsters,True)
            sprite.spritecollide(player,asteriods,True)
            life = life - 1


        if life == 0 or lost>3:
            finish = True
            window.blit(lose,(200,200))

        if score >= goal:
            finish = True
            window.blit(win,(200,200))

        if rel_time == True:
            now_time = timer()

            if now_time - last_time < 3:
                reload = font2.render('Wait, reload...',1,(150,0,0))
                window.blit(reload,(260,460))
            else:
                num_fire = 0
                rel_time = False
