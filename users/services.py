import random


def generate_password():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw = ""
    for i in range(8):
        next_index = random.randrange(len(alphabet))
        pw = pw + alphabet[next_index]
    return pw
