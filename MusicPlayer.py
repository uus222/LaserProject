#import time
#import numpy as np
#from pygame import mixer
import MusicSwitcher as ms
import LaserDetector as LD

# 音の制御クラス(名前変えたほうが良くないか？)
# 音源の数だけ作る
class MusicPlayer:
    PLAYED = False
    #LASER_CH=0
    #DISTANCE_CH=0
    MySoundCh = 0,0
    def __init__(self,laserCh,distCh):
        #self.LASER_CH=laserCh
        #self.DISTANCE_CH=distCh
        self.MySoundCh = laserCh,distCh
    def playMusic(self):
        # 1ループ流した後、音源を止める
        # 書き方が微妙
        #print("LD",self.MySoundCh[0],LD.getLaser(self.MySoundCh[0]))
        currentSound = ms.switchLaser(self.MySoundCh[0]),ms.switchDistance()
        #print("run",self.MySoundCh,currentSound)
        if self.MySoundCh == currentSound:
            if self.PLAYED == False:
                self.speakers[self.MySoundCh].unpause()
                print("run",self.MySoundCh,currentSound)
                self.PLAYED = True
        elif self.PLAYED == True:
        #time.sleep(currentSound.get_length())
            self.speakers[self.MySoundCh].pause()
            self.PLAYED = False
        

    def printCH(self):
        #print(ms.switchLaser(),ms.switchDistance())
        currentSound=ms.switchLaser(),ms.switchDistance()
        if self.MySoundCh == currentSound:
            print(currentSound)
"""
mp1 = MusicPlayer()
list = 1,1
mp1.playMusic(*list)
mp2 = MusicPlayer()
mp2.playMusic(2)
while (True):
    mp.playMusic()

音源の数だけplayMusicを稼働し続ける
→MusicPlayer()の実体を音源の数だけ作る？
 →__init__()を変える
 mixer.init(frequency=44100),mixer.set_num_channels(self.musicFiles.size)は一回だけ
 chの対応
"""
