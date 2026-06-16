a = ["Monday", "Tuesday", 123, 456, 123, 123, 123, 123,4567]

tup= tuple(a)
print(type(a))
print(type(tup))
print(tup[0])
print(tup[-1])
print(tup.index("Tuesday"))
print(tup.count(123))
# Tuble :- It has immutable nature - you cannot change any value inside your tuple.



def students():
    return "Ajay", 21, "codeforasy@gmail.com"

info = students()
name, age, mail = info
# print(info)
# print(type(info))

print(name, age, mail)