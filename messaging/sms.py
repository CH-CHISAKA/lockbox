# otp_sms.py (or whatever your module name is)

import random  # For generating random numbers and characters
import string  # For accessing predefined string constants (e.g., ascii letters, digits)
import requests  # For making HTTP requests to the SMS gateway API
from . import config  # Import configuration settings (e.g., API base URL, device ID)
import hashlib
import secrets
import string
import datetime

def generate_otp(otp_type=None):
    """
    Generate a 6-character OTP using PBKDF2 for better randomness.

    Parameters:
        otp_type (str or None): Type of OTP to generate.
                                Options: 'numeric', 'letters', 'alphanumeric'
                                If None, a random type will be chosen.

    Returns:
        str: 6-character OTP
    """
    # Randomly select OTP type if not provided
    if otp_type is None:
        otp_type = secrets.choice(['numeric', 'letters', 'alphanumeric'])

    # Character set based on type
    if otp_type == 'numeric':
        charset = string.digits
    elif otp_type == 'letters':
        charset = string.ascii_uppercase
    elif otp_type == 'alphanumeric':
        charset = string.ascii_uppercase + string.digits
    else:
        raise ValueError("Invalid OTP type. Choose 'numeric', 'letters', or 'alphanumeric'.")
    # Use PBKDF2 for secure key derivation
    # This ensures the OTP is generated in a secure manner  
    # and is resistant to brute-force attacks.
    # Secure secret and salt generation
    secret = secrets.token_bytes(32)
    salt = secrets.token_bytes(16)

    # Derive a key
    key = hashlib.pbkdf2_hmac('sha256', secret, salt, 100_000, dklen=32)

    # Map derived key bytes to characters in charset
    otp = ''.join([charset[b % len(charset)] for b in key[:6]])

    return otp





def send_otp_via_sms(receiver_phone, otp):
    """
    Send OTP via SMS using a third-party SMS gateway API.

    Parameters:
        receiver_phone (str): Phone number to send OTP to (should be in E.164 format like +2547XXXXXXX)
        otp (str): OTP message to send

    Returns:
        bool: True if the OTP was successfully sent (queued), False otherwise.
    """
    try:
        response = requests.post(
            f'{config.BASE_URL}/gateway/devices/{config.DEVICE_ID}/send-sms',
            json={
                'recipients': [receiver_phone],
                'message': otp
            },
            headers={'x-api-key': config.API_KEY}
        )

        print("🔄 Raw response:", response.status_code, response.json())

        if response.status_code in (200, 201):
            json_response = response.json()

            # Check both top-level and nested 'data.success'
            top_success = json_response.get('success')
            nested_success = json_response.get('data', {}).get('success')

            if top_success is True or nested_success is True:
                print("✅ OTP successfully sent or queued.")
                return True
            else:
                print(f"⚠️ API returned non-success status: {json_response}")
                return False
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"🚨 Exception while sending OTP: {e}")
        return False
