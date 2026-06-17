# Ques 1: Check whether a number is prime or not.

# num = int(input("Enter a number :- "))

# if num <= 1:
#     print("Not Prime")

# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime Number")

# Ques 2: Generate the Fibonacci series upto N terms.

# num = int(input("Enter the number : "))

# a = 0
# b = 1
# c = 0
# for i in range(num):
#     print(a, end = " ")
#     c = a + b
#     a = b
#     b = c


# Ques 3: Reverse a string without using built-in reverse function.
# str = input("Enter the string :- ")
# rev = ""

# for i in range(len(str)-1, -1, -1):
#     rev = rev + str[i]
    
# print(rev)


# Ques 4: Remove duplicate elements from a list.

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 70, 80, 50, 40]
# unique_list = []

# for num in numbers:
#     if num not in unique_list:
#         unique_list.append(num)

# print("Original List: ", numbers)
# print("List after removing duplicates:", unique_list)

# Ques 5: Count the frequency of each character in a string.

# string = input("Enter a string: ")

# for char in string:
#     count = 0

#     for ch in string:
#         if char == ch:
#             count = count + 1
    
#     print(char,":", count)


# Ques 6: Create a function that accepts a list and returns the second largest element.

# Method 1: Without Using Built-in functions like sort()

# def second_largest(lst):
#     largest = second = float('-inf')

#     for num in lst:
#         if num >largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num

#     return second


# numbers = [10, 25, 8, 45, 32]

# print("Second Largest Element : ", second_largest(numbers))



# Method 2: Using sort()

# def second_largest(lst):
#     lst.sort()
#     return lst[-2]

# numbers = [10, 25, 8, 45, 32]
# print("Second Largest Element:", second_largest(numbers))


# Method 3: Interview-Friendly Version

# def second_largest(lst):
#     unique = []

#     for num in lst:
#         if num not in unique:
#             unique.append(num)

#     unique.sort()
#     return unique[-2]


# numbers = [10, 20, 30, 20, 30, 40, 30]
# print(second_largest(numbers))


# Ques 7: Read a text file and count the total number of words.

# def count_words(filename):
#     file = open(filename,"r")

#     content = file.read()
#     words = content.split()

#     file.close()
#     return len(words)

# print("Total Words:", count_words("sample.txt"))

# Ques 8: Create a dictionary from two lists:
# List 1 = Keys
# List 2 = Values


# def create_dictionary(keys, values):
#     result = {}

#     for i in range(len(keys)):
#         result[keys[i]] = values[i]

#     return result

# keys = ["Name", "Branch", "Age"]
# values = ["Ajay", "CSE(AI & ML)", 21]

# print(create_dictionary(keys, values))


# Ques 9: Create a class student with attributes:
# . Name
# . roll_no
# . marks
# Display the student details using a method.


# class Student:

#     def __init__(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks

#     def display_details(self):
#         print("\nStudent Details")
#         print("Name :", self.name)
#         print("Roll No. :", self.roll_no)
#         print("Marks :", self.marks)


# name = input("Enter Name: ")
# roll_no = int(input("Enter Roll Number: "))
# marks = float(input("Enter Marks: "))

# student = Student(name, roll_no, marks)
# student.display_details()


# ques 10: Create a menu-driven calculator using functions.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not possible!"
    return a / b


while True:
    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Calculator Closed.")
        break

    if choice >= 1 and choice <= 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", add(num1, num2))

        elif choice == 2:
            print("Result =", subtract(num1, num2))

        elif choice == 3:
            print("Result =", multiply(num1, num2))

        elif choice == 4:
            print("Result =", divide(num1, num2))

    else:
        print("Invalid Choice! Please enter a number between 1 and 5.")