####################################################
#Project: ICS3U Final Game                         #
#Name: Boxhead Bill Sun Special                    #
#Class: ICS3U1-02                                  #
#Produced By: Bill Sun and Umair Malik             #
####################################################

import pygame,time,random,math #import modules
from pygame.locals import*
pygame.init()

#Functions
def text(text,x,y,font,size,a,b,c): #general function for printing text on screen
    #(x,y)= coordinates; (a,b,c)= colour of text 
    pygame.init()
    font = pygame.font.SysFont(font, size)
    text = font.render(text, 1, (a,b,c))
    screen.blit(text,(x,y))

def audio(A): #function for playing an ogg sound file
    audio = pygame.mixer.Sound(A+".ogg")
    audio.play()

def audio1(A): #another function for playing an ogg sound file (this way sounds can be overlapped)
    audio = pygame.mixer.Sound(A+".ogg")
    audio.play()

def music(B): #function for playing an mp3 sound file
    pygame.mixer.music.load(B+".mp3")
    pygame.mixer.music.set_volume(0.25) 
    pygame.mixer.music.play(-1)
    
def button(msg,x,y,w,h,ic,ac,action): #function for creating any button in the game
    #msg = words on the button; (x,y)= coordinates; (w,h)= width and height
    #(ic,ac) = inactive and active colour; action = follow up function
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        #if the mouse moves over the button, the colour changes from the inactive colour to the active colour
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1:
            audio("button_click")
            time.sleep(0.1) #prevent continuous clicking
            action() #run the follow up function
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    buttonfont = pygame.font.SysFont("Corbel",30)
    text = buttonfont.render(msg, 1, (175,0,0)) #showing text on the button
    text_rect = text.get_rect()
    text_rect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(text, text_rect)

#screen settings
screen = pygame.display.set_mode((1200,768),pygame.FULLSCREEN) #Full screen
logo = pygame.image.load("logo.jpg").convert() #logo images for the menu pages
logo1 = pygame.image.load("logo1.png").convert()
logo2 = pygame.image.load("logo2.png").convert()
clock = pygame.time.Clock()
a = 1 #variables for map/character selections
b = 1
c = 1

def Screen(): #general function for setting up a menu screen
    clock.tick(50)
    screen.fill((255,255,255))
    screen.blit(logo1,[230,25])
    keys = pygame.key.get_pressed()
    for ev in pygame.event.get():
        if keys[K_ESCAPE]:
            quitgame()

#Functions for player and map selection (cannot be simplified due to specifications of the button function)
def next_image():
    global a
    a += 1
    if a > 6:
        a = 1

def next_image1():
    global b
    b += 1
    if b > 6:
        b = 1

def next_image2():
    global c
    c += 1
    if c > 5:
        c = 1

def previous_image():
    global a
    a -= 1
    if a < 1:
        a = 5

def previous_image1():
    global b
    b -= 1
    if b < 1:
        b = 5

def previous_image2():
    global c
    c -= 1
    if c < 1:
        c = 5

#Menu Pages
def quitgame(): #function for exiting the game
    pygame.quit()
    exit()
    
def singleplayer(): #menu page for character and map selection for singleplayer
    keepgoing = True
    while keepgoing:
        img = pygame.image.load("character"+str(a)+".png").convert() #images of characters
        img1 = pygame.image.load("map"+str(c)+".png").convert() #images of maps
        screen.blit(img,[250,420])
        screen.blit(img1,[665,400])
        text("Choose your character",100,325,"comicsansms",30,175,0,0)
        text("Choose your map",600,325,"comicsansms",30,175,0,0)
        button("Start Game!",400,700,400,60,(200,200,200),(150,150,150),play)
        button("Back",1000,700,190,60,(200,200,200),(150,150,150),intro)
        button("<",100,450,40,60,(200,200,200),(150,150,150),next_image) #buttons for selecting the map and characters
        button(">",400,450,40,60,(200,200,200),(150,150,150),previous_image)
        button("<",550,450,40,60,(200,200,200),(150,150,150),next_image2)
        button(">",1100,450,40,60,(200,200,200),(150,150,150),previous_image2)
        pygame.display.flip()
        Screen()

