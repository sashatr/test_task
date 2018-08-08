#!/usr/bin/env python3.5


def even_or_odd(list_number):
    even, odd = 0, 0

    for number in list_number:
        if (number % 2) is 0:
            even += 1
        if (number % 2) is 1:
            odd += 1

        if even is 2 or odd is 2:
            break

    return 1 if even > odd else 0


def different(list_number):
    residue = even_or_odd(list_number)
    for i in list_number:
        if i % 2 is residue:
            return i


list_number = [int(x) for x in input('Enter the list of numbers: \n').split()]
print(different(list_number))

