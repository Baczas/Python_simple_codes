test_string = ['I AM UPPER CASE SENTENCE', 'I am normal sentence', 'i am small sentence', 'I aM PoCkeMoN lanGUAge', 'I @m Al1$ow PoCkEm0n !anguage']
print(test_string)


# UPPER CASE
# test_string = [x.upper() for x in test_string]
# print(test_string)

# LOWER CASE
# test_string = [x.lower() for x in test_string]
# print(test_string)

def reverse(string):
    new_string = ''
    for y in string:
        if y.isupper():
            new_string += y.lower()
        elif y.islower():
            new_string += y.upper()
        else:
            new_string += y
    return new_string


def sentence_case(string):
    new_string = ''
    for counter, y in enumerate(string):
        if counter == 0 and y.islower():
            new_string += y.upper()
        elif counter != 0 and y.upper():
            new_string += y.lower()
        else:
            new_string += y
    return new_string


def capitalize(string):
    new_string, y_min1 = '', ''
    for counter, y in enumerate(string):

        if y.islower() and (y_min1 == ' ' or y_min1 == ''):
            new_string += y.upper()
        elif y.isupper() and (y_min1 == ' ' or y_min1 == ''):
            new_string += y

        else:
            new_string += y.lower()

        y_min1 = y
    return new_string


print('\n' + 'Reverse: ')
for _ in test_string:
    print(reverse(_))

print('\n' + 'Sentence_case: ')
for _ in test_string:
    print(sentence_case(_))

print('\n' + 'Capitalize: ')
for _ in test_string:
    print(capitalize(_))
