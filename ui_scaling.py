# ui_scaling.py
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QSlider, QVBoxLayout, QLabel


def show_scale_dialog(parent):
    dialog = ScaleDialog(parent)
    dialog.exec_()


class ScaleDialog(QDialog):
    def __init__(self, parent=None):
        super(ScaleDialog, self).__init__(parent)
        self.setWindowTitle('Adjust UI Scale')
        self.setStyleSheet("background-color: #333; color: white;")
        self.setFont(QFont('Arial', 14))

        layout = QVBoxLayout(self)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(50)
        self.slider.setMaximum(150)
        self.slider.setValue(100)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.scale_changed)

        layout.addWidget(QLabel('Adjust UI scale:'))
        layout.addWidget(self.slider)

        self.setLayout(layout)
        self.setFixedSize(500, 100)

    def scale_changed(self, value):
        try:
            scale_factor = value / 100.0
            parent = self.parent()
            if parent and hasattr(parent, 'adjust_scale'):
                print(f"Scaling with factor: {scale_factor}")
                parent.adjust_scale(scale_factor)
            else:
                print("Parent not set or doesn't have adjust_scale")
        except Exception as e:
            print(f"Error during scaling: {e}")
