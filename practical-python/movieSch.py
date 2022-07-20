#Movie Schedule

#ex:1
current_movies = {'The Grinch':'11:00am',
                 'Rudolph':'1:00pm',
                 'Frosty the Snowman':'3:00pm',
                 'Christmas Vaction':'5:00pm'}

print('We are showing the following movies:')
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print('Requested showtime isnt playing')
else:
    print(movie, 'is playing at', showtime)


#ex:2 menu list
menus = [ ['Egg Sandwich','Bagel','Coffee'],
        ['BLT', 'PB&J', 'Turkey Sandwich'],
        ['Soup','Sald','Spaghetti','Taco'] ]

print('Breakst menu:\t', menus[0])
print('Lunch Menu:\t', menus[1])
print('Dinner Menu:\t', menus[2])

# get items in list (consules bagel)
print(menus[0][1])

# using a for loop to get key and value
menus = { 'Breakfast': ['Egg Sandwich','Bagel','Coffee'],
          'Lunch':     ['BLT', 'PB&J', 'Turkey Sandwich'],
          'Dinner':    ['Soup','Sald','Spaghetti','Taco'] }

for name, menu in menus.items():
    print(name, ':', menu)

#console result
#Breakfast : ['Egg Sandwich', 'Bagel', 'Coffee']
#Lunch : ['BLT', 'PB&J', 'Turkey Sandwich']
#Dinner : ['Soup', 'Sald', 'Spaghetti', 'Taco']


#ex:3 dictionaries to store objects
person = {'name': 'Sarah Smith',
          'city': 'Orlando',
          'age': '100'}
print(person.get('name'), 'is', person.get('age'), 'years old.')

#console results
# Sarah Smith is 100 years old.