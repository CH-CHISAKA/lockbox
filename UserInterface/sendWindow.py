from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, 
    QMessageBox, QTextEdit, QHBoxLayout
)
import re


class SendMessagePage(QWidget):
    def __init__(self, send_callback, encrypt_only_callback=None):
        super().__init__()
        self.send_callback = send_callback
        self.encrypt_only_callback = encrypt_only_callback
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()

        # Message Input
        layout.addWidget(QLabel("Message:"))
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Enter your message here...")
        layout.addWidget(self.message_input)

        # Phone Input
        layout.addWidget(QLabel("Receiver Phone:"))
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter receiver's phone number")
        layout.addWidget(self.phone_input)

        # Peer Device Selection
        layout.addWidget(QLabel("Peer Device:"))
        self.ip_dropdown = QComboBox()
        layout.addWidget(self.ip_dropdown)

        # Button Layout (Send and Encrypt Only)
        button_layout = QHBoxLayout()
        self._add_action_buttons(button_layout)
        layout.addLayout(button_layout)

        # Encrypted Message Display
        self._setup_encrypted_message_display(layout)

        self.setLayout(layout)

        # Apply linear gradient background and button styling
        self.setStyleSheet("""
            QWidget {
                background: linear-gradient(to bottom, #141A20, #212A34);
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                font-weight: bold;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                color: white;
            }
            QLineEdit {
                background-color: #2e3b47;
                color: white;
                padding: 6px;
                border-radius: 4px;
            }
            QTextEdit {
                background-color: #2e3b47;
                color: white;
                padding: 6px;
                border-radius: 4px;
            }
        """)

    def _add_action_buttons(self, button_layout):
        send_button = QPushButton("Send Secure Message")
        send_button.clicked.connect(self.validate_and_send)
        button_layout.addWidget(send_button)

        encrypt_only_button = QPushButton("Encrypt Only (Don't Send)")
        encrypt_only_button.clicked.connect(self.validate_and_encrypt_only)
        button_layout.addWidget(encrypt_only_button)

    def _setup_encrypted_message_display(self, layout):
        self.encrypted_label = QLabel("Encrypted Message (copy below):")
        self.encrypted_label.setVisible(False)
        layout.addWidget(self.encrypted_label)

        self.encrypted_output = QTextEdit()
        self.encrypted_output.setReadOnly(True)
        self.encrypted_output.setVisible(False)
        layout.addWidget(self.encrypted_output)

    def set_ip_choices(self, device_list):
        """Update the device list in the dropdown menu."""
        self.ip_dropdown.clear()
        self.device_map = {}  # device_name -> ip
        for entry in device_list:
            name = entry['device_name']
            ip = entry['ip']
            self.device_map[name] = ip
            self.ip_dropdown.addItem(name)

    def get_inputs(self):
        """Retrieve user inputs for message sending."""
        message = self.message_input.text().strip()
        phone = self.phone_input.text().strip()
        device_name = self.ip_dropdown.currentText()
        ip = self.device_map.get(device_name, device_name)
        return message, phone, ip

    def validate_and_send(self):
        """Validate input and trigger the send callback."""
        if not self._is_valid_phone_number(self.phone_input.text()):
            QMessageBox.warning(self, "Invalid Phone Number", "Please enter a valid Kenyan phone number (e.g., 0712345678 or +254712345678).")
            return
        message, phone, ip = self.get_inputs()
        if not message:
            QMessageBox.warning(self, "Empty Message", "Please enter a message to send.")
            return
        self.send_callback()

    def validate_and_encrypt_only(self):
        """Validate input and trigger the encrypt-only callback."""
        if not self._is_valid_phone_number(self.phone_input.text()):
            QMessageBox.warning(self, "Invalid Phone Number", "Please enter a valid Kenyan phone number (e.g., 0712345678 or +254712345678).")
            return
        message, phone, ip = self.get_inputs()
        if not message:
            QMessageBox.warning(self, "Empty Message", "Please enter a message to encrypt.")
            return
        if self.encrypt_only_callback:
            self.encrypt_only_callback()

    def _is_valid_phone_number(self, phone: str) -> bool:
        """Validates Kenyan phone numbers (starts with 07 or +2547 and has 10/13 digits)."""
        pattern = r"^(07\d{8}|(\+2547\d{8}))$"
        return bool(re.match(pattern, phone))

    def show_encrypted_message(self, encrypted_msg: str):
        """Display the encrypted message in the UI."""
        self.encrypted_label.setVisible(True)
        self.encrypted_output.setVisible(True)
        self.encrypted_output.setPlainText(encrypted_msg)
