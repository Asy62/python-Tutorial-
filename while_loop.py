import random


# Seperate each digit of a number and print on a newline.

# a = int(input("please tell your number : - "))
# while a >0:
#     print(a%10)
#     a = a//10


# Accept a number and print its reverse.


# a = int(input("Please tell your number : "))
# rev = 0
# while a >0:
#     rev = rev * 10 + a %10
#     a = a//10
# print(rev)


# Check if a number is palindromic (equal to its reverse)
# a = int(input("please tell your number :- "))
# copy = a
# rev = 0

# while a >0:
#     rev = rev * 10 + a % 10
#     a = a// 10
# if rev == copy :
#     print("palindrome")
# else:
#     print("not a palindrome") 


# Build a number guessing game -computer picks a random number, user keeps guessing until correct.

# random.randint(a:b)  ---> means a is a starting point.
                    #    ---> and b is a ending point.

com = (random.randint(1,100))

tries = 0

while True:
    tries = tries + 1
    hum = int(input("guess your number between 1 - 100 :-"))

    if hum == com:
        print(f"congratulations you have won in {tries} tries!")
        break
    elif hum > com:
        print("sorry wrong guess go lower !")
    elif hum < com:
        print("Sorry wrong guess go higher !")
