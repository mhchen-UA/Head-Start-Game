from graphics import *
import random

player1 = "Left person"
player2 = "Right person"

win = GraphWin("",800,600)
winner = ""
h = Text(Point(400,100),"Click to start")
h.draw(win)
win.getMouse()
h.undraw()
while True:
    a = False
    x = random.randint(1,300000)
    if x<10 and not a:
        a = True
        win.setBackground(color_rgb(random.randint(1,255),random.randint(1,255),random.randint(1,255)))
    b = win.checkKey()
    if a:
        if b == 'a':
            winner = player1
            break
        elif b == 'l':
            winner = player2
            break
    else:
        if b == 'a':
            winner = player1
            break
        elif b== 'l':
            winner = player2
            break
print(b)
d = Text(Point(400,300),"WINNER: "+winner)
d.setSize(29)
d.draw(win)
while True:
    d.setTextColor(color_rgb(random.randint(1,255),random.randint(1,255),random.randint(1,255)))
