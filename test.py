import copy

def seek_zero(nums):
    zero_list = []
    for i, val in enumerate(nums):
        if val == 0:
            zero_list.extend([(i, -1), (i, 1)])  # (位置, 方向)，-1左，1右
    return zero_list

def simulate_move(start, direction, nums_copy):
    n = len(nums_copy)
    curr = start
    way = direction
    while True:
        # 检查是否超出范围
        if curr < 0 or curr >= n:
            return all(x == 0 for x in nums_copy)
        val = nums_copy[curr]
        if val == 0:
            # 沿当前方向移动
            curr += way
        else:
            # 减1，反转方向，移动一步
            nums_copy[curr] -= 1
            way *= -1
            curr += way

class Solution:
    def countValidSelections(self, nums) -> int:
        count = 0
        zero_list = seek_zero(nums)
        for pos, dir in zero_list:
            # 每次都使用原始数组的深拷贝，避免相互影响
            nums_copy = copy.deepcopy(nums)
            if simulate_move(pos, dir, nums_copy):
                count += 1
        return count

# 测试示例
Solution_num = Solution()
nums = [21,22,21,22,15,26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,7,9,8,6,5,5,10,7,9,4,2,6,5,7,8,7,6]
print(Solution_num.countValidSelections(nums))