import sys

nums = [int(x) for x in sys.argv[1:]]
occurrences = {}

for num in nums:
    is_present = occurrences.get(num)

    if is_present:
        print("Is not with unique only")
        break
else:
    print("Is with unique only")


