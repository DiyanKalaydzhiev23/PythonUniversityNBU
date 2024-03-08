nums = [1, 2, 3, 4, 5]

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        print("Not sorted")
        break
else:
    print("Sorted")
