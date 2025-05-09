# 🔐 Brute-Force Password Cracker (Python)

This project is a basic brute-force password cracker built with Python. It attempts to guess a user-provided password by generating and comparing all possible character combinations.

---

## 🚀 Features

- Supports:
  - Uppercase and lowercase letters
  - Numbers
  - Special characters
- Measures the time taken to crack the password
- Adjustable max password length
- Easy to extend or optimize (e.g., multithreading or dictionary attacks)

---

## 📦 Requirements

- Python 3.x
- No external libraries required (uses only the Python Standard Library)

---

## 📄 How It Works

1. User inputs a password.
2. The script tries all possible combinations of characters up to a given maximum length.
3. It compares each guess with the target password.
4. When a match is found, the script prints the password and how long it took to find it.

---

## 🛠️ Usage

```bash
python3 password_cracker.py
# 🧪 Simulated Malware for Ethical Hacking Practice

This is a Python-based malware simulation used for ethical training in a controlled virtual machine (e.g., Parrot OS). It mimics basic malware behavior like self-installation, brute-force password cracking, and data exfiltration.

---

## 🚀 How It Works

- `daemon.py`: Simulates malware by self-installing, cracking a password, and "sending" it.
- `password_cracker.py`: Module to brute-force guess a password using defined charset.

---

## ✅ Usage

```bash
python3 daemon.py
