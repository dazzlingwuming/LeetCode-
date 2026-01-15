'''
2943. 最大化网格图中正方形空洞的面积

提示
给你两个整数 n 和 m，以及两个整数数组 hBars 和 vBars。网格由 n + 2 条水平线和 m + 2 条竖直线组成，形成 1x1 的单元格。网格中的线条从 1 开始编号。

你可以从 hBars 中 删除 一些水平线条，并从 vBars 中删除一些竖直线条。注意，其他线条是固定的，无法删除。

返回一个整数表示移除一些线条（可以不移除任何线条）后，网格中 正方形空洞的最大面积 。

'''
from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        '''
        思路：
        要找到正方形空洞的最大面积，我们需要找到不可删的水平线条和竖直线条之间的最大间距。具体步骤如下：
        1. 获取不可删去的水平线条和竖直线条的坐标。
        2. 计算这些线条之间的间距，找到最大的间距。
        3. 最大正方形空洞的面积就是最大间距的平方。

        '''

        # # 获取不可删去的水平线条和竖直线条
        # hBars_set = set(hBars)
        # vBars_set = set(vBars)
        # h_set= set(range(1, n + 3)) - hBars_set
        # v_set= set(range(1, m + 3)) - vBars_set
        # h_list = sorted(list(h_set), reverse=True)
        # v_list = sorted(list(v_set), reverse=True)
        # # 计算差值
        # h_diffs = sorted([i - j  for  i , j in zip(h_list[:-1], h_list[1:])])
        # v_diffs = sorted([i - j  for  i , j in zip(v_list[:-1], v_list[1:])])
        # max_area = max(h_diffs[-1],v_diffs[-1]) ** 2
        #
        # print(max_area)

        '''
        直接计算可删去的连续线条之间的最大间距
        '''
        hBars.sort()
        vBars.sort()
        hmax,vmax = 1,1
        hcur , vcur = 1,1
        #遍历
        for i in range(len(hBars)-1):
            if hBars[i+1] == hBars[i] +1:
                hcur += 1
            else:
                hmax = max(hmax,hcur)
                hcur = 1
        for i in range(len(vBars)-1):
            if vBars[i+1] == vBars[i] +1:
                vcur += 1
            else:
                vmax = max(vmax,vcur)
                vcur = 1
        hmax = max(hmax,hcur)
        vmax = max(vmax,vcur)
        side = min(hmax,vmax)+1
        return side**2


if __name__ == '__main__':
    solution = Solution()
    n = 2
    m = 1
    hBars = [2, 3]
    vBars = [2]
    print(solution.maximizeSquareHoleArea(n, m, hBars, vBars))

