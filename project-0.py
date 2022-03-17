import pygame, os

pygame.init()
pygame.display.set_caption("Pang")
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

current_path = os.path.dirname(__file__) #현재파일의 위치를 받아옴
image_path = os.path.join(current_path, "images") #image폴더 위치 반환

background = pygame.image.load(os.path.join(image_path, "background1.png"))
character = pygame.image.load(os.path.join(image_path, "character1.png"))
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
#weapon = pygame.image.load("C:/Users/Admin/Desktop/vs.c/images/weapon.png")
#balloon1 = pygame.image.load("C:/Users/Admin/Desktop/vs.c/images/balloon1.png")
#balloon2 = pygame.image.load("C:/Users/Admin/Desktop/vs.c/images/balloon2.png")
#balloon3 = pygame.image.load("C:/Users/Admin/Desktop/vs.c/images/balloon3.png")
#balloon4 = pygame.image.load("C:/Users/Admin/Desktop/vs.c/images/balloon4.png")

character_to_x = 0

stage_rect = stage.get_rect().size
stage_width = stage_rect[0]
stage_height = stage_rect[1]
stage_x_pos = 0
stage_y_pos = screen_height - stage_height

character_rect = character.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height
character_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                character_to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
    
    character_x_pos += character_to_x

    screen.blit(background, (0,0))
    screen.blit(stage, (stage_x_pos, stage_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    




    pygame.display.update()

pygame.init()


