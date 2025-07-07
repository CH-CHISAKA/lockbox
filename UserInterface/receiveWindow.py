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

        # Apply linear gradient background with proper PyQt syntax
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #141A20, stop:1 #212A34);
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }
            QLabel {
                color: #ffffff;
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }
            QLineEdit, QTextEdit {
                background-color: #2e3b47;
                color: #ffffff;
                border: 1px solid #4a5a6a;
                border-radius: 4px;
                padding: 8px;
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }
            QLineEdit:focus, QTextEdit:focus {
                border: 2px solid #4CAF50;
            }
            QPushButton {
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }
        """)

    def get_otp(self) -> str:
        return self.otp_input.text().strip()

    def get_encrypted_message(self) -> str:
        return self.encrypted_input.toPlainText().strip()
