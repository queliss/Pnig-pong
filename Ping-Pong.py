from pygame import*
from random import*
from time import time as timer
clock = time.Clock()
FPS = 60

# окно
win_width = 700
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption('Shooter game')
background = transform.scale(image.load('backgr.png'),(win_width, win_height))

font.init()
font2 = font.Font(None, 36)
font1 = font.Font(None, 80)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

racket1 = Player("racket.png", 30, 250, 25, 90, 30)
racket2 = Player("racket.png", 650, 250, 25, 90, 30)
game = True
while game:
    for e in event.get():
        if e.type == QUIT: 
            game = False
    window.blit(background, (0,0))
    racket1.update_l()
    racket2.update_r()
    racket1.reset()
    racket2.reset()
    

    display.update()
    clock.tick(FPS)