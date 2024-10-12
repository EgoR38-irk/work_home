def  print_params(a = 1, b = 'Cтрока', c = True):
        print(a, b, c)

values_list = [27, 'String', True]
values_dict = { 'a': 2, 'b': 'Строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [ 37, 'string']
print_params(*values_list_2, 42)