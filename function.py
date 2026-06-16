

def palindrome_checker(a):
    copy = a
    rev = 0

    while a > 0:
        rev = rev * 10 + a%10
        a = a//10

    if copy == rev:
        print(f"{copy} is a Palindrome  Number")
    else : 
        print(f"{copy} is Not a palindrome")

palindrome_checker(121)
palindrome_checker(232222114543)
palindrome_checker(2345)
palindrome_checker(34534)