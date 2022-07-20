#Lists, loops

#ex:1
#append method added tbh to list
acronyms = ['LOL', 'IDK', 'SMH']
acronyms.append('TBH')
print(acronyms)

#remove method removed lol from list
acronyms.remove('LOL')
print(acronyms)

#ex:2 checking if exists in list
acronyms = ['LOL', 'IDK', 'SMH']
word = 'BFN'
if word in acronyms:
    print(word + ' is in the list')
else:
    print(word + ' is NOT in the list')

#ex:3 loop
acronyms = ['LOL', 'IDK', 'SMH']
for acronym in acronyms:
    print(acronym)





