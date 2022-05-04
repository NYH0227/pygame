import pygame

pygame.init() #초기화

# 화면크기 설정
screen_width = 480 #가로
screen_hight = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("young game")

#FPS
clock = pygame.time.Clock()

#배경 이미지 (프린트)
background = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_basic\\background.png")

#캐릭터 이미지 (프린트)
character = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_basic\\character.png")
character_size = character.get_rect().size #이미지 크기 리스트로 [가로 , 세로]
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 중간
character_y_pos = screen_hight - 70  # 640인 하이트 - 70 해서 

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

# 적 캐릭터 (프린트)
enemy = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기 리스트로 [가로 , 세로]
enemy_width = enemy_size[0] #가로
enemy_height = enemy_size[1] #세로
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 중간
enemy_y_pos = (screen_hight / 2) - (enemy_width / 2)  # 640인 하이트 - 70 해서 


#이벤트 루프
running = True # 게임이 진행중인지 체크용
while running:
    dt = clock.tick(60) # 초당 프레임수 설정
#   print("fps : "+str(clock.get_fps())) # fps 눈으로 확인 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 받히는 이벤트면
            running = False # 게임 off
        if event.type == pygame.KEYDOWN: #키보드를 누름
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 키보드에서 손을 땜
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계
    if character_x_pos < 0 : 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    #세로 경계
    if character_y_pos < 0 : 
        character_y_pos = 0
    elif character_y_pos > screen_hight - character_height :
        character_y_pos = screen_hight - character_height

    #충돌처리

    #위치정보 (프린트에 맞는 실제 위치)
    character_rect = character.get_rect() # 캐릭터 위치 받기
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos # 캐릭터 위치 업데이트

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0)) #배경 삽입
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭 삽입
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 삽입


    pygame.display.update() #게임화면 유지

pygame.quit() #게임 종료