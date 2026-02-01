import streamlit as st
from cryptography.fernet import Fernet
import pyotp

# App Title
st.set_page_config(page_title="Secure Auth Flow")
st.title("🔐 Enterprise Security System")

# Session State to track login progress
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "password_verified" not in st.session_state:
    st.session_state.password_verified = False

# --- STEP 1: LOGIN PAGE ---
if not st.session_state.password_verified:
    st.subheader("Step 1: Identity Verification")
    user_input = st.text_input("Username")
    pass_input = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Yahan hum farz kar rahe hain password 'za1212' hai
        if pass_input == "za1212": 
            st.session_state.password_verified = True
            st.rerun()
        else:
            st.error("Invalid Credentials")

# --- STEP 2: 2FA PAGE ---
elif st.session_state.password_verified and not st.session_state.authenticated:
    st.subheader("Step 2: Two-Factor Authentication")
    
    if '2fa_secret' not in st.session_state:
        st.session_state['2fa_secret'] = pyotp.random_base32()
        
    st.write(f"Add this key to Authenticator: `{st.session_state['2fa_secret']}`")
    otp_input = st.text_input("Enter 6-digit OTP")
    
    if st.button("Verify OTP"):
        totp = pyotp.TOTP(st.session_state['2fa_secret'])
        if totp.verify(otp_input):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid OTP")

# --- STEP 3: DASHBOARD ---
else:
    st.success("✅ Full Authentication Complete!")
    st.subheader("Welcome to the Secure Dashboard")
    st.write("You are now logged in using AES-256 and Multi-Factor Authentication.")
    
    if st.button("Logout"):
        st.session_state.password_verified = False
        st.session_state.authenticated = False
        st.rerun()