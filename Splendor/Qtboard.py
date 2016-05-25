import random

from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QLabel, QRadioButton, QCheckBox, QWidget, QLCDNumber
from game_board import SplendorTable


class NotifyParent(QEvent):
    idType = QEvent.registerEventType()

    def __init__(self, data):
        QEvent.__init__(self, NotifyParent.idType)
        self.data = data

    def get_data(self):
        return self.data


class ColourLabel(QLabel):
    def __init__(self, card, parent=None):
        super(ColourLabel, self).__init__(str(card.gem_type), parent)
        self.card = card
        self.pressed = False
        self.justPressed = False

    def paintEvent(self, event):
        rect = self.frameGeometry()
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(Qt.black))
        qp.drawRect(0, 0, rect.width(), rect.height())

        colorTable = {'Emerald': QColor(0, 255, 0, 127),
                      'Sapphire': QColor(0, 0, 255, 127),
                      'Ruby': QColor(255, 0, 0, 127),
                      'Diamond': QColor(255, 255, 255, 127),
                      'Onyx': QColor(100, 100, 0, 127),
                      '1': QColor(100, 0, 100, 127)}

        color = QColor(colorTable[self.card.gem_type])
        qp.fillRect(1, 1, rect.width() - 2, rect.height() - 2, QBrush(color))

        indent = 18
        for key, value in self.card.cost.items():
            s = key + ': ' + str(value)
            qp.drawText(12, indent, s)
            indent += 20

        indent += 20
        qp.drawText(12, indent, "Points: " + str(self.card.points))
        qp.end()


class ColourChip(QLabel):
    def __init__(self, chip, parent=None):
        super(ColourChip, self).__init__(str(chip[0].gem_type), parent)
        self.chip = chip[0]
        self.number = chip[1]

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawEllipse(0, 0, self.width() / 2 - 1, self.height() / 2 - 1)
        colorTable = {'Emerald': QColor(0, 255, 0, 127),
                      'Sapphire': QColor(0, 0, 255, 127),
                      'Ruby': QColor(255, 0, 0, 127),
                      'Diamond': QColor(255, 255, 255, 127),
                      'Onyx': QColor(100, 100, 0, 127),
                      'Gold': QColor(100, 0, 100, 127)}
        color = QColor(colorTable[self.chip.gem_type])
        qp.setPen(QPen(color, 1, Qt.SolidLine, Qt.RoundCap))
        qp.setBrush(QBrush(color, Qt.SolidPattern))
        qp.drawText(12, 18, str(self.number))
        qp.end()


class SplendorWindow(QWidget):
    def __init__(self):
        super(SplendorWindow, self).__init__()
        self.setWindowTitle("Splendor")
        self.resize(950, 670)

        self.board = SplendorBoard()
        layout = QGridLayout()
        self.game_table = SplendorTable()
        layout_cards = QGridLayout()
        layout_chips = QGridLayout()
        layout_lords = QGridLayout()
        scoreLcd = QLCDNumber(2)
        scoreLcd.setSegmentStyle(QLCDNumber.Filled)

        layout.addWidget(self.createLabel("Name: "), 0, 0)
        layout.addWidget(self.createLabel("Sandy"), 0, 1)
        layout.addWidget(self.createLabel("Score: "), 0, 2)
        layout.addWidget(scoreLcd, 0, 3)

        self.frame_cards = QFrame()
        self.frame_cards.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.frame_cards.setLayout(layout_cards)

        self.frame_chips = QFrame()
        self.frame_chips.setFrameStyle(QFrame.Box | QFrame.Raised)
        frame_lords = QFrame()
        frame_lords.setFrameStyle(QFrame.Box | QFrame.Raised)

        layout.addWidget(self.frame_cards, 2, 0, 4, 5)
        layout.addWidget(self.frame_chips, 2, 6, 4, 2)
        #layout.addWidget(frame_lords, 2, 10)

        self.frame_chips.setLayout(layout_chips)
        frame_lords.setLayout(layout_lords)

        for r in (0, 4, 8):
            row = self.game_table.state[int(r / 4)]
            bord_line_cards = []
            indent = 0
            for i in range(4):
                card = row[i]
                bord_line_cards.append(self.createCardSelector(card, self.frame_cards))

                layout_cards.addWidget(self.createCard(card, self.frame_cards), 0 + r, indent, 3, 2)
                layout_cards.addWidget(bord_line_cards[i], 3 + r, indent)
                indent += 2
        self.setLayout(layout)

        rr = 0
        for r in (0, 2, 4):
            row = self.game_table.state[int(r / 2)]
            bord_line_chips = []
            indent = 0
            for i in range(2):
                chip = row[4 + i]
                bord_line_chips.append(self.createChipSelector(chip, self.frame_chips))

                layout_chips.addWidget(self.createChip(chip, self.frame_chips), 0 + rr, 0, 4, 2)
                layout_chips.addWidget(bord_line_chips[i], 2 + rr, 0)
                rr += 2
        self.setLayout(layout)

    def customEvent(self, event):
        if event.type() is NotifyParent.idType:
            print("NotifyParent")

    def mousePressEvent1(self, event):
        print("Main Widget Mouse Press")
        super(QWidget, self).mousePressEvent(event)

    def createLabel(self, text):
        lbl = QLabel(text)
        lbl.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        lbl.setFrameStyle(QFrame.Box | QFrame.Raised)

        return lbl

    def createCard(self, card, parent):
        btn = ColourLabel(card, parent)
        return btn

    def createChip(self, chip, parent):
        btn = ColourChip(chip, parent)
        return btn

    def createCardSelector(self, card, parent):
        btn = QRadioButton(None, parent)
        btn.setChecked(False)
        btn.setAutoExclusive(True)
        return btn

    def createChipSelector(slef, chip, parent):
        btn = QCheckBox(parent)
        btn.setChecked(False)
        return btn


class SplendorBoard(QFrame):
    BoardWidth = 100
    BoardHeight = 170

    def __init__(self, parent=None):
        super(SplendorBoard, self).__init__(parent)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = SplendorWindow()
    window.show()
    random.seed(None)
    sys.exit(app.exec_())
