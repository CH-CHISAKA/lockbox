# Import necessary PyQt6 modules
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFrame
)
from PyQt6.QtCore import Qt

class ReceiveMessagePage(QWidget):
    def __init__(self, decrypt_callback):
        super().__init__()
        self.decrypt_callback = decrypt_callback
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(25)

        # Page title
        title_label = QLabel("📥 Receive Secure Message")
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

        # Instructions section
        instructions = QLabel("🔓 Enter your OTP and paste the encrypted message to decrypt it securely.")
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

        # Input form frame
        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 25px;
                margin: 10px 0;
            }
        """)
        
        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)

        # OTP Input Section
        otp_label = QLabel("🔑 One-Time Password (OTP):")
        otp_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: 600;
                color: #FFFFFF;
                margin-bottom: 8px;
            }
        """)
        form_layout.addWidget(otp_label)

        self.otp_input = QLineEdit()
        self.otp_input.setPlaceholderText("Enter the OTP received via SMS...")
        self.otp_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addWidget(self.otp_input)

        # Show/Hide OTP button
        otp_toggle_layout = QVBoxLayout()
        otp_toggle_layout.setSpacing(10)
        
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
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #7D8A96,
                    stop: 1 #5A6269
                );
            }
        """)
        otp_toggle_layout.addWidget(self.show_otp_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        form_layout.addLayout(otp_toggle_layout)

        # Encrypted Message Input Section
        enc_label = QLabel("📄 Encrypted Message:")
        enc_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: 600;
                color: #FFFFFF;
                margin-bottom: 8px;
            }
        """)
        form_layout.addWidget(enc_label)

        self.encrypted_input = QTextEdit()
        self.encrypted_input.setPlaceholderText("Paste the encrypted message content here...")
        self.encrypted_input.setMinimumHeight(120)
        self.encrypted_input.setMaximumHeight(200)
        form_layout.addWidget(self.encrypted_input)

        form_frame.setLayout(form_layout)
        layout.addWidget(form_frame)

        # Action button section
        button_frame = QFrame()
        button_frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 255, 255, 0.03);
                border-radius: 12px;
                padding: 20px;
                margin: 15px 0;
            }
        """)
        
        button_layout = QVBoxLayout()
        
        # Decrypt Button
        decrypt_button = QPushButton("🔓 Decrypt Message")
        decrypt_button.clicked.connect(self.decrypt_callback)
        decrypt_button.setToolTip("Decrypt the message using your OTP")
        button_layout.addWidget(decrypt_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        button_frame.setLayout(button_layout)
        layout.addWidget(button_frame)

        # Tips section
        tips_label = QLabel("💡 Security Tips:")
        tips_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: 600;
                color: #FFFFFF;
                margin-top: 20px;
                margin-bottom: 10px;
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
        layout.addWidget(tips_text)

        layout.addStretch()
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
            }
            
            QLineEdit, QTextEdit {
                background: rgba(255, 255, 255, 0.1);
                color: #FFFFFF;
                border: 2px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                padding: 12px 15px;
                font-size: 14px;
                min-height: 20px;
            }
            
            QLineEdit:focus, QTextEdit:focus {
                border: 2px solid rgba(240, 125, 0, 0.6);
                background: rgba(255, 255, 255, 0.15);
            }
            
            QLineEdit::placeholder, QTextEdit::placeholder {
                color: rgba(255, 255, 255, 0.6);
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
                min-width: 200px;
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

    def toggle_otp_visibility(self):
        """Toggle OTP field visibility between password and normal mode"""
        if self.otp_input.echoMode() == QLineEdit.EchoMode.Password:
            self.otp_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_otp_btn.setText("🙈 Hide OTP")
        else:
            self.otp_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.show_otp_btn.setText("👁️ Show OTP")

    def get_otp(self) -> str:
        return self.otp_input.text().strip()

    def get_encrypted_message(self) -> str:
        return self.encrypted_input.toPlainText().strip()
