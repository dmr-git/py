#!/usr/bin/env python3

num_grades = int(input("How many grades? "))
grades = []
avg = 0.0
sum_grades = 0.0

for x in range(num_grades):
    grade = int(input(f"Enter grade {x+1}: "))
    grades.append(grade)


for grade in grades:
    sum_grades = sum_grades + grade

for grade in grades:
    print(grade)

avg = round(sum_grades/num_grades,2)

print(f"Average = {avg}") 

