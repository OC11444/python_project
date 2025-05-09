import itertools
import time

def brute_force_password(target_password, max_length=4):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#"
    start = time.time()
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess_str = ''.join(guess)
            print(f"Trying: {guess_str}")
            if guess_str == target_password:
                end = time.time()
                print(f"[+] Password cracked: {guess_str} in {round(end - start, 2)}s")
                return guess_str
    print("[-] Password not found.")
    return None
