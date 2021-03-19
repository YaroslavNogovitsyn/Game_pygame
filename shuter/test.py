from pygame import *

run = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed


# class Enemy(GameSprite):
#    side = "up"
#
#    def update(self):
#        if self.rect.y <= 145:
#            self.side = "down"
#        if self.rect.y >= 470:
#            self.side = "up"
#        if self.side == "up":
#            self.rect.y -= self.speed
#        else:
#            self.rect.y += self.speed

spaceship = Hero("rocket.png", 640, 675, 7)
# warship = Enemy("warship.png", 780, 300, 2)


win_width = 1280
win_height = 768
display.set_caption("Ш У Т Е Р")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("galaxy.jpg"), (1280, 768))

finish = False
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0, 0))
        window.fill((255, 255, 255))
        spaceship.update()
        spaceship.reset()
    # if ((sprite.collide_rect(packman, monster_1)) or (sprite.collide_rect(packman,monster_2)) or (sprite.collide_rect(packman,w1)) or (sprite.collide_rect(packman,w2)) or (sprite.collide_rect(packman,w3)) or (sprite.collide_rect(packman,w4)) or (sprite.collide_rect(packman,w5)) or (sprite.collide_rect(packman,w6)) or (sprite.collide_rect(packman,w7)) or (sprite.collide_rect(packman,w8)) or (sprite.collide_rect(packman,w9)) or (sprite.collide_rect(packman,w10)) or (sprite.collide_rect(packman,w11)) or (sprite.collide_rect(packman,w12)) or (sprite.collide_rect(packman,w13)) or (sprite.collide_rect(packman,w14)) or (sprite.collide_rect(packman,w15)) or (sprite.collide_rect(packman,w16)) or (sprite.collide_rect(packman,w17)) or (sprite.collide_rect(packman,w18)) or (sprite.collide_rect(packman,w19)) or (sprite.collide_rect(packman,w20)) or (sprite.collide_rect(packman,w21)) or (sprite.collide_rect(packman,w22)) or (sprite.collide_rect(packman,w23)) or (sprite.collide_rect(packman,w24)) or (sprite.collide_rect(packman,w25)) or (sprite.collide_rect(packman,w26)) or (sprite.collide_rect(packman,w27)) or (sprite.collide_rect(packman,w28)) or (sprite.collide_rect(packman,w29)) or (sprite.collide_rect(packman,w30)) or (sprite.collide_rect(packman,w31)) or (sprite.collide_rect(packman,w32)) or (sprite.collide_rect(packman,w33)) or (sprite.collide_rect(packman,w34)) or (sprite.collide_rect(packman,w35)) or (sprite.collide_rect(packman,w36)) or (sprite.collide_rect(packman,w37)) or (sprite.collide_rect(packman,w38)) or (sprite.collide_rect(packman,w39)) or (sprite.collide_rect(packman,w40)) or (sprite.collide_rect(packman,w41)) or (sprite.collide_rect(packman,w42)) or (sprite.collide_rect(packman,w43)) or (sprite.collide_rect(packman,w44)) or (sprite.collide_rect(packman,w45)) or (sprite.collide_rect(packman,w46)) or (sprite.collide_rect(packman,w47)) or (sprite.collide_rect(packman,w48))):
    #     finish = True
    #     img_1 = image.load("game-over-3.jpg")
    #     window.fill((255,255,255))
    #     window.blit(transform.scale(img_1, (win_width, win_height)), (0,0))

    # if sprite.collide_rect(packman, final_sprite):
    #    finish = True
    #    img = image.load("end.jpg")
    #    window.fill((255,255,255))
    #    window.blit(transform.scale(img, (win_width, win_height)), (0,0))

    display.update()