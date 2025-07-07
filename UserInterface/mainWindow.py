from PyQt6.QtWidgets import (
    QMainWindow, QTextEdit, QStatusBar, QMessageBox, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
)
from PyQt6.QtCore import Qt
from UserInterface.sendWindow import SendMessagePage
from UserInterface.receiveWindow import ReceiveMessagePage
from UserInterface.aboutPage import AboutPage


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("LockBox")
        
        # Better window management
        self.resize(800, 600)
        self.setMinimumSize(600, 400)
        
        # Center the window on screen
        self._center_window()

        # Define color scheme
        self._define_colors()

        # Main stylesheet setup
        self._setup_styles()

        # Sidebar setup
        sidebar = self._create_sidebar()

        # Central area setup
        self.central_area = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_layout.setContentsMargins(24, 24, 24, 24)  # Padding inside central area
        self.central_layout.setSpacing(16)
        self.central_area.setLayout(self.central_layout)

        # Initialize central area log
        self.central_log = QTextEdit("Welcome to LockBox.")
        self.central_log.setReadOnly(True)
        self.central_log.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
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

        # Apply linear gradient background with proper PyQt syntax
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #141A20, stop:1 #212A34);
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }
        """)

    def _define_colors(self):
        self.columbia_blue = "#bfd7ea"
        self.cadet_gray = "#91aec1"
        self.air_force_blue = "#508ca4"
        self.sea_green = "#0a8754"
        self.cal_poly_green = "#004f2d"

    def _setup_styles(self):
        """Main stylesheet for color scheme and padding"""
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {self.columbia_blue};
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }}
            QWidget {{
                background-color: {self.columbia_blue};
                color: {self.cal_poly_green};
                font-size: 15px;
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }}
            QPushButton {{
                background-color: {self.air_force_blue};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 18px;
                margin: 6px 0;
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }}
            QPushButton:hover {{
                background-color: {self.sea_green};
            }}
            QLabel {{
                color: {self.cal_poly_green};
                padding: 4px 0;
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }}
            QTextEdit {{
                background-color: {self.cadet_gray};
                color: {self.cal_poly_green};
                border-radius: 8px;
                padding: 12px;
                font-size: 15px;
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }}
            QStatusBar {{
                background-color: {self.air_force_blue};
                color: white;
                padding: 6px;
                font-family: 'Ubuntu', 'DejaVu Sans', 'Liberation Sans', sans-serif;
            }}
        """)

    def _create_sidebar(self):
        """Create the sidebar UI with buttons"""
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(18, 18, 18, 18)
        sidebar_layout.setSpacing(12)
        sidebar.setLayout(sidebar_layout)
        sidebar.setFixedWidth(180)
        sidebar.setStyleSheet(f"background-color: {self.cadet_gray}; border-radius: 12px;")

        # Server control section
        self._create_server_control(sidebar_layout)

        # Sidebar buttons
        self._add_sidebar_buttons(sidebar_layout)

        sidebar_layout.addStretch()

        return sidebar

    def _create_server_control(self, layout):
        """Creates the server control button with indicator"""
        server_row = QHBoxLayout()
        server_row.setSpacing(10)

        self.server_btn = QPushButton("Start Server")
        self.server_btn.clicked.connect(self.toggle_server)

        self.server_indicator = QLabel()
        self.set_server_indicator(False)
        self.server_indicator.setFixedSize(16, 16)
        self.server_indicator.setStyleSheet("margin-left: 8px; margin-right: 8px;")

        server_row.addWidget(self.server_btn)
        server_row.addWidget(self.server_indicator)
        server_row.addStretch()

        layout.addLayout(server_row)
        layout.addSpacing(10)

    def _add_sidebar_buttons(self, layout):
        """Adds buttons to the sidebar"""
        btn_send = QPushButton("Send Message")
        btn_send.clicked.connect(self.controller.show_send_page)
        layout.addWidget(btn_send)

        btn_receive = QPushButton("Receive Message")
        btn_receive.clicked.connect(self.controller.show_receive_page)
        layout.addWidget(btn_receive)

        layout.addSpacing(10)

        btn_about = QPushButton("About")
        btn_about.clicked.connect(self.show_about)
        layout.addWidget(btn_about)

        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.close)
        layout.addWidget(btn_exit)

    def set_server_indicator(self, running: bool):
        """Sets the server status indicator color"""
        color = "#0a8754" if running else "#b22222"  # green or red
        self.server_indicator.setStyleSheet(
            f"background-color: {color}; border-radius: 8px; border: 1px solid #333;"
        )

    def toggle_server(self):
        """Toggle between starting and stopping the server"""
        if self.server_running:
            self.controller.stop_server()
        else:
            self.controller.start_server()

    def update_server_status(self, running: bool):
        """Updates the server status"""
        self.server_running = running
        self.set_server_indicator(running)
        self.server_btn.setText("Stop Server" if running else "Start Server")

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

    def _center_window(self):
        """Center the window on the screen"""
        from PyQt6.QtGui import QGuiApplication
        screen = QGuiApplication.primaryScreen().geometry()
        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)
