import pygame
import random
################################################
# 기본 초기화
pygame.init() #초기화

# 화면크기 설정
screen_width = 480 #가로
screen_hight = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("young game")

#FPS
clock = pygame.time.Clock()
################################################

#1. 사용자 게임 초기화 (배경,게임 이미지, 좌표 ,폰트, 속도 등)
background = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_basic\\background.png")

#캐릭터 이미지 (프린트)
character = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_basic\\character.png")
character_size = character.get_rect().size #이미지 크기 리스트로 [가로 , 세로]
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 중간
character_y_pos = screen_hight - 70  # 640인 하이트 - 70 해서 
to_x = 0
character_speed = 10

# 적 캐릭터 (프린트)
enemy = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기 리스트로 [가로 , 세로]
enemy_width = enemy_size[0] #가로
enemy_height = enemy_size[1] #세로
enemy_x_pos = random.randint(0,screen_width-70) # 화면 중간
enemy_y_pos = 0  # 640인 하이트 - 70 해서 
enemy_speed = 10


running = True 
while running:
    dt = clock.tick(60) 

    # 2. 이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_LEFT:
                to_x -= character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or  event.key == pygame.K_LEFT:
                to_x = 0
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_hight:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width-70)
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        ruuning = False

    # 5.화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

    pygame.display.update() #게임화면 유지

pygame.quit() 