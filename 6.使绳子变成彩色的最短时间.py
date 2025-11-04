'''
Alice 把 n 个气球排列在一根绳子上。给你一个下标从 0 开始的字符串 colors ，其中 colors[i] 是第 i 个气球的颜色。

Alice 想要把绳子装扮成 五颜六色的 ，且她不希望两个连续的气球涂着相同的颜色，所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成 彩色 。给你一个 下标从 0 开始 的整数数组 neededTime ，其中 neededTime[i] 是 Bob 从绳子上移除第 i 个气球需要的时间（以秒为单位）。

返回 Bob 使绳子变成 彩色 需要的 最少时间 。
'''
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)  #长度
        total_time = sum(neededTime)  #所有时间
        max_1 = 0  #当前最大时间之和 （无论结尾字符是什么）
        max_2 = 0  # 当前第二大的时间之和 （考虑结尾字符相同的情况）
        color_1 = -1  #当前最大时间对应的颜色
        global_max = 0 #全局最大时间之和
        f = [0]*26  #每个颜色为结尾对应的最大时间之和
        for i in range(n):
            c = colors[i]#当前颜色
            idx = ord(c) - ord('a')#当前颜色对应的索引
            t = neededTime[i]#当前时间

            if idx == color_1:#如果当前颜色和最大颜色相同 , 将第二大的时间放进去
                max_f = max_2
            else:
                max_f= max_1

            #计算当前的气球的最大时间之和
            curr_time = max_f + t

            #更新全局最大时间之和
            if curr_time > global_max:
                global_max = curr_time

            #更新f数组
            old_f= f[idx]
            f[idx] = max(old_f, curr_time)

            #更新最大和第二大
            if idx == color_1:
                if f[idx] > max_1:
                    max_1 = f[idx]
            else:
                if f[idx] > max_1:
                    max_2 = max_1
                    max_1 = f[idx]
                    color_1 = idx
                elif f[idx] > max_2:
                    max_2 = f[idx]
        return total_time - global_max


if __name__ == "__main__":
    s = Solution()
    colors = "bbbaaa"
    neededTime = [4,9,3,8,8,9]
    print(s.minCost(colors, neededTime))

