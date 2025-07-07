from crypto import encrypt_message, decrypt_message
import requests

def send_secure_message_to_peer(message, otp, peer_ip):
    """
    Sends an encrypted message to the peer device at peer_ip.
    The message is encrypted using the provided OTP.
    """
    try:
        # Encrypt the message
        encrypted = encrypt_message(message, otp)
        
        # Send the encrypted message to the peer
        response = requests.post(f"http://{peer_ip}:5000/receive", json={'encrypted_msg': encrypted})
        
        # Check the response status code
        if response.status_code == 200:
            return response.status_code
        else:
            print(f"Error: Received unexpected status code {response.status_code} from peer.")
            return response.status_code
    except requests.exceptions.RequestException as e:
        # Handle network errors
        print(f"Error sending secure message: {e}")
        return None


def read_secure_message_from_local(otp):
    """
    Reads an encrypted message from the local server and decrypts it using the provided OTP.
    """
    try:
        # Get the encrypted message from the local server
        response = requests.get("http://127.0.0.1:5000/get_message")
        
        # Check if the response is successful
        if response.status_code == 200:
            encrypted_msg = response.json().get('encrypted_msg', '')
            if not encrypted_msg:
                print("No encrypted message received.")
                return None
            # Decrypt the message
            return decrypt_message(encrypted_msg, otp)
        else:
            print(f"Error: Received unexpected status code {response.status_code} from local server.")
            return None
    except requests.exceptions.RequestException as e:
        # Handle network errors
        print(f"Error reading secure message: {e}")
        return None
