# Ques 1. Print all positive and negative elements separately.

# l = [3, -1, 4, -5, 9 ]

# pos =[]
# neg = []

# for i in l:
#     if i >= 0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(f"Your positive elements are {pos}")
# print(f"Your negative elements are {neg}")





# Ques 2. Find the mean (average) of all list elements.

# l = [10, 20, 30, 40]
# sum = 0
# for i in l:
#     sum = sum + i
# avg = sum/len(l)
# print(f"your average is {avg}")




# Ques 3. Find the greatest element and print its index.

# a = [20, 43, 17, 68, 29, 90, 47]
# index = 0
# largest = a[0]
# for i in range(len(a)):
#     if a [i] > largest:
#         largest = a[i]
#         index = i

# print(f"Your largest value is {largest} at index {index}")




# Ques 4. Find the second greatest element.

# a = [4, 7, 2, 9, 1, 8]
# largest = a[0]
# sec_largest = a[0]
# for i in a: 
#     if i > largest:
#         sec_largest = largest
#         largest = i 
#     elif i > sec_largest:
#         sec_largest = i
# print(sec_largest)



# Ques 5. Check if the list is already sorted.

a = [10,20, 30, 40, 45, 50]

for i in range(len(a)-1):
     if a[i]  > a[i+1]:
        print("your list is not sorted")
        break
else:
     print("your list is sorted")


