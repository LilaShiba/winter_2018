# https://www.codewars.com/kata/scramblies/train/python
def scramble(my_str, check_str):

    my_str = list(my_str)
    check_str = list(check_str)
    
    for x in check_str:
        if x in my_str:
            my_str.remove(x)
        else:
            return False



def scramble(my_str, check_str):

    my_str = list(my_str)
    check_str = list(check_str)
    new_boy = []
    main_count = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
    }
    for x in check_str:
        main_count[x] += 1
    x_count = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
    }


    for x in my_str:
        if x in check_str and x_count[x] != main_count[x]:
            new_boy.append(x)
            x_count[x] += 1

    new_boy.sort()
    check_str.sort()
    if new_boy == check_str:
        return True
    else:
        return False

print(scramble('cedewaraaossoqqyt', 'codewarss'))
