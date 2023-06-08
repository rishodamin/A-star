from pathFinder import FindPath
from random import choice as rd
from random import randint as ri
import pygame
pygame.init()

# color variables
white = (250,250,250)
greenL = (150,255,150)
dark = (50,50,50)
halfwhite = (199,189,153)
darkgrey = (100,100,100)
red = (255,100,140)
blue = (50,80,255)
grey = (130,130,130)
yellow =(246,190,0)
brown = (65,25,0)

# font variables
font128 = pygame.font.Font("font/font.ttf",128)
font32 = pygame.font.Font("font/font.ttf",32)

#   Window  setting......
win_width = 1000
win_height = 680
pygame.display.set_caption("Maze Router")
win = pygame.display.set_mode((win_width,win_height))

# Maze...........
row = 36
col = 40
side = (win_height/row)*0.9
speed = 5
start = None
goal = None
searched_box_ind = 0
route_ind = 0
path = None
route = None

maze = [[rd([1,0,0]) for _ in range(col)] for _ in range(row)]

def splash():
    color = 255
    while color != 1:
        text1 = font128.render("Risho's",True,(color,color,color),1)
        text2 = font128.render("Project",True,(color,color,color),1)
        win.blit(text1,(win_width/5,win_height/5))
        win.blit(text2,(win_width/5.5,win_height/2))
        pygame.display.update()
        pygame.time.delay(10)
        color-=2      
        
def drawMaze(side):
    box_wid = win_width/2-(side/2)*len(maze[0])
    box_hig = win_height/2-(side/2)*len(maze)
    pygame.draw.rect(win,dark,(box_wid,box_hig,side,side),2)
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col]:
                pygame.draw.rect(win,grey,(box_wid+col*side,box_hig+row*side,side,side))
            else:
                pygame.draw.rect(win,greenL,(box_wid+col*side,box_hig+row*side,side,side),2)
    pygame.draw.rect(win,red,(box_wid+start[1]*side,box_hig+start[0]*side,side,side)) ## StartBox coloring
    pygame.draw.rect(win,brown,(box_wid+goal[1]*side,box_hig+goal[0]*side,side,side)) ## GoalBox coloring
    
            
def interface(search=False):
    win.fill(white)
    drawMaze(side)
    if search:
        find()
    pygame.display.update()
    pygame.time.delay(speed)
    
def find():
    global searched_box_ind, route_ind
    box_wid = win_width/2-(side/2)*len(maze[0])
    box_hig = win_height/2-(side/2)*len(maze)
    for count, pos in enumerate(path.path_history):
        pygame.draw.rect(win,yellow,(box_wid+pos[1]*side,box_hig+pos[0]*side,side,side),2)
        if count==searched_box_ind:
            break
    if searched_box_ind<len(path.path_history)+1:
        searched_box_ind += 1
    else:
        for count, pos in enumerate(route):
            pygame.draw.rect(win,brown,(box_wid+pos[1]*side,box_hig+pos[0]*side,side,side))
            if count==route_ind:
                break
        if route_ind<len(route)+1:
            route_ind += 1
    
splash() 
run = True
enter = False
ispath = True
restart = True
    
while run:
    if restart: 
        restart = False
        path = FindPath(maze)
        start = ri(0,row-1),ri(0,col-1)
        goal = ri(0,row-1),ri(0,col-1)
        maze[start[0]][start[1]] = 0
        maze[goal[0]][goal[1]] = 0
        route = path.find_path(start,goal)
        if route[0]!=goal:
            ispath = False
            route.clear()
        else:
            del route[0]
    if enter and ispath:
        interface(search=True)
    else:
        interface()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                side += 1
            if event.key == pygame.K_DOWN:
                side -= 1
            if event.key == pygame.K_RETURN:
                if enter:
                    searched_box_ind = 0
                    route_ind = 0
                    route.clear()
                    restart = True
                    enter = False
                    ispath  = True
                    continue
                enter = True
                

