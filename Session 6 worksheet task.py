
#Task 1
'''number=int(input("Enter a number or type 0 to end program: "))
while number != 0:
    if number == 0:
        continue
    binary_number = bin(number).replace('0b','')
    print(binary_number)
    number=int(input("Enter a number or type 0 to end program: "))'''
    
#Task 2
'''bin_number=input("Enter a binary number or type 0 to end program:")
while bin_number!="0":
    if bin_number=="0":
        continue
    decimal_number=int(bin_number,2)
    print(decimal_number)
    bin_number = input("Enter a binary number or type 0 to end program:")'''

#Task 3
max_attempts = 4
password=input("Enter your password:")
complex_password="P@ssw0rd"
count=0
while password != complex_password:
    if password == complex_password:
        continue
    count+=1
    if count>= max_attempts:
        print("Your account is locked.")
        break
    else:
        password=input("Enter your password:")
