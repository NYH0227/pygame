import pygame

pygame.init() #초기화

# 화면크기 설정
screen_width = 480 #가로
screen_hight = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("young game")

#배경
background = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_basic\\background.png")

#이벤트 루프
running = True # 게임이 진행중인지 체크용
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 받히는 이벤트면
            running = False # 게임 off
    
    screen.blit(background, (0,0))
    #screnn.fill((0,0,255)) # 윗 라인이랑 같은데 배경을 채우는 것
    
    pygame.display.update() #게임화면 유지

pygame.quit() #게임 종료