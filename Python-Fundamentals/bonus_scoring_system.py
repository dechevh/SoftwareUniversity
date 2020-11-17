import math

students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())

highest_bonus = 0
best_student_attendances = 0

for x in range(students_count):
    attendances_of_each_student = int(input())
    total_bonus = attendances_of_each_student / lectures_count * (5 + initial_bonus)

    if total_bonus > highest_bonus and attendances_of_each_student > best_student_attendances:
        highest_bonus = total_bonus
        best_student_attendances = attendances_of_each_student
    else:
        pass

print(f"Max Bonus: {math.ceil(highest_bonus)}.")
print(f"The student has attended {best_student_attendances} lectures.")
