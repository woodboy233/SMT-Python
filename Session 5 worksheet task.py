
#Task 1 
'''age=int(input("Enter your age: "))
if age>18:
    print("Eligible for voting, you are:", age)
    print("Enrol to vote, and to keep your details current.")
else:
    #print("Sorry chum. Better luck next time. >:)")
    print("Not eligible for voting.")'''
    
#Task 2
password=input("Enter your password:")
if len(password)< 9 or len(password)>= 15:
    print("Invalid password. Wrong length.")
elif password.isalpha()==False:
    print("Not all characters in string are alphabetic letters [A-Z].")
elif password.isupper()==False:
    print("Not all characters in string are uppercase [A-Z].")
else:
    print("Valid password.")
    
