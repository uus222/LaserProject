import numpy as np
from pygame import mixer

class MusicInitializer:
    # フォルダ名と拡張子(後でくっつける)0
    #MUSIC_FOLDER = "C:\\Users\\tomy0\\Desktop" + "\\music\\"
    MUSIC_FOLDER = "/home/pi/Desktop/piLaserProject/LaserProject/music/"
    EXTENSION = ".wav"
    # 実際の音源ファイル名
    # Musicフォルダ内を探索して自動生成とかできない？
    MUSIC_FILES = [["C", "C#", "D"],
                   ["off_ass", "off_bell", "off_connect"],
                   ["off_intro", "off_loop", "off_melo2"],
                   ["off_ass", "off_bell", "off_connect"]]
    musicFiles = np.array(MUSIC_FILES)  # numpyで使えるようにする
    # 音源の数だけ空配列を作
    speakers = np.empty((len(MUSIC_FILES), len(MUSIC_FILES[0])), object)
    def initMusicPayer(self):
        print("--Music Initializing--")
        ch = 0
        mixer.init(frequency=44100)
        # 音源の数だけspeakerを作る
        mixer.set_num_channels(self.musicFiles.size)
        # 各speakerに音源を設定する
        for music in range(self.musicFiles.shape[0]):
            for index in range(self.musicFiles.shape[1]):
                # mixer.channelは配列ではだめなので別口の変数を作る
                musicFile = self.MUSIC_FOLDER + \
                    self.musicFiles[music, index] + self.EXTENSION
                #print(os.path.isfile(musicFile))
                print(musicFile)
                # read to static speakers
                MusicInitializer.speakers[music, index] = mixer.Channel(ch)
                MusicInitializer.speakers[music, index].play(mixer.Sound(musicFile), -1)
                MusicInitializer.speakers[music, index].pause()
                ch += 1
    
    def getShapes(self):
        return len(self.MUSIC_FILES),len(self.MUSIC_FILES[0])
