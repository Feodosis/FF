from random import randint

from pygame import *
mixer.init()
mixer.music.load("mp3rington_club_id_16140.mp3")
mixer.music.play()
# fire_sound = mixer.Sound()
img_back = "65e9f93db0799.jpg"
img_hero = "65e9f9072ba18.png"
img_bullet = "kisspng-bowling-ball-ten-pin-bowling-real-bowling-5aa257a9ddaa75.318842411520588713908(1).jpg"
img_enemy = "65e9f8f545f4e.png"

score = 0
lost = 0
max_lost = 3


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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_wigth - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_wigth - 80)
            self.rect.y = -10
            lost += 1
win_wigth = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_wigth, win_height))
background = transform.scale(image.load(img_back), (win_wigth, win_height))

ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
bullets = sprite.Group()




finish = False
run = TrueIT:
while run:
    for e in event.get():
        if e.type == QU
            run = False
        elif e.type == KEYDOWN:
            if e.type == K_SPACE:
                ship.fire()

    if not finish:
        window.blit(background, (0, 0))
        ship.update()
        bullets.update()
        ship.reset()
        bullets.draw(window)
        display.update()
    time.delay(50)
