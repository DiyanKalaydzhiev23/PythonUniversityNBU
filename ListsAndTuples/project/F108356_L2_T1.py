import sys

nums = [int(x) for x in sys.argv[1:]]

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        print("Not sorted")
        break
else:
    print("Sorted")
