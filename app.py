import json

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return 'This word doesn\'t exist. Please try again'

user_word = input('Enter a word: ')

print(translate(user_word))