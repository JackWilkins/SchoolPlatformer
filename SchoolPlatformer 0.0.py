import pygame

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def changespeed(self,x,y):
        self.change_x +- x
        self.change_y +- y
    def update(self,nWall):
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block,rect.right
        self.rect.y +- self.change_y
        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


pygame.init()

screen = pygame.display.set_mode([1024,768])
screen = pygame.display.set_caption('Platformer')


player = Player(30,30)

all_sprites_list = pygame.sprite.Group()
all_sprite_list.add(player)

wall_list = pygame.sprite.Group()
wall = Wall(0,0,15,768)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(15,0,1009,15)
wall_list.add(wall)
all_sprite_list.add(wall)

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3,0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3,0)
            elif event.key == pygame.K_UP:
                player.changespeed(0,3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,-3)

    player.update(wall_list)

    screen.fill(white)
    all_sprite_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

    
                
            
                
                










        
        
        
