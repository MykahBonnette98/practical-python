##Dictionary

#ex:1
acronyms = {'LOL': 'laugh out loud',
            'IDK': 'I dont know',
            'TBH': 'to be honest'}

#ex:2 adding values
acronyms = {}
acronyms['LOL'] = 'laugh out loud'
acronyms['IDK'] = 'I dont know'
acronyms['TBH'] = 'to be honest'
print(acronyms)

#ex:4 upddating value
print(acronyms)
acronyms['TBH'] = 'honestly'
print(acronyms['TBH'])

#ex: 5 deleting value
del acronyms['LOL']
print(acronyms)

#ex:6 getting value that isnt there (prints none, else key doesnt exist)
definition = acronyms.get('BTW')
print(definition)
if definition:
    print(definition)
else: 
    print('Key doesnt exist') 


#ex:7 tranlating
sentence = 'IDK' + ' what happen ' + 'TBH'
translation = acronyms.get('IDK') +' what happen '+ acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)
#console result
# sentence: IDK what happen TBH
# translation: I dont know what happen to be honest