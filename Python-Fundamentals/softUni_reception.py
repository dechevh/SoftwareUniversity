efficiency_one = int(input())
efficiency_two = int(input())
efficiency_three = int(input())
students_count = int(input())

all_employees_per_hour = efficiency_one + efficiency_two + efficiency_three

time_needed = 0

while students_count > 0:
    time_needed += 1
    if time_needed % 4 == 0:
        pass
    else:
        students_count -= all_employees_per_hour

print(f"Time needed: {time_needed}h.")
