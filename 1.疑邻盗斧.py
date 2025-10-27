'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
'''


def rob(nums):
    if not nums:  # 空数组
        return 0
    n = len(nums)
    if n == 1:  # 只有1间房
        return nums[0]

    # 初始化前两个状态
    prev_prev = nums[0]  # 对应dp[0]
    prev = max(nums[0], nums[1])  # 对应dp[1]

    if n == 2:
        return prev

    # 从第3间房开始计算（索引2）
    for i in range(2, n):
        current = max(prev, prev_prev + nums[i])  # 状态转移
        prev_prev, prev = prev, current  # 更新前两个状态

    return prev

nums = [1,3,6]
print(rob(nums))

'''
当屋子是连起来的，也就是最后一家不能和第一家一起
'''

def rob_circle(nums):
    '''
    这里需要考虑的是两种方法取[0:n-1]和[1:n],然后比较大小
    '''
    n = len(nums)
    return max (rob(nums[0:n-1]), rob(nums[1:n]))

print(rob_circle(nums))


