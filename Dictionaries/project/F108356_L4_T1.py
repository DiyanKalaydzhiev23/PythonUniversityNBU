from sys import argv

my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'd', 6: 'e', 7: 'a', 8: 'b'}

searched_value = argv[1]
found_keys = [k for k, v in my_dict.items() if v == searched_value]

print(found_keys)


# print([k for k, v in {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'd', 6: 'e', 7: 'a', 8: 'b'}.items() if v == argv[1]])