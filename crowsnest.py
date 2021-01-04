# Program which takes user inputs and puts it into a given statement then outputs full statement

word = input('enter a word: ')
vowels = {'a', 'e', 'i', 'o', 'u'}
article = 'a'

for vowel in vowels:
    if word[0] == vowel:
        article = 'an'

statement = f'Howdy! Did you get {article} {word} today? If not, I hope you do!'

print(statement)