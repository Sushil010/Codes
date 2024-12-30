
# nums=[3,3]
# target=6
# nums=[2,7,11,15]
# target=9

nums=[3,2,4]
target=6


for num in range(len(nums)):
    a = target-nums[num]
    print(f"{target}-{nums[num]}={a}")
    if a in nums:
        print(nums.index(a),num)
        break