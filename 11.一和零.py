'''
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
'''
from typing import List

'''
个人思路：
动态规划，二维01背包问题
dp[i][j]表示在有i个0和j个1的情况下，能组成的最大子集长度
遍历每个字符串，计算其中0和1的数量
然后从后往前更新dp数组
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 初始化DP数组：(m+1)行（0~m个0），(n+1)列（0~n个1），初始值0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 遍历每个字符串（每个“物品”）
        for s in strs:
            # 统计当前字符串的0和1的个数
            count0 = s.count('0')
            count1 = len(s) - count0

            # 倒序遍历0的数量（从m到count0）
            for i in range(m, count0 - 1, -1):
                # 倒序遍历1的数量（从n到count1）
                for j in range(n, count1 - 1, -1):
                    # 状态转移：选或不选当前字符串，取最大值
                    dp[i][j] = max(dp[i][j], dp[i - count0][j - count1] + 1)

        return dp[m][n]

# 测试用例
if __name__ == "__main__":
    solution = Solution()
    strs1 = ["10", "0001", "111001", "1", "0"]
    m1, n1 = 5, 3
    print(solution.findMaxForm(strs1, m1, n1))  # 输出: 4

    strs2 = ["10", "0", "1"]
    m2, n2 = 1, 1
    print(solution.findMaxForm(strs2, m2, n2))  # 输出: 2