# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ["Alyssa", "Cynthia", "An",] # list of named created

print(students[1]) # Second student's name - calling index 1 
print(students[2]) # Last student's name - calling index 2


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

foodscontaining = ('pizza', 'coffee', 'brownies') #syntax uses parentheses () and commas (commas make the tuple)
for food in foodscontaining:
    print(f'{food} is a good food')

   

# Exercise 3
# Using a forloop, print just the last two food strings from foods.

for food in foodscontaining[1:]: #[x:] moves to the right x amount of times
 print(food)

# Exercise 4
# Create a dictionary named home_towncontaining the keys of city, stateand population.
# Print a string with this format:
# "I was born in city, state - population of population"


home_towncontaining = { # dictionary created with keys of city, state, and population 
    "city": "San Francisco",
    "state": "California",
    "population": "too much"
}

print(f"I was born in {home_towncontaining['city']}, {home_towncontaining['state']} - with a population of {home_towncontaining['population']}")

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# 	"city = Arcadia"
# 	"state = California"
# 	"population = 58000"

for key, val in home_towncontaining.items(): #"Iterate" = for loop
    print(f'{key} = {val}')

# Exercise 6
# Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape:
# {
# 	'student': 'Tina',
# 	'fav_food': 'Cheeseburger'
# }
# Iterate over cohort printing out each element.

cohort = [] #created empty list named cohort
for idx, student in enumerate(students):
    cohort.append({
        'student': student,
        'foodscontaining': foodscontaining [idx]}) #why do we need an idx in foodscontaining?

    print(cohort[idx])



# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_studentsprinting out each string.

awesome_students = [(f"{student} is awesome!") for student in students [:]] #variable named awesome_students containing the string w/ a splice 
for student in awesome_students: #iterate = for loop. Loop through each student 
    print(student) #print student 


# Exercise 8
# Using the tuple foods and list comprehension within a forloop, print each food string that contains the letter a.

newlist = [] #you want a new list only containing the words with the letter a 

for foods in foodscontaining:
    if "a" in foods:
        newlist.append(foods) #append adds items to the end of the given list 
print(newlist)
