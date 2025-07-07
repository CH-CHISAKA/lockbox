from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import secrets
import string

def generate_secure_key(length=32):
    """
    Generates a cryptographically secure random key.
    
    Args:
        length (int): Length of the key in bytes (default: 32 for AES-256)
    
    Returns:
        str: Base64 encoded secure random key
    """
    key_bytes = get_random_bytes(length)
    return base64.b64encode(key_bytes).decode()

def generate_password_based_key(password, salt=None, iterations=100000):
    """
    Derives a secure key from a user password using PBKDF2.
    
    Args:
        password (str): User password
        salt (bytes): Salt for key derivation (generates random if None)
        iterations (int): Number of PBKDF2 iterations
    
    Returns:
        tuple: (base64_encoded_key, base64_encoded_salt)
    """
    if salt is None:
        salt = get_random_bytes(16)
    
    key = PBKDF2(password, salt, 32, count=iterations, hmac_hash_module=SHA256)
    return base64.b64encode(key).decode(), base64.b64encode(salt).decode()

def generate_random_password(length=16):
    """
    Generates a secure random password.
    
    Args:
        length (int): Length of the password
    
    Returns:
        str: Secure random password
    """
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def generate_rsa_keypair(key_size=2048):
    """
    Generates an RSA key pair for asymmetric encryption.
    
    Args:
        key_size (int): Size of the RSA key in bits
    
    Returns:
        tuple: (private_key_pem, public_key_pem)
    """
    key = RSA.generate(key_size)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    return private_key.decode(), public_key.decode()

def encrypt_with_rsa(message, public_key_pem):
    """
    Encrypts a message using RSA public key.
    
    Args:
        message (str): Message to encrypt
        public_key_pem (str): PEM encoded public key
    
    Returns:
        str: Base64 encoded encrypted message
    """
    public_key = RSA.import_key(public_key_pem.encode())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted = cipher_rsa.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_with_rsa(encrypted_message, private_key_pem):
    """
    Decrypts a message using RSA private key.
    
    Args:
        encrypted_message (str): Base64 encoded encrypted message
        private_key_pem (str): PEM encoded private key
    
    Returns:
        str: Decrypted message
    """
    private_key = RSA.import_key(private_key_pem.encode())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    encrypted_bytes = base64.b64decode(encrypted_message.encode())
    decrypted = cipher_rsa.decrypt(encrypted_bytes)
    return decrypted.decode()

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