def multiplayer(): #first menu page for character and map selection for multiplayer
    keepgoing = True
    while keepgoing:
        img = pygame.image.load("character"+str(a)+".png").convert() #images of character 1
        img1 = pygame.image.load("character"+str(b)+".png").convert() #images of character 2
        screen.blit(img,[270,420])
        screen.blit(img1,[720,420])
        text("Choose your characters",100,300,"comicsansms",30,175,0,0)
        text("Player 1",100,350,"comicsansms",25,175,0,0)
        text("Player 2",600,350,"comicsansms",25,175,0,0)
        button("Continue",1000,630,190,60,(200,200,200),(150,150,150),multiplayer1)
        button("Back",1000,700,190,60,(200,200,200),(150,150,150),intro)
        button("<",100,450,40,60,(200,200,200),(150,150,150),next_image)
        button(">",450,450,40,60,(200,200,200),(150,150,150),previous_image)
        button("<",550,450,40,60,(200,200,200),(150,150,150),next_image1)
        button(">",900,450,40,60,(200,200,200),(150,150,150),previous_image1)
        pygame.display.flip()
        Screen()

def multiplayer1(): #second menu page for character and map selection for multiplayer
    keepgoing = True
    while keepgoing:
        img = pygame.image.load("map"+str(c)+".png").convert() #images of maps
        screen.blit(img,[210,400])
        text("Choose your map",100,325,"comicsansms",30,175,0,0)
        button("Start Game!",400,700,400,60,(200,200,200),(150,150,150),play)
        button("Back",10,700,190,60,(200,200,200),(150,150,150),multiplayer)
        button("Back to Menu",1000,700,190,60,(200,200,200),(150,150,150),intro)
        button("<",100,450,40,60,(200,200,200),(150,150,150),next_image2)
        button(">",650,450,40,60,(200,200,200),(150,150,150),previous_image2)
        pygame.display.flip()
        Screen()
        
def instructions(): #menu page for game instructions
    keepgoing = True
    while keepgoing:
        text("Instructions",100,285,"comicsansms",40,175,0,0)
        text("Welcome to Boxhead-Bill Sun Special!",100,350,"comicsansms",20,175,0,0)
        text("This is a survival game. Kill the zombies and creepers to pass each level.",100,380,"comicsansms",20,175,0,0)
        text("There is friendly fire. Be careful where you're shooting!.",100,410,"comicsansms",20,175,0,0)
        text("Controls",100,500,"comicsansms",25,0,0,0)
        text("Player 1: Arrow keys for movement, left click mouse for shooting",100,540,"comicsansms",20,175,0,0)
        text("Player 2: W, A, S, D for movement, space bar for shooting",100,570,"comicsansms",20,175,0,0)
        text("Both player use the mouse to aim",100,600,"comicsansms",20,175,0,0)
        button("Back",1000,700,190,60,(200,200,200),(150,150,150),intro)
        pygame.display.flip()
        Screen()
        #WILL BE UPDATED WHEN THE GAME IS SET

def settings(): #menu page for game settings
    keepgoing = True
    while keepgoing:
        text("Settings",100,285,"comicsansms",40,175,0,0)
        button("Back",1000,700,190,60,(200,200,200),(150,150,150),intro)
        pygame.display.flip()
        Screen()
        #volume
        #music on/off
        #difficulty (creepers on and off)
        #WILL BE UPDATED SOON

def Credits(): #menu page for game credits
    keepgoing = True
    while keepgoing:
        screen.blit(logo2,[600,315])
        text("Credits",100,285,"comicsansms",40,175,0,0)
        text("#$w@g Productions Inc.",100,350,"comicsansms",25,175,0,0)
        text("Production team: Bill Sun and Umair Malik",100,390,"comicsansms",25,0,0,0)
        text("Graphics and effects by: Umair Malik",100,430,"comicsansms",25,0,0,0)
        text("Sounds and visuals by: Umair Malik",100,470,"comicsansms",25,0,0,0)
        text("Game code written by: Bill Sun",100,510,"comicsansms",25,0,0,0)
        text("Debugged and edited by: Umair Malik",100,550,"comicsansms",25,0,0,0)
        text("Game idea based on Boxhead 2Play",100,620,"comicsansms",25,0,0,0)
        text("A Sean Cooper Game",100,660,"comicsansms",25,0,0,0)
        text("Earl Haig Secondary School",800,430,"comicsansms",25,0,0,0)
        text("Introduction to Computer Programming",670,470,"comicsansms",25,0,0,0)
        text("Class code: ICS3U1-02",856,510,"comicsansms",25,0,0,0)
        text("Teacher: Dr. S. Noukhovitch",793,550,"comicsansms",25,0,0,0)
        button("Back",1000,700,190,60,(200,200,200),(150,150,150),intro)
        pygame.display.flip()
        Screen()

