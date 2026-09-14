nums = [1,2,3,4,5,6]

result = []

for i in range(len(nums)):
    if i % 2 == 0:
        result.append(nums[i] * 2)
    else:
        result.append(nums[i] * 3) 

result = result[::-1]
print(result)
