

def camel_case(word):
    '''
    example:
    s1 = 'the_phantom_menace'    # the_phantom_menace -> thePhantomMenace
    s2 = 'The-Phantom-Menace'    # The-Phantom-Menace -> ThePhantomMenace
    '''

    r = word.title().replace('-', '').replace('_', '')
    first, first_true = r[0], word[:1]
    return r.replace(first, first_true, 1)


word = str(input('Entes text: \n'))
print(camel_case(word))

