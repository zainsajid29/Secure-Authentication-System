# Secure User Authentication System 🔐

This project was developed as part of my **Cyber Security Internship at Internee.pk**. The goal is to demonstrate a robust authentication system that protects sensitive user data and prevents unauthorized access using industry-standard security measures.

## 🚀 Features Implemented

### 1. AES-256 Data Encryption
- **Objective:** Protect user passwords "at rest" in the database.
- **Implementation:** Used the `cryptography` library in Python to encrypt plain-text passwords into secure ciphertexts.
- **Standard:** AES-256 (Military-grade encryption).

### 2. Two-Factor Authentication (2FA)
- **Objective:** Add an extra layer of security beyond passwords.
- **Implementation:** Integrated `pyotp` to generate Time-based One-Time Passwords (TOTP) compatible with **Google Authenticator**.
- **Result:** Users must provide a 6-digit sync code to verify their identity.

### 3. OAuth 2.0 Integration (In Progress)
- **Objective:** Provide seamless and secure social logins.
- **Standard:** Using Google OAuth 2.0 protocols for user sign-ins.
- **Client ID:** 1062713848522-da807lnlci1gtiq2i5g7vs64dlh0mu7i.apps.googleusercontent.com
- 
## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** `cryptography`, `pyotp`, `json`
- **Data Source:** Mock user dataset generated via Mockaroo.

## 📁 Project Structure
- `app.py`: Contains the logic for AES-256 encryption and data processing.
- `auth_test.py`: Script to test the 2FA / Google Authenticator logic.
- `secure_users.json`: The final output showing encrypted user data.

## 🛡️ Security Disclaimer
This is a staging/test environment project for educational purposes. Secret keys are generated dynamically for demonstration.
