#!/usr/bin/env python3

num_grades = int(input("How many grades? "))

grades = []
for x in range(num_grades):
    grade = int(input(f"Enter grade {x+1}: "))
    grades.append(grade)

print(f"Average of grades = {sum(grades)/len(grades):.2f}")
