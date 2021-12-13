#import time
#import numpy as np
from numpy.core.arrayprint import _object_format
from pygame import mixer
from MusicInitializer import MusicInitializer
import MusicSwitcher as ms
import LaserDetector as LD

# 音の制御クラス(名前変えたほうが良くないか？)
# 音源の数だけ作る
class MusicPlayer:
    isPlayed = False
    mySoundCh = 0,0
    def __init__(self,laserCh,distCh):
        # laser tyousei
        self.mySoundCh = laserCh,distCh
    def playMusic(self):
        # 1ループ流した後、音源を止める
        # 書き方が微妙
        #print("LD",self.mySoundCh[0],LD.getLaser(self.mySoundCh[0]))
        currentSound = ms.switchLaser(self.mySoundCh[0]),ms.switchDistance()
        if currentSound[0] == -1:
            if self.isPlayed == True:
                print("pause")
                MusicInitializer.speakers[self.mySoundCh].pause()
                self.isPlayed = False
            return 0#print("nonne laser")
        #print("my",self.mySoundCh,"cur",currentSound,"LD",self.mySoundCh[0],LD.getLaser(self.mySoundCh[0]))
        if self.mySoundCh == currentSound:
            #ongen +1 zureru
            print(self.mySoundCh)
            MusicInitializer.speakers[self.mySoundCh].unpause()
            #print("run",self.mySoundCh,currentSound)
            self.isPlayed = True
        

    def testPrint(self):
        #print(ms.switchLaser(),ms.switchDistance())
        print("test")
        
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
