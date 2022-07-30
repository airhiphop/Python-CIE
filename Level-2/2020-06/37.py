nums = []
for i in range(10):
    n = int(input())
    nums.append(n)
r = max(nums)
l = min(nums)
nums.remove(r)
nums.remove(l)
print("去掉一个最高分：{}分，去掉一个最低分：{}，最后得分为：{}".format(r, l, sum(nums)//8))