#Implement the function unique_in_order which takes as argument a sequence and
#returns a list of items without any elements with the same value next to each other
#and preserving the original order of elements.

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']

# Logic of the Program
# LETTERS = []
# STR = "AAAABBBCCDAABBB" <= break into an array
# loop while STR.hasNext()
    # if x != LETTERS[-1]
        # LETTERS.addItem(x)


def unique_in_order(str):
    letters = []
    for x in str:
        if len(letters) == 0 or x != letters[-1]:
            letters.append(x)
    print(letters)
    return(letters)

str = "AAAABBBCCDAABBB"
unique_in_order(str)
