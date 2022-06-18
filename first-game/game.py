
import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('first-game/graphics/player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(200,300))
        self.grav = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >=300:
            self.grav = -20
    
    def apply_grav(self):
        self.grav += 1
        self.rect.y += self.grav
        if self.rect.bottom >=300:
            self.rect.bottom = 300

    def update(self):
        self.player_input()
        self.apply_grav()

		

def display_score():
    current = int(pygame.time.get_ticks()/1000) - start_time
    
    score_surf = test_font.render(f'Score: {current} ', False, (64,64,64))
    score_rect = score_surf.get_rect(center =(400, 50))
    screen.blit(score_surf, score_rect)

    return current

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else: 
                screen.blit(fly_surf, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: return []

def colissions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False

    return True

def  player_animation():
    global player_surf, player_index

    if player_rect.bottom <300:
        player_surf = player_jump
    else:
        player_index+=0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]



pygame.init()

screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

game_active = False
start_time = 0
score = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

test_font = pygame.font.Font('first-game/font/Pixeltype.ttf' , 40)
gameover_font = pygame.font.Font('first-game/font/Pixeltype.ttf' , 80)

sky_surface = pygame.image.load('first-game/graphics/Sky.png').convert()
ground_surface = pygame.image.load('first-game/graphics/ground.png').convert()


# obstacles
snail = pygame.image.load('first-game/graphics/snail/snail1.png').convert_alpha()
snail2 = pygame.image.load('first-game/graphics/snail/snail2.png').convert_alpha()
snail_frame = [snail, snail2]
snail_frame_index = 0
snail_surf = snail_frame[snail_frame_index]

fly = pygame.image.load('first-game/graphics/fly/Fly1.png').convert_alpha()
fly2 = pygame.image.load('first-game/graphics/fly/Fly2.png').convert_alpha()
fly_frame = [fly, fly2]
fly_frame_index = 0
fly_surf = fly_frame[fly_frame_index]

obstacle_rect_list = []


# player
player_walk_1 = pygame.image.load('first-game/graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('first-game/graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_jump = pygame.image.load('first-game/graphics/player/jump.png').convert_alpha()
player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_grav = 0

# intro screen
player_stand = pygame.image.load('first-game/graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

start_game_text = test_font.render('Press spacebar to start game ', False, 'White').convert()
start_game_text_rect = start_game_text.get_rect(center = (400 , 350))

start_game_message = test_font.render('Pixel Runner ', False, 'White').convert()
start_game_message_rect = start_game_message.get_rect(center = (400, 80))

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500 )

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200 )
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
        if game_active:
            if event.type == pygame.KEYDOWN:
                if player_rect.bottom >= 300 and event.key == pygame.K_SPACE:
                        player_grav = -20

            if event.type == obstacle_timer:
                if randint(0,2):
                     obstacle_rect_list.append(snail_surf.get_rect(midbottom=(randint(900,1100), 300))) 
                     
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom=(randint(900,1100), 210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                    snail_surf = snail_frame[snail_frame_index]
                else: 
                    snail_frame_index =  0
                    snail_surf = snail_frame[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                    fly_surf = fly_frame[fly_frame_index]
                else: 
                    fly_frame_index =  0
                    fly_surf = fly_frame[fly_frame_index]

        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active= True
                
                start_time = int(pygame.time.get_ticks()/1000)  

        



    if game_active:  
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        
    # score   
         
        score =   display_score()
  
    # player                                                              
        player_grav+=1
        player_rect.y += player_grav
        if player_rect.bottom >= 300: player_rect.bottom=300
        player_animation()
        screen.blit(player_surf, player_rect)
        player.draw(screen)
        player.update()

    
    # obstacle
        obstacle_rect_list =  obstacle_movement(obstacle_rect_list)

    # colission
        game_active = colissions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94,129,162)) 
        screen.blit(player_stand, player_stand_rect)  
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_grav = 0

        score_message = test_font.render(f'Your score: {score}', False, 'White')
        score_message_rect = score_message.get_rect(center=(400, 350))
        screen.blit(start_game_message, start_game_message_rect)
        

        if score == 0:
            screen.blit(start_game_text, start_game_text_rect)
        else:
            screen.blit(score_message, score_message_rect)
    
    pygame.display.update()     
    clock.tick(60)
    

