#Password Generator
#special characters
#uppercase letter
#lowercase letter
#length limit
#numbers
import random

def main():
    print("Hello!Welcome to The Password Generator!")
    print("Please answer Y or N to the below questions to create the best possible password!")
    no_of_choices=0
    chars=""
    upper=input("Does the password need uppercase letters?Y/N: ")
    if upper=="Y":
        no_of_choices+=1
        
        chars+="QWERTYUIOPLKJHGFDSAZXCVBNM"
    special=input("Does the password need special characters?Y/N: ")
    if special=="Y":
        no_of_choices+=1
        chars+="!@#$%^&*"
    nums=input("Does the password need numbers?Y/N: ")
    if nums=="Y":
        no_of_choices+=1
        chars+="1234567890"
    first=input("Can the password start with a special character or a number?Y/N: ")
    min_length=int(input("Enter the minimum number of characters needed: "))
    max_length=int(input("Enter the maximum number of characters needed: "))
    password_length=random.randint(min_length,max_length)
    chars+="qwertyuiopasdfghjklzxcvbnm"
    ans="Y"
    while ans=="Y":
        pwd=""
        i=0
        while i<password_length:
            if first=="N":
                pwd+=random.choice("qazxswedcvfrtgbnhyuijompklQAZXSWEDCVFRTGBNHYUJMKIOLP")
                first="Y"
            else:
                pwd+=random.choice(chars)
            i+=1
        print(pwd)
        print("Would you like to regenerate the password?Y/N: ")
        ans=input()
    print("Your password is: ", pwd)
        
        
main()
