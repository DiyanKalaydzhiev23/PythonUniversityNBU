numbers = [1, 2, 3, 3, 4, 5]
new_nums = []

for num in numbers:
    if num not in new_nums:
        new_nums.append(num)

print(new_nums)
