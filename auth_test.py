import pyotp
import time

secret_key = pyotp.random_base32()
print(f"User's Secret Key: {secret_key}")

totp = pyotp.TOTP(secret_key)
current_otp = totp.now()

print(f"Current 6-digit OTP: {current_otp}")

user_input = input("Enter the 6-digit code you see: ")

if totp.verify(user_input):
    print("Success! 2FA Verified.")
else:
    print("Error: Invalid code or expired.")