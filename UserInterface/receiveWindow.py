# Import necessary PyQt6 modules
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
)
from PyQt6.QtCore import Qt

class ReceiveMessagePage(QWidget):
    def __init__(self, decrypt_callback):
        super().__init__()
        self.decrypt_callback = decrypt_callback
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        # Title
        title_label = QLabel("Receive Secure Message")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title_label)

        # OTP Input
        otp_label = QLabel("Enter OTP:")
        self.otp_input = QLineEdit()
        self.otp_input.setPlaceholderText("One-Time Password")
        self.otp_input.setStyleSheet("padding: 6px;")
        layout.addWidget(otp_label)
        layout.addWidget(self.otp_input)

        # Encrypted Message Input
        enc_label = QLabel("Paste Encrypted Message:")
        self.encrypted_input = QTextEdit()
        self.encrypted_input.setPlaceholderText("Encrypted message here...")
        self.encrypted_input.setStyleSheet("padding: 6px;")
        layout.addWidget(enc_label)
        layout.addWidget(self.encrypted_input)

        # Decrypt Button
        decrypt_button = QPushButton("Decrypt Message")
        decrypt_button.clicked.connect(self.decrypt_callback)
        decrypt_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                font-weight: bold;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(decrypt_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

        # Apply linear gradient background
        self.setStyleSheet("""
            QWidget {
                background: linear-gradient(to bottom, #141A20, #212A34);
            }
        """)

    def get_otp(self) -> str:
        return self.otp_input.text().strip()

    def get_encrypted_message(self) -> str:
        return self.encrypted_input.toPlainText().strip()
