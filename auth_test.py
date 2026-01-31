import pyotp
import time

# 1. Aik naya secret key generate karein (Har user ke liye alag hota hai)
secret_key = pyotp.random_base32()
print(f"User's Secret Key: {secret_key}")

# 2. Is key ko Google Authenticator app mein 'Manual Entry' ke zariye add kiya ja sakta hai
# Lekin hum abhi code se OTP generate kar ke test karte hain
totp = pyotp.TOTP(secret_key)
current_otp = totp.now()

print(f"Current 6-digit OTP: {current_otp}")

# 3. Verification Test
# Farz karein user ne app se dekh kar code enter kiya
user_input = input("Enter the 6-digit code you see: ")

if totp.verify(user_input):
    print("Success! 2FA Verified.")
else:
    print("Error: Invalid code or expired.")