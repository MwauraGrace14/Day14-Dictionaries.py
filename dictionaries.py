programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
                         "Program": "A set of instructions."}
print(programming_dictionary)

# creating an empty dictionary and wiping an existing dictionary
empty_dictionary = {}
programming_dictionary = empty_dictionary

#adding an item to a dictionary
programming_dictionary["Loop"] = "A repetitive function"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#Practical example 1
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score >90:
    student_grades[student] = "Outstanding"
  elif score >80:
    student_grades[student] = "Exceeds Expectations"
  elif score >70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"


print(student_grades)

#Nesting lists and dictionaries
["A","B",["C","D"]]
travel_log = {
  "Kenya":{"cities_visited": ["Kiambu","Nyandarua","Nairobi","Mombasa"], "total visits": 12},
  "France":{"cities_visited": ["Paris","Lille"], "total visits": 12}
}
print(travel_log)

#Nesting dictionaries in dictionaries
["A","B",["C","D"]]
travel_log = {
  {"country": "Kenya", 
   "cities_visited": ["Kiambu","Nyandarua","Nairobi","Mombasa"], 
   "total visits": 12,
  },
  {
   "country": "France",
   "cities_visited": ["Paris","Lille"],
   "total visits": 12,
  }
}
print(travel_log)
