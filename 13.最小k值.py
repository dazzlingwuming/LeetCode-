'''
给你一个二维整数数组 squares ，其中 squares[i] = [xi, yi, li] 表示一个与 x 轴平行的正方形的左下角坐标和正方形的边长。

找到一个最小的 y 坐标，它对应一条水平线，该线需要满足它以上正方形的总面积 等于 该线以下正方形的总面积。

答案如果与实际答案的误差在 10-5 以内，将视为正确答案。

注意：正方形 可能会 重叠。重叠区域应该被 多次计数 。
'''
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        '''
        解决方案：
        现在要找到一个最小的 y 坐标，使得该水平线以上和以下的正方形总面积相等。
        那么及存在一个函数f(k) = 总面积的一半（上半区的面积）单调递增，当k从负无穷增加到正无穷时，f(k)从0增加到总面积。
        总面积应该等于数组里每个正方形的面积之和
        然后对函数进行分析，对于每一个正方形存在三种情况：
        1. 当k小于正方形的底边y坐标时，正方形的面积全部在k上方，对总面积没有贡献
        2. 当k大于正方形的顶边y坐标时，正方形的面积全部在k下方，对总面积有全部贡献
        3. 当k在正方形的底边和顶边之间时，正方形的一部分在k上方，一部分在k下方，对总面积有部分贡献
        综上所述，我们可以通过二分查找来找到这个最小的y坐标k，使得f(k)等于总面积的一半。
        具体步骤如下：
        1. 计算所有正方形的总面积total_area。
        2. 设置二分查找的上下界low和high，初始值分别为所有正方形的最小底边y坐标和最大顶边y坐标。
        3. 在low和high之间进行二分查找，计算中间值mid。

        :param squares:
        :return:
        '''

        sum_area = sum([(l * l) for x, y, l in squares])
        half_area = sum_area / 2
        low = min([y for x, y, l in squares])
        high = max([y + l for x, y, l in squares])
        precision = 1e-5  # 精度要求
        while high - low > precision:
            mid = (low + high) / 2
            area_above = 0
            for x, y, l in squares:
                if mid >= y + l:
                    continue
                elif mid <= y:
                    area_above += l * l
                else:
                    area_above += (y + l - mid) * l
            if area_above <= half_area:
                high = mid
            else:
                low = mid
        return low

# 测试用例
if __name__ == "__main__":
    squares =[[0,0,1],[2,2,1]]
    solution = Solution()
    print(solution.separateSquares(squares))