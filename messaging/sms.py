# Importing necessary modules
import random  # For generating random numbers and characters
import string  # For accessing predefined string constants (e.g., ascii letters, digits)
import requests  # For making HTTP requests to the SMS gateway API
from . import config  # Import configuration settings (e.g., API base URL, device ID)

# Function to generate an OTP (One-Time Password)
def generate_otp(otp_type='numeric'):
    """
    Generate a 6-character OTP based on the specified type.
    
    Parameters:
        otp_type (str): Type of OTP to generate. 
                        Available options:
                        - 'numeric' : Only numeric characters (0-9)
                        - 'letters' : Only uppercase letters (A-Z)
                        - 'alphanumeric' : A mix of uppercase letters (A-Z) and digits (0-9)
        
    Returns:
        str: Generated OTP (a string of 6 characters).
        
    Raises:
        ValueError: If an invalid otp_type is provided (i.e., not one of 'numeric', 'letters', or 'alphanumeric').
    """
    # Case when the OTP type is numeric (digits only)
    if otp_type == 'numeric':
        # Generate a 6-digit OTP by choosing random digits (0-9)
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])

    # Case when the OTP type is letters (uppercase alphabet letters only)
    elif otp_type == 'letters':
        # Generate a 6-character OTP by selecting random uppercase letters
        return ''.join([random.choice(string.ascii_uppercase) for _ in range(6)])

    # Case when the OTP type is alphanumeric (letters and digits)
    elif otp_type == 'alphanumeric':
        # Generate a 6-character OTP by selecting random characters from uppercase letters and digits
        return ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(6)])
    
    # Raise an error if the otp_type does not match the valid options
    else:
        raise ValueError("Invalid OTP type. Choose 'numeric', 'letters', or 'alphanumeric'.")

# Function to send the generated OTP via SMS
def send_otp_via_sms(receiver_phone, otp):
    """
    Send OTP via SMS using a third-party SMS gateway API.

    Parameters:
        receiver_phone (str): The phone number of the recipient to send OTP to.
        otp (str): The OTP value to be sent via SMS.
        
    Returns:
        bool: True if the OTP was successfully sent, False otherwise.
        
    Raises:
        requests.exceptions.RequestException: If a network-related or request error occurs.
    """
    try:
        # Send a POST request to the SMS gateway's API endpoint to deliver the OTP
        response = requests.post(
            f'{config.BASE_URL}/gateway/devices/{config.DEVICE_ID}/send-sms',  # Construct the API URL using the base URL and device ID
            json={  # Provide the necessary JSON payload to send the SMS
                'recipients': [receiver_phone],  # List of phone numbers to send the OTP to (just one in this case)
                'message': otp  # The OTP message content
            },
            headers={'x-api-key': config.API_KEY}  # Include the API key for authentication
        )
        
        # Log the API response (for debugging purposes)
        print(response.json()) 
        
        # Check if the API response status code is 200 (indicating a successful request)
        if response.status_code == 200:
            # Parse the JSON response body
            json_response = response.json()
            
            # Check if the API indicates success (based on the 'status' field in the response)
            if json_response.get('status') == 'success':
                return True  # Return True if OTP was sent successfully
            else:
                # If status is not success, print the error message and return False
                print(f"Error: {json_response.get('message', 'Unknown error')}")
                return False
        else:
            # If the response status code is not 200, print an error message and return False
            print(f"Failed to send OTP. Status code: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        # Handle any errors related to the network request (e.g., connection error, timeout, etc.)
        print(f"Error occurred while sending OTP: {e}")
        return False  # Return False in case of an error