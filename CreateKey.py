import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    Key = rand_string
    f = open('Key.txt', 'w',)
    f.write(Key)
    f.close()
    print("Ваш ключ: " + Key)

generate_random_string(20)



