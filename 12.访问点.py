'''平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi] 。请你计算访问所有这些点需要的 最小时间（以秒为单位）。

你需要按照下面的规则在平面上移动：

每一秒内，你可以：
沿水平方向移动一个单位长度，或者
沿竖直方向移动一个单位长度，或者
跨过对角线移动 sqrt(2) 个单位长度（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
必须按照数组中出现的顺序来访问这些点。
在访问某个点时，可以经过该点后面出现的点，但经过的那些点不算作有效访问。'''
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''
        思路：对于两个点最近的移动时间，就是两个点在x轴和y轴上距离的较大值
        :param points:
        :return:
        '''
        sum = 0
        for point in points[1:]:
            dx = abs(point[0] - points[points.index(point) - 1][0])
            dy = abs(point[1] - points[points.index(point) - 1][1])
            sum += max(dx, dy)
        return sum