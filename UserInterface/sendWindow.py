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

        # Button Layout
        button_layout = QHBoxLayout()
        self._add_action_buttons(button_layout)
        layout.addLayout(button_layout)

        # Encrypted Message Display
        self._setup_encrypted_message_display(layout)

        self.setLayout(layout)

        # Styling
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
            QLineEdit, QTextEdit {
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
        self.device_map = {}
        for entry in device_list:
            name = entry['device_name']
            ip = entry['ip']
            self.device_map[name] = ip
            self.ip_dropdown.addItem(name)

    def get_inputs(self):
        """Retrieve user inputs for message sending."""
        message = self.message_input.text().strip()
        phone = self.normalize_kenyan_number(self.phone_input.text().strip())
        device_name = self.ip_dropdown.currentText()
        ip = self.device_map.get(device_name, device_name)
        return message, phone, ip

    def validate_and_send(self):
        phone = self.phone_input.text().strip()
        if not self._is_valid_phone_number(phone):
            QMessageBox.warning(self, "Invalid Phone Number",
                "Please enter a valid Kenyan phone number (e.g., 07XXXXXXXX, 011XXXXXXX, +2547XXXXXXXX, +25411XXXXXXX).")
            return
        message, phone, ip = self.get_inputs()
        if not message:
            QMessageBox.warning(self, "Empty Message", "Please enter a message to send.")
            return
        self.send_callback()

    def validate_and_encrypt_only(self):
        phone = self.phone_input.text().strip()
        if not self._is_valid_phone_number(phone):
            QMessageBox.warning(self, "Invalid Phone Number",
                "Please enter a valid Kenyan phone number (e.g., 07XXXXXXXX, 011XXXXXXX, +2547XXXXXXXX, +25411XXXXXXX).")
            return
        message, phone, ip = self.get_inputs()
        if not message:
            QMessageBox.warning(self, "Empty Message", "Please enter a message to encrypt.")
            return
        if self.encrypt_only_callback:
            self.encrypt_only_callback()

    def _is_valid_phone_number(self, phone: str) -> bool:
        """Validates Kenyan phone numbers including all valid prefixes."""

        # Valid 07xx and 01xx prefixes
        valid_prefixes = (
            # 07xx legacy
            "070", "071", "072", "073", "0740", "0741", "0742", "0743", "0745", "0746",
            "0748", "0757", "0758", "0759", "0768", "0769", "0770", "0771", "0772",
            "0780", "0781", "0782", "0783", "0784", "0785", "0786", "0787", "0788",
            "0790", "0791", "0792", "0793", "0794", "0795", "0796", "0797", "0798", "0799",
            # 01xx current
            "0100", "0101", "0102", "0103", "0104", "0105", "0106", "0107", "0108", "0109",
            "0110", "0111", "0112", "0113", "0114", "0115", "0116", "0117", "0118", "0119"
        )

        phone = phone.strip()

        # Local: 0XXXXXXXXX
        if phone.startswith("0") and len(phone) == 10:
            return any(phone.startswith(p) for p in valid_prefixes)

        # International: +254XXXXXXXXX
        elif phone.startswith("+254") and len(phone) == 13:
            suffix = phone[4:]
            return any(suffix.startswith(p[1:]) for p in valid_prefixes)  # compare with stripped prefix

        return False

    def normalize_kenyan_number(self, number: str) -> str:
        """Converts local Kenyan numbers to +254 format (E.164)."""
        number = number.strip()
        if number.startswith("0"):
            return "+254" + number[1:]
        elif number.startswith("+254"):
            return number
        else:
            return number

    def show_encrypted_message(self, encrypted_msg: str):
        self.encrypted_label.setVisible(True)
        self.encrypted_output.setVisible(True)
        self.encrypted_output.setPlainText(encrypted_msg)
