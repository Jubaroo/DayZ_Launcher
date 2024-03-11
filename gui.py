# gui.py

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QTabWidget, QAction, QTableWidget, \
    QHBoxLayout, QLineEdit, QDesktopWidget, QHeaderView

from info import show_info_dialog
from themes import dark_theme_stylesheet, light_theme_stylesheet, apply_stylesheet
from ui_scaling import show_scale_dialog
from utils import initiate_cleanup, get_last_server_info, launch_dayz
from server_query import query_servers


class DayZManager(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the current theme
        self.current_theme = "dark"
        self.apply_theme()

        # Window settings
        self.community_table = None
        self.server_name_input = None
        self.setWindowTitle('DayZ Launcher')
        self.setMinimumSize(800, 600)
        self.setStyleSheet("background-color: #333; color: white;")
        self.center_and_resize()

        # Menu Bar
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu('File')
        self.options_menu = self.menu_bar.addMenu('Options')
        self.help_menu = self.menu_bar.addMenu('Help')

        # Add actions to File menu
        exit_action = QAction(' Exit ', self)
        exit_action.triggered.connect(self.close)
        self.file_menu.addAction(exit_action)

        # Add actions to Options menu
        cleanup_action = QAction(' Clean Up Files ', self)
        cleanup_action.triggered.connect(initiate_cleanup)
        self.options_menu.addAction(cleanup_action)

        # Add 'Change Theme' action to Options menu
        change_theme_action = QAction(' Change Theme ', self)
        change_theme_action.triggered.connect(self.toggle_theme)
        self.options_menu.addAction(change_theme_action)

        # Add 'Adjust UI Scale' action to Options menu
        adjust_scale_action = QAction('Adjust UI Scale', self)
        adjust_scale_action.triggered.connect(lambda: show_scale_dialog(self))
        self.options_menu.addAction(adjust_scale_action)

        # Add 'Info' action to Help menu
        info_action = QAction(' About ', self)
        info_action.triggered.connect(show_info_dialog)
        self.help_menu.addAction(info_action)

        # Create a horizontal layout for search criteria
        search_layout = QHBoxLayout()

        # Example: QLineEdit for server name search
        self.server_name_input = QLineEdit(self)
        self.server_name_input.setPlaceholderText("Enter server name")

        # Example: QPushButton for triggering the search
        search_btn = QPushButton('Search', self)
        search_btn.clicked.connect(self.search_servers)

        # Add widgets to the search layout
        search_layout.addWidget(self.server_name_input)
        search_layout.addWidget(search_btn)

        # Tabs
        self.tabs = QTabWidget(self)

        # Styling for tabs
        self.tabs.tabBar().setStyleSheet("""
            QTabBar::tab {
                background: #555;
                color: white;
                padding: 5px;
            }
            QTabBar::tab:selected {
                background: #888;
            }
        """)
        self.tabs.addTab(self.create_tab_content("Favorites"), "Favorites")
        self.tabs.addTab(self.create_tab_content("Recent"), "Recent")
        self.tabs.addTab(self.create_tab_content("Friends"), "Friends")
        self.tabs.addTab(self.create_tab_content("Official"), "Official")
        self.tabs.addTab(self.create_community_tab(), "Community")
        self.tabs.addTab(self.create_tab_content("LAN"), "LAN")
        self.tabs.addTab(self.create_tab_content("Mods"), "Mods")

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        layout.addLayout(search_layout)

        # Server info display
        self.server_info_label = QLabel("Loading server info...", self)
        self.server_info_label.setFont(QFont('Arial', 14))
        self.server_info_label.setAlignment(Qt.AlignCenter)
        self.server_info_label.setWordWrap(True)
        layout.addWidget(self.server_info_label)

        # Update server info
        last_server_name, last_server_ip = get_last_server_info()
        self.server_info_label.setText(f"Last Server: {last_server_name}\nIP: {last_server_ip}")

        # Launch DayZ button
        launch_btn = QPushButton('Launch DayZ', self)
        launch_btn.setFont(QFont('Arial', 12))
        launch_btn.setStyleSheet("QPushButton { background-color: #555; }")
        launch_btn.clicked.connect(launch_dayz)
        layout.addWidget(launch_btn)

        # Set the layout for the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set the initial theme
        self.apply_theme()

    def create_community_tab(self):
        # Create a layout for the tab
        tab_layout = QVBoxLayout()

        # Create the table for displaying server results
        self.community_table = QTableWidget()
        self.community_table.setColumnCount(3)  # Adjust columns as needed
        self.community_table.setHorizontalHeaderLabels(["Name", "IP", "Players", "PvP"])

        # For the QTableWidget
        self.community_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Add search layout and table to the main layout
        tab_layout.addWidget(self.community_table)

        # Create a container widget and set the layout
        tab_widget = QWidget()
        tab_widget.setLayout(tab_layout)
        return tab_widget

    def search_servers(self):
        # Get the search criteria from the input fields
        server_name = self.server_name_input.text()
        # Determine which tab is currently active and set the criteria accordingly
        current_tab = self.tabs.currentWidget()
        if current_tab == self.community_table:
            query_servers(self, server_name)
        # Add similar conditions for other tabs if they have unique search functionality

    def create_tab_content(self, tab_name):
        if tab_name == "Community":
            return self.create_community_tab()
        else:
            tab_widget = QWidget()
            tab_layout = QVBoxLayout()
            tab_label = QLabel(f"Content for {tab_name} tab.", tab_widget)
            tab_label.setWordWrap(True)
            tab_layout.addWidget(tab_label)
            tab_widget.setLayout(tab_layout)

        return tab_widget

    def apply_theme(self):
        if self.current_theme == "dark":
            self.setStyleSheet(dark_theme_stylesheet)
            apply_stylesheet(self, dark_theme_stylesheet)

        else:
            self.setStyleSheet(light_theme_stylesheet)
            apply_stylesheet(self, light_theme_stylesheet)

    def toggle_theme(self):
        if self.current_theme == "dark":
            self.current_theme = "light"
        else:
            self.current_theme = "dark"
        self.apply_theme()

    def adjust_scale(self, scale_factor):
        # Apply the scaling to the main window's font
        font = self.font()
        font.setPointSizeF(font.pointSizeF() * scale_factor)
        self.setFont(font)

        # Apply the scaling to all child widgets
        for widget in self.findChildren(QWidget):
            widget_font = widget.font()
            widget_font.setPointSizeF(widget_font.pointSizeF() * scale_factor)
            widget.setFont(widget_font)
            widget.update()  # Update individual widgets
        self.update()  # Update the main window

    def center_and_resize(self):
        # Get the screen size
        screen = QDesktopWidget().screenGeometry()
        # Calculate width and height for 50% of the screen size
        width = int(screen.width() * 0.7)
        height = int(screen.height() * 0.7)
        # Set the geometry of the window
        self.setGeometry(int((screen.width() - width) / 2), int((screen.height() - height) / 2), width, height)
