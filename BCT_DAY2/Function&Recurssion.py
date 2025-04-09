# #normal_function
# #lamda_function
# # def add(num1, num2,name):
# #    return f"{name} of {num1} +{num2}={int(num1)+int(num2)}"
# # print(add(name="addition",num1=10,num2= 20))

# #switch_case using function and if-else...
# # def switch_case(case):
# #     if case == 1:
# #         return f"Addition of:{num1} + {num2} = {num1 + num2}"
# #     elif case == 2:
# #         return f"Subtraction from :{num1} - {num2} = {num1 - num2}"
# #     elif case == 3:
# #         return f"Multiplication of :{num1} * {num2} = {num1 * num2}"
# #     elif case == 4:
# #         return f"Division from :{num1} / {num2} = { num1 / num2}"
# #     else:
# #         return "default case"
# # print("welcome to Simple Calculator................")
# # num1 = int(input("Enter first number:"))
# # num2 = int(input("Enter second number:"))    
# # case = int(input("Enter a case number (1-4):"))
# # print(switch_case(case))

# # def add(*args):
# #    return  sum(args)
# # print(add(1,2,3,4,5,6,7,8,9,10))
# # def info (**kwargs):
# #     # for key, value in kwargs.items():
# #     print(kwargs)
# # print(info(name="JIS", age=20, city="kolkata", country="India"))
# # print(type(info))

# #Lambda function
# # add=lambda num1,num2:num1+num2
# # print(add(10,20))
# # Using function and lembgda functuion make sequre and qube of a number
# # num=int(input("Enter a number:"))
# # power_factor=int(input("Enter a power factor:"))
# # # def power(num,power_factor):
# # #     return num**power_factor
# # # print(power(num,power_factor))
# # power1=lambda num,opwer_factor:num**power_factor
# # print("Power of ",num ,"is",power1(num,power_factor))

# # #LIST
# # my_list=[1,"Sayantan",True]
# # val=int(input("Enter a value:"))
# # my_list.append(val)
# # print(my_list)
# my_dict={"name":"Sayantan","age":20,"city":"kolkata",}
# my_dict["age"]=23
# my_dict["country"]="India"
# print(my_dict["age"])
# print(my_dict["country"])
# for key ,value in my_dict.items():
#     print(f"{key}:{value}")
   