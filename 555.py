#Создай собственный Шутер!

from pygame import *
window = display.set_mode((700,500))
display.set_caption('Пинг Понг')
background = transform.scale(image.load('mat.jpg'),(700,500))
x = 65
y = 65
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x, y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed

    
player = Player("raketka.png", 25, 250, 5, 80, 100)
player1 = Player("raketka.png", 600, 250, 5, 80, 100)
ball = Player('mych.png',250, 250, 5, 80, 80)
chet1 = 0
propusk1 = 0
speed_x = 3
speed_y = 3
rel_time = False #Флаг отвечающий за перезарядку
num_fire = 0
run = True 
finish = False
font.init()
font = font.Font(None, 36)    
lose1 = font.render('PLAYER 1 LOSE!', True,(180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True,(180,0,0))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(background,(0,0))
        player.reset()
        player1.reset()
        player.update()
        player1.update1() 
        ball.update()
        ball.reset()

        if ball.rect.y > 500 - 80 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player,ball) or sprite.collide_rect(player1,ball):
            speed_x *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200,200))
    display.update()
