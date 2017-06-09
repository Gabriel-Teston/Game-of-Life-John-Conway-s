import pygame, sys
from pygame.locals import *

board = [[0 for x in xrange(87)] for y in xrange(162)]
aux = [[0 for x in xrange(87)] for y in xrange(162)]

pygame.init()

windowSurface = pygame.display.set_mode((1300, 700), 0, 32)

pygame.display.set_caption("Running!-Press <space>")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (67, 18, 174)
YELLOW = (255, 211, 0)

windowSurface.fill(WHITE)


def print_board_and_aux():
    os.system("clear")
    print "\n" * 50
    for x in xrange(len(board)):
        for y in xrange(len(board[0])):
            print board[x][y],
            if y == len(board[0]) - 1:
                print
    print
    for x in xrange(len(aux)):
        for y in xrange(len(aux[0])):
            print aux[x][y],
            if y == len(aux[0]) - 1:
                print
    print


def print_aux():
    print "\n" * 50
    for x in xrange(len(aux)):
        for y in xrange(len(aux[0])):
            print aux[x][y],
            if y == len(aux[0]) - 1:
                print
    print


def print_board():
    print "\n" * 50
    for x in xrange(len(board)):
        for y in xrange(len(board[0])):
            print board[x][y],
            if y == len(board[0]) - 1:
                print


def print_ascii():
    print "\n" * 50
    for x in xrange(len(board)):
        for y in xrange(len(board[0])):
            if board[x][y] == 1:
                print "*",
            else:
                print ".",
            if y == len(board[0]) - 1:
                print
    print


def print_py_game():
    for x in xrange(len(board)):
        for y in xrange(len(board[0])):
            if board[x][y] == 1:
                draw_cell(x * 8, y * 8)
            else:
                draw_board(x * 8, y * 8)


def check(x, y):
    neighborns = 0
    if y > 0:
        if x > 0:
            if board[x - 1][y - 1] == 1:
                neighborns += 1
        if board[x][y - 1] == 1:
            neighborns += 1
        if x < len(board) - 1:
            if board[x + 1][y - 1] == 1:
                neighborns += 1
    if x > 0:
        if board[x - 1][y] == 1:
            neighborns += 1
    if neighborns < 4:
        if x < len(board) - 1:
            if board[x + 1][y] == 1:
                neighborns += 1
        if y < len(board[0]) - 1:
            if x > 0:
                if board[x - 1][y + 1] == 1:
                    neighborns += 1
            if board[x][y + 1] == 1:
                neighborns += 1
            if x < len(board) - 1:
                if board[x + 1][y + 1] == 1:
                    neighborns += 1
        if neighborns == 2 and board[x][y] != 1:
            neighborns -= 1
    else:
        neighborns = 0
    aux[x][y] = neighborns


def gerate(x, y):
    if aux[x][y] == 3:
        board[x][y] = 1
    if aux[x][y] > 3:
        board[x][y] = 0
    if aux[x][y] == 2:
        board[x][y] = 1
    if aux[x][y] < 2:
        board[x][y] = 0


def draw_cell(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, YELLOW, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


def draw_board(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, BLUE, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


running = True
paused = False
erase = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            mouseX -= 3
            mouseY -= 3
            if erase:
                erase = (True, False)[erase]
                for x in xrange(5):
                    for y in xrange(5):
                        board[mouseX / 8 - x][mouseY / 8 - y] = 0
                        board[mouseX / 8 - x][mouseY / 8 + y] = 0
                        board[mouseX / 8 + x][mouseY / 8 - y] = 0
                        board[mouseX / 8 + x][mouseY / 8 + y] = 0
            else:
                if board[mouseX / 8][mouseY / 8] == 1:
                    board[mouseX / 8][mouseY / 8] = 0
                else:
                    board[mouseX / 8][mouseY / 8] = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
                if paused:
                    pygame.display.set_caption("Paused...-Press <space>")
                else:
                    pygame.display.set_caption("Running!-Press <space>")
            elif event.key == pygame.K_c:
                for x in xrange(len(board)):
                    for y in xrange(len(board[0])):
                        board[x][y] = 0
            elif event.key == pygame.K_DELETE:
                erase = (True, False)[erase]
            elif event.key == pygame.K_F1:
                for x in xrange(len(board)):
                    for y in xrange(len(board[0])):
                        board[x][y] = 1
            elif event.key == pygame.K_F2:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                mouseX -= 3
                mouseY -= 3
                board[mouseX / 8 - 1][mouseY / 8 - 1] = 1
                board[mouseX / 8][mouseY / 8] = 1
                board[mouseX / 8 + 1][mouseY / 8 - 1] = 1
                board[mouseX / 8 + 1][mouseY / 8] = 1
                board[mouseX / 8][mouseY / 8 + 1] = 1
            elif event.key == pygame.K_F3:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                mouseX -= 3
                mouseY -= 3
                for x in xrange(3):
                    for y in xrange(3):
                        board[mouseX / 8 - x][mouseY / 8 - y] = 1
                        board[mouseX / 8 - x][mouseY / 8 + y] = 1
                        board[mouseX / 8 + x][mouseY / 8 - y] = 1
                        board[mouseX / 8 + x][mouseY / 8 + y] = 1
    if not paused:
        for x in xrange(len(aux)):
            for y in xrange(len(aux[0])):
                check(x, y)
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                gerate(x, y)
    print_py_game()
    pygame.display.update()
pygame.quit()
sys.exit()
