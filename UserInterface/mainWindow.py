from UserInterface import aboutPage


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = aboutPage()
    window.setWindowTitle("About Page")
    window.resize(400, 300)  # Optional: Set a default size
    window.show()
    sys.exit(app.exec())
