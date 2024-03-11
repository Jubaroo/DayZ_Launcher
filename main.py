from PyQt5.QtWidgets import QApplication

from gui import DayZManager


def main():
    app = QApplication([])
    window = DayZManager()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
