def names_str(list_name):
    names = [i['name'] for i in list_name]
    if len(names) is 1:
        return names[0]
    elif len(names) is 2:
        return ' & '.join(map(str, names))
    else:
        return ', '.join(names[:-1]) + ' & '+ str(names[-1:])[2:-2]


list_name_1 = [{'name': 'John'}]
list_name_2 = [{'name': 'John'}, {'name': 'Jack'}]
list_name_3 = [{'name': 'John'}, {'name': 'Jack'}, {'name': 'Joe'}]

print(names_str(list_name_1))
print(names_str(list_name_2))
print(names_str(list_name_3))