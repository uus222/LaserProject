import DistanceDetector as dd
import LaserDetector as ld

#距離センサのしきい値
DISTANCES_THRES = [0, 1, 5]
#レーザーの数
LASER_NUM = 2
#レーザーのしきい値
LASER_THRES = 2.8
def switchDistance():
    musicIndex = 2
    currentDistance = dd.getDistance()
    #enumerateでインデックスがとれる
    for index, dsVal in enumerate(DISTANCES_THRES): #処理落ちしそう？
        if currentDistance >= dsVal: #ここバグりそう？
            #ここでreturnすると配列の後ろを評価してくれないので、しない
            musicIndex = index
    return musicIndex

#問題：for文で順次見ると同時にレーザー押さえても２つの音が鳴らない
# →Laserクラスを作りレーザーの数だけインスタンス生成し、なんとかする？
#現状解決方法を思いつかないのでクソコードで実装する
#何も入力がない時０にする？
def switchLaser():
    musicIndex = 2
    if ld.getLaser(0) >= LASER_THRES:
        musicIndex = 1
    if ld.getLaser(1) >= LASER_THRES:
        musicIndex = 2
    return musicIndex