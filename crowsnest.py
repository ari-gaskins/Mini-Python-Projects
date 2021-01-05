# Program which takes user inputs and puts it into a given statement then outputs full statement
# Logic: user gives cpu string, cpu understands vowels, cpu provides articles for the string,
# cpu prints article and word inside new f string

# set word, address vowels, create article
word = input('enter a word: ')
vowels = {'a', 'e', 'i', 'o', 'u'}
article = 'a'

# iterate through vowels, if first letter of word has vowel, article is changed to an
for vowel in vowels:
    if word[0] == vowel:
        article = 'an'

# creates f string of statement including article for the user's string value
statement = f'Howdy! Did you get {article} {word} today? If not, I hope you do!'

# prints new statement
print(statement)