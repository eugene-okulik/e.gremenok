my_dict = {
        'tuple': (42, 'test', True, None, 36.6),
        'list': ['Guido', 1990, 3.14, False, 'Flack'],
        'dict':
            {
                'int': 123,
                'f_string': 'QWERTY',
                'float': 640.0,
                'boolean': True,
                'l_string': 'Monty'
            },
        'set': {True, 2, 3.0, 'Quattro', 'V'}
    }

print(my_dict['tuple'][-1])

my_dict['list'].append('last_element')
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = '2025'
my_dict['dict'].pop('f_string')

my_dict['set'].add('abracadabra')
my_dict['set'].remove('V')

print(my_dict['tuple'])
print(my_dict['list'])
print(my_dict['dict'])
print(my_dict['set'])
