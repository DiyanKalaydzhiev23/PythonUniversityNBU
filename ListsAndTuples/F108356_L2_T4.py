import sys

numbers = [int(x) for x in sys.argv[1:]]
new_nums = []

for num in numbers:
    if num not in new_nums:
        new_nums.append(num)

print(new_nums)
