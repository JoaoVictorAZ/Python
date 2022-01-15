import pygame,os,random

pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Olá mundo")
##
WHITE = (255,255,255)
RED = (169,23,23)
BLUE = (102,223,236)
COR = [WHITE,RED,BLUE]
##
FPS = 1
##
PONTO =  pygame.image.load(os.path.join('images', 'Webcam Circle.png'))
PONTO2 =  pygame.image.load(os.path.join('images', 'Webcam Circle.png'))
##
hellofont = pygame.font.SysFont('roboto',280)
##

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(PONTO,(400, 1))

    hello_text = hellofont.render('Hello World', 1, random.choice(COR))
    WIN.blit(hello_text,(397,455))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()
