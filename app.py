import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        guess = get_close_matches(word, data.keys())[0]
        yes_no = input(
            f'Did you mean \'{guess}\' instead? Enter Y if yes, or N if no: ').lower()
        if yes_no == 'y':
            return data[guess]
        elif yes_no == 'n':
            return 'Please double check your input'
        else:
            return 'We do not understand the input'
    else:
        return 'This word doesn\'t exist. Please try again'


user_word = input('Enter a word: ')

output = translate(user_word)

if type(output) == list:
    for i in output:
        print(f'{user_word}: {i}')
else:
    print(output)

# Fun snippet - discovering another python library - in this instance difflib and within it being able
# to use get_close_matches and understanding a little bit about how it works with SequenceMatcher and the
# ratio of similarity between strings, using it to guess what someone may have misspelled.
