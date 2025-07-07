from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox,
    QMessageBox, QTextEdit, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
import re

class SendMessagePage(QWidget):
    def __init__(self, send_callback, encrypt_only_callback=None):
        super().__init__()
        self.send_callback = send_callback
        self.encrypt_only_callback = encrypt_only_callback
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(25)

        # Page title
        title_label = QLabel("📤 Send Secure Message")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #FFFFFF;
                padding: 15px 0;
                border-bottom: 2px solid rgba(255, 255, 255, 0.2);
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title_label)

        # Create input form
        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)
        
        # Message Input Section
        self._create_message_section(form_layout)
        
        # Phone Input Section
        self._create_phone_section(form_layout)
        
        # Peer Device Selection Section
        self._create_device_section(form_layout)
        
        layout.addLayout(form_layout)

        # Button Section
        self._create_button_section(layout)

        # Encrypted Message Display Section
        self._setup_encrypted_message_display(layout)

        self.setLayout(layout)

        # Apply the new gradient styling
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #000B3F,
                    stop: 1 #001DA5
                );
                color: #FFFFFF;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            QLabel {
                color: #FFFFFF;
                font-weight: 500;
                font-size: 14px;
                margin-bottom: 8px;
            }
            
            QLineEdit, QTextEdit, QComboBox {
                background: rgba(255, 255, 255, 0.1);
                color: #FFFFFF;
                border: 2px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                padding: 12px 15px;
                font-size: 14px;
                min-height: 20px;
            }
            
            QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
                border: 2px solid rgba(240, 125, 0, 0.6);
                background: rgba(255, 255, 255, 0.15);
            }
            
            QLineEdit::placeholder, QTextEdit::placeholder {
                color: rgba(255, 255, 255, 0.6);
            }
            
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            
            QComboBox::down-arrow {
                image: none;
                border: 2px solid #FFFFFF;
                width: 8px;
                height: 8px;
                border-top: none;
                border-right: none;
                transform: rotate(-45deg);
                margin-right: 10px;
            }
            
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #F07D00,
                    stop: 1 #8A4800
                );
                color: white;
                border: none;
                border-radius: 10px;
                padding: 15px 25px;
                font-weight: 600;
                font-size: 14px;
                min-height: 25px;
            }
            
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #FF8A00,
                    stop: 1 #A05000
                );
                transform: translateY(-2px);
            }
            
            QPushButton:pressed {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #D06D00,
                    stop: 1 #743F00
                );
            }
        """)

    def _create_message_section(self, layout):
        """Create the message input section"""
        msg_label = QLabel("💬 Message Content:")
        layout.addWidget(msg_label)
        
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Enter your secure message here...")
        layout.addWidget(self.message_input)

    def _create_phone_section(self, layout):
        """Create the phone input section"""
        phone_label = QLabel("📱 Receiver Phone Number:")
        layout.addWidget(phone_label)
        
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("e.g., 0712345678 or +254712345678")
        layout.addWidget(self.phone_input)
        
        # Add phone format help text
        help_text = QLabel("📋 Supported formats: 07XXXXXXXX, 011XXXXXXX, +2547XXXXXXXX, +25411XXXXXXX")
        help_text.setStyleSheet("""
            QLabel {
                color: rgba(255, 255, 255, 0.7);
                font-size: 12px;
                font-style: italic;
                margin-top: 5px;
                padding: 8px 12px;
                background: rgba(255, 255, 255, 0.05);
                border-radius: 6px;
                border-left: 3px solid rgba(240, 125, 0, 0.6);
            }
        """)
        layout.addWidget(help_text)

    def _create_device_section(self, layout):
        """Create the device selection section"""
        device_label = QLabel("🌐 Target Device:")
        layout.addWidget(device_label)
        
        self.ip_dropdown = QComboBox()
        self.ip_dropdown.setEditable(False)
        layout.addWidget(self.ip_dropdown)

    def _create_button_section(self, layout):
        """Create the action buttons section"""
        button_frame = QFrame()
        button_frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 20px;
                margin: 10px 0;
            }
        """)
        
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        
        # Send button
        send_button = QPushButton("🚀 Send Secure Message")
        send_button.clicked.connect(self.validate_and_send)
        send_button.setToolTip("Encrypt and send message to selected device")
        
        # Encrypt only button
        encrypt_only_button = QPushButton("🔐 Encrypt Only")
        encrypt_only_button.clicked.connect(self.validate_and_encrypt_only)
        encrypt_only_button.setToolTip("Encrypt message without sending (for testing)")
        encrypt_only_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #6C757D,
                    stop: 1 #495057
                );
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #7D8A96,
                    stop: 1 #5A6269
                );
            }
        """)
        
        button_layout.addWidget(send_button)
        button_layout.addWidget(encrypt_only_button)
        
        button_frame.setLayout(button_layout)
        layout.addWidget(button_frame)

    def _setup_encrypted_message_display(self, layout):
        """Create the encrypted message display section"""
        self.encrypted_label = QLabel("🔐 Encrypted Message (Ready to Copy):")
        self.encrypted_label.setVisible(False)
        self.encrypted_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: 600;
                color: #FFFFFF;
                margin-top: 20px;
                margin-bottom: 10px;
                padding: 10px;
                background: rgba(40, 167, 69, 0.2);
                border-radius: 8px;
                border-left: 4px solid #28A745;
            }
        """)
        layout.addWidget(self.encrypted_label)

        self.encrypted_output = QTextEdit()
        self.encrypted_output.setReadOnly(True)
        self.encrypted_output.setVisible(False)
        self.encrypted_output.setMinimumHeight(120)
        self.encrypted_output.setStyleSheet("""
            QTextEdit {
                background: rgba(255, 255, 255, 0.08);
                border: 2px solid rgba(40, 167, 69, 0.4);
                color: #FFFFFF;
                font-family: 'Courier New', monospace;
                font-size: 12px;
                line-height: 1.4;
                padding: 15px;
            }
        """)
        layout.addWidget(self.encrypted_output)

    def set_ip_choices(self, device_list):
        """Update the device list in the dropdown menu."""
        self.ip_dropdown.clear()
        self.device_map = {}
        
        if not device_list or device_list[0].get('device_name') == 'No devices found':
            self.ip_dropdown.addItem("🔍 No devices found - Click to refresh")
            self.device_map["🔍 No devices found - Click to refresh"] = ""
        else:
            for entry in device_list:
                name = entry['device_name']
                ip = entry['ip']
                display_name = f"📱 {name} ({ip})"
                self.device_map[display_name] = ip
                self.ip_dropdown.addItem(display_name)

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
            QMessageBox.warning(self, "❌ Invalid Phone Number",
                "Please enter a valid Kenyan phone number.\n\n" +
                "Supported formats:\n" +
                "• 07XXXXXXXX (legacy format)\n" +
                "• 011XXXXXXX (current format)\n" +
                "• +2547XXXXXXXX (international legacy)\n" +
                "• +25411XXXXXXX (international current)")
            return
        message, phone, ip = self.get_inputs()
        if not message:
            QMessageBox.warning(self, "❌ Empty Message", "Please enter a message to send.")
            return
        if not ip:
            QMessageBox.warning(self, "❌ No Device Selected", "Please select a target device.")
            return
        self.send_callback()

    def validate_and_encrypt_only(self):
        phone = self.phone_input.text().strip()
        if not self._is_valid_phone_number(phone):
            QMessageBox.warning(self, "❌ Invalid Phone Number",
                "Please enter a valid Kenyan phone number.\n\n" +
                "Supported formats:\n" +
                "• 07XXXXXXXX (legacy format)\n" +
                "• 011XXXXXXX (current format)\n" +
                "• +2547XXXXXXXX (international legacy)\n" +
                "• +25411XXXXXXX (international current)")
            return
        message, phone, ip = self.get_inputs()
        if not message:
            QMessageBox.warning(self, "❌ Empty Message", "Please enter a message to encrypt.")
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
        """Display the encrypted message with enhanced styling"""
        self.encrypted_label.setVisible(True)
        self.encrypted_output.setVisible(True)
        
        # Format the encrypted message nicely
        formatted_msg = f"""Encrypted Message Generated Successfully!

Encryption Details:
• Algorithm: AES-256-GCM
• Mode: Galois/Counter Mode
• Key Source: OTP sent via SMS
• Message Length: {len(encrypted_msg)} characters

Encrypted Content:
{encrypted_msg}

📋 Copy the encrypted content above and share it securely with your recipient."""
        
        self.encrypted_output.setPlainText(formatted_msg)
