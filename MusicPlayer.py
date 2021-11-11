import time
import numpy as np
import os
from pygame import mixer
import MusicSwitcher as ms


class MusicPlayer:
    # フォルダ名と拡張子(後でくっつける)
    MUSIC_FOLDER = "C:\main\大学の色々\挑戦型プロジェクト\LaserProject" + "\music\\"
    EXTENSION = ".wav"
    # 実際の音源ファイル名
    MUSIC_FILES = [["mute", "mute", "mute"],
                   ["off_ass", "off_bell", "off_connect"],
                   ["off_intro", "off_loop", "off_melo2"]]
    musicFiles = np.array(MUSIC_FILES)  # numpyで使えるようにする

    speakers = np.empty((3, 3), object)

    def __init__(self):
        print("--Sound Initializing--")
        ch = 0
        mixer.init(frequency=44100)
        # 音源の数だけspeakerを作る
        mixer.set_num_channels(self.musicFiles.size)
        # 各speakerに音源を設定する
        for music in range(self.musicFiles.shape[0]):
            for index in range(self.musicFiles.shape[1]):
                # mixer.channelは配列ではだめなので別口の変数を作る
                musicFile = self.MUSIC_FOLDER + self.musicFiles[music, index] + self.EXTENSION
                print(os.path.isfile(musicFile))
                print(musicFile)
                self.speakers[music, index] = mixer.Channel(ch)
                self.speakers[music, index].play(mixer.Sound(musicFile), -1)
                self.speakers[music, index].pause()
                ch += 1
    
    def playMusic(self):
        # 1ループ流した後、音源を止める
        # 書き方が微妙
        # 動いてない
        currentLaser = ms.switchLaser()
        currentDistance = ms.switchDistance()
        currentSound = self.speakers[currentLaser, currentDistance].get_sound()
        print("実行中...")
        self.speakers[currentLaser, currentDistance].unpause()
        time.sleep(currentSound.get_length())
        self.speakers[currentLaser, currentDistance].pause()

mp = MusicPlayer()
while (True):
    mp.playMusic()