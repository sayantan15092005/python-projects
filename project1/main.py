import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
spchs = "&@#$*"

password = ""


for i in range(4):
    char = letters[random.randint(0, len(letters) - 1)]
    password += char

for i in range(4):
    char = numbers[random.randint(0, len(numbers) - 1)]
    password += char


for i in range(2):
    char = spchs[random.randint(0, len(spchs) - 1)]
    password += char

password = ''.join(random.sample(password, len(password)))

print("Password is: ", password)
UserPassword = input("Enter your password: ")
if len(UserPassword) < 5:
    print("password length should be 10")
for char in UserPassword:
    if char in letters:
        pass
    elif char in spchs:
        pass
    elif char in numbers:
        pass
    else:
        print("Password should be contain number or charecter")


          