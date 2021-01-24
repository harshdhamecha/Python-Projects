import secrets
import string

def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(secrets.choice(chars) for _ in range(length))
    print('The password generated by python is:', pwd)

length = int(input('Enter the length of the password: '))
password_generator(length)