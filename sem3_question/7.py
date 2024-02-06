# 	Consider a file name student.txt, write a python program to take the names, roll number, phone number of the students from the user and save it into the file.
def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def main():
    print("Enter student details. Type 'done' to finish.")
    while True:
        name = input("Enter student name: ")
        if name.lower() == 'done':
            break
        roll_number = input("Enter roll number: ")
        phone_number = input("Enter phone number: ")
        student_data = f"Name: {name}, Roll Number: {roll_number}, Phone Number: {phone_number}"
        write_to_file("student.txt", student_data)
        print("Student details saved.")

if __name__ == "__main__":
    main()

    
