import pygame
import random 
import sys
pygame.init()
screenSize = 600
pygame.display.set_caption('BlockJump')
win = pygame.display.set_mode((screenSize,screenSize))
score = 0
clock = pygame.time.Clock()
global run
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height
        self.vel = 10
        self.jumpCount = 7
        self.isJump = False
        self.hitbox = (self.x , self.y  , 40, 40)
        self.health = 100
        
    def draw(self,win):
        self.hitbox = (self.x , self.y  , 40, 40)
        pygame.draw.rect(win, (255,0,0), (self.x,self.y,self.width,self.height))
        
    def hit(self):
        pass
        
class enemy(object):
    def __init__ (self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 9
        self.hitbox = (self.x , self.y  , 40, 40)
        self.health = 10
        self.visible = True
    
    def draw(self,win):
        self.move() 
        if self.visible :
            self.hitbox = (self.x , self.y  , 40, 40)
            pygame.draw.rect(win, (255,255,0), (self.x,self.y,self.width,self.height))

    def move(self):
        if self.vel>0 :
            self.vel += 0.03
            if(self.x + self.vel < screenSize-40):
                self.x += self.vel
            else:
                self.vel *= -1
        else :
            if self.x - self.vel > 0:
                self.x += self.vel
            else:
                self.vel *= -1
    
    def hit(self):
        if self.health>0 :
            self.health -= 1
        if self.health==0 :
            self.visible = False
    
class goal(object):
    def __init__ (self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x , self.y  , 10, 10)
        self.is_hit = False
    
    def draw(self,win):
        if self.is_hit :
            self.move()
        self.hitbox = (self.x , self.y  , 10, 10)
        pygame.draw.rect(win, (255,255,255), (self.x,self.y,self.width,self.height))

    def move(self):
        self.x = random.randint(0,590)
        self.is_hit = False
    
    def hit(self):
        self.is_hit = True   
        
def redrawWindow():
    win.fill((0,0,0))
    font = pygame.font.SysFont('verdana', 18, False, True)
    quit_inst = font.render('Press q to quit', True, (255, 255, 255))
    win.blit(quit_inst, (10,10))
    
    font = pygame.font.SysFont('verdana', 22)
    score_text = font.render('score : ' + str(score), True, (105,105,105))
    win.blit(score_text, (300 - score_text.get_width()/2,300))
    
    pygame.draw.rect(win, (255,255,255), (0,343,600,20))
    font = pygame.font.SysFont('verdana', 12)
    text = font.render('dhanraj322.github.io', True, (255, 255, 255))
    win.blit(text, (580 - text.get_width(),570))
    goal1.draw(win)
    obs.draw(win)
    man.draw(win)
    pygame.display.update()
    
def start_screen():
    intro = True
    while intro:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                 intro = False
        pygame.time.delay(40)
        win.fill((0,0,0))
        font = pygame.font.SysFont('verdana', 40, True)
        text = font.render('START', True, (255, 255, 255))
        win.blit(text, (300 - text.get_width()/2,50))
        font = pygame.font.SysFont('verdana', 18)
        
        text = font.render('Move', True, (255, 255, 255))
        win.blit(text, (260,150))
        pygame.draw.rect(win, (255,0,0), (320,140,40,40))
        
        font = pygame.font.SysFont('verdana', 17, False, True)
        text = font.render('a to left        d to right', True, (255, 255, 255))
        win.blit(text, (300 - text.get_width()/2,200))
        
        text = font.render('space to jump', True, (255, 255, 255))
        win.blit(text, (300 - text.get_width()/2,230))
        
        font = pygame.font.SysFont('verdana', 17)
        text = font.render('Goal is to collect', True, (255, 255, 255))
        win.blit(text, (150,300))
        pygame.draw.rect(win, (255,255,255), (350,307,10,10))
        
        text = font.render('Game over if you get hit by', True, (255, 255, 255))
        win.blit(text, (100,350))
        pygame.draw.rect(win, (255,255,0), (400,345,40,40))
        
        font = pygame.font.SysFont('verdana', 17, False, True)
        text = font.render('Press w to start', True, (255, 255, 255))
        win.blit(text, (300 - text.get_width()/2,500))
        
        text = font.render('Press q to quit', True, (255, 255, 255))
        win.blit(text, (300 - text.get_width()/2,530))
            
        font = pygame.font.SysFont('verdana', 12)
        text = font.render('dhanraj322.github.io', True, (255, 255, 255))
        win.blit(text, (580 - text.get_width(),570))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            intro = False
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit(0)
            
def exit_screen():
    pygame.time.delay(40)
    win.fill((0,0,0))
    font = pygame.font.SysFont('verdana', 35, True, True)
    text = font.render('Game Over', True, (255, 255, 255))
    win.blit(text, (300 - text.get_width()/2,200))
    font = pygame.font.SysFont('verdana', 18)
    text = font.render('Score : ' + str(score), True, (255, 255, 255))
    win.blit(text, (300 - text.get_width()/2,300))
    font = pygame.font.SysFont('verdana', 12)
    text = font.render('dhanraj322.github.io', True, (255, 255, 255))
    win.blit(text, (580 - text.get_width(),570))
    pygame.display.update()
    pygame.time.delay(2000)
    
man = player(20,300,40,40)
obs = enemy(500,300,40,40)
goal1 = goal(random.randint(0,590),230,10,10)
start_screen()
run = True

while run:
    pygame.time.delay(40)
        
    if man.hitbox[0] <= obs.hitbox[0] + obs.hitbox[2] and man.hitbox[0] >= obs.hitbox[0] :
        if man.hitbox[1] <= obs.hitbox[1] + obs.hitbox[3] and man.hitbox[1] >= obs.hitbox[1]:
            man.hit()
            pygame.time.delay(500)
            exit_screen()
            man = player(20,300,40,40)
            obs = enemy(500,300,40,40)
            goal1 = goal(random.randint(0,590),230,10,10)
            start_screen()
            run = True
            score = 0
            
    if goal1.hitbox[0] <= man.hitbox[0] + man.hitbox[2] and goal1.hitbox[0] >= man.hitbox[0] :
        if goal1.hitbox[1] <= man.hitbox[1] + man.hitbox[3] and goal1.hitbox[1] >= man.hitbox[1]:
            goal1.hit()
            score+=1
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
             run = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        man.x = max(0, man.x - man.vel)
    if keys[pygame.K_d]:
        man.x = min(screenSize-man.width, man.x + man.vel)

    if not(man.isJump):
        if keys[pygame.K_q]:
            run = False
        if keys[pygame.K_SPACE]:
            man.isJump = True
    else:
        if man.jumpCount >= -7:
            temp = 1
            if man.jumpCount < 0:
                temp = -1
            man.y -= (man.jumpCount ** 2)*0.8*temp
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 7
        
    redrawWindow()
pygame.quit()