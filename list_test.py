#!/usr/bin/env python3

# Filename:     arrays_test.py
# Author:       DMR

from collections import Counter
from collections import defaultdict
import copy

# list
squares = []

for x in range(1, 11):
    squares.append(x**2)
print(squares)

squares2 = [value**2 for value in range(1, 11)]
print(squares2)

squares3 = copy.copy(squares2)
squares3[0] = 1000
print(squares2[0])
print(squares3[0])
print("")

ll = [x for x in range(1, 1_000_001)]

print(f"ll starts at: {ll[0]}")
print(f"ll min is: {min(ll)}")
print(f"ll ends at: {ll[-1]}")
print(f"ll max is: {max(ll)}")
print(f"ll sum is: {sum(ll)}")

odds = [x for x in range(1, 20, 2)]
print(f"odds: {odds}")

threes = [x for x in range(3, 31, 3)]
print(f"threes: {threes}\n")

list1 = [3, 1, 56, 34, 22, 67]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list2 = [[2, 4], [3, 3], [52, 1], [33, 33]]
list2.sort()
print(list2)


def s2(item):
    return item[1]


list2.sort(key=s2)
print(list2)
print("")

letters = ['A', 'T', 's', 'c', 'D']
print(letters)
letters.sort()
print(letters, '# default sort by ASCII value')
letters.sort(key=str.lower)
print(letters, '# sorted using key=str.lower')
print("")

# dictionary
age = {
    "dennis": 62,
    "karen": 53,
    "will": 23,
    "ben": 21,
    "claire": 18,
}

for name in age:
    print(f"{name.title()} is {age[name]} years old.")
print("")

# sort by the key
for name in sorted(age.keys()):
    print(f"{name.title()} is {age[name]} years old.")
print("")

# sort by the value
value_sort = dict(sorted(age.items(), key=lambda x: x[1]))
print(value_sort)
print("")
for name in value_sort:
    print(f"{name.title()} is {age[name]} years old.")
print("")

family = {
    "dennis": {
        "middle": "michael",
        "age": 60,
    },
    "karen": {
        "middle": "elise",
        "age": 51,
    },
    "will": {
        "middle": "walter",
        "age": 22,
    },
    "ben": {
        "middle": "john",
        "age": 20,
    },
    "claire": {
        "middle": "elizabeth",
        "age": 17,
    },
}

# print specific fields from the dictionary
for person, person_info in family.items():
    print(f"{person} middle: {person_info['middle']} age: {person_info['age']}")

print("")

acronyms = {"LOL": "laugh out loud", "IDK": "I don't know"}
print(acronyms)

# use the get method to avoid no-key errors
print(acronyms.get("IDK", "Not found"))
print(acronyms.get("IK", "Not found"))

# change an item based on the key
acronyms["IDK"] = "Don't know"
print(acronyms)

# delete an item based on the key
del acronyms["LOL"]
print(acronyms)

print("")

newdict = defaultdict(int)

newdict['item1'] = 2
print(newdict['item1'])
print(newdict['item2'])

current_movies = {
    "The Grinch": "11:00am",
    "Rudolph": "1:00pm",
    "Frosty the Snowman": "3:00pm",
    "Christmas Vacation": "5:00pm",
}

print("We're showing the following movies:")
for key in current_movies:
    print(f"\t{key}")

movie = input("Which movie do you want to go to? ")

showtime = current_movies.get(movie)

if showtime == None:
    print("Not a valid movie")
else:
    print(f"{movie} is playing at {showtime}")

print("")

contacts = {
    "number": 4,
    "students": [
        {"name": "Sarah Holderness", "email": "sarah@hogwarts.com"},
        {"name": "Harry Potter", "email": "harry@hogwarts.com"},
        {"name": "Hermione Granger", "email": "hermione@hogwarts.com"},
        {"name": "Ron Weasley", "email": "ron@hogwarts.com"},
    ],
}

# print only the email addresses
for contact in contacts["students"]:
    print(contact["email"])

print("")

# demonstrate counters

c = Counter()

c['apples'] += 1
c['bananas'] += 1
c['apples'] += 2
c['cheries'] += 4

print(c.most_common) # prints the elements which are in order from most to
                     # least common

prose = "On this day in nineteen ninety nine Peter Piper picked a " \
        "perfect peck of pickled peppers and sold some seashells by the seashore"

prose = prose.lower()
words = prose.split(' ')
prose_count = Counter()

for word in words:
    prose_count[word[0]] +=1

print(prose_count.most_common())    

print("")
print(list(prose_count.elements()))
