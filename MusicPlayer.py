import time
import numpy as np
from pygame import mixer
import MusicSwitcher as ms

# 音の制御クラス(名前変えたほうが良くないか？)
# 音源の数だけ作る
class MusicPlayer:
    LASER_CH=0
    DISTANCE_CH=0
    def __init__(self,laserCh,distCh):
        self.LASER_CH=laserCh
        self.DISTANCE_CH=distCh
    def playMusic(self):
        # 1ループ流した後、音源を止める
        # 書き方が微妙
        currentSound = self.speakers[self.LASER_CH, self.DISTANCE_CH].get_sound()
        print("実行中...")
        self.speakers[self.LASER_CH, self.DISTANCE_CH].unpause()
        time.sleep(currentSound.get_length())
        self.speakers[self.LASER_CH, self.DISTANCE_CH].pause()

mp1 = MusicPlayer()
list = 1,1
mp1.playMusic(*list)
mp2 = MusicPlayer()
mp2.playMusic(2)
while (True):
    mp.playMusic()

"""
音源の数だけplayMusicを稼働し続ける
→MusicPlayer()の実体を音源の数だけ作る？
 →__init__()を変える
 mixer.init(frequency=44100),mixer.set_num_channels(self.musicFiles.size)は一回だけ
 chの対応

"""