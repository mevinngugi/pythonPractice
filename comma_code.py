# Comma Code

'''

Comma Code

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and
returns a string with all the items separated by a comma and a space,
with and inserted before the last item. For example, passing the previous
spam list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.

'''

# The sample list
spam = ['apples', 'bananas', 'tofu', 89, 56]


def commaCode(yourList):

    new_string = ""

    for x in range(len(yourList)):

        if len(yourList) == 1:
            new_string += str(yourList[x])

        elif x < (len(yourList)-1):
            new_string += (str(yourList[x]) + ", ")

        else:
            new_string += ("and " + str(yourList[x]))

    return new_string


print(commaCode(spam))
