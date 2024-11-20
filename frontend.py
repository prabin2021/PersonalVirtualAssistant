
from PyQt5.QtGui import QMovie,QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class Ui_Logo(object):
    def setupUi(self, Logo):
        Logo.setWindowTitle("Jarwis")
        Logo.setWindowIcon(QIcon("C:/Users/sigde/OneDrive/Desktop/logo.png"))
        Logo.setObjectName("Logo")
        Logo.resize(1325, 815)
        self.gif_label = QtWidgets.QLabel(Logo)
        self.gif_label.setGeometry(QtCore.QRect(0, 0, 1325, 815))  # Adjust the size as per your needs
        self.gif_label.setScaledContents(True)  # Ensures the GIF scales to fit the QLabel
        
        self.movie = QMovie("C:/Users/sigde/OneDrive/Desktop/QNBH.gif")  # Make sure the path is correct
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        Logo.setStyleSheet("")
        Logo.setSizeGripEnabled(False)
        Logo.setModal(False)
        self.Face = QtWidgets.QPushButton(Logo)
        self.Face.setGeometry(QtCore.QRect(380, 740, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.Face.setFont(font)
        self.Face.setStyleSheet("QPushButton {\n"
"                background: rgb(255, 255, 0);\n"
"                border-radius: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background: rgb(255, 204, 204);  /* Pinkish glow */\n"
"                border: 2px solid rgb(255, 153, 153);\n"
"                \n"
"            }")
        self.Face.setObjectName("Face")
        # self.Face.clicked.connect(self.take_sample)
        self.Name = QtWidgets.QPushButton(Logo)
        self.Name.setGeometry(QtCore.QRect(250, 740, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.Name.setFont(font)
        self.Name.setStyleSheet("QPushButton {\n"
"                background: rgb(255, 255, 0);\n"
"                border-radius: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background: rgb(255, 204, 204);  /* Pinkish glow */\n"
"                border: 2px solid rgb(255, 153, 153);\n"
"                \n"
"            }")
        self.Name.setObjectName("Name")
        self.Start = QtWidgets.QPushButton(Logo)
        self.Start.setGeometry(QtCore.QRect(1140, 650, 161, 71))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(12)
        self.Start.setFont(font)
        self.Start.setStatusTip("")
        self.add_glow_animation(self.Start)
        self.Start.setStyleSheet("QPushButton {\n"
"                background: rgb(255, 255, 0);\n"
"                border-radius: 10px;\n"
   "background-image: url('C:/Users/sigde/OneDrive/Desktop/mic.jpg');"  # Replace with your microphone image path
"                background-repeat: no-repeat;\n"
"                background-position: center;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background: rgb(200, 255, 200);  /* Greenish glow effect */\n"
"                border: 2px solid rgb(102, 255, 102);\n"
"            \n"
"            }")
        
        icon = QtGui.QIcon.fromTheme("mike")
        self.Start.setIcon(icon)
        self.Start.setIconSize(QtCore.QSize(60, 50))
        self.Start.setObjectName("Start")
        self.Password = QtWidgets.QPushButton(Logo)
        self.Password.setGeometry(QtCore.QRect(520, 740, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setStyleSheet("QPushButton {\n"
"                background: rgb(255, 255, 0);\n"
"                border-radius: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background: rgb(255, 204, 204);  /* Pinkish glow */\n"
"                border: 2px solid rgb(255, 153, 153);\n"
"                \n"
"            }")
        self.Password.setObjectName("Password")
        self.Reset = QtWidgets.QPushButton(Logo)
        self.Reset.setGeometry(QtCore.QRect(660, 740, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.Reset.setFont(font)
        self.Reset.setStyleSheet("QPushButton {\n"
"                background: rgb(255, 255, 0);\n"
"                border-radius: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background: rgb(255, 204, 204);  /* Pinkish glow */\n"
"                border: 2px solid rgb(255, 153, 153);\n"
"                \n"
"            }")
        self.Reset.setObjectName("Reset")
        self.Terminate = QtWidgets.QPushButton(Logo)
        self.Terminate.setGeometry(QtCore.QRect(1140, 730, 161, 71))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(12)
        self.Terminate.setFont(font)
        self.Terminate.setStyleSheet("QPushButton {\n"
"                background: rgb(255, 255, 0);\n"
"                border-radius: 10px;\n"
"                background-image: url('C:/Users/sigde/OneDrive/Desktop/stop.jpg');"  # Replace with your microphone image path
"                background-repeat: no-repeat;\n"
"                background-position: center;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background: rgb(255, 102, 102);  /* Reddish glow */\n"
"                border: 2px solid rgb(255, 51, 51);\n"
"              \n"
"            }")
        self.Terminate.setObjectName("Terminate")
        self.searchbar = QtWidgets.QLineEdit(Logo)
        self.searchbar.setGeometry(QtCore.QRect(20, 680, 771, 51))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.searchbar.setFont(font)
        self.searchbar.setStyleSheet("QLineEdit {\n"
"                background: white;\n"
                "background-color: rgba(255, 255, 255, 0.3);"
"                border: 2px solid rgb(255, 255, 153);\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"            }\n"
"            QLineEdit:hover {\n"
"background-color: rgba(255, 255, 255, 0.2);"
"                background: rgb(240, 255, 240);\n"
"                border: 2px solid rgb(102, 255, 102);\n"
"            }")
        self.searchbar.setObjectName("searchbar")
        self.Clear = QtWidgets.QPushButton(Logo)
        self.Clear.setGeometry(QtCore.QRect(1110, 580, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.Clear.setFont(font)
        self.Clear.setStyleSheet("QPushButton {\n"
"                background: rgb(255, 0,0 );\n"
"                border-radius: 10px;\n"
"              \n"
"            }\n"
"            QPushButton:hover {\n"
"                border: 2px solid rgb(153, 153, 255);\n"
"                background: rgb(204, 204, 255);  /* Blueish glow */\n"
"               \n"
"            }gb(255, 255, 0)")
        self.Clear.setObjectName("Clear")
        self.chatplace = QtWidgets.QTextEdit(Logo)
        self.chatplace.setGeometry(QtCore.QRect(20, 120, 1091, 541))
        self.chatplace.setStyleSheet(" QTextEdit {\n"
"\n"
"background-color: rgba(255, 255, 255, 0.1);"
"        border: 3px solid rgb(102, 255, 102); /* Green glow when focused */\n"
"    }\n"
"    QTextEdit:hover {\n"
"background-color: rgba(255, 255, 255, 0.2);"
"        border: 3px solid rgb(255, 204, 153); /* Change border color on hover */\n"
"    }\n"
"\n"
"            @keyframes borderGlow {\n"
"                0% {\n"
"                    border-image: linear-gradient( \n"
"                        to right,\n"
"                        rgb(255, 204, 153) 0%,\n"
"                        rgb(255, 102, 102) 50%,\n"
"                        rgb(255, 204, 153) 100%\n"
"                    );\n"
"                }\n"
"                100% {\n"
"                    border-image: linear-gradient( \n"
"                        to right,\n"
"                        rgb(255, 204, 153) 100%,\n"
"                        rgb(255, 102, 102) 50%,\n"
"                        rgb(255, 204, 153) 0%\n"
"                    );\n"
"                }\n"
"            }")
        self.chatplace.setObjectName("chatplace")
        self.Date = QtWidgets.QLabel(Logo)
        self.Date.setGeometry(QtCore.QRect(1170, 130, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(10)
        self.Date.setFont(font)
        self.Date.setStyleSheet("border-radius: 10px;\n"
" background:rgb(85, 255, 255);\n"
"border: 2px solid rgb(102, 255, 102);")
        self.Date.setObjectName("Date")
        self.Time = QtWidgets.QLabel(Logo)
        self.Time.setGeometry(QtCore.QRect(1170, 210, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(10)
        self.Time.setFont(font)
        self.Time.setStyleSheet("border-radius: 10px;\n"
" background:rgb(85, 255, 255);\n"
"border: 2px solid rgb(102, 255, 102);")
        self.Time.setObjectName("Time")
        self.Temperature = QtWidgets.QLabel(Logo)
        self.Temperature.setGeometry(QtCore.QRect(1170, 290, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(10)
        self.Temperature.setFont(font)
        self.Temperature.setStyleSheet("border-radius: 10px;\n"
" background:rgb(85, 255, 255);\n"
"border: 2px solid rgb(102, 255, 102);")
        self.Temperature.setObjectName("Temperature")
        self.Clear_2 = QtWidgets.QPushButton(Logo)
        self.Clear_2.setGeometry(QtCore.QRect(710, 680, 81, 51))
        font = QtGui.QFont()
        font.setFamily("PT Bold Dusky")
        font.setPointSize(10)
        self.Clear_2.setFont(font)
        self.Clear_2.setStyleSheet("QPushButton {\n"
"                background: rgb(255, 255, 0);\n"
"                border-radius: 10px;\n"
"              \n"
"            }\n"
"            QPushButton:hover {\n"
"                border: 2px solid rgb(153, 153, 255);\n"
"                background: rgb(204, 204, 255);  /* Blueish glow */\n"
"               \n"
"            }gb(255, 255, 0)")
        self.Clear_2.setObjectName("Clear_2")
        self.label = QtWidgets.QLabel(Logo)
        self.label.setGeometry(QtCore.QRect(10, 0, 281, 71))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("""
    QLabel {
        color: white;  /* Set text color to white */
    }
""")
        self.label_2 = QtWidgets.QLabel(Logo)
        self.label_2.setGeometry(QtCore.QRect(220, 70, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("""
    QLabel {
        color: white;  /* Set text color to white */
    }
""")
        Logo.setStyleSheet("QDialog {"
                           "background-image: url('C:/Users/sigde/OneDrive/Desktop/QNBH.gif');"  # Replace with your image file name
                           "background-repeat: no-repeat;"
                           "background-position: center;"
                           "background-attachment: fixed;"
                           "}")
        self.retranslateUi(Logo)
        QtCore.QMetaObject.connectSlotsByName(Logo)
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("D:/Downloads/jarvis_ringtone.mp3")))  # Correct path to sound
        self.player.setVolume(100)  # Set volume level (0 to 100)
        self.player.play()
        self.retranslateUi(Logo)
        QtCore.QMetaObject.connectSlotsByName(Logo)
    def add_glow_animation(self, button):
        # Create a shadow effect with an animated glow
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QtGui.QColor(255, 255, 0))
        shadow.setOffset(0)
        button.setGraphicsEffect(shadow)

        # Create an animation for the glow effect
        self.animation = QtCore.QPropertyAnimation(shadow, b"blurRadius")
        self.animation.setStartValue(15)
        self.animation.setEndValue(50)
        self.animation.setDuration(1000)
        # self.animation.setLoopCount(-1)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.start()
    def retranslateUi(self, Logo):
        _translate = QtCore.QCoreApplication.translate
        self.Face.setText(_translate("Logo", "Face?"))
        self.Name.setStatusTip(_translate("Logo", "Input Your Name"))
        self.Name.setText(_translate("Logo", "Name?"))
        self.Start.setText(_translate("Logo", "Start"))
        self.Password.setText(_translate("Logo", "Password?"))
        self.Reset.setText(_translate("Logo", "Reset?"))
        self.Terminate.setText(_translate("Logo", "Terminate"))
        self.searchbar.setPlaceholderText(_translate("Logo", "Enter your query here"))
        self.Clear.setText(_translate("Logo", "Clear"))
        self.chatplace.setHtml(_translate("Logo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Date.setText(_translate("Logo", "Date"))
        self.Time.setText(_translate("Logo", "Time"))
        self.Temperature.setText(_translate("Logo", "Temperature"))
        self.Clear_2.setText(_translate("Logo", "Enter"))
        self.label.setText(_translate("Logo", "JARWIS"))
        self.label_2.setText(_translate("Logo", "The Virtual Assistant"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Logo = QtWidgets.QDialog()
    ui = Ui_Logo()
    ui.setupUi(Logo)
    Logo.show()
    sys.exit(app.exec_())

