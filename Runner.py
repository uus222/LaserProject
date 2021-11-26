"""
import MusicSwitcher as ms

currentLaser = ms.switchLaser()
currentDistance = ms.switchDistance()
"""

from MusicPlayer import MusicPlayer as mp
import MusicSwitcher as ms
from MusicInitializer import MusicInitializer as mi
import numpy as np

musicIn = mi()
musicIn.initMusicPayer()
shapes = musicIn.getShapes()

#MusicPlayerを音源の個数分作成
musicplayers = np.empty((shapes), object)
for row in range(shapes[0]):
    for line in range(shapes[1]):
        musicplayers[row,line] = mp(row,line)

while True:
    #test no houhou
    """
    for row in range(shapes[0]):
        for line in range(shapes[1]):
            #musicplayers[row,line].playMusic(currentCh)
            print("checked musicplayer",row,line) #動作確認用

    """