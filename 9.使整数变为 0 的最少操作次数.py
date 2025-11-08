'''
1611. 使整数变为 0 的最少操作次数
困难
相关标签
premium lock icon
相关企业
提示
给你一个整数 n，你需要重复执行多次下述操作将其转换为 0 ：

翻转 n 的二进制表示中最右侧位（第 0 位）。
如果第 (i-1) 位为 1 且从第 (i-2) 位到第 0 位都为 0，则翻转 n 的二进制表示中的第 i 位。
返回将 n 转换为 0 的最小操作次数。



示例 1：

输入：n = 3
输出：2
解释：3 的二进制表示为 "11"
"11" -> "01" ，执行的是第 2 种操作，因为第 0 位为 1 。
"01" -> "00" ，执行的是第 1 种操作。
示例 2：

输入：n = 6
输出：4
解释：6 的二进制表示为 "110".
"110" -> "010" ，执行的是第 2 种操作，因为第 1 位为 1 ，第 0 到 0 位为 0 。
"010" -> "011" ，执行的是第 1 种操作。
"011" -> "001" ，执行的是第 2 种操作，因为第 0 位为 1 。
"001" -> "000" ，执行的是第 1 种操作。

'''

#弄错了题意
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
#         #思路：
#         '''
#         计算二进制的一的个数和位置关系
#         每一个1的位置都会影响后续的操作次数，从左到右的第一个1和第二个1之间的0的个数决定了后续的操作次数，如果没有第二个1，那就直接计算到最后一个0的位置即可
#         '''
#         num = list(map(int , bin(n)[2:]))#得到数组
#         min = 0 #最小操作次数
#         length = len(num)
#         start = None#第一个1的位置
#         end = None#下一个1的位置
#         if num[-1] == 0:
#             #如果最后一位是0，那么将最后一位改为1
#             num[-1] = 1
#             min += 2
#         else:
#             min = 1
#
#         for i in range(length):
#             if num[i] == 1:
#                 if start is None:
#                     start = i
#                 else:
#                     end = i
#                     #计算start和end之间0的个数
#                     zero_count = end - start - 1
#                     min += (zero_count)*2 + 1
#                     start = end
#
#         return min

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while (n > 0):
            res ^= n
            n >>= 1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.minimumOneBitOperations(9))
    print(s.minimumOneBitOperations(6))