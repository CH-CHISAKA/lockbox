# Import necessary PyQt6 modules
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel  # For UI widgets and layout
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
        
        # Set padding/margin around the layout: 24 pixels on each side
        layout.setContentsMargins(24, 24, 24, 24)
        
        # Set spacing between widgets within the layout to 16 pixels
        layout.setSpacing(16)

        # Create the title label (header of the page)
        title_label = self._create_title_label()
        
        # Create the informational label (descriptive text)
        info_label = self._create_info_label()

        # Add the created labels to the layout (in vertical order)
        layout.addWidget(title_label)
        layout.addWidget(info_label)

        # Apply the layout to the current widget
        self.setLayout(layout)

        # Apply linear gradient background
        self.setStyleSheet("""
            QWidget {
                background: linear-gradient(to bottom, #141A20, #212A34);
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
            font-size: 22px;
            font-weight: bold;
            color: #2E3440;
        """)
        
        # Align the text to the left
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
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
            "Secure Messenger\n\n"
            "A simple, secure messaging application for sending and receiving encrypted messages.\n"
            "Developed as a project for BBT4102 Cryptography and Network Security.\n\n"
            "By:\n"
            "• 138402  Abdikadir Fatmasarah Abdirahman\n"
            "• 136948  Wesonga Edward Chisaka\n"
        )
        
        # Create a QLabel with the multiline info text
        label = QLabel(info_text)
        
        # Enable word wrapping so long lines break into the next line
        label.setWordWrap(True)
        
        # Apply inline CSS to style the font and text color
        label.setStyleSheet("font-size: 14px; color: #4C566A;")
        
        # Set an accessible name for screen readers and accessibility tools
        label.setAccessibleName("Information")
        
        # Return the configured label
        return label
