'''
给你一个由 n 个整数组成的数组 nums，以及两个整数 k 和 x。

数组的 x-sum 计算按照以下步骤进行：

统计数组中所有元素的出现次数。
仅保留出现次数最多的前 x 个元素的每次出现。如果两个元素的出现次数相同，则数值 较大 的元素被认为出现次数更多。
计算结果数组的和。
注意，如果数组中的不同元素少于 x 个，则其 x-sum 是数组的元素总和。

返回一个长度为 n - k + 1 的整数数组 answer，其中 answer[i] 是 子数组 nums[i..i + k - 1] 的 x-sum。

子数组 是数组内的一个连续 非空 的元素序列。
'''
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        #思路：
        '''
        对于每个长度为k的子数组，统计每个数字的出现频率

        根据频率和数值对元素进行排序（频率高的在前，频率相同时数值大的在前）

        取前x个元素，计算这些元素在子数组中出现的所有次数的和
        '''
        n = len(nums)
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            freq = {}#给子数组中的数字计数
            for num in subarray:
                freq[num] = freq.get(num, 0) + 1
            #根据频率和数值对元素进行排序
            sored_freq = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            #取前x个元素，计算这些元素在子数组中出现的所有次数的和
            x_sum = 0
            for j in range(min(x, len(sored_freq))):
                num, count = sored_freq[j]
                x_sum += num * count
            nums[i] = x_sum
        return nums[:n - k + 1]

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,2,3,4]
    k = 3
    x = 2
    print(s.findXSum(nums, k, x))
