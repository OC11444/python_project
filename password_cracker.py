import time
import itertools

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
password = input("Enter the password: ")
start = time.time()

found = False
max_length = 5  # You can increase this, but it gets exponentially slower

for length in range(1, max_length + 1):
    for guess in itertools.product(chars, repeat=length):
        guess_str = ''.join(guess)
        if guess_str == password:
            end = time.time()
            print(f"[+] Password found: {guess_str}")
            print(f"[+] Time taken: {round(end - start, 2)} seconds")
            found = True
            break
    if found:
        break

if not found:
    print("[-] Password not found within length limit.")
