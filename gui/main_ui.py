# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 733)
        icon = QIcon()
        icon.addFile(u"../icon/icons8-workstation-94.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#btn_add_new:hover , #btn_add_cancel:hover , #btn_add_del:hoverl , #m_ip:hover , #m_port:hover , #m_i_1:hover , #m_i_2:hover , #m_i_3:hover , #m_i_4:hover , #m_i_5:hover , #btn_m_request:hover {\n"
"border-radius:5px;\n"
"background-color:#cccccc;\n"
"height:31px;\n"
"}\n"
"#btn_add_new , #btn_add_cancel , #btn_add_del , #m_ip , #m_port , #m_i_1 , #m_i_2 , #m_i_3 , #m_i_4 , #m_i_5 {\n"
"border-radius:5px;\n"
"background-color:gray;\n"
"height:31px;\n"
"color:white;\n"
"}\n"
"\n"
"\n"
"#btn_m_start:hover , #btn_m_stop:hover , #btn_mouse_msg:hover , #btn_auto_click:hover , #btn_stop_click:hover , #btn_lds_i6_start:hover , #btn_lds_i6_timer_start:hover , #btn_lds_i6_timer_stop:hover , #btn_ft_i6_start:hover , #btn_ft_i6_timer_start:hover , #btn_ft_i6_timer_stop:hover , #btn_socket_client_send:hover , #btn_start_socket_server:hover , #btn_iaeris52_startLhover , #btn_iaeris52_timer_start:hover , #btn_iaeris52_timer_stop:hover , #btn_ddos_analysis_submit:hover , #ddos_anysisistics_edit:hover , #btn_reload_ddos_list:"
                        "hover , #btn_library_sd_start:hover , #btn_library_sd_stop:hover , #library_monitor_per_sec:hover{\n"
"border-radius:5px;\n"
"background-color:gray;\n"
"color:white;\n"
"height:31px;\n"
"}\n"
"#btn_m_start , #btn_m_stop ,  #btn_mouse_msg , #btn_auto_click , #btn_stop_click , #btn_lds_i6_start , #btn_lds_i6_timer_start , #btn_lds_i6_timer_stop , #btn_ft_i6_start , #btn_ft_i6_timer_start , #btn_ft_i6_timer_stop , #btn_socket_client_send , #btn_start_socket_server , #btn_iaeris52_start , #btn_iaeris52_timer_start , #btn_iaeris52_timer_stop , #btn_ddos_analysis_submit , ddos_anysisistics_edit , #btn_reload_ddos_list , #btn_library_sd_start , #btn_library_sd_stop , #library_monitor_per_sec{\n"
"border-radius:5px;\n"
"background-color:white;\n"
"height:31px;\n"
"}\n"
"\n"
"#add_date , #add_kind , #add_money , #add_content , #add_kind_comboBox , #add_no{\n"
"border-radius:5px;\n"
"height:31px;\n"
"}\n"
"\n"
"\n"
"#centralwidget{\n"
"border-radius:5px;\n"
"}")
        self.action_jnc_cb = QAction(MainWindow)
        self.action_jnc_cb.setObjectName(u"action_jnc_cb")
        icon1 = QIcon()
        icon1.addFile(u"../icon/icons8-signing-a-document-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_jnc_cb.setIcon(icon1)
        self.action_lds_I6 = QAction(MainWindow)
        self.action_lds_I6.setObjectName(u"action_lds_I6")
        icon2 = QIcon()
        icon2.addFile(u"../icon/icons8-edit-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_lds_I6.setIcon(icon2)
        self.action_Socket = QAction(MainWindow)
        self.action_Socket.setObjectName(u"action_Socket")
        icon3 = QIcon()
        icon3.addFile(u"../icon/icons8-load-balancer-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Socket.setIcon(icon3)
        self.action_DDos = QAction(MainWindow)
        self.action_DDos.setObjectName(u"action_DDos")
        icon4 = QIcon()
        icon4.addFile(u"../../scraping/icon/icons8-load-balancer-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_DDos.setIcon(icon4)
        self.action_library_sd = QAction(MainWindow)
        self.action_library_sd.setObjectName(u"action_library_sd")
        icon5 = QIcon()
        icon5.addFile(u"../icon/icons8-accounting-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_library_sd.setIcon(icon5)
        self.actionQTreeWidgets = QAction(MainWindow)
        self.actionQTreeWidgets.setObjectName(u"actionQTreeWidgets")
        icon6 = QIcon()
        icon6.addFile(u"../icon/bullet-list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQTreeWidgets.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.verticalLayout_2 = QVBoxLayout(self.page_welcome)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.page_welcome)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_welcome)
        self.page_test_treewidgets = QWidget()
        self.page_test_treewidgets.setObjectName(u"page_test_treewidgets")
        self.verticalLayout_14 = QVBoxLayout(self.page_test_treewidgets)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_17 = QGroupBox(self.page_test_treewidgets)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.test_treeWidget = QTreeWidget(self.groupBox_17)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.test_treeWidget.setHeaderItem(__qtreewidgetitem)
        self.test_treeWidget.setObjectName(u"test_treeWidget")

        self.verticalLayout_15.addWidget(self.test_treeWidget)


        self.verticalLayout_14.addWidget(self.groupBox_17)

        self.stackedWidget.addWidget(self.page_test_treewidgets)
        self.page_library_sd = QWidget()
        self.page_library_sd.setObjectName(u"page_library_sd")
        self.gridLayout_9 = QGridLayout(self.page_library_sd)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_15 = QGroupBox(self.page_library_sd)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_16 = QLabel(self.groupBox_15)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_2.addWidget(self.label_16)

        self.library_monitor_per_sec = QLineEdit(self.groupBox_15)
        self.library_monitor_per_sec.setObjectName(u"library_monitor_per_sec")

        self.horizontalLayout_2.addWidget(self.library_monitor_per_sec)

        self.label_15 = QLabel(self.groupBox_15)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_2.addWidget(self.label_15)

        self.btn_library_sd_start = QPushButton(self.groupBox_15)
        self.btn_library_sd_start.setObjectName(u"btn_library_sd_start")
        self.btn_library_sd_start.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"../icon/icons8-edit-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_library_sd_start.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.btn_library_sd_start)

        self.btn_library_sd_stop = QPushButton(self.groupBox_15)
        self.btn_library_sd_stop.setObjectName(u"btn_library_sd_stop")
        self.btn_library_sd_stop.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"../icon/icons8-close-window-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_library_sd_stop.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.btn_library_sd_stop)


        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.library_sd_list = QTreeWidget(self.groupBox_15)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.library_sd_list.setHeaderItem(__qtreewidgetitem1)
        self.library_sd_list.setObjectName(u"library_sd_list")

        self.verticalLayout_13.addWidget(self.library_sd_list)


        self.gridLayout_9.addWidget(self.groupBox_15, 0, 0, 1, 1)

        self.groupBox_16 = QGroupBox(self.page_library_sd)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_10 = QGridLayout(self.groupBox_16)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.kedge_cb_list_1 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.kedge_cb_list_1.setHeaderItem(__qtreewidgetitem2)
        self.kedge_cb_list_1.setObjectName(u"kedge_cb_list_1")

        self.gridLayout_10.addWidget(self.kedge_cb_list_1, 0, 0, 1, 1)

        self.kedge_cb_list_8 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, u"1");
        self.kedge_cb_list_8.setHeaderItem(__qtreewidgetitem3)
        self.kedge_cb_list_8.setObjectName(u"kedge_cb_list_8")

        self.gridLayout_10.addWidget(self.kedge_cb_list_8, 2, 1, 1, 1)

        self.kedge_cb_list_12 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setText(0, u"1");
        self.kedge_cb_list_12.setHeaderItem(__qtreewidgetitem4)
        self.kedge_cb_list_12.setObjectName(u"kedge_cb_list_12")

        self.gridLayout_10.addWidget(self.kedge_cb_list_12, 3, 2, 1, 1)

        self.kedge_cb_list_6 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem5 = QTreeWidgetItem()
        __qtreewidgetitem5.setText(0, u"1");
        self.kedge_cb_list_6.setHeaderItem(__qtreewidgetitem5)
        self.kedge_cb_list_6.setObjectName(u"kedge_cb_list_6")

        self.gridLayout_10.addWidget(self.kedge_cb_list_6, 1, 2, 1, 1)

        self.kedge_cb_list_9 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem6 = QTreeWidgetItem()
        __qtreewidgetitem6.setText(0, u"1");
        self.kedge_cb_list_9.setHeaderItem(__qtreewidgetitem6)
        self.kedge_cb_list_9.setObjectName(u"kedge_cb_list_9")

        self.gridLayout_10.addWidget(self.kedge_cb_list_9, 2, 2, 1, 1)

        self.kedge_cb_list_7 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem7 = QTreeWidgetItem()
        __qtreewidgetitem7.setText(0, u"1");
        self.kedge_cb_list_7.setHeaderItem(__qtreewidgetitem7)
        self.kedge_cb_list_7.setObjectName(u"kedge_cb_list_7")

        self.gridLayout_10.addWidget(self.kedge_cb_list_7, 2, 0, 1, 1)

        self.kedge_cb_list_10 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem8 = QTreeWidgetItem()
        __qtreewidgetitem8.setText(0, u"1");
        self.kedge_cb_list_10.setHeaderItem(__qtreewidgetitem8)
        self.kedge_cb_list_10.setObjectName(u"kedge_cb_list_10")

        self.gridLayout_10.addWidget(self.kedge_cb_list_10, 3, 0, 1, 1)

        self.kedge_cb_list_11 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem9 = QTreeWidgetItem()
        __qtreewidgetitem9.setText(0, u"1");
        self.kedge_cb_list_11.setHeaderItem(__qtreewidgetitem9)
        self.kedge_cb_list_11.setObjectName(u"kedge_cb_list_11")

        self.gridLayout_10.addWidget(self.kedge_cb_list_11, 3, 1, 1, 1)

        self.kedge_cb_list_2 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem10 = QTreeWidgetItem()
        __qtreewidgetitem10.setText(0, u"1");
        self.kedge_cb_list_2.setHeaderItem(__qtreewidgetitem10)
        self.kedge_cb_list_2.setObjectName(u"kedge_cb_list_2")

        self.gridLayout_10.addWidget(self.kedge_cb_list_2, 0, 1, 1, 1)

        self.kedge_cb_list_5 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem11 = QTreeWidgetItem()
        __qtreewidgetitem11.setText(0, u"1");
        self.kedge_cb_list_5.setHeaderItem(__qtreewidgetitem11)
        self.kedge_cb_list_5.setObjectName(u"kedge_cb_list_5")

        self.gridLayout_10.addWidget(self.kedge_cb_list_5, 1, 1, 1, 1)

        self.kedge_cb_list_4 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem12 = QTreeWidgetItem()
        __qtreewidgetitem12.setText(0, u"1");
        self.kedge_cb_list_4.setHeaderItem(__qtreewidgetitem12)
        self.kedge_cb_list_4.setObjectName(u"kedge_cb_list_4")

        self.gridLayout_10.addWidget(self.kedge_cb_list_4, 1, 0, 1, 1)

        self.kedge_cb_list_3 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem13 = QTreeWidgetItem()
        __qtreewidgetitem13.setText(0, u"1");
        self.kedge_cb_list_3.setHeaderItem(__qtreewidgetitem13)
        self.kedge_cb_list_3.setObjectName(u"kedge_cb_list_3")

        self.gridLayout_10.addWidget(self.kedge_cb_list_3, 0, 2, 1, 1)

        self.kedge_cb_list_13 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem14 = QTreeWidgetItem()
        __qtreewidgetitem14.setText(0, u"1");
        self.kedge_cb_list_13.setHeaderItem(__qtreewidgetitem14)
        self.kedge_cb_list_13.setObjectName(u"kedge_cb_list_13")

        self.gridLayout_10.addWidget(self.kedge_cb_list_13, 4, 0, 1, 1)

        self.kedge_cb_list_14 = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem15 = QTreeWidgetItem()
        __qtreewidgetitem15.setText(0, u"1");
        self.kedge_cb_list_14.setHeaderItem(__qtreewidgetitem15)
        self.kedge_cb_list_14.setObjectName(u"kedge_cb_list_14")

        self.gridLayout_10.addWidget(self.kedge_cb_list_14, 4, 1, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_16, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_library_sd)
        self.page_jnc_cb = QWidget()
        self.page_jnc_cb.setObjectName(u"page_jnc_cb")
        self.gridLayout = QGridLayout(self.page_jnc_cb)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(self.page_jnc_cb)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.autogui_record = QTreeWidget(self.groupBox_4)
        __qtreewidgetitem16 = QTreeWidgetItem()
        __qtreewidgetitem16.setText(0, u"1");
        self.autogui_record.setHeaderItem(__qtreewidgetitem16)
        self.autogui_record.setObjectName(u"autogui_record")

        self.verticalLayout_5.addWidget(self.autogui_record)


        self.gridLayout.addWidget(self.groupBox_4, 2, 1, 1, 1)

        self.groupBox = QGroupBox(self.page_jnc_cb)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.cb_tcp_realtime_list = QTreeWidget(self.groupBox)
        __qtreewidgetitem17 = QTreeWidgetItem()
        __qtreewidgetitem17.setText(0, u"1");
        self.cb_tcp_realtime_list.setHeaderItem(__qtreewidgetitem17)
        self.cb_tcp_realtime_list.setObjectName(u"cb_tcp_realtime_list")

        self.verticalLayout.addWidget(self.cb_tcp_realtime_list)


        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.page_jnc_cb)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_3 = QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.m_i_1 = QLineEdit(self.groupBox_5)
        self.m_i_1.setObjectName(u"m_i_1")
        self.m_i_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.m_i_1, 1, 1, 1, 1)

        self.m_port = QLineEdit(self.groupBox_5)
        self.m_port.setObjectName(u"m_port")
        self.m_port.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.m_port, 0, 3, 1, 1)

        self.btn_m_stop = QPushButton(self.groupBox_5)
        self.btn_m_stop.setObjectName(u"btn_m_stop")
        self.btn_m_stop.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_m_stop, 3, 3, 1, 1)

        self.m_i_5 = QLineEdit(self.groupBox_5)
        self.m_i_5.setObjectName(u"m_i_5")
        self.m_i_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.m_i_5, 2, 3, 1, 1)

        self.btn_m_start = QPushButton(self.groupBox_5)
        self.btn_m_start.setObjectName(u"btn_m_start")
        self.btn_m_start.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_m_start, 3, 1, 1, 1)

        self.m_i_3 = QLineEdit(self.groupBox_5)
        self.m_i_3.setObjectName(u"m_i_3")
        self.m_i_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.m_i_3, 1, 5, 1, 1)

        self.m_i_2 = QLineEdit(self.groupBox_5)
        self.m_i_2.setObjectName(u"m_i_2")
        self.m_i_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.m_i_2, 1, 3, 1, 1)

        self.m_ip = QLineEdit(self.groupBox_5)
        self.m_ip.setObjectName(u"m_ip")
        self.m_ip.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.m_ip, 0, 1, 1, 1)

        self.m_i_4 = QLineEdit(self.groupBox_5)
        self.m_i_4.setObjectName(u"m_i_4")
        self.m_i_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.m_i_4, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 4, 1, 1)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.page_jnc_cb)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(1, 1, 1, 1)
        self.btn_mouse_msg = QPushButton(self.groupBox_2)
        self.btn_mouse_msg.setObjectName(u"btn_mouse_msg")
        self.btn_mouse_msg.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_mouse_msg, 3, 2, 1, 1)

        self.btn_auto_click = QPushButton(self.groupBox_2)
        self.btn_auto_click.setObjectName(u"btn_auto_click")
        self.btn_auto_click.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_auto_click, 3, 0, 1, 1)

        self.autogui_msg = QLabel(self.groupBox_2)
        self.autogui_msg.setObjectName(u"autogui_msg")

        self.gridLayout_4.addWidget(self.autogui_msg, 0, 0, 1, 1)

        self.autogui_size = QLabel(self.groupBox_2)
        self.autogui_size.setObjectName(u"autogui_size")

        self.gridLayout_4.addWidget(self.autogui_size, 1, 0, 1, 1)

        self.btn_stop_click = QPushButton(self.groupBox_2)
        self.btn_stop_click.setObjectName(u"btn_stop_click")
        self.btn_stop_click.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_stop_click, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_jnc_cb)
        self.page_lds_i6 = QWidget()
        self.page_lds_i6.setObjectName(u"page_lds_i6")
        self.gridLayout_5 = QGridLayout(self.page_lds_i6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_12 = QGroupBox(self.page_lds_i6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.btn_iaeris52_start = QPushButton(self.groupBox_12)
        self.btn_iaeris52_start.setObjectName(u"btn_iaeris52_start")
        icon9 = QIcon()
        icon9.addFile(u"../icon/icons8-arrow-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_iaeris52_start.setIcon(icon9)

        self.verticalLayout_10.addWidget(self.btn_iaeris52_start)

        self.btn_iaeris52_timer_start = QPushButton(self.groupBox_12)
        self.btn_iaeris52_timer_start.setObjectName(u"btn_iaeris52_timer_start")
        icon10 = QIcon()
        icon10.addFile(u"../icon/icons8-download-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_iaeris52_timer_start.setIcon(icon10)

        self.verticalLayout_10.addWidget(self.btn_iaeris52_timer_start)

        self.btn_iaeris52_timer_stop = QPushButton(self.groupBox_12)
        self.btn_iaeris52_timer_stop.setObjectName(u"btn_iaeris52_timer_stop")
        icon11 = QIcon()
        icon11.addFile(u"../icon/icons8-high-priority-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_iaeris52_timer_stop.setIcon(icon11)

        self.verticalLayout_10.addWidget(self.btn_iaeris52_timer_stop)


        self.gridLayout_5.addWidget(self.groupBox_12, 2, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.page_lds_i6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.btn_lds_i6_start = QPushButton(self.groupBox_6)
        self.btn_lds_i6_start.setObjectName(u"btn_lds_i6_start")
        self.btn_lds_i6_start.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u"../icon/icons8-edit-file-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lds_i6_start.setIcon(icon12)

        self.verticalLayout_6.addWidget(self.btn_lds_i6_start)

        self.btn_lds_i6_timer_start = QPushButton(self.groupBox_6)
        self.btn_lds_i6_timer_start.setObjectName(u"btn_lds_i6_timer_start")
        self.btn_lds_i6_timer_start.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u"../icon/icons8-search-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lds_i6_timer_start.setIcon(icon13)

        self.verticalLayout_6.addWidget(self.btn_lds_i6_timer_start)

        self.btn_lds_i6_timer_stop = QPushButton(self.groupBox_6)
        self.btn_lds_i6_timer_stop.setObjectName(u"btn_lds_i6_timer_stop")
        self.btn_lds_i6_timer_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lds_i6_timer_stop.setIcon(icon8)

        self.verticalLayout_6.addWidget(self.btn_lds_i6_timer_stop)


        self.gridLayout_5.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.page_lds_i6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.btn_ft_i6_start = QPushButton(self.groupBox_8)
        self.btn_ft_i6_start.setObjectName(u"btn_ft_i6_start")
        self.btn_ft_i6_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ft_i6_start.setIcon(icon2)

        self.verticalLayout_8.addWidget(self.btn_ft_i6_start)

        self.btn_ft_i6_timer_start = QPushButton(self.groupBox_8)
        self.btn_ft_i6_timer_start.setObjectName(u"btn_ft_i6_timer_start")
        self.btn_ft_i6_timer_start.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u"../icon/icons8-new-copy-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ft_i6_timer_start.setIcon(icon14)

        self.verticalLayout_8.addWidget(self.btn_ft_i6_timer_start)

        self.btn_ft_i6_timer_stop = QPushButton(self.groupBox_8)
        self.btn_ft_i6_timer_stop.setObjectName(u"btn_ft_i6_timer_stop")
        self.btn_ft_i6_timer_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ft_i6_timer_stop.setIcon(icon8)

        self.verticalLayout_8.addWidget(self.btn_ft_i6_timer_stop)


        self.gridLayout_5.addWidget(self.groupBox_8, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.page_lds_i6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.lds_i6_list = QTreeWidget(self.groupBox_3)
        __qtreewidgetitem18 = QTreeWidgetItem()
        __qtreewidgetitem18.setText(0, u"1");
        self.lds_i6_list.setHeaderItem(__qtreewidgetitem18)
        self.lds_i6_list.setObjectName(u"lds_i6_list")
        self.lds_i6_list.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.lds_i6_list)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.page_lds_i6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.ft_i6_list = QTreeWidget(self.groupBox_7)
        __qtreewidgetitem19 = QTreeWidgetItem()
        __qtreewidgetitem19.setText(0, u"1");
        self.ft_i6_list.setHeaderItem(__qtreewidgetitem19)
        self.ft_i6_list.setObjectName(u"ft_i6_list")

        self.verticalLayout_7.addWidget(self.ft_i6_list)


        self.gridLayout_5.addWidget(self.groupBox_7, 1, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.page_lds_i6)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.iaeris52_list = QTreeWidget(self.groupBox_11)
        __qtreewidgetitem20 = QTreeWidgetItem()
        __qtreewidgetitem20.setText(0, u"1");
        self.iaeris52_list.setHeaderItem(__qtreewidgetitem20)
        self.iaeris52_list.setObjectName(u"iaeris52_list")

        self.verticalLayout_4.addWidget(self.iaeris52_list)

        self.label_13 = QLabel(self.groupBox_11)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_4.addWidget(self.label_13)

        self.realtime_progressbar = QProgressBar(self.groupBox_11)
        self.realtime_progressbar.setObjectName(u"realtime_progressbar")
        self.realtime_progressbar.setValue(24)

        self.verticalLayout_4.addWidget(self.realtime_progressbar)


        self.gridLayout_5.addWidget(self.groupBox_11, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_lds_i6)
        self.page_socket = QWidget()
        self.page_socket.setObjectName(u"page_socket")
        self.gridLayout_6 = QGridLayout(self.page_socket)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_9 = QGroupBox(self.page_socket)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_8 = QGridLayout(self.groupBox_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(1, 1, 1, 1)
        self.socket_server_list = QTreeWidget(self.groupBox_9)
        __qtreewidgetitem21 = QTreeWidgetItem()
        __qtreewidgetitem21.setText(0, u"1");
        self.socket_server_list.setHeaderItem(__qtreewidgetitem21)
        self.socket_server_list.setObjectName(u"socket_server_list")

        self.gridLayout_8.addWidget(self.socket_server_list, 1, 0, 1, 1)

        self.btn_start_socket_server = QPushButton(self.groupBox_9)
        self.btn_start_socket_server.setObjectName(u"btn_start_socket_server")

        self.gridLayout_8.addWidget(self.btn_start_socket_server, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.page_socket)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.socket_client_msg = QLineEdit(self.groupBox_10)
        self.socket_client_msg.setObjectName(u"socket_client_msg")
        self.socket_client_msg.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.socket_client_msg)

        self.btn_socket_client_send = QPushButton(self.groupBox_10)
        self.btn_socket_client_send.setObjectName(u"btn_socket_client_send")
        self.btn_socket_client_send.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_socket_client_send)

        self.socket_client_list = QTreeWidget(self.groupBox_10)
        __qtreewidgetitem22 = QTreeWidgetItem()
        __qtreewidgetitem22.setText(0, u"1");
        self.socket_client_list.setHeaderItem(__qtreewidgetitem22)
        self.socket_client_list.setObjectName(u"socket_client_list")

        self.verticalLayout_9.addWidget(self.socket_client_list)


        self.gridLayout_6.addWidget(self.groupBox_10, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_socket)
        self.page_ddos = QWidget()
        self.page_ddos.setObjectName(u"page_ddos")
        self.gridLayout_7 = QGridLayout(self.page_ddos)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_13 = QGroupBox(self.page_ddos)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ddos_anysisistics_edit = QLineEdit(self.groupBox_13)
        self.ddos_anysisistics_edit.setObjectName(u"ddos_anysisistics_edit")
        self.ddos_anysisistics_edit.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.ddos_anysisistics_edit)

        self.btn_ddos_analysis_submit = QPushButton(self.groupBox_13)
        self.btn_ddos_analysis_submit.setObjectName(u"btn_ddos_analysis_submit")
        self.btn_ddos_analysis_submit.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u"../../scraping/icon/icons8-automatic-40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ddos_analysis_submit.setIcon(icon15)

        self.horizontalLayout.addWidget(self.btn_ddos_analysis_submit)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.label_9 = QLabel(self.groupBox_13)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_11.addWidget(self.label_9)

        self.ddos_attack_ip_list = QTreeWidget(self.groupBox_13)
        __qtreewidgetitem23 = QTreeWidgetItem()
        __qtreewidgetitem23.setText(0, u"1");
        self.ddos_attack_ip_list.setHeaderItem(__qtreewidgetitem23)
        self.ddos_attack_ip_list.setObjectName(u"ddos_attack_ip_list")

        self.verticalLayout_11.addWidget(self.ddos_attack_ip_list)

        self.label_12 = QLabel(self.groupBox_13)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_11.addWidget(self.label_12)

        self.ddos_attack_ip_detail_list = QTreeWidget(self.groupBox_13)
        __qtreewidgetitem24 = QTreeWidgetItem()
        __qtreewidgetitem24.setText(0, u"1");
        self.ddos_attack_ip_detail_list.setHeaderItem(__qtreewidgetitem24)
        self.ddos_attack_ip_detail_list.setObjectName(u"ddos_attack_ip_detail_list")

        self.verticalLayout_11.addWidget(self.ddos_attack_ip_detail_list)


        self.gridLayout_7.addWidget(self.groupBox_13, 0, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.page_ddos)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_reload_ddos_list = QPushButton(self.groupBox_14)
        self.btn_reload_ddos_list.setObjectName(u"btn_reload_ddos_list")
        self.btn_reload_ddos_list.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u"../../scraping/icon/icons8-search-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reload_ddos_list.setIcon(icon16)

        self.verticalLayout_12.addWidget(self.btn_reload_ddos_list)

        self.label_10 = QLabel(self.groupBox_14)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_12.addWidget(self.label_10)

        self.ddos_statistics_list = QTreeWidget(self.groupBox_14)
        __qtreewidgetitem25 = QTreeWidgetItem()
        __qtreewidgetitem25.setText(0, u"1");
        self.ddos_statistics_list.setHeaderItem(__qtreewidgetitem25)
        self.ddos_statistics_list.setObjectName(u"ddos_statistics_list")

        self.verticalLayout_12.addWidget(self.ddos_statistics_list)

        self.label_11 = QLabel(self.groupBox_14)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.ddos_attack_ip_statistics_list = QTreeWidget(self.groupBox_14)
        __qtreewidgetitem26 = QTreeWidgetItem()
        __qtreewidgetitem26.setText(0, u"1");
        self.ddos_attack_ip_statistics_list.setHeaderItem(__qtreewidgetitem26)
        self.ddos_attack_ip_statistics_list.setObjectName(u"ddos_attack_ip_statistics_list")

        self.verticalLayout_12.addWidget(self.ddos_attack_ip_statistics_list)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_14 = QLabel(self.groupBox_14)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_3.addWidget(self.label_14)

        self.ddos_total_attack_amount = QLabel(self.groupBox_14)
        self.ddos_total_attack_amount.setObjectName(u"ddos_total_attack_amount")

        self.horizontalLayout_3.addWidget(self.ddos_total_attack_amount)


        self.verticalLayout_12.addLayout(self.horizontalLayout_3)


        self.gridLayout_7.addWidget(self.groupBox_14, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_ddos)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.action_jnc_cb)
        self.menu.addAction(self.action_library_sd)
        self.menu_2.addAction(self.action_lds_I6)
        self.menu_2.addAction(self.action_Socket)
        self.menu_3.addAction(self.action_DDos)
        self.menu_4.addAction(self.actionQTreeWidgets)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TINFAR TEST", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"Tinfar test", None))
#endif // QT_CONFIG(tooltip)
        self.action_jnc_cb.setText(QCoreApplication.translate("MainWindow", u"CB", None))
        self.action_lds_I6.setText(QCoreApplication.translate("MainWindow", u"I6", None))
#if QT_CONFIG(tooltip)
        self.action_lds_I6.setToolTip(QCoreApplication.translate("MainWindow", u"lds_I6", None))
#endif // QT_CONFIG(tooltip)
        self.action_Socket.setText(QCoreApplication.translate("MainWindow", u"Socket", None))
        self.action_DDos.setText(QCoreApplication.translate("MainWindow", u"DDos", None))
        self.action_library_sd.setText(QCoreApplication.translate("MainWindow", u"\u5317\u91ab\u5927\u5716\u66f8\u9928SD,\u6839\u57fa\u71df\u9020", None))
#if QT_CONFIG(tooltip)
        self.action_library_sd.setToolTip(QCoreApplication.translate("MainWindow", u"\u5317\u91ab\u5927\u5716\u66f8\u9928SD", None))
#endif // QT_CONFIG(tooltip)
        self.actionQTreeWidgets.setText(QCoreApplication.translate("MainWindow", u"QTreeWidgets", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TINFAR TEST", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"\u5317\u91ab\u5927\u5716\u66f8\u9928SD CO2  & \u6839\u57fa\u71df\u9020 JNC Server CB", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"per", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"sec , monitor sd co2 value.", None))
        self.btn_library_sd_start.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.btn_library_sd_stop.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"\u6839\u57fa\u71df\u9020 JNC Server CB", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"autoGUI record", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"modbusTCP - realtime", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"modbusTCP -realtime", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"address 2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PORT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"address 1", None))
        self.m_i_1.setText(QCoreApplication.translate("MainWindow", u"0x0000", None))
        self.m_i_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"item 1", None))
        self.m_port.setText(QCoreApplication.translate("MainWindow", u"502", None))
        self.m_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.btn_m_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.m_i_5.setText(QCoreApplication.translate("MainWindow", u"0x0004", None))
        self.m_i_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"item 5", None))
        self.btn_m_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.m_i_3.setText(QCoreApplication.translate("MainWindow", u"0x0002", None))
        self.m_i_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"item 3", None))
        self.m_i_2.setText(QCoreApplication.translate("MainWindow", u"0x0001", None))
        self.m_i_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"item 2", None))
        self.m_ip.setText(QCoreApplication.translate("MainWindow", u"61.220.205.144", None))
        self.m_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.m_i_4.setText(QCoreApplication.translate("MainWindow", u"0x0003", None))
        self.m_i_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"item 4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"address 3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"address 4", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"address 5", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"autoGui", None))
        self.btn_mouse_msg.setText(QCoreApplication.translate("MainWindow", u"mouse msg", None))
        self.btn_auto_click.setText(QCoreApplication.translate("MainWindow", u"Auto click", None))
        self.autogui_msg.setText(QCoreApplication.translate("MainWindow", u"position", None))
        self.autogui_size.setText(QCoreApplication.translate("MainWindow", u"size", None))
        self.btn_stop_click.setText(QCoreApplication.translate("MainWindow", u"Stop auto", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u7dad\u65b0iAeris52", None))
        self.btn_iaeris52_start.setText(QCoreApplication.translate("MainWindow", u"Get value", None))
        self.btn_iaeris52_timer_start.setText(QCoreApplication.translate("MainWindow", u"Timer(60 sec)", None))
        self.btn_iaeris52_timer_stop.setText(QCoreApplication.translate("MainWindow", u"Stop Timer", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u9023\u5927\u8208 realtime", None))
        self.btn_lds_i6_start.setText(QCoreApplication.translate("MainWindow", u"Get Value", None))
        self.btn_lds_i6_timer_start.setText(QCoreApplication.translate("MainWindow", u"Timer(60 sec)", None))
        self.btn_lds_i6_timer_stop.setText(QCoreApplication.translate("MainWindow", u"Stop Timer", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u5bcc\u6cf0 realtime", None))
        self.btn_ft_i6_start.setText(QCoreApplication.translate("MainWindow", u"Get value", None))
        self.btn_ft_i6_timer_start.setText(QCoreApplication.translate("MainWindow", u"Timer(60 sec)", None))
        self.btn_ft_i6_timer_stop.setText(QCoreApplication.translate("MainWindow", u"Stop Timer", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u9023\u5927\u8208 - I6", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u5bcc\u6cf0 - I6", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u7dad\u65b0 iAeris52", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u5373\u6642\u8b80\u53d6\u9032\u5ea6", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Socket - server", None))
        self.btn_start_socket_server.setText(QCoreApplication.translate("MainWindow", u"start socket server", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Socket - client", None))
        self.btn_socket_client_send.setText(QCoreApplication.translate("MainWindow", u"send", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"DDos ", None))
        self.btn_ddos_analysis_submit.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e DDos", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"DDos \u653b\u64caIP\u8a73\u7d30\u7d71\u8a08", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"DDos \u7d71\u8a08", None))
        self.btn_reload_ddos_list.setText(QCoreApplication.translate("MainWindow", u"Reload DDos list", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"DDos \u7e3d\u7d71\u8a08", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"DDos \u653b\u64caIP\u6b21\u6578\u7d71\u8a08", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DDos \u7e3d\u653b\u64ca\u6b21\u6578", None))
        self.ddos_total_attack_amount.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"JNC", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u9023\u5927\u8208 , \u5bcc\u6cf0", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7db2\u8def\u8cc7\u5b89", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6e2c\u8a66", None))
    # retranslateUi

