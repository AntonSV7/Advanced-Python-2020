nums = [int(x) for x in input().split()]
n = 1
while n < len(nums):
   for i in range(len(nums) - n):
       if nums[i] > nums[i + 1]:
           nums[i], nums[i + 1] = nums[i + 1], nums[i]
   n += 1
for i in range(len(nums) - 2):
    if nums[i] == nums[i+1]:
        nums.pop(i)
for i in range(len(nums)):
    nums[i] = (nums[i])**2

print(*nums)


