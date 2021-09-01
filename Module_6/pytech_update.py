import pymongo

from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cluster0.299vf.mongodb.net/pytech"
client = MongoClient(url) 

db = client.pytech 

students = db.students 

student_list = students.find({})

rachel = {
    "student_id": "1007", 
    "first_name": "Rachel", 
    "last_name": "Roberts" 
}

leah = { 
    "student_id": "1008", 
    "first_name": "Leah", 
    "last_name": "Roberts" 
}

anna = { 
    "student_id": "1009", 
    "first_name": "Anna", 
    "last_name": "Roberts" 
}


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")


for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Henry"}})


rachel = students.find_one({"student_id": "1007"})


print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")


print("  Student ID: " + rachel["student_id"] + "\n  First Name: " + rachel["first_name"] + "\n  Last Name: " + rachel["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")