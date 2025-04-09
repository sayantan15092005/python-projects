import database


#curd - create, read, update, delete
import time
db = []
#create
def createEntry(bookname,issueDate,renewDate,assignPerson):
    entry = {
        "bookname": bookname,
        "issueDate": issueDate,
        "renewDate": renewDate,
        "assignPerson": assignPerson,
        "id": id
    }
    db.append(entry)
#delete
    def deleteEntry(id):
        for i, item in enumerate(db):
            if item["id"] == id:
                del db[i]
                break
#read
def displayEntries():
    for i, item in enumerate(db):
        print("id",item["id"])
        print("bookname",item["bookname"])
        print("issueDate",item["issueDate"])
        print("renewDate",item["renewDate"])
        print("assignPerson",item["assignPerson"])
        print("***************")
def search(name):
    for i, item in enumerate(db):
        if item["assignPerson"] == name:
            print("id",item["id"])
            print("bookname",item["bookname"])
            print("issueDate",item["issueDate"])
            print("renewDate",item["renewDate"])
            print("assignPerson",item["assignPerson"])
            print("***************")
#update
def updateEntry(id,issueDate="", renewDate="", assignPerson=""):
    for i, item in enumerate(db):
        if item["id"] == id:
            if issueDate != "":
                item["issueDate"] = issueDate
            if renewDate != "":
                item["renewDate"] = renewDate
            if assignPerson != "":
                item["assignPerson"] = assignPerson
            break

filename = "db.txt"
database.create_database(filename)

#interface
while True:
    ops = input("press Y for entry or pass [e] for exit: ")
    print("press [c] to create entry :")
    print("press [d] to displays all entries :")
    print("press [s] to search entry :")
    print("press [x] to delete entry :")
    print("press [u] to update entry :")
    if ops == "c" or  ops == "C":
        id = int(input("enter id: "))
        bookname = input("enter book name: ")
        issueDate = time.ctime()
        renewDate = input("enter renew date: ")
        assignPerson = input("enter assign person: ")
        createEntry(bookname, issueDate, renewDate, assignPerson)
        
    if ops == "d" or  ops == "D":
        break
    if ops == "s" or  ops == "S":
        break
    if ops == "x" or  ops == "X":
        break
    if ops == "u" or  ops == "U":
        break