#Task 1
'''tuple1 = (1,2,3,3,4,2)
print(tuple1)
tuple2 = (3,)
tuple3 = tuple1 + tuple2
print(tuple3)
tuple3 = tuple3[:4] + (3,) + tuple3[4:]
print(tuple3)
my_list = list(tuple3)
my_list.append(3)
tuple3 = tuple(my_list)
print(tuple3)'''

#Task 2 
'''dict_students = {"Joe": 17, "Jack": 18, "Jim": 20}
new_student = "Jane"
if new_student in dict_students.keys():
    print("Key is present.")
else:
    print("Key is not present.")
    dict_students["Jane"] = 17
print(dict_students)'''

#Task 3
ascii_dict = {'a':'97',
              'A':'65',
              'b':'68',
              'B':'66',
              'z':'122',
              'K':'75',
              'C':'67'}
for i in sorted(ascii_dict):
    print("Letter:%s ASCII Code:%s" % (i, ascii_dict[i]))