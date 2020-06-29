import pygame
pygame.init()


SCREEN = pygame.display.set_mode((400,400))
FPS = pygame.time.Clock()

GAME_STARTED = False
GAME_OVER = False

def textOnScreen(message, x, y):
    font = pygame.font.SysFont("None", 32)
    txt = font.render(message, (0,0,0), True, None)
    SCREEN.blit(txt, (x, y))
    '''
    You can create another paramethers to this function, as color,
    for example.
    '''

class Player:
    def __init__(self):
        self.image = pygame.Surface((50,50))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = 225
        
    def move(self):
        mouse = pygame.mouse.get_pos()
        self.rect.x = mouse[0]
        self.rect.y = mouse[1]

    def check_area(self):
        '''

        This is a very simple example to show you how we can manage the variables
        GAME_STARTED and GAME_OVER to show messages at right time.
        
        '''
        global GAME_OVER
        if self.rect.x < 100 or self.rect.x > 300:
            GAME_OVER = True

    def update(self):
        self.move()
        self.check_area()
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

        print(self.rect.x, self.rect.y)
            

player = Player()

while True:    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if GAME_STARTED == False:
                    GAME_STARTED = True

                    
    if GAME_STARTED == False:
        # Create your menu here
        
        SCREEN.fill((255,255,255))        
        textOnScreen("Hello, World!", 150, 150)
        textOnScreen("Press ENTER to Start", 100, 250)

    else:
        if GAME_OVER == False:
            # Create your game here        
            SCREEN.fill((255,0,0))
            player.update()

        else:
            # Create your game over screen here
            SCREEN.fill((0,0,255))        
            textOnScreen("Game Over!", 150, 150)                    

    FPS.tick(30)
    pygame.display.update()
