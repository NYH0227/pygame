import pygame
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
running = True 
while running:
    dt = clock.tick(30) 

    # 2. 이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리
    
    # 5.화면에 그리기
    
    pygame.display.update() #게임화면 유지

pygame.quit() 