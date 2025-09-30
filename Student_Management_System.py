import datetime
import Validation

Studentfile = "students.txt"

def add_new_student():
    pass
def login():
    username="admin"
    password="admin"
    for i in range(4):
        user_name=input("Enter the username: ")
        pass_word=input("Enter the password: ")
        if user_name==username and pass_word==password:
            print("Login successful")
            return
        else:
            print("Invalid User name or Password")
    print("Too many failed login attempts. Your account is temporarily locked.")
    return exit()    
def get_studentdata():
    students = []
    try:
        with open(Studentfile, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 6:
                    students.append({
                        "id": data[0],
                        "name": data[1],
                        "roll": data[2],
                        "age": data[3],
                        "dept": data[4],
                        "marks": int(data[5])
                    })
    except FileNotFoundError:
        open(Studentfile, "w").close()
    return students

def add_new_student(students):
    sid = str(len(students) + 1)  
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    age = int(input("Enter age: "))
    dept = input("Enter department: ")
    marks = int(input("Enter marks: "))

    new_student = {"id": sid, "name": name, "roll": roll, "age": str(age), "dept": dept, "marks": marks}
    students.append(new_student)
    append_student(new_student)
    print("Student added successfully!")

def append_student(student):
    with open(Studentfile, "a") as f: 
        f.write(f"{student['id']},{student['name']},{student['roll']},{student['age']},{student['dept']},{student['marks']}\n")

def write_students(students):
    with open(Studentfile, "w") as f:
        for s in students:
            f.write(f"{s['id']},{s['name']},{s['roll']},{s['age']},{s['dept']},{s['marks']}\n")

def view_student_details(students):
    if not students:
        print("No records found.")
        return
    print("Student Records")
    for s in students:
        print(f"ID:{s['id']} | Name:{s['name']} | Roll:{s['roll']} | Age:{s['age']} | Dept:{s['dept']} | Marks:{s['marks']}")
    print()
    
def update_student_details(students):
    roll = input("Enter roll number to update: ")
    for s in students:
        if s["roll"] == roll:
            name = input("Enter new name: ") or s["name"]
            age = input("Enter new age: ") or s["age"]
            dept = input("Enter new department: ") or s["dept"]
            marks = input("Enter new marks: ") or s["marks"]

            s.update({"name": name, "age": age, "dept": dept, "marks": int(marks)})
            write_students(students)
            print("Record updated.")
            return
    print("Student not found.")

def delete_student_record(students):
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            write_students(students)
            print("Record deleted.")
            return
    print("Student not found.")

def search_student(students):
    keyword = input("Search by name/department: ").lower()
    results = [s for s in students if keyword in s["name"].lower() or keyword in s["dept"].lower()]
    if results:
        for s in results:
            print(f"ID:{s['id']} | Name:{s['name']} | Dept:{s['dept']} | Marks:{s['marks']}")
    else:
        print("No match found.")

def view_top_students(students):
    if not students:
        print("No records.")
        return
    sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
    print("Top Performers")
    for s in sorted_students[:3]:
        print(f"{s['name']} (Dept:{s['dept']}) -> Marks: {s['marks']}")
    print()


#-----------------------------------------------------#
login()
students_data=get_studentdata()
while(True):
    print("Student Management System")
    print("1.Add New Student Record ")
    print("2.View Student Record  ")
    print("3.Update Student Details ")
    print("4.Delete Student Record ")
    print("5.Search student by name or department ")
    print("6.View top-performing students ")
    print("7.Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        add_new_student(students_data)  
    elif ch==2:
        view_student_details(students_data)
    elif ch==3:
        update_student_details(students_data)
    elif ch==4:
        delete_student_record(students_data)
    elif ch==5:
        search_student(students_data)
    elif ch==6:
        view_top_students(students_data)
    elif ch==7:
        print("Exiting... Thank you for using the system")
        exit()
    else:
        print("Invalid choice. Try again")

    


