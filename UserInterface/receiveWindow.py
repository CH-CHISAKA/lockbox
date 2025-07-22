from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QScrollArea
)
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator


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
        title_label.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            background: transparent;
        """)
        layout.addWidget(title_label)

        # Instructions
        instructions = QLabel(
            "Enter your One-Time Password or paste the encrypted message to decrypt it securely."
        )
        instructions.setWordWrap(True)
        instructions.setStyleSheet("""
            QLabel {
                color: rgba(255, 255, 255, 0.8);
                font-size: 14px;
                padding: 15px;
                background: rgba(255, 255, 255, 0.05);
                border-radius: 10px;
                border-left: 4px solid rgba(240, 125, 0, 0.6);
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(instructions)

        # OTP Input
        otp_label = QLabel("Enter OTP:")
        otp_label.setStyleSheet("background: transparent;")
        self.otp_input = QLineEdit()
        self.otp_input.setPlaceholderText("Enter the OTP received via SMS...")
        self.otp_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.otp_input.setMaxLength(6)
        otp_regex = QRegularExpression("^[A-Z0-9]{0,6}$")
        self.otp_input.setValidator(QRegularExpressionValidator(otp_regex))
        self.otp_input.setStyleSheet("padding: 6px;")
        layout.addWidget(otp_label)
        layout.addWidget(self.otp_input)

        self.otp_input.textChanged.connect(self._on_otp_input_changed)

        # Show/Hide OTP Button
        self.show_otp_btn = QPushButton("👁️ Show OTP")
        self.show_otp_btn.clicked.connect(self.toggle_otp_visibility)
        self.show_otp_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #6C757D,
                    stop: 1 #495057
                );
                padding: 8px 15px;
                font-size: 12px;
                max-width: 120px;
                margin-bottom: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #7D8A96,
                    stop: 1 #5A6269
                );
            }
        """)
        layout.addWidget(self.show_otp_btn, alignment=Qt.AlignmentFlag.AlignLeft)

        # Encrypted Message Input
        enc_label = QLabel("Paste Encrypted Message:")
        enc_label.setStyleSheet("background: transparent;")
        self.encrypted_input = QTextEdit()
        self.encrypted_input.setPlaceholderText("Paste the encrypted message content here...")
        self.encrypted_input.setStyleSheet("padding: 6px;")
        layout.addWidget(enc_label)
        layout.addWidget(self.encrypted_input)

        self.encrypted_input.textChanged.connect(self._on_encrypted_input_changed)

        # Decrypt Button
        self.decrypt_button = QPushButton("Decrypt Message")
        self.decrypt_button.setEnabled(False)
        self.decrypt_button.clicked.connect(self.decrypt_callback)
        self.decrypt_button.setStyleSheet("""
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
                max-height: 30px;
                max-width: 120px;
            }
            QPushButton:disabled {
                background: gray;
                color: lightgray;
            }
            QPushButton:hover:!disabled {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #FF8A00,
                    stop: 1 #A05000
                );
                transform: translateY(-2px);
            }
            QPushButton:pressed:!disabled {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #D06D00,
                    stop: 1 #743F00
                );
            }
        """)
        layout.addWidget(self.decrypt_button, alignment=Qt.AlignmentFlag.AlignRight)

        # Background gradient
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #141A20,
                    stop: 1 #212A34
                );
            }
        """)

        # Tips section
        tips_label = QLabel("💡 Security Tips:")
        tips_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: 600;
                color: #FFFFFF;
                margin-top: 20px;
                margin-bottom: 10px;
                background-color: transparent;
            }
        """)
        layout.addWidget(tips_label)

        tips_text = QLabel("""• Keep your OTP confidential and never share it
• Verify the sender before entering your OTP
• Delete the OTP message after successful decryption
• If decryption fails, verify your OTP and message content""")
        tips_text.setWordWrap(True)
        tips_text.setStyleSheet("""
            QLabel {
                color: rgba(255, 255, 255, 0.7);
                font-size: 13px;
                padding: 15px;
                background: rgba(0, 11, 63, 0.3);
                border-radius: 8px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                line-height: 1.4;
            }
        """)

        # Make tips_text scrollable with fixed height
        tips_scroll = QScrollArea()
        tips_scroll.setWidgetResizable(True)
        tips_scroll.setFixedHeight(120)  # You can adjust height here
        tips_scroll.setWidget(tips_text)
        layout.addWidget(tips_scroll)

        layout.addStretch()
        self.setLayout(layout)

    def toggle_otp_visibility(self):
        if self.otp_input.echoMode() == QLineEdit.EchoMode.Password:
            self.otp_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_otp_btn.setText("🙈 Hide OTP")
        else:
            self.otp_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.show_otp_btn.setText("👁️ Show OTP")

    def _on_otp_input_changed(self, text: str):
        # Force auto-capitalization
        current_cursor = self.otp_input.cursorPosition()
        clean_text = ''.join(c.upper() for c in text if c.isalnum())
        if text != clean_text:
            self.otp_input.setText(clean_text)
            self.otp_input.setCursorPosition(min(current_cursor, len(clean_text)))

        self._update_decrypt_button_state()

    def _on_encrypted_input_changed(self):
        self._update_decrypt_button_state()

    def _update_decrypt_button_state(self):
        otp = self.get_otp()
        enc = self.get_encrypted_message()

        # Enable only if OTP is full (6 chars) or Encrypted message is non-empty
        otp_valid = len(otp) == 6
        enc_valid = len(enc) > 0

        self.decrypt_button.setEnabled(otp_valid or enc_valid)

    def get_otp(self) -> str:
        return self.otp_input.text().strip()

    def get_encrypted_message(self) -> str:
        return self.encrypted_input.toPlainText().strip()
