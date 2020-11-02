#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Dr. Z
Check Win example code

Run this script to see a random board filled and checked and announcement of a random winner! 
"""

import random
import checkWin
    # you can import any .py file as a library! This allows us to use
    # dot notation to access the functions that are in that file
    
# Global variables
numside = 3 # number of spaces per side of the board

def makeBoardList(numside=3,empty=[]):
    '''Makes an empty scoreboard for tictactoe, based on the number of sides.
    The default 3x3 looks like this:
        [ [ [],[],[] ],
          [ [],[],[] ],
          [ [],[],[] ] ]
    Parameters-
    numside - (int) number of squares per side of the tic tac toe board
    empty - the indicator to use for an empty board. Try 0 or a string value.'''
    boardList = [] # empty list
    for i in range(numside):
        #make rows
        boardRow=[]
        for k in range(numside):
            # make columns
            boardRow.append(empty)
        boardList.append(boardRow)
    return boardList

def fillBoardList(boardList,empty=[],style=['X','O']):
    '''Randomly fills a 2D board (list of lists) with random values from list.
    Parameters - 
    boardList - 2D list to represent a playing board
    empty - indicator for an empty place on the board (the value you want to change)
    style - a list of values to put in place'''
    for i in range(len(boardList)):
        while empty in boardList[i]:
            col = random.randint(0,2) # pick a random column
            marker = random.choice(style) # pick a random play value
            
            boardList[i][col]=marker # replace value
            # continue until the row is filled
    return boardList
    
    
# Using the functions

boardList = fillBoardList(makeBoardList())
print(boardList[0],'\n',
      boardList[1],'\n',
      boardList[2]) # show the boardlist, but so it looks like a board!

# Now lets check to see if there's a winner
WINNER = checkWin.checkWin(boardList)
if type(WINNER) == str:
    print(WINNER + ' is the winner!')
else:
    print("It's a draw! No winner! \n",
          '\n',
          "Play again?")