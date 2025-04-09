# file = open("./BCT_DAY3/db.txt","a")
# # contains = file.read()
# # contains = file.readlines()
# file.write("Hello World\n")
# file.write("Hello India\n")
# # for i in range(0, len(contains)):  
# #    print(contains[i])
# file.close()    
with open("./BCT_DAY3/db.txt", "r") as file:
   content=file.read()
   print(content)