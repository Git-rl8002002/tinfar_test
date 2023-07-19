# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(800, 600)
        login.setStyleSheet(u"#login_user:hover , #login_pwd:hover , #btn_login:hover , #btn_cancel:hover{\n"
"border-radius:10px;\n"
"background-color:gray;\n"
"color:white;\n"
"}\n"
"#login_user , #login_pwd , #btn_login , #btn_cancel{\n"
"border-radius:10px;\n"
"background-color:white;\n"
"}\n"
"\n"
"#label_2{\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;\n"
"background-color:gray;\n"
"color:white;\n"
"}\n"
"\n"
"#label{\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"background-color:#cccccc;\n"
"}")
        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 110, 471, 441))
        font = QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label_2 = QLabel(login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 110, 271, 441))
        font1 = QFont()
        font1.setPointSize(24)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.login_user = QLineEdit(login)
        self.login_user.setObjectName(u"login_user")
        self.login_user.setGeometry(QRect(370, 240, 291, 31))
        self.login_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_pwd = QLineEdit(login)
        self.login_pwd.setObjectName(u"login_pwd")
        self.login_pwd.setGeometry(QRect(370, 290, 291, 31))
        self.login_pwd.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_pwd.setEchoMode(QLineEdit.Password)
        self.btn_login = QPushButton(login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(370, 350, 113, 32))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../icon/icons8-arrow-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_login.setIcon(icon)
        self.btn_cancel = QPushButton(login)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(540, 350, 113, 32))
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../icon/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.login_msg = QLabel(login)
        self.login_msg.setObjectName(u"login_msg")
        self.login_msg.setGeometry(QRect(340, 420, 381, 101))
        self.login_msg.setAlignment(Qt.AlignCenter)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"TINFAR TEST", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("login", u"TINFAR TEST", None))
#if QT_CONFIG(tooltip)
        self.login_user.setToolTip(QCoreApplication.translate("login", u"\u5e33\u865f", None))
#endif // QT_CONFIG(tooltip)
        self.login_user.setPlaceholderText(QCoreApplication.translate("login", u"\u5e33\u865f", None))
#if QT_CONFIG(tooltip)
        self.login_pwd.setToolTip(QCoreApplication.translate("login", u"\u5bc6\u78bc", None))
#endif // QT_CONFIG(tooltip)
        self.login_pwd.setPlaceholderText(QCoreApplication.translate("login", u"\u5bc6\u78bc", None))
        self.btn_login.setText(QCoreApplication.translate("login", u"\u767b\u5165", None))
        self.btn_cancel.setText(QCoreApplication.translate("login", u"\u53d6\u6d88", None))
        self.login_msg.setText("")
    # retranslateUi

