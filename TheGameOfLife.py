import os
import subprocess
board=[[0 for x in range(15)] for y in range(15)]
board[0][0]=1
board[1][1]=1
board[1][2]=1
board[2][1]=1
board[0][2]=1
screen=[[0 for x in range(15)] for y in range(15)]
def printBoardAndScreen():
    os.system("clear")
    print "\n"*50
    for x in range(len(board)):
        for y in range(len(board[0])):
            print board[x][y],
            if y ==len(board[0])-1:
                print
    print
    for x in range(len(screen)):
        for y in range(len(screen[0])):
            print screen[x][y],
            if y ==len(screen[0])-1:
                print
    print
def printScreen():
    for x in range(len(screen)):
        for y in range(len(screen[0])):
            print screen[x][y],
            if y ==len(screen[0])-1:
                print
    print
def printBoard():
    os.system("clear")
    print "\n"*50
    for x in range(len(board)):
        for y in range(len(board[0])):
            print board[x][y],
            if y ==len(board[0])-1:
                print
def printAscii():
    os.system("clear")
    print "\n"*50
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y]==1:
                print "*",
            else:
                print ".",
            if y ==len(board[0])-1:
                print
    print
def check(x,y):
    viz=0
    if y>0:
        if x>0:
            if board[x-1][y-1]==1:
                viz+=1
        if board[x][y-1]==1:
            viz+=1
        if x<len(board)-1:
            if board[x+1][y-1]==1:
                viz+=1
    if x>0:
        if board[x-1][y]==1:
            viz+=1
    if x<len(board)-1:
        if board[x+1][y]==1:
            viz+=1
    if y<len(board[0])-1:
        if x>0:
            if board[x-1][y+1]==1:
                viz+=1
        if board[x][y+1]==1:
            viz+=1
        if x<len(board)-1:
            if board[x+1][y+1]==1:
                viz+=1
    if viz == 2 and board[x][y]!=1:
        viz-=1
    screen[x][y]=viz
def gerate(x,y):
    if screen[x][y]==3:
        board[x][y]=1
    if screen[x][y]>3:
        board[x][y]=0
    if screen[x][y]==2:
        board[x][y]=1
    if screen[x][y]<2:
        board[x][y]=0

    
    
    
