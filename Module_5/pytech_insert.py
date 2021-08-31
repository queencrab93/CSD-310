import pymongo

from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cluster0.299vf.mongodb.net/pytech"
client = MongoClient(url) 

db = client.pytech 

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

students = db.students 

print("\n  -- INSERT STATEMENTS --")
rachel_student_id = students.insert_one(rachel).inserted_id
print("  Inserted student record Rachel Roberts into the students collection with document_id " + str(rachel_student_id))

leah_student_id = students.insert_one(leah).inserted_id
print("  Inserted student record Leah Roberts into the students collection with document_id " + str(leah_student_id))

anna_student_id = students.insert_one(anna).inserted_id
print("  Inserted student record Anna Roberts into the students collection with document_id " + str(anna_student_id)) 

input("\n\n  End of program, press any key to exit... ")