def intro(): #main menu page
    keepgoing = True
    while keepgoing:
        screen.blit(logo,[230,25])
        button("Singleplayer",400,420,400,60,(200,200,200),(150,150,150),singleplayer)
        button("Multiplayer",400,490,400,60,(200,200,200),(150,150,150),multiplayer)
        button("Help",400,560,195,60,(200,200,200),(150,150,150),instructions)
        button("Settings",605,560,195,60,(200,200,200),(150,150,150),settings)
        button("Exit",400,630,195,60,(200,200,200),(150,150,150),quitgame)
        button("Credits",605,630,195,60,(200,200,200),(150,150,150),Credits)
        text("#$w@g Productions Inc.",900,720,"comicsansms",25,175,0,0)
        pygame.display.flip()
        Screen()

#Sprites

#Sprite groups
playerI = pygame.sprite.Group()
playerII = pygame.sprite.Group()
walls = pygame.sprite.Group()
zombies = pygame.sprite.Group()
creepers = pygame.sprite.Group()
bullets = pygame.sprite.Group()
            
class player1(pygame.sprite.Sprite):
    def __init__(player1):
        pygame.sprite.Sprite.__init__(player1)
        player1.image = pygame.image.load("character"+str(a)+".png").convert_alpha() #load the selected character (index a)
        player1.rect = player1.image.get_rect()
        player1.rect.x = 500 #starting location
        player1.rect.y = 350
        player1.health = 1000 #full health = 1000
 
    def move(player1, dx, dy):#move each axis separately
        if dx != 0:
            player1.move_object(dx, 0)
        if dy != 0:
            player1.move_object(0, dy)
    
    def move_object(self, dx, dy): #move the rect object
        self.rect.x += dx
        self.rect.y += dy

        for wall in walls: #if the player collides with a wall, move out based on velocity
            if self.rect.colliderect(wall.rect):
                if dx > 0: #moving right, hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: #moving left, hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: #moving down, hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: #moving up, hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

    def main(player1):
        key = pygame.key.get_pressed() #move the player as keys get pressed
        if key[pygame.K_LEFT]:
            player1.move(-1,0)
        if key[pygame.K_RIGHT]:
            player1.move(1,0)
        if key[pygame.K_UP]:
            player1.move(0,-1)
        if key[pygame.K_DOWN]:
            player1.move(0,1)

        mouse = pygame.mouse.get_pressed()
        if mouse[0]: #firing mechanism for player 1
            audio("machine_gun_fire") 
            target_pos = pygame.mouse.get_pos()
            angle1 = math.atan2(target_pos[1]-player1.rect.center[1],target_pos[0]-player1.rect.center[0]) #angle of the gunfire
            bullet = mbullet(player1, angle1) 
            bullets.add(bullet)

        if player1.health <= 0: #player dies
            audio("player_hurt")
            player1.kill()

