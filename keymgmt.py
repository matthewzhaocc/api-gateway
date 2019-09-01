import random
def create_new_key():
    key = ''
    for i in range(16):
        key += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+\{\}:"><?')
    return key
print(create_new_key())