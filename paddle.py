import pygame
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):    
    def __init__(self, color, width, height):
        super().__init__()

        # set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # draw the paddle (a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        # check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        # check that you are not going too far (off the screen)
        if self.rect.y > 400:
          self.rect.y = 400