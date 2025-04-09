# 1. sum of numbers in a list
# list=[1,2,3,4,5,6]
# sum=0
# for i in list:
#     sum=sum+i
# print("sum of numbers in a list is:",sum)

# 2. count vowels in a string
# vowels="aeiouAEIOU"
# string="Hello everyone!"
# count=0
# for i in string:
#     for j in vowels:
#         if i==j:
#             count+=1
# print("The number of vowels in the string is:",count)

# 3. print multiplication table
# MultiplicationTable=int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{MultiplicationTable} * {i} = {MultiplicationTable*i}")

# 4.Find the max number from a  list

# My_List=[1,2,3,4,5,6,7,8,9]
# max_number=0
# for i in My_List:
#     if i>max_number:
#       max_number=i
# print("The maximum number in this list is:",max_number)

# # 5.Create a factorial calculator
# factorial_input=int(input("Enter a number:"))
# factorial=1
# for i in range(2,factorial_input+1):
#     if factorial_input == 0 or factorial_input == 1:
#         factorial=1
#     else:
#         factorial*=i
#         # factorial_input-=1
# print("The factorial of",factorial_input,"is:",factorial)

# palindrome_checker
# String=input("Enter a string:")
# rev_strring=reversed(String)
# if list(String)==list(rev_strring):
#     print("The string is a palindrome")
# else:  
#     print("The string is not a palindrome")
# rev_string=String[::-1]
# if list(String)==list(rev_string):
#     print("The string is a palindrome")
# else:  
#     print("The string is not a palindrome")
# fizzbuzz
# for i in range(1,50):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)


# reverse a list
# list=[1,2,3,4,5]
# reversed_list=list[::-1]
# print("the reversed list:",reversed_list)

# Find the duplicates in a list
# List=[1,2,3,4567,456,345,2,3,1]
# duplicates=[]
# def print_duplicates(List):
#     for i in List:
#         if List.count(i)>1 and i not in duplicates:
#             duplicates.append(i)
#     print("The duplicate elements in the list are:",duplicates)
# print_duplicates(List)

# word count in a string
# string="Hello everyone! How are you?"
# words=string.split()
# word_count=len(words)
# print("The number of words in the string is:",word_count)

# charecter frequency in a string
string="Hello i am a student if JIS.JIS is a bad college"
charCount = 0
targetChar = 'a'
for i in string:
    if i == targetChar:
        charCount += 1
print("The no of  a in ",charCount)