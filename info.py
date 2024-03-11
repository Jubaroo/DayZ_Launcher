from PyQt5.QtWidgets import QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, QDialog


class InfoDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Information")
        self.resize(600, 400)

        # Apply the same stylesheet as the main application
        self.setStyleSheet("background-color: #333; color: white;")

        layout = QVBoxLayout()

        info_text = """
        <h1>DayZ Launcher</h1>
        <p>This application allows you to manage your DayZ game experience. Features include:</p>
        <ul>
            <li>Cleaning up unnecessary files</li>
            <li>Launching DayZ</li>
            <li>Displaying server information</li>
            <li>Real-time server search functionality</li>
        </ul>
        <p>Developed by Jarrod. For more information, visit: <a href='https://example.com'>DayZ Launcher Website</a></p>
        """

        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setHtml(info_text)
        layout.addWidget(text_edit)

        # Close button
        close_btn = QPushButton("Close", self)
        close_btn.clicked.connect(self.close)

        # Button layout (align to the right)
        btn_layout = QHBoxLayout()
        btn_layout.addStretch(1)  # This ensures the button is pushed to the right
        btn_layout.addWidget(close_btn)

        # Add button layout to the main layout
        layout.addLayout(btn_layout)

        self.setLayout(layout)


def show_info_dialog():
    dialog = InfoDialog()
    dialog.exec_()
