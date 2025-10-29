'''
给你一个整数数组 nums 。

开始时，选择一个满足 nums[curr] == 0 的起始位置 curr ，并选择一个移动 方向 ：向左或者向右。

此后，你需要重复下面的过程：

如果 curr 超过范围 [0, n - 1] ，过程结束。
如果 nums[curr] == 0 ，沿当前方向继续移动：如果向右移，则 递增 curr ；如果向左移，则 递减 curr 。
如果 nums[curr] > 0:
将 nums[curr] 减 1 。
反转 移动方向（向左变向右，反之亦然）。
沿新方向移动一步。
如果在结束整个过程后，nums 中的所有元素都变为 0 ，则认为选出的初始位置和移动方向 有效 。

返回可能的有效选择方案数目。

'''
import copy


def seek_zero(nums):  # 找到0的点 ——>list
    zero_list = []
    for i, j in enumerate(nums):
        if j == 0:
            zero_list.extend([(i, -1), (i, 1)])  # (i,-1)为向左，(i,1)为向右
    return zero_list


def left_move(current, nums, way):  # 三个参数，一个当前位置，一个数组,移动方向 ->移动后的位置，数组 ，下一次移动方向
    current = current + way
    while True:
        if current<0 or current>=len(nums):
            if all(x == 0 for x in nums):
                return True
            else:
                return False
        if nums[ current] == 0:
            current += way
        else:
            nums[current] -= 1
            way = -way
            current += way




class Solution:
    def countValidSelections(self, nums) -> int:
        x = 0# 计数器
        zero_list = seek_zero(nums)
        for i in zero_list:
            temp = copy.deepcopy(nums)
            current, temp, way = i[0], temp, i[1]
            if left_move(current, temp, way):
                 x += 1
        return  x




Solution_num = Solution()
nums =[21,22,21,22,15,26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,7,9,8,6,5,5,10,7,9,4,2,6,5,7,8,7,6]
x = Solution_num.countValidSelections(nums)
print(x)