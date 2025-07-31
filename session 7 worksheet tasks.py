
#Task 1
'''number=int(input("Input a number:"))
for i in range(1,11):
    print(number,'x',i,'=',number*i)'''

#Task 2
'''numbers=(1,2,3,4,5,6,7,8,9,10)
count_odd=0
count_even=0
for i in numbers:
    if not i % 2:
        count_even += 1
    else:
        count_odd = count_odd +1
print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)'''

#Task 3
import random

my_numbers = random.sample(range(1,35),6) #enter code
print("Your numbers are:",my_numbers)
my_powerball = random.sample(range(1,20),1)#enter code
print("Your powerball number is:",my_powerball)

lottery_numbers = random.sample(range(1,35),6)
lottery_numbers.sort()
print("The winning numbers are:",lottery_numbers)
powerball_num = random.choice(range(1,20))
print("The Powerball number is:",powerball_num)

winning = 0
for numbers in my_numbers:
    if numbers in lottery_numbers:
        winning += 1
print("\nPowerball Results.\nTotal winning numbers:",winning)
if my_powerball == powerball_num: print("and P'ball")
