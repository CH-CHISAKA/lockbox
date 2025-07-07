from controller import SecureMessengerController
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from UserInterface.mainWindow import MainWindow  # Updated import
from PyQt6.QtCore import Qt

def create_app():
    """
    Function to initialize the application, set up the window, and start the application loop.
    Includes error handling and validation for required components.
    """
    try:
        # Initialize the application
        app = QApplication(sys.argv)
        app.setApplicationName("LockBox")

        # Initialize the controller
        controller = SecureMessengerController(None)

        # Ensure controller is properly initialized
        if not controller:
            raise ValueError("Failed to initialize LockBoxController.")

        # Create the main window, passing the controller
        window = MainWindow(controller)

        # Ensure the window is created correctly
        if not window:
            raise ValueError("Failed to initialize the main window.")

        # Assign the controller's main window reference
        controller.main_window = window #check if this is needed

        # Apply a linear gradient background to the window
        window.setStyleSheet("""
            QMainWindow {
                background: linear-gradient(to bottom, #141A20, #212A34);  /* Gradient from dark to light */
            }
        """)

        # Show the window
        window.show()

        # Start the application loop
        sys.exit(app.exec())

    except Exception as e:
        # Handle errors and show message box
        print(f"Error: {e}")
        sys.exit(1)  # Exit with error code

if __name__ == "__main__":
    # Validate the script is being run correctly
    try:
        create_app()
    except Exception as e:
        print(f"Application failed to start: {e}")
        sys.exit(1)  # Exit with error code
