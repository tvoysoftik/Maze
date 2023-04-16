from pygame import*

win_width = 700
win_height = 500

window = display.set_mode((700,500))
display.set_caption("Maze")
background = transform.scale(image.load('background.jpg'),(700,500))
clock = time.Clock()
FPS = 60

def print_info():
    pass

# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()
# kick = mixer.Sound('kick.ogg')
# money = mixer.Sound('money.ogg')

font.init()
font1 = font.SysFont('Algerian', 50)
win = font1.render('YOU WIN!', True, (0, 0, 255))
lose  = font1.render('YOU LOSE!', True, (0, 0, 255))

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (65,65))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x =  x
       self.rect.y = y
       self.direction = 'left'

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update(self):
        keys  = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:  
            self.rect.x -= self.speed    
        if keys[K_RIGHT] and self.rect.x < 600:  
            self.rect.x += self.speed    
        if keys[K_UP] and self.rect.y > 5:  
            self.rect.y -= self.speed    
        if keys[K_DOWN] and self.rect.y < 400:  
            self.rect.y += self.speed 

class Enemy(Gamesprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 615:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right': 
            self.rect.x += self.speed      


class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_width, wall_height, wall_x, wall_y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2   
        self.color3 = color3
        self.wigth = wall_width
        self.height = wall_height
        self.image = Surface((self.wigth, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall_1 = Wall(255, 255, 0, 400, 20, 100, 10)
wall_2 = Wall(255, 255, 0, 20, 300, 100, 10)  
wall_3 = Wall(255, 255, 0, 20, 400, 300, 100)          


player = Player('hero.png', 5, 400, 5)
enemy = Enemy('cyborg.png', 600, 300, 2)   
treasure = Gamesprite('treasure.png', 600, 400, 0)     



game = True 
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        window.blit(background,(0, 0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        treasure.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        
    if sprite.collide_rect(player, treasure):
        finish = True 
        #money.play()
        window.blit(win, (200, 200))   

    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3):    
        
        finish = True
        #kick.play()
        window.blit(lose, (200, 200))        
        
    display.update()        
    clock.tick(FPS)
