import os
import shutil
import time
from password_cracker import brute_force_password

# ----- [1] Simulate Self-Installation -----
def self_install():
    hidden_path = os.path.expanduser("~/.config/.sysdaemon_sim")
    script_path = os.path.realpath(__file__)
    if not os.path.exists(hidden_path):
        os.makedirs(hidden_path)
    dest_path = os.path.join(hidden_path, "daemon.py")
    if script_path != dest_path:
        shutil.copy(script_path, dest_path)
        print(f"[+] Simulated self-installation to {dest_path}")
        # Would normally restart from new path
    else:
        print("[*] Already running from hidden path.")

# ----- [2] Simulate Sending Data (No actual email) -----
def send_data_mock(password):
    print(f"[!] Simulated sending of cracked password to attacker@example.com: {password}")

# ----- Main Execution -----
if __name__ == "__main__":
    self_install()
    target = input("Enter simulated target password: ")
    cracked = brute_force_password(target)
    if cracked:
        send_data_mock(cracked)
