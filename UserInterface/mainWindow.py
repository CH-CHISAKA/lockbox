from PyQt6.QtWidgets import (
    QMainWindow, QTextEdit, QStatusBar, QMessageBox, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from UserInterface.sendWindow import SendMessagePage
from UserInterface.receiveWindow import ReceiveMessagePage
from UserInterface.aboutPage import AboutPage


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("🔒 LockBox - Secure Messaging")
        self.resize(800, 600)
        self.setMinimumSize(700, 500)

        # Main stylesheet setup with new gradient theme
        self._setup_styles()

        # Sidebar setup
        sidebar = self._create_sidebar()

        # Central area setup
        self.central_area = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_layout.setContentsMargins(30, 30, 30, 30)  # Increased padding
        self.central_layout.setSpacing(20)
        self.central_area.setLayout(self.central_layout)

        # Initialize central area log with welcome message
        self.central_log = QTextEdit()
        self.central_log.setReadOnly(True)
        self.central_log.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        welcome_text = """
🔒 Welcome to LockBox

Your secure messaging companion for encrypted communications.

Features:
• End-to-end encryption with AES-256
• RSA key pair generation
• Secure OTP verification via SMS
• Network device discovery
• Real-time message encryption/decryption

Get started by clicking 'Send Message' to encrypt and send a secure message,
or 'Receive Message' to decrypt an incoming message.

Stay secure! 🛡️
        """
        self.central_log.setPlainText(welcome_text.strip())
        self.central_layout.addWidget(self.central_log)

        # Main layout: sidebar + central area
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_widget.setLayout(main_layout)
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.central_area, 1)  # Stretch factor for central area

        self.setCentralWidget(main_widget)

        # Server state
        self.server_running = False

    def _setup_styles(self):
        """Enhanced stylesheet with new gradient theme and improved UX"""
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #000B3F,
                    stop: 1 #001DA5
                );
            }
            
            QWidget {
                background: transparent;
                color: #FFFFFF;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 14px;
            }
            
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #F07D00,
                    stop: 1 #8A4800
                );
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                margin: 8px 4px;
                font-weight: 600;
                font-size: 13px;
                min-height: 20px;
            }
            
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #FF8A00,
                    stop: 1 #A05000
                );
                transform: translateY(-1px);
            }
            
            QPushButton:pressed {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #D06D00,
                    stop: 1 #743F00
                );
            }
            
            QLabel {
                color: #FFFFFF;
                padding: 6px 2px;
                font-weight: 500;
            }
            
            QTextEdit {
                background: rgba(255, 255, 255, 0.1);
                color: #FFFFFF;
                border: 2px solid rgba(255, 255, 255, 0.2);
                border-radius: 12px;
                padding: 15px;
                font-size: 14px;
                line-height: 1.4;
            }
            
            QTextEdit:focus {
                border: 2px solid rgba(240, 125, 0, 0.6);
            }
            
            QStatusBar {
                background: rgba(0, 11, 63, 0.8);
                color: white;
                padding: 8px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
            }
        """)

    def _create_sidebar(self):
        """Create the enhanced sidebar UI with improved styling"""
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(20, 25, 20, 25)
        sidebar_layout.setSpacing(15)
        sidebar.setLayout(sidebar_layout)
        sidebar.setFixedWidth(220)
        
        # Enhanced sidebar styling with glass effect
        sidebar.setStyleSheet("""
            QWidget {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                backdrop-filter: blur(10px);
            }
        """)

        # Add title
        title_label = QLabel("🔒 LockBox")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #FFFFFF;
                padding: 10px 0;
                border-bottom: 2px solid rgba(255, 255, 255, 0.2);
                margin-bottom: 10px;
            }
        """)
        sidebar_layout.addWidget(title_label)

        # Server control section
        self._create_server_control(sidebar_layout)

        # Sidebar buttons
        self._add_sidebar_buttons(sidebar_layout)

        sidebar_layout.addStretch()

        return sidebar

    def _create_server_control(self, layout):
        """Creates the enhanced server control section"""
        server_label = QLabel("Server Status")
        server_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #FFFFFF;
                margin-top: 10px;
                margin-bottom: 5px;
            }
        """)
        layout.addWidget(server_label)

        server_row = QHBoxLayout()
        server_row.setSpacing(12)

        self.server_btn = QPushButton("▶ Start Server")
        self.server_btn.clicked.connect(self.toggle_server)
        self.server_btn.setStyleSheet("""
            QPushButton {
                font-size: 12px;
                padding: 10px 15px;
            }
        """)

        self.server_indicator = QLabel()
        self.set_server_indicator(False)
        self.server_indicator.setFixedSize(20, 20)
        self.server_indicator.setStyleSheet("""
            QLabel {
                border-radius: 10px;
                border: 2px solid rgba(255, 255, 255, 0.3);
            }
        """)

        server_row.addWidget(self.server_btn)
        server_row.addWidget(self.server_indicator)
        server_row.addStretch()

        layout.addLayout(server_row)
        layout.addSpacing(15)

    def _add_sidebar_buttons(self, layout):
        """Adds enhanced buttons to the sidebar"""
        # Main action buttons
        btn_send = QPushButton("📤 Send Message")
        btn_send.clicked.connect(self.controller.show_send_page)
        btn_send.setToolTip("Encrypt and send a secure message")
        layout.addWidget(btn_send)

        btn_receive = QPushButton("📥 Receive Message")
        btn_receive.clicked.connect(self.controller.show_receive_page)
        btn_receive.setToolTip("Decrypt and read received messages")
        layout.addWidget(btn_receive)

        layout.addSpacing(20)

        # Utility buttons
        btn_about = QPushButton("ℹ️ About")
        btn_about.clicked.connect(self.show_about)
        btn_about.setToolTip("About LockBox application")
        layout.addWidget(btn_about)

        btn_exit = QPushButton("🚪 Exit")
        btn_exit.clicked.connect(self.close)
        btn_exit.setToolTip("Close the application")
        btn_exit.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #DC3545,
                    stop: 1 #A71F2B
                );
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #E74C5C,
                    stop: 1 #C82333
                );
            }
        """)
        layout.addWidget(btn_exit)

    def set_server_indicator(self, running: bool):
        """Sets the enhanced server status indicator"""
        if running:
            color = "#28A745"  # Success green
            self.server_indicator.setStyleSheet(f"""
                QLabel {{
                    background: qradialgradient(
                        cx: 0.5, cy: 0.5, radius: 0.5,
                        stop: 0 {color},
                        stop: 0.7 {color},
                        stop: 1 rgba(40, 167, 69, 0.3)
                    );
                    border-radius: 10px;
                    border: 2px solid rgba(255, 255, 255, 0.3);
                }}
            """)
        else:
            color = "#DC3545"  # Danger red
            self.server_indicator.setStyleSheet(f"""
                QLabel {{
                    background: qradialgradient(
                        cx: 0.5, cy: 0.5, radius: 0.5,
                        stop: 0 {color},
                        stop: 0.7 {color},
                        stop: 1 rgba(220, 53, 69, 0.3)
                    );
                    border-radius: 10px;
                    border: 2px solid rgba(255, 255, 255, 0.3);
                }}
            """)

    def toggle_server(self):
        """Toggle between starting and stopping the server"""
        if self.server_running:
            self.controller.stop_server()
        else:
            self.controller.start_server()

    def update_server_status(self, running: bool):
        """Updates the server status with enhanced styling"""
        self.server_running = running
        self.set_server_indicator(running)
        if running:
            self.server_btn.setText("⏹ Stop Server")
        else:
            self.server_btn.setText("▶ Start Server")

    def show_about(self):
        """Displays the About page"""
        self.set_central_widget(AboutPage())

    def set_central_widget(self, widget):
        """Sets the central widget of the window"""
        # Clear previous central widget
        for i in reversed(range(self.central_layout.count())):
            old_widget = self.central_layout.itemAt(i).widget()
            if old_widget:
                old_widget.setParent(None)
        self.central_layout.addWidget(widget)

    def show_log(self):
        """Shows the log in the central area"""
        self.set_central_widget(self.central_log)
