nums = [1, 2, 2, 3, 4, 5]
occurrences = {}

for num in nums:
    is_present = occurrences.get(num)

    if is_present:
        print("Is not with unique only")
        break
else:
    print("Is with unique only")
