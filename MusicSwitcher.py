import DistanceDetector as DD
import LaserDetector as LD

DISTANCES_THRES = [[0,5], [5,10], [10,20]]
#レーザーのしきい値
LASER_THRES = 1.5
def switchDistance(ch):
    musicIndex = -1
    currentDistance = DD.getDistance()
    if DISTANCES_THRES[ch][0] <= currentDistance <= DISTANCES_THRES[ch][1]:
        musicIndex = ch
    return musicIndex

#何も入力がない時-1にする
def switchLaser(ch):
    musicIndex = -1
    if LD.getLaser(ch) <= LASER_THRES:
        musicIndex = ch
    return musicIndex

