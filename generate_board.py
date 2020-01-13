"""
Pulls a randomly generated Sudoku board from sudokuweb.org
"""

from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.sudokuweb.org/")
res.raise_for_status()
soup = BeautifulSoup(res.text,features="html.parser")

#takes all the HTML lines with <span>
tags = soup('span')

board = []
row = []

count = 0
count2 = 0
tags.pop(0)

#appends all the numbers in the Sudoku set
for tag in tags:

    #in the HTML, the solved board is hidden by two things
    #a span that's equal to true (why we pop)
    #and a span that's equal to "vloz" or "\xa0" (why we append 0 for an empty space)
    if tag.contents[0] == "\xa0":
        row.append("0")
        row.pop(len(row)-2)
    else:
        row.append(tag.contents[0])

    #easiest way to make this board a matrix
    if len(row) == 9:
        board.append(row)
        row = []

#I don't exactly know why
#but at the end theres the numbers 1-9 that doesn't do anything
board.pop(len(board)-1)


if __name__ == '__main__':
    # prints board
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")

            if j == 2 or j == 5:
                print("|", end=" ")

        print()

        if i == 2 or i == 5:
            print("---------------------")