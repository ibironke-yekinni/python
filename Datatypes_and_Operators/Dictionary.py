'''
Quiz: Define a Dictionary
Define a dictionary named population that contains this data:

Keys	Values
Shanghai	17.8
Istanbul	13.3
Karachi	13.0
Mumbai	12.5
'''
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}
print(population)
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

'''
Quiz: Adding Values to Nested Dictionaries
Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. After inserting the new entries you should be able to perform these lookups:

>>> print(elements['hydrogen']['is_noble_gas'])
False
>>> print(elements['helium']['is_noble_gas'])
True
'''
elements = {'hydrogen': {'number': 1, 
                        'weight': 1.00794, 
                        'symbol': 'H',
                        'is_noble_gas': False},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He', 'is_noble_gas': True}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
#hydrogen = elements["hydrogen"] 
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
