#Password Generator Project
from random import choice, randint, shuffle
import string
letters = list(string.ascii_letters)
numbers = [str(item) for item in range(10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(1, 3)
nr_numbers = randint(2, 4)



password_list = [choice(letters) for item in range(nr_letters)] + [choice(symbols) for item in range(nr_symbols)] + [choice(numbers) for item in range(nr_numbers)]

shuffle(password_list)

password = "".join(password_list)

print(f"Your password is: {password}")