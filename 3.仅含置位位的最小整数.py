'''
给你一个正整数 n。
返回 大于等于 n 且二进制表示仅包含 置位 位的 最小 整数 x 。
置位 位指的是二进制表示中值为 1 的位。
 
示例 1：
输入： n = 5
输出： 7
解释：
7 的二进制表示是 "111"。
示例 2：
输入： n = 10
输出： 15
解释：
15 的二进制表示是 "1111"。
示例 3：
输入： n = 3
输出： 3
解释：
3 的二进制表示是 "11"。
'''

class Solution:
    def smallestNumber(self, n: int) -> int:
        #将n转换为二进制字符串，并计算其中1的个数
        count_ones = bin(n)[2:]
        #计算len的长度
        length = len(count_ones)
        #返回2的length次方减1
        return (1 << length) - 1

if __name__ == "__main__":
    solution = Solution()
    n1 = 5
    n2 = 10
    n3 = 3
    print(solution.smallestNumber(n1))  # 输出: 7
    print(solution.smallestNumber(n2))  # 输出: 15
    print(solution.smallestNumber(n3))  # 输出: 3