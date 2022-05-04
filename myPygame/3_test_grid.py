
import pygame
from random import *
import os
import time

def setup(block_count): #경우에 따라 지우자
    number_count = block_count

    shuffle_grid(number_count)
    
def shuffle_grid(number_count):

    rows = 11
    columns = 11
    cell_size = 65 ################## 셀 크기
    button_size = 60 ############ 실제 셀 안에 버튼 크기
    grid = [[1 for col in range(columns)] for row in range(rows)] #10 x 10 칸 0으로 설정

    # 부술수 없는 object 생성 # 나중에 사용자 설정맵으로 가능하도록
    for i in range(rows):
        for j in range(columns):
            if i%2 ==1 and j%2 ==1:
                grid[i][j] = 0
            

    # 랜덤으로 부술 블록            
    number = 1
    while number <= number_count:
        row_idx = randrange(0,rows)
        col_idx = randrange(0,columns)

        # 스타트 지점은 블록 안주기
        if (row_idx < 2 and col_idx <2) or (row_idx >= 9 and col_idx <2):
            continue
        elif (row_idx < 2 and col_idx >= 9) or (row_idx >= 9 and col_idx >= 9):
            continue
        
        # 지나다닐수 있는 장소만 부술 수 있는 블록 설치
        if grid[row_idx][col_idx] == 1:
            grid[row_idx][col_idx] = 2
            number +=1
            
            # x,y위치 구하기
            center_x = (col_idx * cell_size) + (cell_size/2)
            center_y = (row_idx * cell_size) + (cell_size/2)

            button = pygame.Rect(0,0,button_size,button_size)
            button.center = (center_x, center_y)
            breakable.append(button)
    
    # 못 부수는 블럭 설치
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 0:
                
                center_x = (j * cell_size) + (cell_size/2)
                center_y = (i * cell_size) + (cell_size/2)

                button = pygame.Rect(0,0,cell_size,cell_size)
                button.center = (center_x, center_y)
                breakness.append(button)


# 시작 화면 함수
def display_start_screen():

    # 4가지 버튼과 선택용 동그라미 생성
    start_button.center = (650,circle_y) # 390 455 520 585
    pygame.draw.circle(screen, WHIHE, start_button.center, 15, 8)
    pygame.draw.rect(screen,WHIHE,solo_start_button)
    pygame.draw.rect(screen,WHIHE,duo_start_button)
    pygame.draw.rect(screen,WHIHE,showInfo_button)
    pygame.draw.rect(screen,WHIHE,end_button)

# 시작화면에서 버튼 이벤트
def check_buttons(pos):
    global start
    global playerNum
    global running
    if start == False:
        if solo_start_button.collidepoint(pos):
            start = True
            playerNum = 1
            print(playerNum,"인용 게임 시작")
        elif duo_start_button.collidepoint(pos):
            start = True
            playerNum = 2
            print(playerNum,"인용 게임을 시작")
        elif showInfo_button.collidepoint(pos):
            print("아직 미구현")
        elif end_button.collidepoint(pos):
            running = False


         
# 인게임 화면 함수
def display_game_screen():
    for idx, rect in enumerate(breakable, start =1):
        pygame.draw.rect(screen, SEMIGRAY, rect)
    
    for idx, rect in enumerate(breakness, start =1):
        pygame.draw.rect(screen, BLACK, rect)
    pygame.draw.line(screen,WHIHE,(720,5),(720,715),1) # line(화면,색,시작점,끝나는점,굵기)

    
pygame.init() # 초기화

# 바탕 도형 설정
circle_y = 390
start_button = pygame.Rect(0,0,15,15)

solo_start_button = pygame.Rect(360,360,240,60) # (360,360) ~ (600,420)
duo_start_button = pygame.Rect(360,425,240,60) # (360,425) ~ (600,485)
showInfo_button = pygame.Rect(360,490,240,60) # (360,490) ~ (600,550)
end_button = pygame.Rect(360,555,240,60) # (360,555) ~ (600,615)

# 화면 설정
screen_width = 1008 # 가로
screen_hight = 720 # 세로
screen = pygame.display.set_mode((screen_width,screen_hight))


# 화면 타이틀 설정
pygame.display.set_caption("my game")

# FPS
clock = pygame.time.Clock()

# 색
WHIHE = (255,255,255)
GRAY = (120,120,120)
SEMIGRAY = (60,60,60)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,120)

runnable = []
breakness = []
breakable = []

#인게임 변수
playerNum = 0

# 1. 사용자 게임 초기화 (배경,게임 이미지, 좌표 ,폰트, 속도 등)

# 게임 시작여부
start = False
# 게임 running 여부

setup(40) # 블록 개수

running = True 
while running:
    click_pos = None
    dt = clock.tick(30) 

    # 2. 이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos) ####################### 삭제 예정
    
        if event.type == pygame.KEYUP: # 키보드에서 손을 땜
            
            if event.key == pygame.K_UP:
                if circle_y > 390: circle_y -= 65

            if event.key == pygame.K_DOWN:
                if circle_y < 585: circle_y += 65

            if event.key == pygame.K_ESCAPE:
                if start:
                    start = False
                    print("일 시 정 지")
                else:
                    running = False
                    time.sleep(0.5)

            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: #엔터키 
                click_pos = (400,circle_y)
        
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리
    
    # 5.화면에 그리기
    if start:
        screen.fill(GRAY)
        display_game_screen() # 게임 화면
    else:
        screen.fill(GRAY)
        display_start_screen() # 시작 화면

    if click_pos:
        check_buttons(click_pos)

    # 게임화면 유지
    pygame.display.update()

# 종료
pygame.quit() 