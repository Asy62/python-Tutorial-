# Ques 1: Write a program to input a user's name and print:
# name = input("Enter your name :- ")
# print(f"Hello, {name}! Welcome to Python")





# Ques 2: Take two numbers as input and print their sum, difference, product, and quotient.

# num1 = int(input("Enter 1st Number :- "))
# num2 = int(input("Enter 2nd Number :-"))

# sum = num1 + num2 
# print(f"Sum of two number is {sum}")

# diff = num1 - num2
# print(f"Difference of two number is {diff}")

# procuct = num1 * num2
# print(f"The product of two number is {procuct}")

# quo = num1/num2
# print(f"The quotient of two number is {quo}")






# Ques 3: Check whether a given number is even or odd.
# num1 = int(input("Enter the 1st number :- "))


# if num1%2 ==0:
#     print("Even Number ")

# else: 
#     print("Odd Number ")





# Ques 4: Find the largest of three numbers entered by the user.
# num1 = int(input("Enter the 1st number :- "))
# num2 = int(input("Enter the 2nd number :- "))
# num3 = int(input("Enter the 3rd number :- "))

# if num1 > num2 and num1 >num3:
#     print(f"{num1} is the largest number . ")

# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is the largest number.")

# else:
#     print(f"{num3} is the largest number.")



# Ques 5: print numbers from 1 to 20 using a loop.

# for i in range(1,21):
#     print(f"The number is {i}")



# Ques 6: Calculate the factorial of a number using a loop.

# num = int(input("Enter the number of which you want factorial :- "))

# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial*i

# print(f"factorial of {num} is {factorial}")





# Ques 7: Count the number of vowels in a given string.

# strr = input("Enter a string:- ")
# count = 0
# vowels = "aeiouAEIOU"

# for char in strr:
#     if char in vowels:
#         count = count + 1 
# print(f"the total number of vowel in string is {count}")




# Ques 8: Create a list of 5 numbers and print the largest and smallest number.

# l = [4, 5, 6, 7, 8 , 1, 5 ,3,9 ,100]
# largest = l [0]
# smallest = l [0]
# for i in l : 
#     if i > largest : 
#         largest = i
#     elif i < smallest:
#         smallest = i 
# print(f"Your largest number is {largest} and smallest is {smallest}")





# Ques 9: Store student details(name, age, course) in a dictionary and  display them.

# student = {
#     "name" : "Ajay Shankar",
#     "age": 21,
#     "course": "B.Tech"
# }
# print(student)


# Ques 10 : Write a function that returns the square of a number.
a =int(input("Enter the number :- "))
def square (a):
    return  a * a

result = square(a)
print(result)