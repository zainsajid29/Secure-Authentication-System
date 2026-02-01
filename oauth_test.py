import os
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_ID = "1062713848522-da807lnlci1gtiq2i5g7vs64dlh0mu7i.apps.googleusercontent.com"
CLIENT_SECRET = "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" 


SCOPES = ['https://www.googleapis.com/auth/userinfo.email', 'openid']

def google_login_test():
    # Client configuration dictionary
    client_config = {
        "web": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
    }

    # Flow setup
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES, redirect_uri='http://localhost:8501')
    
    print("Please login in the browser window that opens...")
    
    print("OAuth setup logic is ready!")

if __name__ == "__main__":
    print("Starting OAuth 2.0 Verification Test...")
    
    if CLIENT_ID == "1062713848522-da807lnlci1gtiq2i5g7vs64dlh0mu7i.apps.googleusercontent.com":
        print("Error: Please update CLIENT_ID in the script first.")
    else:
        google_login_test()