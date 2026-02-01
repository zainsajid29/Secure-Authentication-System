import streamlit as st
from cryptography.fernet import Fernet
import pyotp

st.title("🔐 Secure Auth System - Internee.pk")

# Sidebar for OAuth Info
st.sidebar.info("OAuth Client ID: [1062713848522-da807lnlci1gtiq2i5g7vs64dlh0mu7i.apps.googleusercontent.com]")

menu = ["Encryption Test", "2FA Verification"]
choice = st.sidebar.selectbox("Select Security Task", menu)

if choice == "Encryption Test":
    st.subheader("AES-256 Encryption")
    text = st.text_input("Enter a password to encrypt:")
    if st.button("Encrypt"):
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted = cipher.encrypt(text.encode())
        st.success(f"Encrypted: {encrypted.decode()}")

elif choice == "2FA Verification":
    st.subheader("Google Authenticator (2FA)")
    # Logic from your auth_test.py
    secret = pyotp.random_base32()
    st.write(f"Secret Key: `{secret}`")
    otp_input = st.text_input("Enter 6-digit OTP:")
    if st.button("Verify"):
        totp = pyotp.TOTP(secret)
        if totp.verify(otp_input):
            st.balloons()
            st.success("Verified!")
        else:
            st.error("Invalid Code")