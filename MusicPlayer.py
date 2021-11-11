import time
import numpy as np
from pygame import mixer
import MusicSwitcher as ms


class MusicPlayerd:
    # フォルダ名と拡張子(後でくっつける)
    MUSIC_FOLDER = "music/"
    EXTENSION = ".wav"
    # 実際の音源ファイル名
    MUSIC_FILES = [["mute", "mute", "mute"],
                   ["off_ass", "off_bell", "off_connect"],
                   ["off_intro", "off_loop", "off_melo2"]]
    musicFiles = np.array(MUSIC_FILES)  # numpyで使えるようにする

    speakers = np.empty((3, 3), object)

    def __init__(self):
        ch = 0
        mixer.init(frequency=44100)
        # 音源の数だけspeakerを作る
        mixer.set_num_channels(self.musicFiles.size)
        # 各speakerに音源を設定する
        for music in range(self.musicFiles.shape[0]):
            for index in range(self.musicFiles.shape[1]):
                # mixer.channelは配列ではだめなので別口の変数を作る
                musicFile = self.MUSIC_FOLDER + self.musicFiles[music, index] + self.EXTENSION
                #print(musicFile)
                self.speakers[music, index] = mixer.Channel(ch)
                self.speakers[music, index].play(mixer.Sound(musicFile), -1)
                self.speakers[music, index].pause()
                ch += 1
    
    def playMusic(self):
        # 1ループ流した後、音源を止める
        # 書き方が微妙
        # 動いてない
        currentLaser = ms.switchLaser()
        currentDist_fileance = ms.switchDistance()
        currentSound = self.speakers[currentLaser, currentDist_fileance].get_sound()
        self.speakers[currentLaser, currentDist_fileance].unpause()
        time.sleep(currentSound.get_length())
        self.speakers[currentLaser, currentDist_fileance].pause()
