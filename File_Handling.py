
# We use this command to create a txt file.
# open("hello.text","x")  


# from the below command we can create a txt file and from there we can put anything in that file.
# file = open("superman.txt","w")
# data = input("What you want to write in your file :-")
# file.write(data)



# From the below command we can read the created txt file.
# file = open("Question_based_on_list.py","r")
# print(file.read())




# Opening the file with the help of with 
with open("superman.txt","a") as f:
    f.write("\n " + "i want to see if it is working or not ")
