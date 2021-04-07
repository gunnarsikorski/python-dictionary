import json

data = json.load(open('data.json'))

def translate(word):
    return data[word]

user_word = input('Enter a word: ')

print(translate(user_word))