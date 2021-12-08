import numpy as np
import pygame
import math
#from enum import IntEnum

#class Playerturn(IntEnum):
#    Player1=0
#    Player2=1
ROWS= 3
COLUMNS = 3

WHITE=(255,255,255)
BLACK=(0,0,0)
RED= (255,0,0)
BLUE=(0,0,255)
WIDTH = 600
HEIGHT= 600
SIZE=(WIDTH,HEIGHT)
CIRCLE=pygame.image.load('circle.png')
CROSS=pygame.image.load('x.png')

def draw_lines():
    pygame.draw.line(window, BLACK, (200,0),(200,600), 10)
    pygame.draw.line(window, BLACK, (400,0),(400,600), 10)
    pygame.draw.line(window, BLACK, (0,200),(600,200), 10)
    pygame.draw.line(window, BLACK, (0,400),(600,400), 10)
def draw_board():
    for c in range(COLUMNS):
        for r in range (ROWS):
            if board[r][c]==1:
                window.blit(CIRCLE,((c*200)+50,(r*200)+50))
            elif board[r][c]==2:
                window.blit(CROSS,((c*200)+50,(r*200)+50))    





def mark(row, col, player):
    board[row][col] = player
def is_valid_mark(row, col):
    if(row> ROWS or col>COLUMNS):
        print("Row and Column selection out of specified range of 3x3")
        return False  
    elif(board[row][col]==0):
        return True
    elif(board[row][col]!=0):
        print("Specified Row and Column was already selected by Player {}. Please select a new row and column".format(int(board[row][col])))
        return False
def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c]==0:
                return False
    return True
def is_winning_move(player):
    Announcement="Player {} has won".format(player)
    winning_color=RED if player==1 else BLUE
 
    
    for r in range(ROWS):
        if board[r][0]==player and board[r][1]==player and board[r][2]==player:
            pygame.draw.line(window,winning_color, (10,(r*200) +100), (WIDTH-10,(r*200)+100),10)
            print(Announcement)
            return True
    for c in range(COLUMNS):
        if board[0][c]==player and board[1][c]==player and board[2][c]==player:
            pygame.draw.line(window,winning_color, ((c*200) +100),10, ((c*200)+100,WIDTH-10),10)
            print(Announcement)
            return True
    if board[0][0] ==player and board[1][1] ==player and board[2][2] ==player:
        pygame.draw.line(window, winning_color, (10,10),((590,590),10))
        print(Announcement)
        return True
    if board[2][0] ==player and board[1][1] ==player and board[0][2] ==player:
        pygame.draw.line(window, winning_color, (590,10),((10,590),10))
        print(Announcement)
        return True
board=np.zeros((ROWS,COLUMNS))

game_over= False
turn=0

pygame.init()
window=pygame.display.set_mode(SIZE)
pygame.display.set_caption("TIC TAC TOE")
window.fill(WHITE)
draw_lines()
pygame.display.update()
pygame.time.wait(2000)

while not game_over:   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type== pygame.MOUSEBUTTONDOWN:
           # row = int(input("Player {}:Choose row number (0-2):  ".format(turn+1)))
           # col = int(input("Player {}:Choose column number (0-2):  ".format(turn+1)))
            row = math.floor(event.pos[1]/200)
            col = math.floor(event.pos[0]/200)
            if is_valid_mark(row, col):
                mark(row, col, turn+1)
                if is_winning_move(turn+1):
                    game_over=True
                print(board)
                draw_board()
                turn = not turn  
            
            if is_board_full():
                game_over=True
            if game_over==True:
                print("Game over")
                pygame.time.wait(2000)
                board.fill(0)
                window.fill(WHITE)
                draw_lines()
                draw_board()
                game_over=False
                pygame.display.update()