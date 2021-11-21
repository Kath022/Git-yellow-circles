import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QApplication
from random import randrange

from interfce import Ui_Form


class Wind(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circl(qp)
            qp.end()

    def draw_circl(self, qp):
        qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
        r = randrange(200)
        qp.drawEllipse(QPoint(200, 180), r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Wind()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

