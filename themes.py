# themes.py
from PyQt5.QtWidgets import QWidget


def apply_stylesheet(self, stylesheet):
    self.setStyleSheet(stylesheet)
    for widget in self.findChildren(QWidget):
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()


dark_theme_stylesheet = """
QMainWindow {
    background-color: #333;
    color: white;
}

QPushButton {
    background-color: #555;
    color: white;
    border: 1px solid #444;
}

QPushButton:hover {
    background-color: #666;
}

QPushButton:pressed {
    background-color: #777;
}

QTabBar::tab {
    background: #555;
    color: white;
    padding: 5px;
    border: 1px solid #444;
}

QTabBar::tab:selected {
    background: #666;
    color: white;
}

QTabBar::tab:hover {
    background: #777;
}

QLabel, QCheckBox, QRadioButton, QGroupBox, QSlider {
    color: white;
}

QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QComboBox, QListWidget, QTableView, QTableWidget, QHeaderView {
    background-color: #222;
    color: white;
    border: 1px solid #444;
}

QStatusBar {
    background-color: #555;
    color: white;
}

QMenuBar {
    background-color: #333;
    color: white;
}

QMenuBar::item {
    background-color: #333;
    color: white;
    padding: 4px;
}

QMenuBar::item:selected {
    background-color: #454545; /* Slightly darker for the hover state */
    color: white;
}

QMenu {
    background-color: #333;
    color: white;
    border: 1px solid #444;
}

QMenu::item {
    background-color: #333;
    color: white;
    padding: 4px;
}

QMenu::item:selected {
    background-color: #454545; /* Slightly darker for the hover state */
    color: white;
}
"""

light_theme_stylesheet = """
background-color: white; color: black;
QMainWindow {
    background-color: #EEE;
    color: black;
}
QPushButton {
    background-color: #CCC;
    color: black;
    border: 1px solid #AAA;
}
QPushButton:hover {
    background-color: #BBB;
}
QPushButton:pressed {
    background-color: #AAA;
}
QTabBar::tab {
    background: #CCC;
    color: black;
    padding: 5px;
    border: 1px solid #AAA;
}
QTabBar::tab:selected {
    background: #BBB;
    color: black;
}
QTabBar::tab:hover {
    background: #AAA;
}
QLabel, QCheckBox, QRadioButton, QGroupBox, QSlider {
    color: black;
}
QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QComboBox, QListWidget, QTableView, QTableWidget, QHeaderView {
    background-color: #FFF;
    color: black;
    border: 1px solid #AAA;
}
QStatusBar {
    background-color: #CCC;
    color: black;
}
"""
