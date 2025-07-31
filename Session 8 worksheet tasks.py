
#Task 1
'''numbers = [1,2,3,4,1,5,5,6,7,3,4]
duplicate = set()
unique = []
for num in numbers:
    if num not in duplicate:
        unique.append(duplicate)
        duplicate.add(num)
print(duplicate)'''

#Task 2
set_numbers = {1,2,3,4,5}
set_chars = set("abcdefg")
for i in set_numbers:
    print(i, end="")
print(" --> All numbers.\n")
for i in set_chars:
    print(i, end="")
print(" --> All single characters.")