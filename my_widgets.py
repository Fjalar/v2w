from PySide6 import QtCore, QtGui, QtWidgets

import wavelength


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.wavelength_text = QtWidgets.QLabel()

        self.input = QtWidgets.QLineEdit()

        self.input.setValidator(
            QtGui.QDoubleValidator(
                notation=QtGui.QDoubleValidator.Notation.ScientificNotation
            )
        )

        self.main_layout = QtWidgets.QVBoxLayout(self)

        input_layout = QtWidgets.QHBoxLayout()

        input_layout.addWidget(QtWidgets.QLabel("Voltage: "))
        input_layout.addWidget(self.input)
        input_layout.addWidget(QtWidgets.QLabel("Volt"))
        self.main_layout.addLayout(input_layout)

        result_layout = QtWidgets.QHBoxLayout()
        result_layout.addWidget(QtWidgets.QLabel("Wavelength: "))
        result_layout.addWidget(self.wavelength_text)
        result_layout.addWidget(QtWidgets.QLabel("meters"))

        self.main_layout.addLayout(result_layout)

        self.setLayout(self.main_layout)

        self.input.returnPressed.connect(self.calculate)
        self.input.textChanged.connect(self.calculate)

    @QtCore.Slot()
    def calculate(self):
        if self.input.hasAcceptableInput:
            text = self.input.text()
            if len(text) > 0 and text[-1] != "e" and text[-1] != "-":
                voltage = float(text)
                if voltage > 0:
                    wav = wavelength.wavelength_from_voltage(voltage)
                    self.wavelength_text.setText("{:10.2e}".format(wav))
