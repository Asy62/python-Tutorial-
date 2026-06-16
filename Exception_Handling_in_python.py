
# Example of ZeroDivisionError
# a =10
# b =0

# print(a/b)


# Example of TypeError
# a = "10"
# b = 5
# print(a+b)



# Example of ValueError
# num = int("hello")



a = int(input("please tell your 1st number:-"))
b = int(input("please tell your 2nd number:-"))


try:
    print(a/b)
except Exception as err:
    print("sorry an error occured as {err}")
else:
    print("no errors occured")
finally:
    print("if there are errors or there are no errors I will run no matter what")
name = input("tell your name :-")

print(f"Hello your name is {name}")