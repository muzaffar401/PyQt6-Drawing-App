import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QVBoxLayout, QHBoxLayout, QSlider
from PyQt6.QtGui import QPainter, QPen, QColor, QMouseEvent
from PyQt6.QtCore import Qt, QPoint


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drawing App")
        self.setGeometry(100, 100, 800, 600)

        self.drawing = False
        self.last_point = QPoint()
        self.color = QColor(Qt.GlobalColor.black)
        self.pen_width = 3
        self.paths = []

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear)
        button_layout.addWidget(clear_button)

        color_button = QPushButton("Choose Color")
        color_button.clicked.connect(self.choose_color)
        button_layout.addWidget(color_button)

        self.brush_slider = QSlider(Qt.Orientation.Horizontal)
        self.brush_slider.setMinimum(1)
        self.brush_slider.setMaximum(20)
        self.brush_slider.setValue(self.pen_width)
        self.brush_slider.valueChanged.connect(self.set_brush_width)
        button_layout.addWidget(self.brush_slider)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_point = event.pos()
            self.paths.append((self.last_point, self.last_point, self.color, self.pen_width))

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.drawing:
            new_point = event.pos()
            self.paths.append((self.last_point, new_point, self.color, self.pen_width))
            self.last_point = new_point
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for start, end, color, width in self.paths:
            pen = QPen(color, width, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(start, end)

    def clear(self):
        self.paths.clear()
        self.update()

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color

    def set_brush_width(self, width):
        self.pen_width = width


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
