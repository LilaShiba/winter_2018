# how to import other python files
import binary_hash
# how to use data from other python file once imported
b_hash = binary_hash.binary_hash
#print(b_hash)

#####################################functional programming ##############################################################################################################################
def encrypt(message):
    # store encrpyted message
    new_word = []
    # add delimiter
    message = message.replace(" ", "-")
    # begin encrypt
    for x in message:
        # skip delimiter
        if x == '-':
            pass
        else:
        # get value from key
            x = b_hash[x]
            x = x + '-'
        # add new value to new_word
        new_word.append(x)
    # turn list into string
    return ''.join(new_word)

##################################### call encrypt ##############################################################################################################################
binary_word = encrypt('hello world')
# check encrypt
print(binary_word)

##################################### decrypt function ##############################################################################################################################


def decrypt(message):
    new_word = []
    # add delimiter to split words into letter
    message = message.split('-')
    # begin decrypt
    for x in message:
        # skip to next word
        if x == '-':
            pass
        else:
            # iterate over hash to get value from key
            for key, value in b_hash.items():
                if value == x:
                    x = key
                    new_word.append(x)
    return ''.join(new_word)

##################################### main program run ##############################################################################################################################

print(decrypt(binary_word))
