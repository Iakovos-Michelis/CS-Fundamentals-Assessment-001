from student_dict import students

for student_id, student_info in students.items():
    grades = student_info['grades']
    
    average_grade = sum(grades) / len(grades)
    
    if average_grade < 40:
        print(f"Student ID: {student_id}, Name: {student_info['name']}, Average Grade: {average_grade:.2f}")