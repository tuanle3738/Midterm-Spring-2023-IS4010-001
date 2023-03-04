# main.py

from videoGamePackage.videoGame import *

totalPlays = 1000
won = 0
lost = 0
for i in range(0, totalPlays):

    if play():
        won = won + 1
    else:
        lost = lost + 1

