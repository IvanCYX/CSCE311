def mirror(x):

    # define alphabets with mirrors

    mirrorAlphabets = {'b':'d','d':'b','o':'o','p':'q','q':'p','v':'v','w':'w','x':'x'}

    #initialise an empty 'box'
    mirrorString= ''

    for char in x:

        # if an alphabet is not in the dictionary, the mirror does not exist (INVALID)
        if char not in mirrorAlphabets.keys():

            return 'INVALID'

        else:

            mirrorString = mirrorString + mirrorAlphabets[char]

    return mirrorString[::-1]

# test cases

print(mirror("vow"))

print(mirror("bed"))

print(mirror("wood"))

print(mirror("spoon"))
