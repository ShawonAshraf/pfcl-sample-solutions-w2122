first = input('Enter a word: ')
last = first

word = input('Enter a word: ')
while word != 'done':
    first = min(first, word)
    last = max(last, word)
    word = input('Enter a word: ')

print(first, 'comes first in the dictionary')
print(last, 'comes last in the dictionary')
