
import string
import random


length_of_string = 8

print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

length_of_string = 8

print(''.join(random.choice(string.ascii_letters+str('+*-%/&#!?¿')) for _ in range(length_of_string)))
length_of_string = 8

print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

length_of_string = 8

print(''.join(random.choice(string.ascii_lowercase) for _ in range(length_of_string)))

length_of_string = 8

print(''.join(random.choice(string.ascii_uppercase) for _ in range(length_of_string)))