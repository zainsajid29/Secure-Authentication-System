import streamlit as st
from cryptography.fernet import Fernet
import pyotp

st.title("Secure Auth System - Internee.pk")

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

    if '2fa_secret' not in st.session_state:
        st.session_state['2fa_secret'] = pyotp.random_base32()

    secret = st.session_state['2fa_secret']
    st.write(f"Secret Key: `{secret}`")
    
    st.info("Step: Add this key to your Google Authenticator app first!")

    otp_input = st.text_input("Enter 6-digit OTP from your app:")
    
    if st.button("Verify"):
        totp = pyotp.TOTP(secret)
        if totp.verify(otp_input):
            st.balloons()
            st.success("Success! 2FA Verified.")
        else:
            st.error("Invalid Code.")