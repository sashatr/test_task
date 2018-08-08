def max_number(number):
    sort_number = sorted(number, key=str, reverse=True)
    return ''.join(map(str, sort_number))


number = [int(x) for x in input('Enter the list of numbers: \n').split()]
print(max_number(number))