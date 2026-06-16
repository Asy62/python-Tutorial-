# d = {10:100, 20:200, 30:300,40:400}
# print(type(d))
# print(d)
# print(d[40])


# Ques 1: Merge two dictionaries into one.
# d1 = {"a": 10, "b":20, "c":30}
# d2 = {"d":40, "e":50, "f":60}
# d1.update(d2)

# for i in d2:
#     d1[i] = d2[i]
# print(d1)






# # Ques 2: Sum all values in a dictionary.
# d1 = {"a": 10, "b":20, "c":30}
# sum = 0
# for i in d1:
#     sum = sum + d1[i]
# print(sum)




# Ques 3. Count the frequency of each element in a list using a dictionary.
# d = ["a", "b", "a", "c", "b", "a","c","a","b"]
# count = 0
# for i in d:
#     if i =="a":
#         count = count +1
# print(count)



# # Ques 3. Answer
# l = ["a", "b", "a", "c", "b", "a","c","a","b"]
# d = {}
# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)





# Ques 4: Combine two dicts, adding values for common keys.
d1 = {"a": 10, "b":20, "c":30}
d2 = {"c":40, "e":50, "f":60}


for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]
print(d1)