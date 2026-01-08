import sys

import PySide6.QtCore
from PySide6 import QtCore, QtWidgets

import my_widgets


def main():
    print("Hello from wavelength_calc_gui!")
    print("PySide6 version: " + PySide6.__version__)
    print("Qt version: " + QtCore.qVersion())
    QtCore.QLocale.setDefault(QtCore.QLocale.c())

    print(
        'Decimal point in the current locale: "' + QtCore.QLocale().decimalPoint() + '"'
    )

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName("v2w")
    widget = my_widgets.MyWidget()
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
