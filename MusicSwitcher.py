import DistanceDetector as DD
import LaserDetector as LD

DISTANCES_THRES = [0, 1, 5, 10, 15, 20]
#レーザーの数
LASER_NUM = 2
#レーザーのしきい値
LASER_THRES = 2.0
def switchDistance():
    musicIndex = 0
    currentDistance = DD.getDistance()
    #enumerateでインデックスがとれる
    for index, dsVal in enumerate(DISTANCES_THRES): #処理落ちしそう？
        if currentDistance >= dsVal: #ここバグりそう？
            #ここでreturnすると配列の後ろを評価してくれないので、しない
            musicIndex = index
    return musicIndex

#問題：for文で順次見ると同時にレーザー押さえても２つの音が鳴らない
# →Laserクラスを作りレーザーの数だけインスタンス生成し、なんとかする？
#現状解決方法を思いつかないのでクソコードで実装する
#MusicPlayer de arg watasu
#何も入力がない時０にする
def switchLaser(ch):
    musicIndex = 0
    if LD.getLaser(ch) <= LASER_THRES:
        musicIndex = ch+1
    return musicIndex

