from UserInterface.mainWindow import MainWindow  
from UserInterface.sendWindow import SendMessagePage  
from UserInterface.receiveWindow import ReceiveMessagePage  
from messaging.sms import generate_otp, send_otp_via_sms
from networking.client import send_secure_message_to_peer, read_secure_message_from_local
from crypto import encrypt_message, decrypt_message
from PyQt6.QtWidgets import QMessageBox
import subprocess, sys, os, signal
from networking.network_scan import scan_network_for_servers

class SecureMessengerController:
    def __init__(self, main_window):
        """
        Initializes the SecureMessengerController with the provided main window.
        Sets up pages for sending and receiving messages and initializes server process.
        """
        self.main_window = main_window
        self.send_page = SendMessagePage(self.send_secure_message, self.encrypt_only_message)
        self.receive_page = ReceiveMessagePage(self.read_secure_message)
        self.server_process = None

    def show_send_page(self):
        """
        Displays the SendMessagePage, populating the device dropdown with the available servers.
        If no devices are found, displays a placeholder entry.
        """
        device_list = scan_network_for_servers()
        if not device_list:
            device_list = [{'device_name': 'No devices found', 'ip': ''}]
        self.send_page.set_ip_choices(device_list)
        self.main_window.set_central_widget(self.send_page)

    def show_receive_page(self):
        """
        Displays the ReceiveMessagePage for reading encrypted messages.
        """
        self.main_window.set_central_widget(self.receive_page)

    def send_secure_message(self):
        """
        Validates inputs and sends a secure message after generating and sending an OTP via SMS.
        """
        message, phone, ip = self.send_page.get_inputs()
        if not message or not phone or not ip:
            QMessageBox.warning(self.main_window, "Input Error", "All fields are required.")
            return

        otp = generate_otp()
        
        # Send OTP via SMS and proceed only if successful
        sent = send_otp_via_sms(phone, otp)
        if not sent:
            QMessageBox.critical(self.main_window, "Error", "Failed to send OTP via SMS.")
            return
        
        try:
            # Attempt to send the LockBox message to the peer
            status = send_secure_message_to_peer(message, otp, ip)
            if status == 200:
                QMessageBox.information(self.main_window, "Success", "Message sent!")
            else:
                QMessageBox.critical(self.main_window, "Error", f"Status: {status}")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Error", str(e))

    def encrypt_only_message(self):
        """
        Encrypts the message and sends OTP via SMS without sending the message, for testing purposes.
        """
        message = self.send_page.message_input.text()
        phone = self.send_page.phone_input.text()
        if not message or not phone:
            QMessageBox.warning(self.main_window, "Input Error", "Message and phone are required.")
            return

        otp = generate_otp()
        
        sent = send_otp_via_sms(phone, otp)
        if not sent:
            QMessageBox.critical(self.main_window, "Error", "Failed to send OTP via SMS.")
            return
        
        try:
            # Attempt to encrypt the message and display it
            encrypted = encrypt_message(message, otp)
            self.send_page.show_encrypted_message(encrypted)
            QMessageBox.information(self.main_window, "Encrypted", "Message encrypted and OTP sent via SMS.")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Error", str(e))

    def read_secure_message(self):
        """
        Reads an encrypted message by using the OTP entered by the user and decrypting the message.
        """
        otp = self.receive_page.get_otp()
        encrypted_msg = self.receive_page.get_encrypted_message()
        if not otp:
            return

        try:
            # Attempt to decrypt the message or read from local storage
            if encrypted_msg:
                msg = decrypt_message(encrypted_msg, otp)
            else:
                msg = read_secure_message_from_local(otp)
            
            if msg:
                QMessageBox.information(self.main_window, "Decrypted", msg)
            else:
                raise Exception("No message or bad OTP.")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Error", "Failed to decrypt\n" + str(e))

    def start_server(self):
        """
        Starts the local server in a separate process. Displays status in the main window.
        """
        if self.server_process is None:
            self.server_process = subprocess.Popen(
    ["python3", "networking/server.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
            self.main_window.update_server_status(True)
            QMessageBox.information(self.main_window, "Server", "Local server started.")

    def stop_server(self):
        """
        Stops the running server and updates the status in the main window.
        """
        if self.server_process:
            if sys.platform == "win32":
                self.server_process.terminate()
            else:
                os.kill(self.server_process.pid, signal.SIGTERM)
            self.server_process.wait()
            self.server_process = None
            self.main_window.update_server_status(False)
            QMessageBox.information(self.main_window, "Server", "Server stopped.")
