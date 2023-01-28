# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ["Alyssa", "Cynthia", "An",]

print(students[1]) # Second student's name
print(students[2]) # Last student's name 


# Exercise 2
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

foodscontaining = ('pizza', 'coffee', 'brownies') # syntax uses parentheses ()
for food in foodscontaining:
    print(f'{food} is a good food')

   

# Exercise 3
# Using a forloop, print just the last two food strings from foods.

for food in foodscontaining[1:]: #[1:] moves to the right one 
 print(food)

# Exercise 4
# Create a dictionary named home_towncontaining the keys of city, stateand population.
# Print a string with this format:
# "I was born in city, state - population of population"


home_towncontaining = {
    "city": "San Francisco",
    "state": "California",
    "population": "too much"
}
for key, val in home_towncontaining.items():
    print(f'I was born in the {key} of {val}')


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# 	"city = Arcadia"
# 	"state = California"
# 	"population = 58000"

# print(home_towncontaining)

# Exercise 6
# Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape:
# {
# 	'student': 'Tina',
# 	'fav_food': 'Cheeseburger'
# }
# Iterate over cohortprinting out each element.



# Exercise 7
# Using the list of studentsand list comprehension, assign to a variable named awesome_studentsa new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_studentsprinting out each string.



# Exercise 8
# Using the tuple foodsand list comprehension within a forloop, print each food string that contains the letter a.

