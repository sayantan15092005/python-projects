#text base database
import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
spchs = "&@#$*"

def genUid():
    uid = ""
    for i in range(4):
        char = letters[random.randint(0, len(letters) - 1)]
        uid += char

    for i in range(4):
        char = numbers[random.randint(0, len(numbers) - 1)]
        uid += char


    for i in range(2):
        char = spchs[random.randint(0, len(spchs) - 1)]
        uid += char

    return ''.join(random.sample(uid, len(uid)))




def create_database(filename):
    with open(filename, 'w') as file:
        file.write("Id,Name,Email\n")
        print("Database created successfully.")

def add_user(filename,name,email):
    with open (filename ,'a') as file:
        file.write(f"{genUid()},{name},{email}\n")
        print("User added successfully.")
def read_database(filename):    
    with open(filename, 'r') as file:
        content=file.readlines()
        for line in content:
            print(line)

def search_user(filename,user_id):
    with open(filename, 'r') as file:
        content=file.readlines()
        for line in content:
            user=line.strip().split(",")
            if user[0] == str(user_id):
                print(f"user found ID : {user[0]},name : {user[1]},email : {user[2]}")

#



def update_user(filename,user_id,new_name,new_email):
    updated=False
    with open(filename, 'r') as file:
        lines=file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            user=line.strip().split(",")
            if user[0] == str(user_id):
                file.write(f"{user_id},{new_name},{new_email}\n")
                updated=True
            else:
                file.write(line)
    print("User updated successfully." if updated else "User not found.")


def delete_user(filename,user_id):
    deleted=False
    with open(filename, 'r') as file:
        lines=file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            user=line.strip().split(",")
            if user[0] != str(user_id):
                file.write(line)
            else:
                deleted=True
    print("User deleted successfully." if deleted else "User not found.")
