'''
将所有元素变为 0 的最少操作次数
给你一个大小为 n 的 非负 整数数组 nums 。你的任务是对该数组执行若干次（可能为 0 次）操作，使得 所有 元素都变为 0。

在一次操作中，你可以选择一个子数组 [i, j]（其中 0 <= i <= j < n），将该子数组中所有 最小的非负整数 的设为 0。

返回使整个数组变为 0 所需的最少操作次数。

一个 子数组 是数组中的一段连续元素。
'''
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        思路：这里可以考虑，如果存在多个相同的最小非负整数，我们可以一次性将它们全部变为0，从而减少操作次数。
        然后如果在某个子数组中，存在比多个相同的最小非负整数更小的数，我们需要先将这个更小的数变为0，然后再处理剩下的数。
        所以就可以将数组进行排序，然后依次处理每个数，记录操作次数。
        栈可以解决这个问题，我们依次填入栈中，如果当前数字大于栈顶元素，说明需要进行一次操作，再将当前数字入栈。
        当前数字小于等于栈顶元素或者等于0时，说明当前数字已经被之前的操作覆盖，不需要额外操作，但是需要将栈顶元素弹出，继续比较。
        '''
        # stack = [nums[0]]
        # if stack[0] == 0:
        #     k = 0
        # else:
        #     k = 1# 操作次数
        # for num in nums[1:]:
        #     if num != 0 :
        #         while stack[-1] > num:
        #             stack.pop()
        #             if not stack:
        #                 stack.append(num)
        #                 k += 1
        #                 break
        #         if stack[-1] < num:
        #             stack.append(num)
        #             k += 1
        # return k
        s = []
        res = 0
        for a in nums:
            while s and s[-1] > a:#关键在这里，需要先判断栈顶元素是否大于当前元素，当是0的时候，那么s就会变成空的，然后对下面的k就会+1
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res

# 测试
if __name__ == "__main__":
    solution = Solution()
    nums = [3,1,2,1]
    print(solution.minOperations(nums))  # 输出: 3