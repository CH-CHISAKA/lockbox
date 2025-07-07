# otp_sms.py (or whatever your module name is)

import random  # For generating random numbers and characters
import string  # For accessing predefined string constants (e.g., ascii letters, digits)
import requests  # For making HTTP requests to the SMS gateway API
from . import config  # Import configuration settings (e.g., API base URL, device ID)


def generate_otp(otp_type='numeric'):
    """
    Generate a 6-character OTP based on the specified type.

    Parameters:
        otp_type (str): Type of OTP to generate.
                        Options: 'numeric', 'letters', 'alphanumeric'

    Returns:
        str: 6-character OTP
    """
    if otp_type == 'numeric':
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])
    elif otp_type == 'letters':
        return ''.join([random.choice(string.ascii_uppercase) for _ in range(6)])
    elif otp_type == 'alphanumeric':
        return ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(6)])
    else:
        raise ValueError("Invalid OTP type. Choose 'numeric', 'letters', or 'alphanumeric'.")


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
