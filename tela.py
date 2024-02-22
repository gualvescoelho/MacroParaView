import sys
from PySide6.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QPushButton, QHBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tela com PySide6')
        # self.setGeometry()
        self.creatingLayouts()
        self.creatingButtons()
        self.creatingPoints()
        self.creatingTitles()
        self.creatingComboBox()
        self.addingToLayout()

    def creatingLayouts(self):
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.layoutPoint1 = QHBoxLayout()
        self.layoutPoint2 = QHBoxLayout()

    def creatingButtons(self):
        self.confirm_button = QPushButton('Confirmar')
        self.confirm_button.clicked.connect(self.confirm_action)

    def creatingPoints(self):
        self.Point1_text_input1 = QLineEdit()
        self.Point1_text_input2 = QLineEdit()
        self.Point1_text_input3 = QLineEdit()
        self.Point2_text_input1 = QLineEdit()
        self.Point2_text_input2 = QLineEdit()
        self.Point2_text_input3 = QLineEdit()

    def creatingTitles(self):
        self.point1title = QLabel("point 1")
        self.point2title = QLabel("point 2")

    def creatingComboBox(self):
        self.item_selector = QComboBox()
        self.item_selector.addItems(['PlotOverLine'])

    def addingToLayout(self):
        self.layoutPoint1.addWidget(self.point1title)
        self.layoutPoint1.addWidget(self.Point1_text_input1)
        self.layoutPoint1.addWidget(self.Point1_text_input2)
        self.layoutPoint1.addWidget(self.Point1_text_input3)

        self.layoutPoint2.addWidget(self.point2title)
        self.layoutPoint2.addWidget(self.Point2_text_input1)
        self.layoutPoint2.addWidget(self.Point2_text_input2)
        self.layoutPoint2.addWidget(self.Point2_text_input3)

        self.form_layout.addRow('Seletor de Itens:', self.item_selector)
        self.form_layout.addWidget(self.confirm_button)

        self.layout.addLayout(self.layoutPoint1)
        self.layout.addLayout(self.layoutPoint2)
        self.layout.addLayout(self.form_layout)
        self.setLayout(self.layout)
    
    def confirm_action(self):
        text1 = self.Point1_text_input1.text()
        text2 = self.Point1_text_input2.text()
        selected_item = self.item_selector.currentText()

        print('Texto 1:', text1)
        print('Texto 2:', text2)
        print('Item selecionado:', selected_item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
