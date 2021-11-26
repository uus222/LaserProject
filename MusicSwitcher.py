#import distance as ds
#import photo as pt

#距離センサのしきい値
import MusicPlayer as mp


DISTANCES_THRES = [0, 1, 5, 10, 15, 20]
#レーザーの数
LASER_NUM = 2
#レーザーのしきい値
LASER_THRES = 0.25
def switchDistance():
    musicIndex = 2
    """
    currentDistance = ds.getDistance()
    #enumerateでインデックスがとれる
    for index, dsVal in enumerate(DISTANCES_THRES): #処理落ちしそう？
        if currentDistance >= dsVal: #ここバグりそう？
            #ここでreturnすると配列の後ろを評価してくれないので、しない
            musicIndex = index
    """
    return musicIndex

#問題：for文で順次見ると同時にレーザー押さえても２つの音が鳴らない
# →Laserクラスを作りレーザーの数だけインスタンス生成し、なんとかする？
#現状解決方法を思いつかないのでクソコードで実装する
#何も入力がない時０にする？
def switchLaser():
    musicIndex = 2
    """
    if pt.getPhoto(0) >= LASER_THRES:
        musicIndex = 1
    if pt.getPhoto(1) >= LASER_THRES:
        musicIndex = 2
    """
    return musicIndex

