from random import choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

pwd_length = int(input('Enter password length: '))
pwd_digits = input('Include numbers (yes = y, no = n): ')
pwd_uppercase = input('Include uppercase letters (yes = y, no = n): ')
pwd_lowercase = input('Include lowercase letters (yes = y, no = n): ')
pwd_punctuation = input(
    'Include symbols "!#$%&*+-=?@^_"? (yes = y, no = n): ')

if pwd_digits == 'y':
    chars += digits
if pwd_uppercase == 'y':
    chars += uppercase_letters
if pwd_lowercase == 'y':
    chars += lowercase_letters
if pwd_punctuation == 'y':
    chars += punctuation

password = ''

for i in range(pwd_length):
    password += choice(chars)

print('\n', password, '\n', sep='')