class player2(pygame.sprite.Sprite):
    def __init__(player2):
        pygame.sprite.Sprite.__init__(player2)
        player2.image = pygame.image.load("character"+str(b)+".png").convert_alpha() #load the selected character (index b)
        player2.rect = player2.image.get_rect()
        player2.rect.x = 600 #starting location
        player2.rect.y = 350
        player2.health = 1000 #full health = 1000

    def move(player2, dx, dy):#move each axis separately
        if dx != 0:
            player2.move_object(dx, 0)
        if dy != 0:
            player2.move_object(0, dy)
    
    def move_object(self, dx, dy): #move the rect object
        self.rect.x += dx
        self.rect.y += dy

        for wall in walls: #if the player collides with a wall, move out based on velocity
            if self.rect.colliderect(wall.rect):
                if dx > 0: #moving right, hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: #moving left, hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: #moving down, hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: #moving up, hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

    def main(player2):
        key = pygame.key.get_pressed() #move the player as keys get pressed
        if key[pygame.K_a]:
            player2.move(-1,0)
        if key[pygame.K_d]:
            player2.move(1,0)
        if key[pygame.K_w]:
            player2.move(0,-1)
        if key[pygame.K_s]:
            player2.move(0,1)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]: #firing mechanism for player 2
            audio("machine_gun_fire")
            target_pos = pygame.mouse.get_pos()
            angle2 = math.atan2(target_pos[1]-player2.rect.center[1],target_pos[0]-player2.rect.center[0])
            bullet = mbullet(player2, angle2)
            bullets.add(bullet)

        if player2.health <= 0: #player dies
            audio("player_hurt")
            player2.kill()

