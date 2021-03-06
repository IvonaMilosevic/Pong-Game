import pygame
from paddle import Paddle
from ball import Ball
from tkinter import *
from tkinter import messagebox
 
pygame.init()
 
# define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PongGame")

 
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
 
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
 
# this will be a list that will contain all the sprites we intend to use in our game
all_sprites_list = pygame.sprite.Group()
 
# add the paddle and ball to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
 
# the loop will carry on until the user exit the game (clicks the close button)
carryOn = True
 
# the clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# initialise player scores
scoreA = 0
scoreB = 0

# -------- main program -----------
Tk().wm_withdraw() #to hide the main window
messagebox.showinfo("Play", "Press OK when you want to start, then on a black surface when the game starts so you can play")  
while carryOn:    
    # --- main event 
    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT: # if user clicked close
              carryOn = False # flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: # pressing the x key will quit the game
                     carryOn=False
    
    # moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)    
 
    # --- game logic 
    all_sprites_list.update()
    
    # check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     
 
    # detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
    
    # --- drawing code
    # first, clear the screen to black. 
    screen.fill(BLACK)
    # draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    # now let's draw all the sprites in one go (for now we only have 2 sprites)
    all_sprites_list.draw(screen) 
 
    # display scores:
    font = pygame.font.Font(None, 74)
    text = font.render("A: " + str(scoreA), 1, WHITE)
    screen.blit(text, (230,10))
    text = font.render("B: " + str(scoreB), 1, WHITE)
    screen.blit(text, (370,10))
    if scoreA==30 or scoreB==30:
        if scoreA>scoreB:
            Tk().wm_withdraw() #to hide the main window
            text = "Player A win\nScore: A: {}  B: {} ".format(scoreA, scoreB)
            messagebox.showinfo("Winner", text)            
        else:
            Tk().wm_withdraw() #to hide the main window
            text = "Player A win\nScore: A: {}  B: {} ".format(scoreA, scoreB)
            messagebox.showinfo("Winner", text)
        carryOn = False
             
    # --- go ahead and update the screen with what we've drawn
    pygame.display.flip()
     
    # --- limit to 60 frames per second
    clock.tick(60)
 
# once we have exited the main program loop we can stop the game engine:
pygame.quit()
