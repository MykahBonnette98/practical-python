# Contacts Dictionary

#ex:1
contacts = {
    'number':4,
    'students':
    [
        {'name':'Sarah Holderness', 'email':'sarah@example.com'},
        {'name':'Harry Potter', 'email':'harry@example.com'},
        {'name':'Hermione Granger', 'email':'hermione@example.com'},
        {'name':'Ron Weasley', 'email':'ron@example.com'}
    ]
}

for student in contacts['students']:
    print(student['email'])

#using a for loop to print only emails, console result
# sarah@example.com
# harry@example.com
# hermione@example.com
# ron@example.com