class mbullet(pygame.sprite.Sprite): #machine gun bullets
    def __init__(self, player, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center[0]+25*math.cos(angle), player.rect.center[1]+25*math.sin(angle)
        self.speed = 25 #speed and direction of the bullet
        self.Vx = self.speed*math.cos(angle+random.randrange(-5,6)/200) 
        self.Vy = self.speed*math.sin(angle+random.randrange(-5,6)/200)
        self.posInfo = [self.rect.center[0],self.rect.center[1]]

    def main(self):
        self.posInfo[0] += self.Vx #update the position of each bullet
        self.posInfo[1] += self.Vy
        self.rect.move_ip(self.posInfo[0]-self.rect.center[0],self.posInfo[1]-self.rect.center[1])
        if self.rect.colliderect(player1.rect) == True and self.rect.colliderect(player2.rect) == False: #friendly fire
            player1.health -= 1
            audio("player_hurt")
            self.kill()
        if self.rect.colliderect(player2.rect) == True and self.rect.colliderect(player1.rect) == False:
            player2.health -= 1
            audio("player_hurt")
            self.kill()

class zombie(pygame.sprite.Sprite): #The normal type of enemies. Harmful if the player touches it.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load("character2.png").convert_alpha()
        self.rect = self.image.get_rect()           
        self.speed = 0.2
        self.health = 200 #starting health
        spawning_points = [(1000,-50),(160,750)] #spawns randomly at the two entrances to the map
        self.rect.x, self.rect.y = random.choice(spawning_points)
        self.posInfo = [self.rect.center[0],self.rect.center[1]]

    def move(self, dx, dy):#move each axis separately
        if dx != 0:
            self.move_object(dx, 0)
        if dy != 0:
            self.move_object(0, dy)
    
    def move_object(self, dx, dy): #move the rect object
        self.posInfo[0] += dx
        self.posInfo[1] += dy

        for wall in walls: #if the zombie collides with a wall, move out based on velocity
            if self.rect.colliderect(wall.rect):
                if dx > 0: #moving right, hit the left side of the wall
                    self.posInfo[0] = wall.rect.left - 25
                if dx < 0: #moving left, hit the right side of the wall
                    self.posInfo[0] = wall.rect.right + 25
#                if dy > 0: #moving down, hit the top side of the wall
#                    self.posInfo[1] = wall.rect.top - 42
#                if dy < 0: #moving up, hit the bottom side of the wall
#                    self.posInfo[1] = wall.rect.bottom + 42
   
    def main(self):
        distance1 = ((self.rect.x-player1.rect.x)**2+(self.rect.y-player1.rect.y)**2) #distance from player 1
        distance2 = ((self.rect.x-player2.rect.x)**2+(self.rect.y-player2.rect.y)**2) #distance from player 2

        if distance1 < distance2: #the zombie will chase the closer player relative to its location
            chase_angle = math.atan2(player1.rect.center[1]-self.rect.center[1],player1.rect.center[0]-self.rect.center[0])    
        else:
            chase_angle = math.atan2(player2.rect.center[1]-self.rect.center[1],player2.rect.center[0]-self.rect.center[0])

        self.Vx = self.speed*math.cos(chase_angle)
        self.Vy = self.speed*math.sin(chase_angle)
        self.move_object(self.Vx, self.Vy) #update position
        self.rect.move_ip(self.posInfo[0]-self.rect.center[0],self.posInfo[1]-self.rect.center[1])
         
        if player1.rect.colliderect(self.rect): #health damage to the players if the zombies touch them
            player1.health -= 1
            audio1("player_hurt")
        if player2.rect.colliderect(self.rect):
            player2.health -= 1
            audio1("player_hurt")

class creeper(pygame.sprite.Sprite): #A harder type of enemy. Will explode when the player touches it.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load("character5.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 0.35
        self.health = 500 #starting health
        spawning_points = [(1000,-50),(160,750)]
        self.rect.x, self.rect.y = random.choice(spawning_points)
        self.posInfo = [self.rect.center[0],self.rect.center[1]]
   
    def move(self, dx, dy):#move each axis separately
        if dx != 0:
            self.move_object(dx, 0)
        if dy != 0:
            self.move_object(0, dy)
    
    def move_object(self, dx, dy): #move the rect object
        self.posInfo[0] += dx
        self.posInfo[1] += dy

        for wall in walls: #if the zombie collides with a wall, move out based on velocity
            if self.rect.colliderect(wall.rect):
                if dx > 0: #moving right, hit the left side of the wall
                    self.posInfo[0] = wall.rect.left - 21
                if dx < 0: #moving left, hit the right side of the wall
                    self.posInfo[0] = wall.rect.right + 21
#                if dy > 0: #moving down, hit the top side of the wall
#                    self.posInfo[1] = wall.rect.top - 43
#                if dy < 0: #moving up, hit the bottom side of the wall
#                    self.posInfo[1] = wall.rect.bottom + 43
   
    def main(self):
        distance1 = ((self.rect.x-player1.rect.x)**2+(self.rect.y-player1.rect.y)**2) #distance from player 1
        distance2 = ((self.rect.x-player2.rect.x)**2+(self.rect.y-player2.rect.y)**2) #distance from player 2

        if distance1 < distance2: #the zombie will chase the closer player relative to its location
            chase_angle = math.atan2(player1.rect.center[1]-self.rect.center[1],player1.rect.center[0]-self.rect.center[0])    
        else:
            chase_angle = math.atan2(player2.rect.center[1]-self.rect.center[1],player2.rect.center[0]-self.rect.center[0])

        self.Vx = self.speed*math.cos(chase_angle)
        self.Vy = self.speed*math.sin(chase_angle)
        self.move_object(self.Vx, self.Vy) #update position
        self.rect.move_ip(self.posInfo[0]-self.rect.center[0],self.posInfo[1]-self.rect.center[1])
        
class bloodpack(pygame.sprite.Sprite): #blood packs that restores the player's health if the player touches it
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load("bloodpack.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50,1108) #randomly generated on the map
        self.rect.y = random.randint(78,658)

    def main(self):
        if player1.rect.colliderect(self.rect):
            self.rect.x = random.randint(50,1108) #appears on a random location on the map
            self.rect.y = random.randint(78,658)
            audio1("button_click")
            player1.health += 500 #adds 500 health points to the player that collects it
            if player1.health > 1000:
                player1.health = 1000
        if player2.rect.colliderect(self.rect):
            self.rect.x = random.randint(50,1108)
            self.rect.y = random.randint(78,658)
            audio1("button_click")
            player2.health += 500
            if player2.health > 1000:
                player2.health = 1000

        for enemy in zombies: #if the enemies collect the blood pack, it will heal them as well!
            if enemy.rect.colliderect(self.rect):
                self.rect.x = random.randint(50,1108)
                self.rect.y = random.randint(78,658)
                audio1("button_click")
                enemy.health = 200

        for enemy1 in creepers:
            if enemy1.rect.colliderect(self.rect):
                self.rect.x = random.randint(50,1108)
                self.rect.y = random.randint(78,658)
                audio1("button_click")
                enemy1.health = 500

class Wall(pygame.sprite.Sprite):
    def __init__(Wall, info): #info includes x and y coordinates and walltype
        pygame.sprite.Sprite.__init__(Wall)
        Wall.image = pygame.image.load("wall"+str(info[2])+".png").convert_alpha()
        Wall.rect = Wall.image.get_rect()
        Wall.rect.x = info[0]
        Wall.rect.y = info[1]

#Information for each level and every map
levelinfo = {"1":(10,1), "2":(15,1), "3":(20,2), "4":(30,2), "5":(40,3), "6":(50,3), "7":(60,3), "8":(75,4), "9":(90,4), "10":(100,5), "11":(120,5), "12":(140,6), "13":(165,6)}
#key = level number; value = (Number of zombies, Number of creepers)
maps = {"1":((166,0,5),(332,0,5),(498,0,5),(664,0,5),(830,0,5),(1050,0,5),(0,0,5),(-2,38,6),(1150,38,6),(-10,700,5),(-2,606,6),(210,700,5),(376,700,5),(542,700,5),(708,700,5),(874,700,5),(1150,606,6),(1040,700,5),(-2,180,6),(-2,322,6),(-2,464,6),(1150,180,6),(1150,322,6),(1150,464,6)),
        "2":((540,175,1),(540,475,1),(200,175,1),(200,475,1),(890,175,1),(890,475,1),(745,345,4),(405,345,4),(166,0,5),(332,0,5),(498,0,5),(664,0,5),(830,0,5),(1050,0,5),(0,0,5),(-2,38,6),(1150,38,6),(-2,606,6),(-10,700,5),(210,700,5),(376,700,5),(542,700,5),(708,700,5),(874,700,5),(1150,606,6),(1040,700,5),(-2,180,6),(-2,322,6),(-2,464,6),(1150,180,6),(1150,322,6),(1150,464,6)),
        "4":((155,175,4),(295,175,4),(435,175,4),(575,175,4),(715,175,4),(855,175,4),(995,175,4),(155,350,4),(295,350,4),(435,350,4),(575,350,4),(715,350,4),(855,350,4),(995,350,4),(155,525,4),(295,525,4),(435,525,4),(575,525,4),(715,525,4),(855,525,4),(995,525,4),(166,0,5),(332,0,5),(498,0,5),(664,0,5),(830,0,5),(1050,0,5),(0,0,5),(-2,38,6),(1150,38,6),(-10,700,5),(1040,700,5),(-2,606,6),(210,700,5),(376,700,5),(542,700,5),(708,700,5),(874,700,5),(1150,606,6),(-2,180,6),(-2,322,6),(-2,464,6),(1150,180,6),(1150,322,6),(1150,464,6)),
        "5":((158,200,6),(988,365,6),(158,342,4),(988,507,4),(158,500,5),(210,200,5),(376,200,5),(542,200,5),(708,200,5),(874,200,5),(158,500,5),(324,500,5),(490,500,5),(656,500,5),(822,500,5),(166,0,5),(332,0,5),(498,0,5),(664,0,5),(830,0,5),(1050,0,5),(0,0,5),(-2,38,6),(1150,38,6),(-2,606,6),(-10,700,5),(210,700,5),(376,700,5),(542,700,5),(708,700,5),(874,700,5),(1150,606,6),(1040,700,5),(-2,180,6),(-2,322,6),(-2,464,6),(1150,180,6),(1150,322,6),(1150,464,6)),
        "3":((1050,0,5),(884,223,5),(718,223,5),(552,223,5),(386,223,5),(220,223,5),(156,457,5),(322,457,5),(488,457,5),(654,457,5),(820,457,5),(166,0,5),(332,0,5),(498,0,5),(664,0,5),(830,0,5),(1150,38,6),(0,0,5),(-2,38,6),(1050,38,6),(1050,180,6),(1050,322,6),(-2,606,6),(1050,464,4),(-10,700,5),(210,700,5),(376,700,5),(542,700,5),(708,700,5),(874,700,5),(1040,700,5),(1150,606,6),(104,558,6),(104,416,6),(104,274,6),(104,223,7),(-2,180,6),(-2,322,6),(-2,464,6),(1150,180,6),(1150,322,6),(1150,464,6))}
#key = map number; value = ((x coordinate, y coordinate, type of wall) for each individual wall)

Level = 0
score = 0

def pause(): #function to pause the game
    keepgoing = False
    pause = True
    while pause:
        button("Resume Game",400,270,400,60,(200,200,200),(150,150,150),resume)
        button("Back to Menu",400,340,400,60,(200,200,200),(150,150,150),intro)
        button("Restart Level",400,410,400,60,(200,200,200),(150,150,150),play)
        text("Game Paused",475,170,"comicsansms",40,175,0,0)
        keys = pygame.key.get_pressed()
        for ev in pygame.event.get():
            if keys[K_ESCAPE]:
                quitgame()
        pygame.display.flip()
        
def resume(): #function to resume the game after pausing
    pause = False
    keepgoing = True
    current_level = True
    #requires fixing

def gameover(): #gamepage when the player dies
    gameover = True
    while gameover:
        text("Game Over",490,170,"comicsansms",40,200,0,0)
        text("Your Score: "+str(score),490,230,"comicsansms",30,0,0,0)
        button("Back to Menu",400,320,400,60,(200,200,200),(150,150,150),intro)
        button("Quit",400,390,400,60,(200,200,200),(150,150,150),quitgame)
        keys = pygame.key.get_pressed()
        for ev in pygame.event.get():
            if keys[K_ESCAPE]:
                quitgame()
        pygame.display.flip()


#Main Gameplay
def play():
    global player1, player2, wall, bloodpack, a, b, c, Level, score
    #Initilize sprites and sprite groups
    for level in maps.keys(): 
        if level == str(c):
            wallinfo = list(maps[level]) #enter the map chosen
    
    for info in wallinfo:
        wall = Wall(info) #initilize each wall
        walls.add(wall)
        
    bloodpack = bloodpack() 
    player1 = player1()
    playerI.add(player1)
    player2 = player2()
    playerII.add(player2)
    
    current_level = True
    while current_level: #This loop is looped when the current level is complete       
        Level += 1
        for level, index in levelinfo.items(): #define the enemies according to the level information
            if int(level) == Level:
                index = list(levelinfo[level])
                n_zombies = index[0]
                n_creepers = index[1]

        x = -750 #time variables
        y = -750
        n_zombies = int(n_zombies) #Number of enemies yet to be spawned
        n_creepers = int(n_creepers)
        nz = n_zombies #Number of enemies alive
        nc = n_creepers

        #Main gameloop
        keepgoing = True
        clock = pygame.time.Clock()
        while keepgoing: 
            clock.tick(150) #150 frames per second
            keys = pygame.key.get_pressed()
            for ev in pygame.event.get():
                if keys[K_ESCAPE]:
                    keepgoing = False
                    pygame.quit()
            screen.fill((255,255,255))
                
            #spawning the enemies in a timely manner
            x += 1
            y += 1
            if x >= 250/Level: #when the time reaches a certain point a zombie spawns
            #zombies are spawned at higher rates when the level gets higher
                if n_zombies > 0:
                    x = 0      #and the time is set back to 0 and starts counting again
                    n_zombies -= 1
                    enemy = zombie()
                    zombies.add(enemy)
                if n_zombies <= 0: #once a certain number of enemies are spawned, the loop stops
                    n_zombies = 0

            if y >= 1500/Level: #same concept for spawning the creepers
                if n_creepers > 0:
                    y = 0
                    n_creepers -= 1
                    enemy1 = creeper()
                    creepers.add(enemy1)
                if n_creepers <= 0:
                    n_creepers = 0

            for player1 in playerI: #run the main controls for the players
                player1.main()     
                screen.blit(player1.image, player1.rect)
            for player2 in playerII:
                player2.main()
                screen.blit(player2.image, player2.rect)

            if 0 < player1.health < 1000: #player health is slowly restored
                player1.health += 0.0375               
            if 0 < player2.health < 1000:
                player2.health += 0.0375

            for wall in walls: #runs the main function for the walls
                screen.blit(wall.image, wall.rect)
            for enemy in zombies: #runs the main functions for the zombies
                enemy.main()
                screen.blit(enemy.image, enemy.rect)

            for enemy1 in creepers: #runs the main functions for the creepers
                enemy1.main()
                screen.blit(enemy1.image, enemy1.rect)
                
                explosion = pygame.image.load("explosion.png").convert_alpha()
                if player1.rect.colliderect(enemy1.rect):
                    player1.health -= 500 #when the player hits the creeper, it exploodes with 500 instant health damage to the player
                    audio1("explosion")
                    enemy1.kill() #and the creeper disappears
                    nc -= 1
                    for a in range (1,500): #flash an image of the explosion
                        screen.blit(explosion,[enemy1.posInfo[0]-50, enemy1.posInfo[1]-50])
                if player2.rect.colliderect(enemy1.rect):
                    player2.health -= 500
                    audio1("explosion")
                    enemy1.kill()
                    nc -= 1
                    for a in range (1,500):
                        screen.blit(explosion,[enemy1.posInfo[0]-50, enemy1.posInfo[1]-50])
                    
            for bullet in bullets: #run the main functions for the bullets
                bullet.main()
                screen.blit(bullet.image, bullet.rect)
                for enemy in zombies: #each bullet has a health damage of 1
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.health -= 1
                        bullet.kill()
                    if enemy.health <= 0: #once the enemy's health is below zero, it dies
                        audio1("zombie_death")
                        enemy.kill()
                        score += 100*Level #add to the score (the score is multiplied by the level)
                        nz -= 1
                for enemy1 in creepers: #same concept for the creepers
                    if bullet.rect.colliderect(enemy1.rect):
                        enemy1.health -= 1
                        bullet.kill()
                    if enemy1.health <= 0:
                        audio1("zombie_death")
                        enemy1.kill()
                        score += 250*Level
                        nc -= 1
                for wall in walls:
                    if bullet.rect.colliderect(wall.rect):
                        bullet.kill()

            bloodpack.main() #run the main function for the blood pack
            screen.blit(bloodpack.image, bloodpack.rect)
            
            if x == -400: audio("next_level") #Introduction to new level    
            if -400 < x < 0: text("Level "+str(Level),540,350,"comicsansms",35,0,0,250)
            
            for player1 in playerI: #Health display for each player
                if player1.health > 500: text("Player 1 Health: "+str(int(player1.health))+"/1000",55,80,"comicsansms",20,0,175,0)
                if 500 >= player1.health > 250: text("Player 1 Health: "+str(int(player1.health))+"/1000",55,80,"comicsansms",20,250,150,0)
                if 250 >= player1.health > 0: text("Player 1 Health: "+str(int(player1.health))+"/1000",55,80,"comicsansms",20,250,0,0)
            if player1.health <= 0:
                text("Player 1 is dead",55,80,"comicsansms",20,0,0,0)
                player1.rect.x, player1.rect.y = 10000000,1000000 #place it away from the map
            
            for player2 in playerII: #Different colours are used for different levels of health
                if player2.health > 500: text("Player 2 Health: "+str(int(player2.health))+"/1000",55,105,"comicsansms",20,0,175,0)
                if 500 >= player2.health > 250: text("Player 2 Health: "+str(int(player2.health))+"/1000",55,105,"comicsansms",20,250,150,0)
                if 250 >= player2.health > 0: text("Player 2 Health: "+str(int(player2.health))+"/1000",55,105,"comicsansms",20,250,0,0)
            if player2.health <= 0:
                text("Player 2 is dead",55,105,"comicsansms",20,0,0,0)
                player2.rect.x, player2.rect.y = 10000000,1000000 #place it away from the map

            text("Score: "+str(score),500,85,"comicsansms",25,200,0,255) #Score display
            button("Pause",1090,710,100,50,(200,200,200),(150,150,150),pause) #Button to pause the game

            pygame.display.flip()
            
            if nz <= 0 and nc <= 0: #when there are no enemies alive, go to next level
                keepgoing = False

            if player1.health <= 0 and player2.health <= 0: #direct to final page when game is over
                keepgoing = False
                gameover()
                
music("trololol song") #some background music
intro()

#PROBLEMS TO BE FIXED

#FIX ZOMBIE / CREEPER WALL COLLISION
#FIX THE PAUSING FUNCTION
#ONLY ONE PLAYER DURING SINGLEPLAYER GAMEPLAY
#FIX THE PROBLEM THAT THE GAME CANNOT RUN AGAIN AFTER THE FIRST RUN


#FEATURES TO ADD

#ANIMATED CHARACTERS AND ENEMIES
#MORE SOUND EFFECTS
#OTHER TYPES OF GUNS/WEAPONS
#WEAPON UPGRADES
#RESPAWNING OF PLAYERS (3 LIVES EACH)
#RECORD HIGHSCORES


