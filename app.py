import json
from cryptography.fernet import Fernet

# 1. Aik Secret Key generate karein
# Ye key data ko "lock" aur "unlock" karne ke kaam aati hai
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# 2. Mockaroo wali file ko read karein
with open('MOCK_DATA.json', 'r') as f:
    users = json.load(f)

# 3. Har user ka password AES-256 ke zariye encrypt karein
for user in users:
    original_password = user['password'].encode() # Password ko byte mein convert kiya
    encrypted_password = cipher_suite.encrypt(original_password) # Encrypt kiya
    user['password'] = encrypted_password.decode() # Encrypted password ko wapis save kiya

# 4. Encrypted data ko aik nayi file mein save karein
with open('secure_users.json', 'w') as f:
    json.dump(users, f, indent=4)

print("Step 1 Done! 'secure_users.json' file is created and passwords are secure now.")