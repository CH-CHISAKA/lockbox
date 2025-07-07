# Import necessary PyQt6 modules
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout  # For UI widgets and layout
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
        # Create a vertical box layout to stack widgets vertically
        layout = QVBoxLayout()
        
        # Set padding/margin around the layout: 30 pixels on each side for better spacing
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Set spacing between widgets within the layout to 25 pixels
        layout.setSpacing(25)

        # Create the title section
        title_section = self._create_title_section()
        layout.addWidget(title_section)

        # Create the main info section
        info_section = self._create_info_section()
        layout.addWidget(info_section)

        # Create the features section
        features_section = self._create_features_section()
        layout.addWidget(features_section)

        # Create the developers section
        developers_section = self._create_developers_section()
        layout.addWidget(developers_section)

        # Add stretch to push content to top
        layout.addStretch()

        # Apply the layout to the current widget
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
                background: transparent;
            }
            
            QFrame {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
        """)

    def _create_title_section(self) -> QFrame:
        """
        Creates and returns a title section with app icon and name.
        """
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 255, 255, 0.08);
                border-radius: 20px;
                border: 2px solid rgba(255, 255, 255, 0.15);
                padding: 25px;
                margin-bottom: 15px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # App icon and title
        title_label = QLabel("🔒 LockBox")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #FFFFFF;
                padding: 10px 0;
            }
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Subtitle
        subtitle_label = QLabel("Secure Messaging Application")
        subtitle_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                color: rgba(255, 255, 255, 0.8);
                font-weight: 500;
            }
        """)
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Version info
        version_label = QLabel("Version 2.0 - Enhanced Edition")
        version_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: rgba(255, 255, 255, 0.6);
                font-style: italic;
                margin-top: 5px;
            }
        """)
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addWidget(version_label)
        
        frame.setLayout(layout)
        return frame

    def _create_info_section(self) -> QFrame:
        """
        Creates and returns a QFrame containing general information about the app.
        """
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                padding: 20px;
                margin: 10px 0;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Description
        description_text = (
            "🛡️ LockBox is a comprehensive secure messaging application designed for "
            "end-to-end encrypted communications. Built with advanced cryptographic "
            "protocols and modern security practices."
        )
        
        description_label = QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setStyleSheet("""
            QLabel {
                font-size: 15px;
                color: rgba(255, 255, 255, 0.9);
                line-height: 1.5;
                padding: 15px;
                background: rgba(240, 125, 0, 0.1);
                border-radius: 10px;
                border-left: 4px solid rgba(240, 125, 0, 0.6);
            }
        """)
        
        # Purpose
        purpose_label = QLabel("📚 Academic Project - BBT4102 Cryptography and Network Security")
        purpose_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: rgba(255, 255, 255, 0.7);
                padding: 10px;
                background: rgba(0, 11, 63, 0.3);
                border-radius: 8px;
                font-weight: 500;
            }
        """)
        purpose_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(description_label)
        layout.addWidget(purpose_label)
        
        frame.setLayout(layout)
        return frame

    def _create_features_section(self) -> QFrame:
        """
        Creates and returns a features section highlighting key capabilities.
        """
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                padding: 20px;
                margin: 10px 0;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(12)
        
        # Features title
        features_title = QLabel("🚀 Key Features")
        features_title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #FFFFFF;
                margin-bottom: 15px;
                padding-bottom: 10px;
                border-bottom: 2px solid rgba(255, 255, 255, 0.2);
            }
        """)
        layout.addWidget(features_title)
        
        # Feature items
        features = [
            "🔐 AES-256-GCM End-to-End Encryption",
            "🔑 RSA Key Pair Generation & Management",
            "📱 SMS-based OTP Authentication",
            "🌐 Network Device Discovery",
            "💻 Cross-Platform Compatibility",
            "🛡️ Advanced Security Protocols",
            "📡 Real-time Secure Communication",
            "🎨 Modern Gradient UI Design"
        ]
        
        for feature in features:
            feature_label = QLabel(feature)
            feature_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    color: rgba(255, 255, 255, 0.85);
                    padding: 8px 15px;
                    background: rgba(255, 255, 255, 0.03);
                    border-radius: 6px;
                    border-left: 3px solid rgba(240, 125, 0, 0.5);
                    margin: 2px 0;
                }
            """)
            layout.addWidget(feature_label)
        
        frame.setLayout(layout)
        return frame

    def _create_developers_section(self) -> QFrame:
        """
        Creates and returns a developers section with team information.
        """
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 255, 255, 0.08);
                border-radius: 15px;
                border: 2px solid rgba(255, 255, 255, 0.15);
                padding: 25px;
                margin: 15px 0;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Developers title
        dev_title = QLabel("👥 Development Team")
        dev_title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #FFFFFF;
                margin-bottom: 15px;
                padding-bottom: 10px;
                border-bottom: 2px solid rgba(255, 255, 255, 0.2);
            }
        """)
        dev_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(dev_title)
        
        # Developer cards
        developers = [
            ("👨‍💻 Abdikadir Fatmasarah Abdirahman", "Student ID: 138402", "Lead Developer & Security Specialist"),
            ("👨‍💻 Wesonga Edward Chisaka", "Student ID: 136948", "UI/UX Designer & Cryptography Expert")
        ]
        
        for name, student_id, role in developers:
            dev_frame = QFrame()
            dev_frame.setStyleSheet("""
                QFrame {
                    background: rgba(240, 125, 0, 0.1);
                    border-radius: 10px;
                    border: 1px solid rgba(240, 125, 0, 0.3);
                    padding: 15px;
                    margin: 5px 0;
                }
            """)
            
            dev_layout = QVBoxLayout()
            dev_layout.setSpacing(5)
            
            name_label = QLabel(name)
            name_label.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    color: #FFFFFF;
                }
            """)
            
            id_label = QLabel(student_id)
            id_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    color: rgba(255, 255, 255, 0.8);
                    font-weight: 500;
                }
            """)
            
            role_label = QLabel(role)
            role_label.setStyleSheet("""
                QLabel {
                    font-size: 13px;
                    color: rgba(255, 255, 255, 0.7);
                    font-style: italic;
                }
            """)
            
            dev_layout.addWidget(name_label)
            dev_layout.addWidget(id_label)
            dev_layout.addWidget(role_label)
            
            dev_frame.setLayout(dev_layout)
            layout.addWidget(dev_frame)
        
        # Copyright notice
        copyright_label = QLabel("© 2024 LockBox Team. All rights reserved.")
        copyright_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
                color: rgba(255, 255, 255, 0.6);
                margin-top: 15px;
                padding-top: 10px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
            }
        """)
        copyright_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(copyright_label)
        
        frame.setLayout(layout)
        return frame
