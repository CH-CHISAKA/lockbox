from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_message(message, key):
    """
    Encrypts a message using AES GCM mode with a 32-byte key.
    The key is padded/truncated to ensure it is exactly 32 bytes.
    """
    key = key[:32].ljust(32).encode()  # Ensure the key is 32 bytes long
    cipher = AES.new(key, AES.MODE_GCM)  # Create AES cipher in GCM mode
    nonce = cipher.nonce  # Generate a unique nonce for each encryption
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())  # Encrypt and generate tag
    # Concatenate nonce, tag, and ciphertext for transport
    encrypted = base64.b64encode(nonce + tag + ciphertext).decode()  # Base64 encode the result
    return encrypted

def decrypt_message(encrypted_message, key):
    """
    Decrypts an encrypted message using AES GCM mode and a 32-byte key.
    The key is padded/truncated to ensure it is exactly 32 bytes.
    """
    key = key[:32].ljust(32).encode()  # Ensure the key is 32 bytes long
    enc = base64.b64decode(encrypted_message.encode())  # Decode the base64 encoded message
    nonce = enc[:16]  # The first 16 bytes are the nonce
    tag = enc[16:32]  # The next 16 bytes are the tag
    ciphertext = enc[32:]  # The remaining bytes are the ciphertext
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)  # Initialize the AES cipher with nonce
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)  # Decrypt the ciphertext and verify the tag
    return decrypted.decode()  # Return the decrypted message

