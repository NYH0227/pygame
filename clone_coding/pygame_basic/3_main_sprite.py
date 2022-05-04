import pygame

pygame.init() #초기화

# 화면크기 설정
screen_width = 480 #가로
screen_hight = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("young game")

#배경 이미지
background = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_basic\\background.png")

#캐릭터 이미지
character = pygame.image.load("C:\\Users\\75204\\Desktop\\pws\\pygame_basic\\character.png")
character_size = character.get_rect().size #이미지 크기 리스트로 [가로 , 세로]
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 중간
character_y_pos = screen_hight - 70  # 640인 하이트 - 70 해서 

#이벤트 루프
running = True # 게임이 진행중인지 체크용
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 받히는 이벤트면
            running = False # 게임 off
    
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    
    pygame.display.update() #게임화면 유지

pygame.quit() #게임 종료