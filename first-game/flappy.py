from cmath import rect
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('first-game/flappy/flappybird.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(300,600))
        self.grav = 0


    def apply_grav(self):
        self.grav += 1
        self.rect.y += self.grav
        if self.rect.bottom >=600:
            self.rect.bottom = 600

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >=600:
            self.grav = -20
    def apply_movement(self):
        self.pressed = pygame.key.get_pressed()

        if self.pressed[pygame.K_a]:
            self.rect.x-=7
        if self.pressed[pygame.K_d]:
            self.rect.x+=7
        if self.pressed[pygame.K_s]:
            self.grav+=5

    def update(self):
        self.player_input()
        self.apply_grav()
        self.apply_movement()

    def apply_animation(self):
        pass



def  player_animation():
    global player_surf, player_index

    if player_rect.bottom <600:
        player_index = 1
        player_surf = player_walk[int(player_index)]
    else:
        player_index = 0
        player_surf = player_walk[int(player_index)]
        
    
    
    
    

pygame.init()
screen = pygame.display.set_mode((600, 700)) 
pygame.display.set_caption("Flappy")
clock = pygame.time.Clock()


ground_surf  = pygame.image.load('first-game/graphics/ground.png').convert()

block_surf = pygame.image.load('first-game/flappy/grass.png').convert_alpha()
block_rect = block_surf.get_rect(center =(400, 370))

player = pygame.image.load('first-game/flappy/flappybird.png').convert_alpha()
player_jump =  pygame.image.load('first-game/flappy/flappybird_jump.png').convert_alpha()
player_walk = [player, player_jump]
player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(300, 600))

player_class = pygame.sprite.GroupSingle()
player_class.add(Player())





player_grav = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 600:
                player_grav = -20
            
          
        
    screen.fill("White")
    screen.blit(ground_surf,(0,600)) 

    screen.blit(block_surf, block_rect)
    
    # gravity
    player_grav+=1
    player_rect.y += player_grav 
    
    # screen walls
    if player_rect.bottom >= 600: player_rect.bottom=600
    if player_rect.top <= 0: player_rect.top=0
    if player_rect.left <= 0: player_rect.left=0
    if player_rect.right >= 600: player_rect.right=600

    #  colission
    if player_rect == block_rect: print("colissom")

    # player spawn
    # player_animation()
    # screen.blit(player_surf, player_rect)  
    player_class.draw(screen)
    player_class.update()
    
    # movement
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
       player_rect.x-=7
    if pressed[pygame.K_d]:
       player_rect.x+=7
    if pressed[pygame.K_s]:
       player_grav+=5
    
    

   
    
    pygame.display.update()     
    clock.tick(60)
