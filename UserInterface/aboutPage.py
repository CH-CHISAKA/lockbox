from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame
from PyQt6.QtCore import Qt


class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        content_widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        # Add each section wrapped in a styled frame
        layout.addWidget(self._wrap_section(self._create_title_label()))
        layout.addWidget(self._wrap_section(self._create_info_label()))
        layout.addWidget(self._wrap_section(self._create_features_label()))
        layout.addWidget(self._wrap_section(self._create_technical_label()))
        layout.addWidget(self._wrap_section(self._create_contact_label()))

        layout.addStretch()
        content_widget.setLayout(layout)
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        # Global Style
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #0B0F1C, stop:1 #1B263B);
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }
            QScrollArea {
                border: none;
                background: transparent;
            }
            QScrollBar:vertical {
                background: rgba(255, 255, 255, 0.1);
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: rgba(255, 255, 255, 0.3);
                border-radius: 6px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: rgba(255, 255, 255, 0.5);
            }
        """)

    def _wrap_section(self, widget: QWidget) -> QFrame:
        """
        Wraps a given widget in a stylized QFrame section.
        """
        frame = QFrame()
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(widget)
        frame.setLayout(frame_layout)
        frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 20px;
            }
        """)
        return frame

    def _create_title_label(self) -> QLabel:
        label = QLabel("About LockBox")
        label.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 10px;
        """)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setAccessibleName("Title")
        return label

    def _create_info_label(self) -> QLabel:
        info_text = (
            "🛡️ LockBox is a secure messaging application designed for end-to-end encrypted communication.\n"
            "Developed for BBT4102 Cryptography and Network Security.\n\n"
            "Version: 1.0.0\n"
            "Platform: Cross-platform (Windows, macOS, Linux)\n\n"
            "Developers:\n"
            "👨‍💻 138402  Abdikadir Fatmasarah Abdirahman\n"
            "👨‍💻 136948  Wesonga Edward Chisaka\n"
        )
        label = QLabel(info_text)
        label.setWordWrap(True)
        label.setStyleSheet("""
            font-size: 14px; 
            color: #e0e0e0;
            line-height: 1.4;
        """)
        label.setAccessibleName("Information")
        return label

    def _create_features_label(self) -> QLabel:
        features_text = (
            "🚀 Key Features:\n\n"
            "🔐 AES-256-GCM End-to-End Encryption\n"
            "📱 SMS-based OTP Verification\n"
            "🌐 Automatic Network Device Discovery\n"
            "📨 Peer-to-Peer Messaging without servers\n"
            "🖥️ Cross-Platform Compatibility\n"
            "🔒 Zero-Knowledge Message Handling\n"
        )
        label = QLabel(features_text)
        label.setWordWrap(True)
        label.setStyleSheet("""
            font-size: 14px; 
            color: #b0c4de;
            line-height: 1.5;
        """)
        label.setAccessibleName("Features")
        return label

    def _create_technical_label(self) -> QLabel:
        technical_text = (
            "⚙️ Technical Specifications:\n\n"
            "• Encryption: AES-256 with secure key derivation\n"
            "• Framework: PyQt6 for GUI\n"
            "• Network: Peer-to-peer via sockets\n"
            "• OTP Service: SMS Gateway Integration\n"
            "• Languages: Python 3.8+\n"
        )
        label = QLabel(technical_text)
        label.setWordWrap(True)
        label.setStyleSheet("""
            font-size: 14px; 
            color: #98fb98;
            line-height: 1.5;
        """)
        label.setAccessibleName("Technical Info")
        return label

    def _create_contact_label(self) -> QLabel:
        contact_text = (
            "📨 License & Contact:\n\n"
            "This project was developed for academic purposes under BBT4102.\n\n"
            "For more information or support, please contact the development team.\n\n"
            "© 2024 LockBox Team. All rights reserved."
        )
        label = QLabel(contact_text)
        label.setWordWrap(True)
        label.setStyleSheet("""
            font-size: 12px; 
            color: #dcdcdc;
            line-height: 1.4;
            font-style: italic;
        """)
        label.setAccessibleName("Contact")
        return label
