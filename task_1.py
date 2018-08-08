#!/usr/bin/env python3.5


def sort_list(list_str):
    list_type = ['number' if i.isdigit() else 'word' for i in list_str]
    number = sorted([int(i) for i in list_str if i.isdigit()])
    list_digit = [str(i) for i in number]
    list_word = sorted(list(set(list_str) - set(list_digit)))

    for i in list_word:
        for j in range(len(list_type)):
            if list_type[j] is 'word':
                list_type[j] = i
                break

    for i in list_digit:
        for j in range(len(list_type)):
            if list_type[j] is 'number':
                list_type[j] = i
                break

    return list_type


list_str = [str(x) for x in input('Enter a list of strings: \n').split()]
print(sort_list(list_str))