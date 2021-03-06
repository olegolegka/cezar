import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QMainWindow


class Window(QMainWindow):
    # class MainWindow(object):
    def __init__(self):
        # def setupUi(self, Window):
        super(Window, self).__init__()
        self.setFixedSize(500, 400)
        self.setWindowIcon(QIcon('icons/public.png'))

        self.init_Action()
        self.init_Content()
        self.init_StatusBar()
        self.init_Menu()
        self.set_Actions2Menu()
        self.set_Actions2StatusBar()
        self.set_Triggers2Actions()
        self.show()

    def init_Content(self):
        self.centralwidget = QtWidgets.QWidget(self)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 490, 355))
        self.tabWidget.setStyleSheet("")


        ########____ВКЛАДКА__1__
        self.tab1 = QtWidgets.QWidget()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 475, 320))

        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)

        self.LeftVlLayout = QtWidgets.QVBoxLayout()

        self.option1HLayout = QtWidgets.QHBoxLayout()
        self.labelKey = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKey.setText("<h3>Ключ: </h3>")
        self.key = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.option1HLayout.addWidget(self.labelKey)
        self.option1HLayout.addWidget(self.key)
        self.LeftVlLayout.addLayout(self.option1HLayout)

        self.label1Input = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1Input.setText("<h3>Входной текст:</h3>")
        self.text1Input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label1Input)
        self.LeftVlLayout.addWidget(self.text1Input)

        self.buttonHLayout = QtWidgets.QHBoxLayout()
        self.encryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.encryptButton.setText("Зашифровать")
        self.encryptButton.setStatusTip("Зашифровать")
        self.decryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.decryptButton.setText("Расшифровать")
        self.decryptButton.setStatusTip("Расшифровать")
        self.buttonHLayout.addWidget(self.decryptButton)
        self.buttonHLayout.addWidget(self.encryptButton)
        self.decryptButton.clicked.connect(self.DecryptCV)
        self.encryptButton.clicked.connect(self.EncryptCV)

        self.LeftVlLayout.addLayout(self.buttonHLayout)
        self.label1Output = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1Output.setText("<h3>Вывод результата:</h4>")
        self.text1Output = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label1Output)
        self.LeftVlLayout.addWidget(self.text1Output)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.tabWidget.addTab(self.tab1, "Шифр Цезаря")





        self.MainLayout.addLayout(self.LeftVlLayout)


        self.setCentralWidget(self.centralwidget)
        self.tabWidget.setCurrentIndex(0)

    def init_StatusBar(self):
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setSizeGripEnabled(True)
        self.setStatusBar(self.statusbar)

    def init_Action(self):
        self.ExitAction = QtWidgets.QAction(QIcon('icons/exit.png'), "Выход", self)
        self.HelpAction = QtWidgets.QAction(QIcon('icons/question.png'), "Помощь", self)
        self.AboutAction = QtWidgets.QAction(QIcon('icons/about.png'), "О программе", self)

        self.ExitAction.setShortcut('Ctrl+Q')
        self.HelpAction.setShortcut('Ctrl+H')
        self.AboutAction.setShortcut('Ctrl+I')

    def set_Actions2StatusBar(self):

        self.ExitAction.setStatusTip('Выход')
        self.HelpAction.setStatusTip('Помощь')
        self.AboutAction.setStatusTip('О программе')

    def set_Triggers2Actions(self):
        self.ExitAction.triggered.connect(self.close)
        self.HelpAction.triggered.connect(self.help)
        self.AboutAction.triggered.connect(self.about)

    def init_Menu(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 20))
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setTitle("Файл ")
        self.helpMenu.setTitle("Справка")
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
        self.setMenuBar(self.menubar)

    def set_Actions2Menu(self):

        self.fileMenu.addAction(self.ExitAction)
        self.helpMenu.addAction(self.HelpAction)
        self.helpMenu.addAction(self.AboutAction)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', "Вы действительно хотите покинуть программу?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:

            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def about(self):
        QMessageBox.about(self, 'О программе',
                          "* Шифр Цезаря ")

    def help(self):
        QMessageBox.information(self, 'Помощь', "??")


    def EncryptCV(self):
        key = self.key.value()
        text = str(self.text1Input.toPlainText())
        text = text.upper().replace('', '')
        from prog.Alphabet import encryptCaesar
        text = encryptCaesar(key, text)
        self.text1Output.setPlainText(text)

    def DecryptCV(self):
        key = self.key.value()
        text = str(self.text1Input.toPlainText())
        text = text.upper().replace('', '')
        from prog.Alphabet import decryptCaesar
        text = decryptCaesar(key, text)
        self.text1Output.setPlainText(text)


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
