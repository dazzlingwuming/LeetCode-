'''
给你一个整数数组 digits，你可以通过按 任意顺序 连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。

由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。如果无法得到答案，请返回一个空字符串。返回的结果不应包含不必要的前导零。
'''
from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        #思路：贪心+排序，先排序，然后计算总和，,如果全是0，返回0，如果总和能被3整除，直接返回排序后的结果。
        #差值只有1或2时，删除一个差值对应的数字，但是如果差值是2，但是没有2的数字，就删除两个1的数字，反之亦然，也就是需要构建两个桶
        digits.sort(reverse=True)
        total = sum(digits)
        if total % 3 == 0:
            if digits[0] == 0:
                return "0"
            return ''.join(map(str, digits))
        mod1 = [d for d in digits if d % 3 == 1]
        mod2 = [d for d in digits if d % 3 == 2]
        remainder = total % 3
        if remainder == 1:
            #删除一个mod1的数字，或者删除两个mod2的数字,对于返回值只需要将两个桶中的数字从digits中删除即可
            if mod1:
                digits.remove(mod1[-1])
            elif len(mod2) >= 2:
                digits.remove(mod2[-1])
                digits.remove(mod2[-2])
            else:
                return ""
        else:
            #删除一个mod2的数字，或者删除两个mod1的数字
            if mod2:
                digits.remove(mod2[-1])
            elif len(mod1) >= 2:
                digits.remove(mod1[-1])
                digits.remove(mod1[-2])
            else:
                return ""
        if digits[0] == 0:
            return "0"
        return ''.join(map(str, digits))

if __name__ == "__main__":
    s = Solution()
    digits = [0,0,0,1]
    print(s.largestMultipleOfThree(digits))