import sys
from cryptography.fernet import Fernet

file = sys.argv[1]

# Generowanie klucza
key = Fernet.generate_key()
cipher = Fernet(key)

with open("aes.key", "wb") as key_file:
    key_file.write(key)

# Szyfrowanie
with open(file, "rb") as f:
    plaintext = f.read()

ciphertext = cipher.encrypt(plaintext)

out_file = file + ".enc"
with open(out_file, "wb") as f:
    f.write(ciphertext)

print(f"Saved {out_file}")

