import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)

        self.do_paint = False

        self.setFixedSize(550, 300)

        self.CreateButton.clicked.connect(self.clicked_btn)

    def paintEvent(self, event) -> None:
        if self.do_paint:
            self.draw_circle()

    def clicked_btn(self) -> None:
        self.do_paint = True
        self.repaint()

    def draw_circle(self):
        diameter = random.randint(10, 100)

        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.yellow)
        painter.setBrush(Qt.yellow)
        painter.drawEllipse(100, 100, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())
