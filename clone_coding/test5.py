import pygame
import os
################################################
# 기본 초기화
pygame.init() #초기화

# 화면크기 설정
screen_width = 640 #가로
screen_hight = 480 #세로
screen = pygame.display.set_mode((screen_width,screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("young Pang")

#FPS
clock = pygame.time.Clock()
################################################

#1. 사용자 게임 초기화 (배경,게임 이미지, 좌표 ,폰트, 속도 등)
current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
image_path = os.path.join(current_path, "images") # 폴더 위치 반환

#배경
background = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_project\\images\\background.png")

#스테이지 만들기
stage = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_project\\images\\stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1] 

#캐릭터 만들기
character = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_project\\images\\chararecter.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2)
character_y_pos = screen_hight - character_height - stage_height

#캐릭 이동 방향
character_to_x = 0
character_speed = 5

#무기

weapon = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_project\\images\\weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []
weapon_speed = 10

#공
ball_images = [
    pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_project\\images\\boll1.png"),
    pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_project\\images\\boll2.png"),
    pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_project\\images\\boll3.png"),
    pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_project\\images\\boll4.png")
]
# 공 크기에 따른 처음 스피드
ball_speed_y = [+18,+15,+12,+9]

balls = []
balls.append({ "pos_x" : 50, "pos_y" :50, "img_idx" : 0, "to_x":3 ,"to_y": -6, "init_spd_y": ball_speed_y[0]})


running = True
while running:
    dt = clock.tick(30) 

    # 2. 이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #무기 위치 조정
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons ]
    
    #천장에 닿은 무기
    weapons = [[w[0],w[1]] for w in weapons if w[1]> 0]

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        
        #가로벽에 팅겨서 방향 반대
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
        #바닥에 팅기는 것
        if ball_pos_y <= stage_height -stage_height -ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] -= 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    # 4. 충돌 처리
    
    # 5.화면에 그리기
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))

    screen.blit(stage, (0,screen_hight-stage_height))
    screen.blit(character, (character_x_pos,character_y_pos))
    

    pygame.display.update() #게임화면 유지

pygame.quit() 