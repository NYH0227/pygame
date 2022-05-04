import pygame
import os
import math

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self,image,position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(center=position)

        self.offset = pygame.math.Vector2(default_offset_x_claw,0)
        self.position = position

        self.direction = LEFT # 집게의 이동방향
        self.angle_speed = 2.5 
        self.angle = 10


    def update(self, to_x):
        if self.direction == LEFT:
            self.angle += self.angle_speed
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed

        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle <10:
            self.angle = 10
            self.set_direction(LEFT)

        self.offset.x += to_x #중심점 까지 거리만 늘리기
        
        self.rotate()
        #rect_center = self.position + self.offset
        #self.rect = self.image.get_rect(center=rect_center)
        #print(self.angle,self.direction)

    def rotate(self):
        #회전 대상 이미지 ,회전 각도, 이미지 크기
        self.image = pygame.transform.rotozoom(self.original_image,-self.angle, 1)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center=self.position+offset_rotated)

    def set_direction(self, direction):
        self.direction = direction

    def draw(self, screen):
        screen.blit(self.image,self.rect)
        pygame.draw.circle(screen,RED,self.position,3) #중심
        pygame.draw.line(screen,BLACK,self.position, self.rect.center, 5) #스크린에 검은색으로 x에서 y까지 두께5

    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT
        
# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position,price,speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.price = price
        self.speed = speed
    
    def set_position(self,position,angle):
        r = self.rect.size[0] // 2
        rad_angle = math.radians(angle)
        to_x = r * math.cos(rad_angle)
        to_y = r * math.sin(rad_angle)

        self.rect.center = (position[0]+to_x,position[1]+to_y)
        
        

def setup_gemstone():
    small_gold_price,small_gold_speed = 100,5
    big_gold_price,big_gold_speed = 300,2
    stone_price, stone_speed = 10,2
    diamond_price,diamond = 600 ,7

    small_gold = Gemstone(gemstone_images[0],(200,380),small_gold_price,small_gold_speed) # 이따가 포지션 수정하자 # 0번 스톤이미지
    gemstone_group.add(small_gold)

    gemstone_group.add(Gemstone(gemstone_images[1],(300,500),big_gold_price,big_gold_speed)) # 1번 스톤이미지
    gemstone_group.add(Gemstone(gemstone_images[2],(300,380),stone_price, stone_speed))
    gemstone_group.add(Gemstone(gemstone_images[3],(900,420),diamond_price,diamond))


# 기본설정
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("gold miner")
clock = pygame.time.Clock()

# 게임 옵션 변수
default_offset_x_claw = 40 # 집게와 중심의 거리
to_x = 0
caught_gemstone = None

move_speed = 12
return_speed = 20

LEFT = -1
RIGHT = 1
STOP = 0

# 색
RED =(255,0,0)
BLACK = (0,0,0)


# 배경
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 보석 불러오기 (금 2종류,돌,다이아)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "big_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "stone.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "diamond.png")).convert_alpha()
]

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone()
                    
# 집게
claw_image = pygame.image.load(os.path.join(current_path,"claw.png")).convert_alpha()
claw = Claw(claw_image, (screen_width//2, 110))

# main
running = True
while running:
    clock.tick(30) # 프레임속도 30으로 고정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            claw.set_direction(STOP)
            to_x = move_speed

    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed
    
    if claw.offset.x < default_offset_x_claw:
        to_x = 0
        claw.set_init_state()

        if caught_gemstone:
            #update_score(caught_gemstone.price)
   
            gemstone_group.remove(caught_gemstone)
            caught_gemstone = None

    
    if not caught_gemstone:
        for gemstone in gemstone_group:
            # if claw.rect.colliderect(gemstone.rect): #사각형 충돌
            if pygame.sprite.collide_mask(claw,gemstone): #이미지 충돌
                caught_gemstone = gemstone
                to_x = -gemstone.speed
                break
    
    if caught_gemstone:
        caught_gemstone.set_position(claw.rect.center,claw.angle)

    
    screen.blit(background,(0,0))

    gemstone_group.draw(screen)
    claw.update(to_x)
    claw.draw(screen)

    pygame.display.update()

pygame.quit()


