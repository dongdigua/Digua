#
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
}

#
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
}

#
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#
print('-' * 10)
print('NY State has:', cities['NY'])
print('OR State has:', cities['OR'])

#
print('-' * 10)
print('Michigan:', states['Michigan'])
print('Florida:', states['Florida'])

#
#print('-' * 10)
#print


#
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

#




#






#





#





