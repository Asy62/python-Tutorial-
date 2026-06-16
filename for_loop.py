# for i in range(3,31, 3):
#     print(i)



# Take input from the user and print the table of that number.



# n = int(input("Tell me the Number: "))
# for i in range(n):
#     print("hello Wrold")



# print natural numbers form 1 to n.

# n = int(input("Enter the number : "))
# for i in range(1,n+1):
#     print(i)


# Reverse for loop - print n down to 1.

# n = int(input("Plsease enter your number : "))
# for i in range(n,0,-1):
#     print(i)

# # Print the multiplication table of a number 
# n = int(input("which table you want to print : "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i} ")



# print the sum of first n natural numbers.
# a = 0
# n = int(input("Enter the number : "))
# for i in range (1,n+1):
#     a = a + i
#     print (a)


# # Find the factorial of a number.
# n = int(input("tell your number :- "))
# f = 1
# for i in range(1, n+1):
#     f = f * i
#     print(f)


# print sum of all even and odd numbers in a range separately.
# n = int(input("please tell your number: "))
# oddsum = 0
# evensum = 0

# for i in range(1, n+1):
#     if i % 2 == 0: 
#         evensum = evensum + i
#     else : 
#         oddsum = oddsum + i 
# print(f"your even sum is {evensum} and odd sum is {oddsum}")




# print all factor of a number.
# n = int(input("Enter the number of which you want to print the factor : "))
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)


# check if a number is perfect (sum of factors = the number itself)
# n = int(input("please tell me your number : "))

# s = 0
# for i in range (1, n):
#     if n % i == 0:
#         s = s + i 

# if s == n : 
#         print("perfect number")
# else:
#         print("not a perfect number ")


# Take the input form the user and print whether the number is prime or composite number.
# n = int(input("please tell your number : "))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count = count + 1
    
# if count ==2:
#      print("prime Number")
# else:
#     print("composite number")




# Reverse a string without using built-in function.
# Method -- 1
# a = "Ajay Shankar"
# print(a[: : -1])


# Method -- 2
# a = "Ajay Shankar"
# rev = ""
# for i in range(len(a)-1,-1,-1):
#     rev = rev + a [i]
# print(rev)


# Check if a string is a palindrome.
# a = input("Enter String : ")
# rev = ""
# for i in range(len(a)-1,-1,-1):
#     rev = rev + a[i]

# if rev == a:
#     print("yes palindrome")
# else:
#     print("no not a palindrome")



# Count letters, digits, and special symbols in a string.
# Method - 1
# a ="P@#yn26at^&i5ve"
# char = 0
# spchar = 0
# digits = 0
# for i in a:
#     if i.isdigit():
#         digits = digits + 1
#     elif i.isalpha():
#         char = char +1
#     else : 
#         spchar = spchar + 1
# print(f"characters {char}, special characters - {spchar}, digits - {digits}")



# Method -2
a ="P@#yn26at^&i5ve"
char = 0
spchar =0
digits = 0
for i in a :
    if(ord(i) >= 65 and ord(i) <=90) or (ord (i)>= 97 and ord(i) <= 122):
        char  = char +1
    elif ord(i)>=48 and ord(i) <=90:
        digits = digits +1
    else:
        spchar = spchar + 1
print(f"characters {char}, special characters - {spchar}, digits - {digits}")