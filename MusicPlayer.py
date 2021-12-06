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
    PLAYED = False
    myLaserCh=0
    myDistCh=0
    def __init__(self,laserCh,distCh):
        self.myLaserCh,self.myDistCh = laserCh,distCh
    def playMusic(self):
        # 1ループ流した後、音源を止める
        # 書き方が微妙
        #print("LD",self.MySoundCh[0],LD.getLaser(self.MySoundCh[0]))
        currentSound = ms.switchLaser(self.MySoundCh[0]),ms.switchDistance()
        print("my",self.MySoundCh,"cur",currentSound,"LD",self.MySoundCh[0],LD.getLaser(self.MySoundCh[0]))
        if self.MySoundCh == currentSound:
            #ongen +1 zureru
            MusicInitializer.speakers[self.MySoundCh].unpause()
            print("run",self.MySoundCh,currentSound)
        else :
        #time.sleep(currentSound.get_length())
            print("pause")
            MusicInitializer.speakers[self.MySoundCh].pause()
        

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
