# Import necessary PyQt6 modules
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea  # For UI widgets and layout
from PyQt6.QtCore import Qt  # For alignment and other core Qt enums

# Define a custom QWidget subclass to represent the "About" page
class AboutPage(QWidget):
    def __init__(self):
        """
        Constructor for the AboutPage widget.
        Initializes the parent QWidget and sets up the user interface.
        """
        super().__init__()  # Call the parent class constructor
        self._setup_ui()    # Call method to build and arrange UI elements

    def _setup_ui(self):
        """
        Sets up the layout and adds widgets (title and info label) to the About page.
        """
        # Create main layout for the entire widget
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        # Create content widget for scroll area
        content_widget = QWidget()
        
        # Create a vertical box layout to stack widgets vertically
        layout = QVBoxLayout()
        
        # Set padding/margin around the layout: 24 pixels on each side
        layout.setContentsMargins(24, 24, 24, 24)
        
        # Set spacing between widgets within the layout to 16 pixels
        layout.setSpacing(16)

        # Create the title label (header of the page)
        title_label = self._create_title_label()
        
        # Create the informational label (descriptive text)
        info_label = self._create_info_label()
        
        # Create additional sections
        features_label = self._create_features_label()
        technical_label = self._create_technical_label()
        contact_label = self._create_contact_label()

        # Add the created labels to the layout (in vertical order)
        layout.addWidget(title_label)
        layout.addWidget(info_label)
        layout.addWidget(features_label)
        layout.addWidget(technical_label)
        layout.addWidget(contact_label)
        
        # Add stretch to push content to top
        layout.addStretch()

        # Apply the layout to the content widget
        content_widget.setLayout(layout)
        
        # Set the content widget in the scroll area
        scroll_area.setWidget(content_widget)
        
        # Add scroll area to main layout
        main_layout.addWidget(scroll_area)

        # Apply the layout to the current widget
        self.setLayout(main_layout)

        # Apply linear gradient background with proper PyQt styling
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #141A20, stop:1 #212A34);
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
                margin: 0;
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

    def _create_title_label(self) -> QLabel:
        """
        Creates and returns a QLabel styled as the title for the About page.
        """
        # Initialize the label with the title text
        label = QLabel("About LockBox")
        
        # Apply inline CSS styling to the label: font size, weight, and color
        label.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 10px;
            font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
        """)
        
        # Align the text to the center
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Set an accessible name for assistive technologies
        label.setAccessibleName("Title")
        
        # Return the fully configured label
        return label

    def _create_info_label(self) -> QLabel:
        """
        Creates and returns a QLabel containing detailed information about the app.
        """
        # Define the informational text shown on the About page
        info_text = (
            "A simple, secure messaging application for sending and receiving encrypted messages.\n"
            "Developed as a project for BBT4102 Cryptography and Network Security.\n\n"
            "Version: 1.0.0\n"
            "Platform: Cross-platform (Windows, macOS, Linux)\n\n"
            "By:\n"
            "• 138402  Abdikadir Fatmasarah Abdirahman\n"
            "• 136948  Wesonga Edward Chisaka\n"
        )
        
        # Create a QLabel with the multiline info text
        label = QLabel(info_text)
        
        # Enable word wrapping so long lines break into the next line
        label.setWordWrap(True)
        
        # Apply inline CSS to style the font and text color
        label.setStyleSheet("""
            font-size: 14px; 
            color: #e0e0e0;
            line-height: 1.4;
            margin-bottom: 20px;
            font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
        """)
        
        # Set an accessible name for screen readers and accessibility tools
        label.setAccessibleName("Information")
        
        # Return the configured label
        return label

    def _create_features_label(self) -> QLabel:
        """
        Creates and returns a QLabel containing feature information.
        """
        features_text = (
            "Key Features:\n\n"
            "🔐 End-to-End Encryption: Messages are encrypted using industry-standard AES encryption\n"
            "📱 SMS OTP Verification: Secure one-time passwords sent via SMS for message verification\n"
            "🌐 Network Discovery: Automatic discovery of other LockBox devices on your network\n"
            "📨 Peer-to-Peer Messaging: Direct communication between devices without central servers\n"
            "🖥️ Cross-Platform: Works on Windows, macOS, and Linux systems\n"
            "🔒 Zero-Knowledge: Your messages are never stored unencrypted on any server\n"
        )
        
        label = QLabel(features_text)
        label.setWordWrap(True)
        label.setStyleSheet("""
            font-size: 14px; 
            color: #b0c4de;
            line-height: 1.5;
            margin-bottom: 20px;
            font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
        """)
        label.setAccessibleName("Features")
        
        return label

    def _create_technical_label(self) -> QLabel:
        """
        Creates and returns a QLabel containing technical information.
        """
        technical_text = (
            "Technical Specifications:\n\n"
            "• Encryption: AES-256 with secure key derivation\n"
            "• Framework: PyQt6 for cross-platform GUI\n"
            "• Network: Socket-based peer-to-peer communication\n"
            "• SMS Service: Integration with SMS gateway for OTP delivery\n"
            "• Architecture: Client-server with optional local server mode\n"
            "• Languages: Python 3.8+\n"
        )
        
        label = QLabel(technical_text)
        label.setWordWrap(True)
        label.setStyleSheet("""
            font-size: 14px; 
            color: #98fb98;
            line-height: 1.5;
            margin-bottom: 20px;
            font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
        """)
        label.setAccessibleName("Technical Information")
        
        return label

    def _create_contact_label(self) -> QLabel:
        """
        Creates and returns a QLabel containing contact and license information.
        """
        contact_text = (
            "License & Contact:\n\n"
            "This software is developed for educational purposes as part of the\n"
            "BBT4102 Cryptography and Network Security course.\n\n"
            "For more information or support, please contact the development team.\n\n"
            "© 2024 LockBox Team. All rights reserved.\n"
        )
        
        label = QLabel(contact_text)
        label.setWordWrap(True)
        label.setStyleSheet("""
            font-size: 12px; 
            color: #dcdcdc;
            line-height: 1.4;
            font-style: italic;
            font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
        """)
        label.setAccessibleName("Contact Information")
        
        return label
