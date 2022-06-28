from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from pytube import YouTube
import platform


class Ui_MainWindow(object):

    currentPath = "."
    pathWin = "."

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 270)
        icon = QtGui.QIcon('PYou.png')
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Link = QtWidgets.QLabel(self.centralwidget)
        self.Link.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.Link.setObjectName("Link")
        self.getlink = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.getlink.setGeometry(QtCore.QRect(120, 20, 551, 31))
        self.getlink.setObjectName("getlink")
        self.radioButtonMP3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonMP3.setEnabled(True)
        self.radioButtonMP3.setGeometry(QtCore.QRect(20, 140, 51, 20))
        self.radioButtonMP3.setObjectName("radioButtonMP3")
        self.radioButtonMP4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonMP4.setEnabled(True)
        self.radioButtonMP4.setGeometry(QtCore.QRect(20, 110, 51, 20))
        self.radioButtonMP4.setChecked(True)
        self.radioButtonMP4.setObjectName("radioButtonMP4")

        self.toolButtonPath = QtWidgets.QToolButton(self.centralwidget)
        self.toolButtonPath.setGeometry(QtCore.QRect(640, 60, 31, 31))
        self.toolButtonPath.setObjectName("toolButtonPath")
        self.toolButtonPath.clicked.connect(self.useDialog)

        self.pushButtonstart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonstart.setGeometry(QtCore.QRect(580, 120, 93, 41))
        self.pushButtonstart.setObjectName("pushButtonstart")
        self.pushButtonstart.clicked.connect(self.downloadFromYou)

        self.lableLogo = QtWidgets.QLabel(MainWindow)
        self.lableLogo.setGeometry(QtCore.QRect(280, 100, 180, 180))
        self.lableLogo.setObjectName("LableLogo")
        self.lableLogo.setPixmap(QtGui.QPixmap("PYou.png"))

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 110, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.Save = QtWidgets.QLabel(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(20, 60, 91, 31))
        self.Save.setObjectName("Save")

        self.setPath = QtWidgets.QTextEdit(self.centralwidget)
        self.setPath.setGeometry(QtCore.QRect(120, 60, 511, 31))
        self.setPath.setObjectName("setPath")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PYou"))
        self.Link.setText(_translate("MainWindow", "Enter The Link :"))
        self.radioButtonMP3.setText(_translate("MainWindow", "MP3"))
        self.radioButtonMP4.setText(_translate("MainWindow", "MP4"))
        self.toolButtonPath.setText(_translate("MainWindow", "..."))
        self.pushButtonstart.setText(_translate("MainWindow", "StartDownload"))
        self.comboBox.setItemText(0, _translate("MainWindow", "144p"))
        self.comboBox.setItemText(1, _translate("MainWindow", "240p"))
        self.comboBox.setItemText(2, _translate("MainWindow", "360p"))
        self.comboBox.setItemText(3, _translate("MainWindow", "480p"))
        self.comboBox.setItemText(4, _translate("MainWindow", "720p"))
        self.comboBox.setItemText(5, _translate("MainWindow", "1080p"))
        self.comboBox.setItemText(6, _translate("MainWindow", "1440p"))
        self.Save.setText(_translate("MainWindow", "Path For Save :"))

    def setLink(self):
        link = self.getlink.toPlainText()
        return link

    def setResolotion(self):
        resolotion = self.comboBox.currentText()
        return resolotion

    def setMovieOrSound(self):
        formatFile = ""
        if self.radioButtonMP4.isChecked():
            formatFile = self.radioButtonMP4.text()
        else:
            formatFile = self.radioButtonMP3.text()
        return formatFile

    def useDialog(self):
        self.currentPath = QFileDialog.getExistingDirectory()
        self.pathWin = self.currentPath.replace("/", "\\")
        if self.currentPath:
            self.setPath.setText(self.pathWin)

    def downloadFromYou(self):
        path = ""
        try:
            if self.showOs() == "Windows":
                path = self.pathWin
            else:
                path = self.currentPath
            yt = YouTube(self.setLink())
            yt.streams.filter(file_extension=self.setMovieOrSound()).get_by_resolution(self.setResolotion()).download(
                path
            )
            self.showMsgDownload("Finishing download ...")
        except:
            self.showMsgDownload("Please check your internet or check link and ... .\none thing is wrong!!!")

    def showMsgDownload(self, message):
        icon = QtGui.QIcon('PYou.png')
        msg = QMessageBox()
        msg.setWindowIcon(icon)
        msg.setWindowTitle("PYou")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        e = msg.exec_()

    def showOs(self):
        osName = platform.system()
        return osName


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
