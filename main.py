#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20230220
# Update   : 20230220
# Function : money manager

import logging
import sys , pymysql , hashlib , time , os , platform , pyautogui , cv2 , keyboard , socket , threading , requests , json
from bs4 import BeautifulSoup
from pyModbusTCP.client import *
from PyQt6.QtCore import QTimer , Qt , QThread , QThreadPool, QRunnable, QMetaObject, pyqtSlot , QBasicTimer
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QWidget , QApplication , QMainWindow , QMessageBox , QTreeWidgetItem
from PyQt6.QtCharts import *

from control.dao import *
from gui.ui_login import *
from gui.ui_main import *

########################################################################################################################
#
# main_content
#
########################################################################################################################
class main_content(QMainWindow):
    
    ############
    # logging
    ############
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format , level=logging.INFO , datefmt="%H:%M:%S")
    
    #logging.disable(logging.INFO)

    #########
    # init
    #########
    def __init__(self , parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.main_init()

    ##############
    # main_init
    ##############
    def main_init(self):

        ########
        # JNC
        ########
        self.ui.action_jnc_cb.triggered.connect(self.cb_modbus_tcp)

        ##################
        # 北醫大圖書館 SD
        ##################
        self.ui.action_library_sd.triggered.connect(self.library_sd)
        self.ui.btn_library_sd_stop.setEnabled(False)

        ############
        # autogui
        ############
        self.ui.btn_mouse_msg.clicked.connect(self.autogui)
        self.ui.btn_auto_click.clicked.connect(self.start_auto)
        self.ui.btn_stop_click.clicked.connect(self.stop_auto)
        
        ################
        # 連大興 , 富泰
        ################
        self.ui.action_lds_I6.triggered.connect(self.lds_ft_i6)

        ############
        # 網路資安
        ############
        self.ui.action_DDos.triggered.connect(self.network_attack)
        self.ddos_total_attack_amount()

        ###########
        # socket
        ###########
        self.ui.action_Socket.triggered.connect(self.socket_page)
        self.ui.btn_start_socket_server.clicked.connect(self.socket_thread)
        self.ui.btn_stop_click.clicked.connect(self.socket_client)
        self.ui.btn_socket_client_send.clicked.connect(self.socket_client)

        ########
        # 測試
        ########
        self.ui.actionQTreeWidgets.triggered.connect(self.test_qtreewidgets)

        ############
        # welcome
        ############
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_welcome)
    
    ######################
    # test_qtreewidgets
    ######################
    def test_qtreewidgets(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_test_treewidgets)
        
        self.ui.test_treeWidget.clear()

        data = {"Project A":["file_a.py","file_a.txt","something.xls"],
                "Project B":["file_b.csv","photo.jpg"],
                "Project C":["file_c.exe"]}
        
        self.ui.test_treeWidget.setColumnCount(2)
        self.ui.test_treeWidget.setHeaderLabels(["Name","Type"])
        self.ui.test_treeWidget.setColumnWidth(0, 150)
        self.ui.test_treeWidget.setColumnWidth(1, 100)

        items = []
        
        '''
        for key , val in data.items():
            item = QTreeWidgetItem([key])
            for value in val:
                ext = value.split(".")[-1].upper()
                child = QTreeWidgetItem([value , ext])
                item.addChild(child)
            items.append(item)
        '''

        for key , val in data.items():
            item = QTreeWidgetItem([key])
            for val2 in val:
                ext = val2.split(".")[-1]
                child1 = QTreeWidgetItem([val2 , ext])


                child2 = QTreeWidgetItem(child1) 
                child2.setText(0, ext)

                child3 = QTreeWidgetItem(child2)
                child3.setText(0, ext)

                item.addChild(child1)

            items.append(item)
        
        self.ui.test_treeWidget.insertTopLevelItems(0 , items)

    ###############
    # library_sd
    ###############
    def library_sd(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_library_sd)

        self.ui.btn_library_sd_start.clicked.connect(self.start_library_sd_auto) 
        self.ui.btn_library_sd_stop.clicked.connect(self.stop_library_sd_auto)

    #########################
    # stop_library_sd_auto
    #########################
    def stop_library_sd_auto(self):
        try:
            self.ui.btn_library_sd_start.setEnabled(True)
            self.ui.btn_library_sd_stop.setEnabled(False)

            self.loop.stop()
            self.loop2.stop()

            self.ui.statusbar.showMessage('stop auto monitor SD CO2 value')
            logging.info('stop auto monitor SD CO2 value')
        except Exception as e:
            self.ui.statusbar.showMessage(str(e))
            logging.info(str(e))
        finally:
            pass
    
    ##########################
    # start_library_sd_auto
    ##########################
    def start_library_sd_auto(self):
        try:
            self.ui.btn_library_sd_start.setEnabled(False)
            self.ui.btn_library_sd_stop.setEnabled(True)

            ###############
            # library SD
            ###############
            per_monitor = self.ui.library_monitor_per_sec.text()

            if len(per_monitor) == 0:
                monitor_time = 10000
            else:
                monitor_time = int(per_monitor) * 1000
            
            self.loop = QTimer()
            self.loop.timeout.connect(self.start_library_sd_monitor)
            self.loop.start(monitor_time)

            #################################
            # kedge jnc server cb realtime
            #################################
            self.loop2 = QTimer()
            self.loop2.timeout.connect(self.kedge_jnc_cb_realtime)
            self.loop2.start(60000)

            self.ui.statusbar.showMessage('start auto monitor SD CO2 value')
            logging.info('start auto monitor SD CO2 value')

        except Exception as e:
            self.ui.statusbar.showMessage(str(e))
            logging.info(str(e))
        finally:
            pass

    ##########################
    # kedge_jnc_cb_realtime
    ##########################
    def kedge_jnc_cb_realtime(self):

        #######################
        # Device 1 : 南門市場
        #######################
        d_url_1      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=0&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_1     = requests.get(d_url_1)
        d_r_data_1   = d_data_1.text
        d_data_val_1 = json.loads(d_r_data_1)

        url_1      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=0&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_1     = requests.get(url_1)
        r_data_1   = data_1.text
        data_val_1 = json.loads(r_data_1)

        ### clear
        self.ui.kedge_cb_list_1.clear()
        
        self.ui.kedge_cb_list_1.setColumnCount(4)
        self.ui.kedge_cb_list_1.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_1.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_1.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_1.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_1.setColumnWidth(3 , 200)

        
        for val in data_val_1["Device"]:
            logging.info(str(d_data_val_1['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_1['Connect']))
        
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_1)
            root.setText(0,str(d_data_val_1['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_1['Connect']))

        print('\n')
        
        #######################
        # Device 2 : 桃園會展
        #######################
        d_url_2      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=1&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_2     = requests.get(d_url_2)
        d_r_data_2   = d_data_2.text
        d_data_val_2 = json.loads(d_r_data_2)

        url_2      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=1&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_2     = requests.get(url_2)
        r_data_2   = data_2.text
        data_val_2 = json.loads(r_data_2)

        ### clear
        self.ui.kedge_cb_list_2.clear()
        
        self.ui.kedge_cb_list_2.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_2.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_2.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_2.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_2.setColumnWidth(3 , 200)

        for val in data_val_2["Device"]:
            logging.info(str(d_data_val_2['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_2['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_2)
            root.setText(0,str(d_data_val_2['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_2['Connect']))
            

        print('\n')
        
        #######################
        # Device 3 : 泰山社宅
        #######################
        d_url_3      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=2&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_3     = requests.get(d_url_3)
        d_r_data_3   = d_data_3.text
        d_data_val_3 = json.loads(d_r_data_3)

        url_3      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=2&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_3     = requests.get(url_3)
        r_data_3   = data_3.text
        data_val_3 = json.loads(r_data_3)

        ### clear
        self.ui.kedge_cb_list_3.clear()
        
        self.ui.kedge_cb_list_3.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_3.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_3.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_3.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_3.setColumnWidth(3 , 200)

        for val in data_val_3["Device"]:
            logging.info(str(d_data_val_3['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_3['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_3)
            root.setText(0,str(d_data_val_3['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_3['Connect']))

        print('\n')
        
        #####################
        # Device 4 : 二重埔
        #####################
        d_url_4      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=3&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_4     = requests.get(d_url_4)
        d_r_data_4   = d_data_4.text
        d_data_val_4 = json.loads(d_r_data_4)

        url_4      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=3&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_4     = requests.get(url_4)
        r_data_4   = data_4.text
        data_val_4 = json.loads(r_data_4)
        
        ### clear
        self.ui.kedge_cb_list_4.clear()
        
        self.ui.kedge_cb_list_4.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_4.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_4.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_4.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_4.setColumnWidth(3 , 200)

        for val in data_val_4["Device"]:
            logging.info(str(d_data_val_4['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_4['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_4)
            root.setText(0,str(d_data_val_4['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_4['Connect']))

        print('\n')
        
        ########################
        # Device 5 : 民權東路案
        ########################
        d_url_5      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=4&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_5     = requests.get(d_url_5)
        d_r_data_5   = d_data_5.text
        d_data_val_5 = json.loads(d_r_data_5)

        url_5      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=4&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_5     = requests.get(url_5)
        r_data_5   = data_5.text
        data_val_5 = json.loads(r_data_5)

        ### clear
        self.ui.kedge_cb_list_5.clear()
        
        self.ui.kedge_cb_list_5.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_5.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_5.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_5.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_5.setColumnWidth(3 , 200)

        for val in data_val_5["Device"]:
            logging.info(str(d_data_val_5['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_5['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_5)
            root.setText(0,str(d_data_val_5['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_5['Connect']))

        print('\n')
        
        #######################
        # Device 6 : 秀朗橋案
        #######################
        d_url_6      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=5&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_6     = requests.get(d_url_6)
        d_r_data_6   = d_data_6.text
        d_data_val_6 = json.loads(d_r_data_6)

        url_6      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=5&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_6     = requests.get(url_6)
        r_data_6   = data_6.text
        data_val_6 = json.loads(r_data_6)

        ### clear
        self.ui.kedge_cb_list_6.clear()
        
        self.ui.kedge_cb_list_6.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_6.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_6.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_6.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_6.setColumnWidth(3 , 200)

        for val in data_val_6["Device"]:
            logging.info(str(d_data_val_6['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_6['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_6)
            root.setText(0,str(d_data_val_6['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_6['Connect']))

        print('\n')

        #####################
        # Device 7 : 裕毛屋
        #####################
        d_url_7      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=6&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_7     = requests.get(d_url_7)
        d_r_data_7   = d_data_7.text
        d_data_val_7 = json.loads(d_r_data_7)

        url_7      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=6&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_7     = requests.get(url_7)
        r_data_7   = data_7.text
        data_val_7 = json.loads(r_data_7)

        ### clear
        self.ui.kedge_cb_list_7.clear()
        
        self.ui.kedge_cb_list_7.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_7.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_7.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_7.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_7.setColumnWidth(3 , 200)

        for val in data_val_7["Device"]:
            logging.info(str(d_data_val_7['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_7['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_7)
            root.setText(0,str(d_data_val_7['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_7['Connect']))

        print('\n')

        #######################
        # Device 8 : 後龍大橋
        #######################
        d_url_8      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=7&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_8     = requests.get(d_url_8)
        d_r_data_8   = d_data_8.text
        d_data_val_8 = json.loads(d_r_data_8)

        url_8      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=7&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_8     = requests.get(url_8)
        r_data_8   = data_8.text
        data_val_8 = json.loads(r_data_8)

        ### clear
        self.ui.kedge_cb_list_8.clear()
        
        self.ui.kedge_cb_list_8.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_8.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_8.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_8.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_8.setColumnWidth(3 , 200)

        for val in data_val_8["Device"]:
            logging.info(str(d_data_val_8['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_8['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_8)
            root.setText(0,str(d_data_val_8['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_8['Connect']))

        print('\n')
        
        ################################
        # Device 9 : 嘉義車站C611世賢南
        ################################
        d_url_9      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=8&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_9     = requests.get(d_url_9)
        d_r_data_9   = d_data_9.text
        d_data_val_9 = json.loads(d_r_data_9)

        url_9      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=8&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_9     = requests.get(url_9)
        r_data_9   = data_9.text
        data_val_9 = json.loads(r_data_9)

        ### clear
        self.ui.kedge_cb_list_9.clear()
        
        self.ui.kedge_cb_list_9.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_9.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_9.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_9.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_9.setColumnWidth(3 , 200)

        for val in data_val_9["Device"]:
            logging.info(str(d_data_val_9['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_9['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_9)
            root.setText(0,str(d_data_val_9['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_9['Connect']))

        print('\n')

        ##################################
        # Device 10 : 嘉義車站C611宏仁女中
        ##################################
        d_url_10      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=9&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_10     = requests.get(d_url_10)
        d_r_data_10   = d_data_10.text
        d_data_val_10 = json.loads(d_r_data_10)

        url_10      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=9&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_10     = requests.get(url_10)
        r_data_10   = data_10.text
        data_val_10 = json.loads(r_data_10)

        ### clear
        self.ui.kedge_cb_list_10.clear()
        
        self.ui.kedge_cb_list_10.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_10.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_10.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_10.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_10.setColumnWidth(3 , 200)

        for val in data_val_10["Device"]:
            logging.info(str(d_data_val_10['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_10['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_10)
            root.setText(0,str(d_data_val_10['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_10['Connect']))

        print('\n')

        ##################################
        # Device 11 : 嘉義車站C612嘉北車站
        ##################################
        d_url_11      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=10&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_11     = requests.get(d_url_11)
        d_r_data_11   = d_data_11.text
        d_data_val_11 = json.loads(d_r_data_11)

        url_11      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=10&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_11     = requests.get(url_11)
        r_data_11   = data_11.text
        data_val_11 = json.loads(r_data_11)

        ### clear
        self.ui.kedge_cb_list_11.clear()
        
        self.ui.kedge_cb_list_11.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_11.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_11.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_11.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_11.setColumnWidth(3 , 200)

        for val in data_val_11["Device"]:
            logging.info(str(d_data_val_11['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_11['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_11)
            root.setText(0,str(d_data_val_11['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_11['Connect']))

        print('\n')
        
        ###############################
        # Device 12 : 嘉義車站C612北興
        ###############################
        d_url_12      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=11&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_12     = requests.get(d_url_12)
        d_r_data_12   = d_data_12.text
        d_data_val_12 = json.loads(d_r_data_12)

        url_12      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=11&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_12     = requests.get(url_12)
        r_data_12   = data_12.text
        data_val_12 = json.loads(r_data_12)

        ### clear
        self.ui.kedge_cb_list_12.clear()
        
        self.ui.kedge_cb_list_12.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_12.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_12.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_12.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_12.setColumnWidth(3 , 200)

        for val in data_val_12["Device"]:
            logging.info(str(d_data_val_12['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_12['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_12)
            root.setText(0,str(d_data_val_12['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_12['Connect']))

        print('\n')
        
        #############################
        # Device 13 : 台南車站一號口
        #############################
        d_url_13      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=12&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_13     = requests.get(d_url_13)
        d_r_data_13   = d_data_13.text
        d_data_val_13 = json.loads(d_r_data_13)

        url_13      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=12&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_13     = requests.get(url_13)
        r_data_13   = data_13.text
        data_val_13 = json.loads(r_data_13)

        ### clear
        self.ui.kedge_cb_list_13.clear()
        
        self.ui.kedge_cb_list_13.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_13.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_13.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_13.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_13.setColumnWidth(3 , 200)

        for val in data_val_13["Device"]:
            logging.info(str(d_data_val_13['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_13['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_13)
            root.setText(0,str(d_data_val_13['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_13['Connect']))

        print('\n')

        #############################
        # Device 14 : 台南車站四號口
        #############################
        d_url_14      = "http://www.jnc-demo.tw:11223/JSONDevice?Idx=13&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=123545"
        d_data_14     = requests.get(d_url_14)
        d_r_data_14   = d_data_14.text
        d_data_val_14 = json.loads(d_r_data_14)

        url_14      = "http://www.jnc-demo.tw:11223/JSONDeviceCH?DeviceIdx=13&Key=S2VkZ2UBNDM4NzY3NjA%3D&val=235478"
        data_14     = requests.get(url_14)
        r_data_14   = data_14.text
        data_val_14 = json.loads(r_data_14)

        ### clear
        self.ui.kedge_cb_list_14.clear()
        
        self.ui.kedge_cb_list_14.setHeaderLabels(['位置','點位測項','即時數值','連線狀況(0:斷線,1:連線中)'])
        self.ui.kedge_cb_list_14.setColumnWidth(0 , 180)
        self.ui.kedge_cb_list_14.setColumnWidth(1 , 180)
        self.ui.kedge_cb_list_14.setColumnWidth(2 , 100)
        self.ui.kedge_cb_list_14.setColumnWidth(3 , 200)

        for val in data_val_14["Device"]:
            logging.info(str(d_data_val_14['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_14['Connect']))
            
            root  = QTreeWidgetItem(self.ui.kedge_cb_list_14)
            root.setText(0,str(d_data_val_14['DeviceName']))
            root.setText(1,str(val['TagName']))
            root.setText(2,str(val['Value']) + ' ' + str(val['Unit']))
            root.setText(3,str(d_data_val_14['Connect']))


    #############################
    # start_library_sd_monitor
    #############################
    def start_library_sd_monitor(self):
        
        url      = "http://61.220.205.143:9001/sd" # 雙和
        url2     = "http://61.220.205.143:9002/sd" # 萬芳

        try:
            data     = requests.get(url2)
            r_data   = data.text.replace('&#34;', '"')
            data_val = json.loads(r_data)

            #######################
            # write txt in linux
            #######################
            if sys.platform == "linux":
                
                with open('/var/www/html/tinfar_test/txt/library_sd.txt' , 'a') as w_txt :
                    w_content =  str(data_val['date']) + ' : ' + str(data_val['sd-co2']) + '\n'
                    w_txt.write(w_content)
            
            ### clear
            self.ui.library_sd_list.clear()

            self.ui.library_sd_list.setHeaderLabels(['時間','CO2(ppm)'])
            self.ui.library_sd_list.setColumnWidth(0 , 180)
            self.ui.library_sd_list.setColumnWidth(1 , 50)
            
            root  = QTreeWidgetItem(self.ui.library_sd_list)
            root.setText(0,str(data_val['date']))
            root.setText(1,str(data_val['sd-co2']))

            print(str(data_val['date']) + ' : ' + str(data_val['sd-co2']))    

        except Exception as e:
            logging.info('< Error > library_sd : ' + str(e))
        finally:
            data.close()

    ###################
    # network_attack
    ###################
    def network_attack(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_ddos)

        self.loading_ddos_statistics()


        self.ui.btn_ddos_analysis_submit.clicked.connect(self.analysis_ddos_data)
        self.ui.btn_reload_ddos_list.clicked.connect(self.loading_ddos_statistics)
    
    #############################
    # ddos_total_attack_amount
    #############################
    def ddos_total_attack_amount(self):
        
        conn = pymysql.connect(host=tinfar_VM['host'],port=tinfar_VM['port'],user=tinfar_VM['user'],passwd=tinfar_VM['pwd'],database=tinfar_VM['db2'],charset=tinfar_VM['charset'])    
        curr = conn.cursor()

        try:
            sql = "select count(*) from network_attack"
            curr.execute(sql)
            res = curr.fetchone()

            self.ui.ddos_total_attack_amount.setText(str(res[0]))
            
        except Exception as e:
            logging.info('< Error > ddos_total_attack_amount : ' + str(e))

        finally:
            conn.commit()
            conn.close()

    
    #######################
    # analysis_ddos_data
    #######################
    def analysis_ddos_data(self):
        ddos_val = self.ui.ddos_anysisistics_edit.text()

        if len(ddos_val) < 1:
            QMessageBox.information(self , 'Msg' , 'DDos 解析，不能空白 !')
            logging.info('DDos 解析，不能空白 !')
        else:
            data  = ddos_val.split(']')
            
            ### attack ip
            data2 = data[3].split('->')
            a_ip = data2[0][1:]

            ### attack time
            data3 = data[0].split('--')
            a_time = data3[0]

            ### attack_type
            data4 = data[4][1:]
            a_type = data4

            ### attack_format
            data5 = data[5][1:]
            a_package = data5
            
            ### check ip address
            check_ip = 'https://whatismyipaddress.com/ip/' + a_ip
            header = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                }

            data6 = requests.get(check_ip , headers=header)
            data6.encoding = data6.apparent_encoding
            #soup = BeautifulSoup(data6.text , 'html.parser')
            #content = soup.findAll('span')
            #r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            #for val in content:            
                #logging.info(val.string)

            self.ui.ddos_attack_ip_list.setHeaderLabels(['攻擊時間','攻擊種類','攻擊IP','封包'])
            self.ui.ddos_attack_ip_list.setColumnWidth(0 , 180)
            self.ui.ddos_attack_ip_list.setColumnWidth(1 , 80)
            self.ui.ddos_attack_ip_list.setColumnWidth(2 , 150)
            self.ui.ddos_attack_ip_list.setColumnWidth(3 , 300)
            
            root  = QTreeWidgetItem(self.ui.ddos_attack_ip_list)
            root.setText(0,str(a_time))
            root.setText(1,str(a_type))
            root.setText(2,str(a_ip))
            root.setText(3,str(a_package))

            logging.info(a_time + ' : ' + a_ip + ' , ' + a_type + ' , ' + a_package)

            conn = pymysql.connect(host=tinfar_VM['host'],port=tinfar_VM['port'],user=tinfar_VM['user'],passwd=tinfar_VM['pwd'],database=tinfar_VM['db2'],charset=tinfar_VM['charset'])    
            curr = conn.cursor()

            ### analysis_ddos_address
            try:
                sql = "insert into network_attack(a_time , a_type , a_ip , a_package) values('{0}','{1}','{2}','{3}')".format(a_time , a_type , a_ip , a_package)
                res = curr.execute(sql)

                if res:
                    logging.info('save network attack data successful.')
                    QMessageBox.information(self , 'Msg' , 'save network attack data successful.')
                    
                    self.ui.ddos_anysisistics_edit.clear()
                    self.ui.ddos_statistics_list.clear()
                    self.ui.ddos_attack_ip_statistics_list.clear()

                    ### show attack data
                    sql = "select a_time , a_type , a_ip , a_package from network_attack order by a_time desc"    
                    curr.execute(sql)
                    res = curr.fetchall()

                    for val in res:
                        self.ui.ddos_statistics_list.setHeaderLabels(['攻擊時間','攻擊種類','攻擊IP','封包'])
                        self.ui.ddos_statistics_list.setColumnWidth(0 , 180)
                        self.ui.ddos_statistics_list.setColumnWidth(1 , 80)
                        self.ui.ddos_statistics_list.setColumnWidth(2 , 150)
                        self.ui.ddos_statistics_list.setColumnWidth(3 , 300)
                    
                        root  = QTreeWidgetItem(self.ui.ddos_statistics_list)
                        root.setText(0,str(val[0]))
                        root.setText(1,str(val[1]))
                        root.setText(2,str(val[2]))
                        root.setText(3,str(val[3]))
                    
                    ### show attack ip and total
                    sql = "select a_ip , count(*) from network_attack group by a_ip order by a_ip desc"
                    curr.execute(sql)
                    res = curr.fetchall()

                    self.ui.ddos_attack_ip_statistics_list.setHeaderLabels(['最後攻擊時間','攻擊IP','次數總計'])
                    self.ui.ddos_attack_ip_statistics_list.setColumnWidth(0 , 180)
                    self.ui.ddos_attack_ip_statistics_list.setColumnWidth(1 , 150)
                    self.ui.ddos_attack_ip_statistics_list.setColumnWidth(2 , 30)

                    for val in res:
                        
                        sql = "select a_time from network_attack where a_ip='{0}' order by a_time desc limit 0,1".format(val[0])
                        curr.execute(sql)
                        res = curr.fetchone()

                        root  = QTreeWidgetItem(self.ui.ddos_attack_ip_statistics_list)
                        root.setText(0,str(res[0]))
                        root.setText(1,str(val[0]))
                        root.setText(2,str(val[1]))

                else:
                    logging.info('save network attack data failed.')
                    QMessageBox.information(self , 'Msg' , 'save network attack data failed.')
                    self.ui.ddos_anysisistics_edit.clear()

            except Exception as e:
                logging.info('< Error > analysis_ddos_address : ' + str(e))
            finally:
                conn.commit()
                conn.close()
            
            
            ### write network attack txt file
            try:
                ### record time
                r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                r_year  = time.strftime("%Y" , time.localtime())
                r_month = time.strftime("%Y-%m" , time.localtime())
                r_day   = time.strftime("%Y-%m-%d" , time.localtime())  

                if sys.platform == 'linux':
                    add = open(txt_path['network_attack_linux'] + r_month + '.txt','a')
                    add_content = str(a_time) + ' , ' + str(a_type) + ' , ' + str(a_ip) +  ' , '  + str(a_package) + '\n'
                    add.write(add_content)

                    logging.info('write network attack txt successful.')
                elif sys.platform == 'darwin':
                    add = open(txt['network_attack_mac'] + r_month + '.txt','a')
                    add_content = str(a_time) + ' , ' + str(a_type) + ' , ' + str(a_ip) +  ' , '  + str(a_package) + '\n'
                    add.write(add_content)

                    logging.info('write network attack txt successful.')
                
            except Exception as e:
                logging.info('< Error > write network attack txt : ' + str(e))
            finally:
                add.close()

    ############################
    # loading_ddos_statistics
    ############################
    def loading_ddos_statistics(self):        
        
        ### clear ddos_statistics_list
        self.ui.ddos_statistics_list.clear()
        self.ui.ddos_attack_ip_statistics_list.clear()
        
        ### loading DDos statistics
        conn = pymysql.connect(host=tinfar_VM['host'],port=tinfar_VM['port'],user=tinfar_VM['user'],passwd=tinfar_VM['pwd'],database=tinfar_VM['db2'],charset=tinfar_VM['charset'])    
        curr = conn.cursor()
        try:
            ### show attack data
            sql = "select a_time , a_type , a_ip , a_package from network_attack order by a_time desc"    
            curr.execute(sql)
            res = curr.fetchall()

            for val in res:
                self.ui.ddos_statistics_list.setHeaderLabels(['攻擊時間','攻擊種類','攻擊IP','封包'])
                self.ui.ddos_statistics_list.setColumnWidth(0 , 180)
                self.ui.ddos_statistics_list.setColumnWidth(1 , 80)
                self.ui.ddos_statistics_list.setColumnWidth(2 , 150)
                self.ui.ddos_statistics_list.setColumnWidth(3 , 300)
            
                root  = QTreeWidgetItem(self.ui.ddos_statistics_list)
                root.setText(0,str(val[0]))
                root.setText(1,str(val[1]))
                root.setText(2,str(val[2]))
                root.setText(3,str(val[3]))
            
            
            ### show attack ip and total
            sql = "select a_ip , count(*) from network_attack group by a_ip order by a_ip desc"
            curr.execute(sql)
            res = curr.fetchall()

            self.ui.ddos_attack_ip_statistics_list.setHeaderLabels(['攻擊IP','最後攻擊時間','攻擊次數總計','IP位置'])
            self.ui.ddos_attack_ip_statistics_list.setColumnWidth(0 , 180)
            self.ui.ddos_attack_ip_statistics_list.setColumnWidth(1 , 180)
            self.ui.ddos_attack_ip_statistics_list.setColumnWidth(2 , 100)
            self.ui.ddos_attack_ip_statistics_list.setColumnWidth(3 , 200)

            for val in res:
                
                sql = "select a_time from network_attack where a_ip='{0}' order by a_time desc limit 0,1".format(val[0])
                curr.execute(sql)
                res = curr.fetchone()

                ### 攻擊 ip address
                a_url = "https://whatismyipaddress.com/ip/" + val[0]
                #a_url = "https://www.sciket.com/attention-area?tab=special-offer"
                
                header = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                }

                data6 = requests.get(a_url , headers=header)
                data6.encoding = 'utf-8'
                soup = BeautifulSoup(data6.text , 'html.parser')
                content = soup.find("title")
                #logging.info(content)
                
                r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                
                
                

                root  = QTreeWidgetItem(self.ui.ddos_attack_ip_statistics_list)
                root.setText(0,str(val[0]))
                root.setText(1,str(res[0]))
                root.setText(2,str(val[1]))
            
            ### double click show ip detail data
            self.ui.ddos_attack_ip_statistics_list.doubleClicked.connect(self.loading_ddos_statistics_ip_detail)

            logging.info('loading DDos statistics successful.')

        except Exception as e:
            logging.info('< Error > loading DDos statistics : ' + str(e))
        finally:
            conn.commit()
            conn.close()

    ######################################
    # loading_ddos_statistics_ip_detail
    ######################################
    def loading_ddos_statistics_ip_detail(self):
        
        ### clear
        self.ui.ddos_attack_ip_detail_list.clear()

        ### variable
        item = self.ui.ddos_attack_ip_statistics_list.currentItem()
        a_ip = item.text(0)

        ### loading DDos statistics
        conn = pymysql.connect(host=tinfar_VM['host'],port=tinfar_VM['port'],user=tinfar_VM['user'],passwd=tinfar_VM['pwd'],database=tinfar_VM['db2'],charset=tinfar_VM['charset'])    
        curr = conn.cursor()
        try:
            ### show attack data
            sql = "select a_time , a_type , a_ip , a_package from network_attack  where a_ip='{0}' order by a_time desc".format(a_ip)    
            curr.execute(sql)
            res = curr.fetchall()

            for val in res:
                self.ui.ddos_attack_ip_detail_list.setHeaderLabels(['攻擊時間','攻擊種類','攻擊IP','封包'])
                self.ui.ddos_attack_ip_detail_list.setColumnWidth(0 , 180)
                self.ui.ddos_attack_ip_detail_list.setColumnWidth(1 , 80)
                self.ui.ddos_attack_ip_detail_list.setColumnWidth(2 , 150)
                self.ui.ddos_attack_ip_detail_list.setColumnWidth(3 , 300)
            
                root  = QTreeWidgetItem(self.ui.ddos_attack_ip_detail_list)
                root.setText(0,str(val[0]))
                root.setText(1,str(val[1]))
                root.setText(2,str(val[2]))
                root.setText(3,str(val[3]))

        except Exception as e:
            logging.info('< Error >loading_ddos_statistics_ip_detail : ' + str(e))
        finally:
            conn.commit()
            conn.close()

    ################
    # socket_page
    ################
    def socket_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_socket)

    ##################
    # socket_client
    ##################
    def socket_client(self):
        try:
            host = '0.0.0.0'
            port = 7000
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host , port))

            outdata = self.ui.socket_client_msg.text()

            if len(outdata) == 0:
                QMessageBox.information(self , 'Msg' , '不能是空白')
            else:
                self.ui.socket_client_list.setHeaderLabels(['主機','訊息'])
                self.ui.socket_client_list.setColumnWidth(0,180)
                self.ui.socket_client_list.setColumnWidth(1,180)

                self.root = QTreeWidgetItem(self.ui.socket_client_list)
                self.root.setText(0 , 'send')
                self.root.setText(1 , str(outdata))

                s.send(outdata.encode("utf-8"))

                indata = s.recv(1024)
                self.root = QTreeWidgetItem(self.ui.socket_client_list)
                self.root.setText(0 , 'Server')
                self.root.setText(1 , indata.decode("utf-8"))

                s.close()

        except Exception as e:
            logging.info('< Error > socket_client : ' + str(e))
        finally:
            pass

    ##################
    # socket_thread
    ##################
    def socket_thread(self):
        try:
            #qt = QThread()
            #qt.run = self.socket_server
            #qt.start()
            logging.info("socket server thread start")
            
            t = threading.Thread(target=self.socket_server)
            t.start()

            logging.info("socket server thread running...")

        except Exception as e:
            self.ui.statusbar.showMessage("< Error > socket thread : " + str(e))
            logging.info("< Error > socket thread : " + str(e))
        finally:
            pass

    ##################
    # socket_server
    ##################
    def socket_server(self):

        ### server
        try:
            host = '0.0.0.0'
            port = 7000
            
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(1)

            self.ui.socket_server_list.setHeaderLabels(['主機','訊息'])
            self.ui.socket_server_list.setColumnWidth(0,100)
            self.ui.socket_server_list.setColumnWidth(1,180)

            self.root = QTreeWidgetItem(self.ui.socket_server_list)
            self.root.setText(0 , 'Server')
            self.root.setText(1 , str(host) + ' , port : ' + str(port) + ' , wait for connection...')

            while True:
                conn , addr = s.accept()
                self.root = QTreeWidgetItem(self.ui.socket_server_list)
                self.root.setText(0 , 'Server')
                self.root.setText(1 , 'connected by ' + str(addr))

                indata = conn.recv(1024)
                self.root = QTreeWidgetItem(self.ui.socket_server_list)
                self.root.setText(0 , 'Client')
                self.root.setText(1 , str(indata.decode("utf-8")))

                outdata = 'echo ' + str(indata.decode("utf-8"))
                conn.send(outdata.encode("utf-8"))
                self.root = QTreeWidgetItem(self.ui.socket_server_list)
                self.root.setText(0 , 'Server')
                self.root.setText(1 , outdata)
                conn.close()

        except Exception as e:
            logging.info('< Error > socket server : ' + str(e))
        finally:
            s.close()
        
    
    ###########
    # lds_i6
    ###########
    def lds_ft_i6(self):
        
        self.ui.btn_lds_i6_timer_stop.setEnabled(False)
        self.ui.btn_ft_i6_timer_stop.setEnabled(False)
        self.ui.btn_iaeris52_timer_stop.setEnabled(False)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_lds_i6)
        
        ### 連大興 lds 
        self.ui.btn_lds_i6_start.clicked.connect(self.lds_i6_monitor)
        self.ui.btn_lds_i6_timer_start.clicked.connect(self.lds_ft_i6_timer_start)
        self.ui.btn_lds_i6_timer_stop.clicked.connect(self.lds_ft_i6_timer_stop)

        ### 富泰 ft
        self.ui.btn_ft_i6_start.clicked.connect(self.ft_i6_monitor)
        self.ui.btn_ft_i6_timer_start.clicked.connect(self.lds_ft_i6_timer_start)
        self.ui.btn_ft_i6_timer_stop.clicked.connect(self.lds_ft_i6_timer_stop)

        ### 維新 iAeris52
        self.ui.btn_iaeris52_start.clicked.connect(self.iaeris52_monitor)
        self.ui.btn_iaeris52_timer_start.clicked.connect(self.lds_ft_i6_timer_start)
        self.ui.btn_iaeris52_timer_stop.clicked.connect(self.lds_ft_i6_timer_stop)

    #########################
    # lds_ft_i6_timer_stop
    #########################
    def lds_ft_i6_timer_stop(self):
        
        self.ui.statusbar.showMessage("stop lds , ft I6 , iAeris52 monitor timer (60 sec.)")
        
        ########################
        # iaeris52 timer stop 
        ########################
        self.ui.btn_iaeris52_timer_start.setEnabled(True)
        self.ui.btn_iaeris52_timer_stop.setEnabled(False)
        try:
            self.start_iaeris52.stop()
            logging.info("stop iaeris52 timer")
        except Exception as e:
            logging.info("< Error > iaeris52_timer_stop : " + str(e))
        finally:
            pass
        
        ######################
        # lds i6 timer stop 
        ######################
        self.ui.btn_lds_i6_timer_start.setEnabled(True)
        self.ui.btn_lds_i6_timer_stop.setEnabled(False)
        try:
            self.start_lds.stop()
            logging.info("stop lds i6 timer")
        except Exception as e:
            logging.info("< Error > lds_i6_timer_stop : " + str(e))
        finally:
            pass
        
        #####################
        # ft i6 timer stop
        #####################
        self.ui.btn_ft_i6_timer_start.setEnabled(True)
        self.ui.btn_ft_i6_timer_stop.setEnabled(False)
        try:
            self.start_ft.stop()
            logging.info("stop ft i6 timer")
        except Exception as e:
            logging.info("< Error > ft_i6_timer_stop : " + str(e))
        finally:
            pass
    
    #######################
    # lds_ft_i6_timer_start
    #######################
    def lds_ft_i6_timer_start(self):
        
        self.ui.statusbar.showMessage("start lds , ft I6 , iAeris52 monitor timer (60 sec.)")
        logging.info("start lds , ft I6 , iAeris52 monitor timer (60 sec.)")

        ###################
        # iAeris52 timer
        ###################
        '''
        self.ui.btn_iaeris52_timer_start.setEnabled(False)
        self.ui.btn_iaeris52_timer_stop.setEnabled(True)

        self.start_iaeris52 = QTimer()
        try:
            self.start_iaeris52.timeout.connect(self.iaeris52_monitor)
            self.start_iaeris52.start(60000)
            ### realtime progressbar
            self.ui.realtime_progressbar.setValue(30)
        except Exception as e:
            logging.info("< Error > iAeris52_timer_start : " + str(e))
        finally:
            pass
        '''
        
        #################
        # lds i6 timer
        #################
        self.ui.btn_lds_i6_timer_start.setEnabled(False)
        self.ui.btn_lds_i6_timer_stop.setEnabled(True)

        self.start_lds = QTimer()
        try:
            self.start_lds.timeout.connect(self.lds_i6_monitor)
            self.start_lds.start(60000)

        except Exception as e:
            logging.info("< Error > lds_i6_timer_start : " + str(e))
        finally:
            pass

        ################
        # ft i6 timer
        ################
        self.ui.btn_ft_i6_timer_start.setEnabled(False)
        self.ui.btn_ft_i6_timer_stop.setEnabled(True)

        self.start_ft = QTimer()
        try:
            self.start_ft.timeout.connect(self.ft_i6_monitor)
            self.start_ft.start(60000)
            
        except Exception as e:
            logging.info("< Error > lds_i6_timer_start : " + str(e))
        finally:
            pass
        

    #####################
    # iaeris52_monitor
    #####################
    def iaeris52_monitor(self):
        ### record time
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%Y-%m" , time.localtime())
        r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 

        self.ui.statusbar.showMessage("start iAeris52 monitor now value (60 sec.)")
        logging.info("start iAeris52 monitor now value (60 sec.)")
        
        #########
        # JSON
        #########
        json_url = requests.get(iaeris52['json_url'])
        json_val = json_url.text.strip('(').strip(')')
        json_val = json.loads(json_val)
        
        try:
            self.ui.iaeris52_list.setHeaderLabels(['日期','設備','序號','溫度 °C','濕度 %','二氧化碳 ppm','PM2.5 ppm'])
            self.ui.iaeris52_list.setColumnWidth(0,180)
            self.ui.iaeris52_list.setColumnWidth(1,100)
            self.ui.iaeris52_list.setColumnWidth(2,180)
            self.ui.iaeris52_list.setColumnWidth(3,100)
            self.ui.iaeris52_list.setColumnWidth(4,100)
            self.ui.iaeris52_list.setColumnWidth(5,100)
            self.ui.iaeris52_list.setColumnWidth(6,100)

            self.root = QTreeWidgetItem(self.ui.iaeris52_list)
            self.root.setText(0 , str(json_val['date']))
            self.root.setText(1 , str(json_val['PID']))
            self.root.setText(2 , str(json_val['SNO']))
            self.root.setText(3 , str(json_val['Temperature']) + ' °C')
            self.root.setText(4 , str(json_val['RH']) + ' %')
            self.root.setText(5 , str(json_val['CO2']) + ' ppm')
            self.root.setText(6 , str(json_val['PM2_5']) + ' ppm')

        except Exception as e:
            logging.info("< Error > start_iAeris52_monitor : " + str(e))
        finally:
            pass

    ###################
    # ft_i6_monitor
    ###################
    def ft_i6_monitor(self):
        
        ### record time
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%Y-%m" , time.localtime())
        r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 

        self.ui.statusbar.showMessage("start ft I6 monitor now value (60 sec.)")
        logging.info("start ft I6 monitor now value (60 sec.)")

        ### realtime progressbar
        self.ui.realtime_progressbar.setValue(80)
        
        ##############
        # modbusTCP
        ##############
        ft_i6_tcp = ModbusClient(host=ft_i6['ip'],port=ft_i6['port'],auto_open=True,auto_close=True,debug=False)
        
        try:
            ### PH 酸鹼
            ft_i6_val1 = ft_i6_tcp.read_input_registers(int(ft_i6['ph'],16),1)
            ### EC 導電度
            ft_i6_val2 = ft_i6_tcp.read_input_registers(int(ft_i6['ec'],16),1)
            ### watch temp 水溫
            ft_i6_val3 = ft_i6_tcp.read_input_registers(int(ft_i6['temp'],16),1)
            ### mf 瞬間流量
            ft_i6_val4 = ft_i6_tcp.read_input_registers(int(ft_i6['mt'],16),1)
            ### cf 累計流量
            ft_i6_val5 = ft_i6_tcp.read_input_registers(int(ft_i6['cf'],16),1)
            
            self.ui.ft_i6_list.setHeaderLabels(['日期','設備','酸鹼度 PH','導電度 EC','水溫 TEMP','瞬間流量 MT',' 累計流量 CF'])
            self.ui.ft_i6_list.setColumnWidth(0,180)
            self.ui.ft_i6_list.setColumnWidth(1,100)
            self.ui.ft_i6_list.setColumnWidth(2,100)
            self.ui.ft_i6_list.setColumnWidth(3,100)
            self.ui.ft_i6_list.setColumnWidth(4,100)
            self.ui.ft_i6_list.setColumnWidth(5,100)
            self.ui.ft_i6_list.setColumnWidth(6,100)

            self.root = QTreeWidgetItem(self.ui.ft_i6_list)
            self.root.setText(0 , str(r_time))
            self.root.setText(1 , '富泰 I6')
            self.root.setText(2 , str(ft_i6_val1[0]/100) + ' pH')
            self.root.setText(3 , str(ft_i6_val2[0]) + ' us/cm')
            self.root.setText(4 , str(ft_i6_val3[0]/10) + ' °C')
            self.root.setText(5 , str(ft_i6_val4[0]/100) + ' M3/H')
            self.root.setText(6 , str(ft_i6_val5[0]) + ' M3')

            ### realtime progressbar
            self.ui.realtime_progressbar.setValue(100)

        except Exception as e:
            logging.info("< Error > start_ft_i6_monitor : " + str(e))
        finally:
            ft_i6_tcp.close()

    ###################
    # lds_i6_monitor
    ###################
    def lds_i6_monitor(self):
        
        ### record time
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%Y-%m" , time.localtime())
        r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 

        self.ui.statusbar.showMessage("start lds I6 monitor now value (60 sec.)")
        logging.info("start lds I6 monitor now value (60 sec.)")

        ### realtime progressbar
        self.ui.realtime_progressbar.setValue(20)
        
        ##############
        # modbusTCP
        ##############
        lds_i6_tcp = ModbusClient(host=lds_i6['ip'],port=lds_i6['port'],auto_open=True,auto_close=True,debug=False)
        
        try:
            ### PH 酸鹼
            lds_i6_val1 = lds_i6_tcp.read_input_registers(int(lds_i6['ph'],16),1)
            ### EC 導電度
            lds_i6_val2 = lds_i6_tcp.read_input_registers(int(lds_i6['ec'],16),1)
            ### watch temp 水溫
            lds_i6_val3 = lds_i6_tcp.read_input_registers(int(lds_i6['temp'],16),1)
            ### mf 瞬間流量
            lds_i6_val4 = lds_i6_tcp.read_input_registers(int(lds_i6['mt'],16),1)
            ### cf 累計流量
            lds_i6_val5 = lds_i6_tcp.read_input_registers(int(lds_i6['cf'],16),1)
            
            self.ui.lds_i6_list.setHeaderLabels(['日期','設備','酸鹼度 PH','導電度 EC','水溫 TEMP','瞬間流量 MT',' 累計流量 CF'])
            self.ui.lds_i6_list.setColumnWidth(0,180)
            self.ui.lds_i6_list.setColumnWidth(1,100)
            self.ui.lds_i6_list.setColumnWidth(2,100)
            self.ui.lds_i6_list.setColumnWidth(3,100)
            self.ui.lds_i6_list.setColumnWidth(4,100)
            self.ui.lds_i6_list.setColumnWidth(5,100)
            self.ui.lds_i6_list.setColumnWidth(6,100)

            self.root = QTreeWidgetItem(self.ui.lds_i6_list)
            self.root.setText(0 , str(r_time))
            self.root.setText(1 , '連大興 I6')
            self.root.setText(2 , str(lds_i6_val1[0]/100) + ' pH')
            self.root.setText(3 , str(lds_i6_val2[0]) + ' us/cm')
            self.root.setText(4 , str(lds_i6_val3[0]/10) + ' °C')
            self.root.setText(5 , str(lds_i6_val4[0]/100) + ' M3/H')
            self.root.setText(6 , str(lds_i6_val5[0]) + ' M3')

            ### realtime progressbar
            self.ui.realtime_progressbar.setValue(60)

        except Exception as e:
            logging.info("< Error > start_lds_i6_monitor : " + str(e))
        finally:
            lds_i6_tcp.close()
    
    ##############
    # stop_auto
    ##############
    def stop_auto(self):
        try:
            self.ui.btn_auto_click.setEnabled(True)
            self.ui.btn_stop_click.setEnabled(False)

            self.loop.stop()

            self.ui.statusbar.showMessage('stop auto click')
            logging.info('stop auto click')
        except Exception as e:
            self.ui.statusbar.showMessage(str(e))
            logging.info(str(e))
        finally:
            pass

    ###############
    # start_auto
    ###############
    def start_auto(self):
        try:
            self.ui.btn_auto_click.setEnabled(False)
            self.ui.btn_stop_click.setEnabled(True)
            
            self.loop = QTimer()
            self.loop.timeout.connect(self.auto_click)
            self.loop.start(60000)

            self.ui.statusbar.showMessage('start auto click')
            logging.info('start auto click')
        except Exception as e:
            self.ui.statusbar.showMessage(str(e))
            logging.info(str(e))
        finally:
            pass
    
    def auto_click(self):
        try:
            
            self.ui.autogui_record.setHeaderLabels(['日期','操作內容'])
            self.ui.autogui_record.setColumnWidth(0,180)
            self.ui.autogui_record.setColumnWidth(1,300)
            
            r_time3 = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            r_day   = time.strftime("%Y-%m-%d" , time.localtime())
            pyautogui.click(1812 , 8 , duration=1)
            self.ui.statusbar.showMessage(str('1).' + r_time3 + ' click 新聞'))
            self.root = QTreeWidgetItem(self.ui.autogui_record)
            self.root.setText(0 , str(r_time3))
            self.root.setText(1 , 'click 新聞')
            
            if platform.system() == 'Darwin':
                self.add = open(txt['mac_path'] + r_day + '.txt','a')
                self.add.write(r_time3 + ' , click 新聞\n')
                self.add.close()
            elif platform.system() == 'Linux':
                self.add = open(txt['linux_path'] + r_day + '.txt','a')
                self.add.write(r_time3 + ' , click 新聞\n')
                self.add.close()
            
            
            r_time3 = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            r_day   = time.strftime("%Y-%m-%d" , time.localtime())
            pyautogui.click(1817 , 42 , duration=1)
            self.ui.statusbar.showMessage('2).' + r_time3 + ' click 新聞/news , wait 20 sec')
            self.root = QTreeWidgetItem(self.ui.autogui_record)
            self.root.setText(0 , str(r_time3))
            self.root.setText(1 , 'click 新聞/news , wait 20 sec')
            
            if platform.system() == 'Darwin':
                self.add = open(txt['mac_path'] + r_day + '.txt','a')
                self.add.write(r_time3 + ' , click 新聞/news , wait 20 sec\n')
                self.add.close()
            elif platform.system() == 'Linux':
                self.add = open(txt['linux_path'] + r_day + '.txt','a')
                self.add.write(r_time3 + ' , click 新聞/news , wait 20 sec\n')
                self.add.close()
            time.sleep(20)
            
            r_time3 = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            r_day   = time.strftime("%Y-%m-%d" , time.localtime())
            pyautogui.click(3454 , 155 , duration=1)
            self.ui.statusbar.showMessage('3).' + r_time3 + ' click 新聞/news/ET news statistics , wait 30 sec')
            self.root = QTreeWidgetItem(self.ui.autogui_record)
            self.root.setText(0 , str(r_time3))
            self.root.setText(1 , 'click 新聞/news/ET news statistics , wait 20 sec')

            if platform.system() == 'Darwin':
                self.add = open(txt['mac_path'] + r_day + '.txt','a')
                self.add.write(r_time3 + ' , click 新聞/news/ET news statistics , wait 20 sec\n')
                self.add.close()
            elif platform.system() == 'Linux':
                self.add = open(txt['linux_path'] + r_day + '.txt','a')
                self.add.write(r_time3 + ' , click 新聞/news/ET news statistics , wait 20 sec\n')
                self.add.close()
            time.sleep(20)

            r_time3 = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            r_day   = time.strftime("%Y-%m-%d" , time.localtime())
            pyautogui.click(2256 , 240 , duration=1)
            self.ui.statusbar.showMessage('4).' + r_time3 + ' click close 新聞/news/ET news statistics')   
            self.root = QTreeWidgetItem(self.ui.autogui_record)
            self.root.setText(0 , str(r_time3))
            self.root.setText(1 , 'click close 新聞/news/ET news statistics')
            
            if platform.system() == 'Darwin':
                self.add = open(txt['mac_path'] + r_day + '.txt','a')
                self.add.write(r_time3 + ' , click close 新聞/news/ET news statistics\n\n')
                self.add.close()
            elif platform.system() == 'Linux':
                self.add = open(txt['linux_path'] + r_day + '.txt','a')
                self.add.write(r_time3 + ' , click close 新聞/news/ET news statistics\n\n')
                self.add.close()
            
            

        except Exception as e:
            self.ui.statusbar.showMessage(str(e))
        finally:
            pass


    ############
    # autogui
    ############
    def autogui(self):
        try:
            
            msg = {'msg1':'test msg 1' ,'msg2':'test msg 2' ,'msg3':'test msg 3' }

            pyautogui.click(2073,1002,duration=1)
            pyautogui.typewrite(msg['msg1'])
            pyautogui.click(1900,1040,duration=1)
            pyautogui.click(2073,1002,duration=1)
            pyautogui.hotkey('shift','ctrl','left')
            pyautogui.press('delete')

            time.sleep(60)

            pyautogui.click(2073,1002,duration=1)
            pyautogui.typewrite(msg['msg2'])
            pyautogui.click(1900,1040,duration=1)
            pyautogui.hotkey('shift','ctrl','left')
            pyautogui.press('delete')
            

            time.sleep(60)

            pyautogui.click(2073,1002,duration=1)
            pyautogui.typewrite(msg['msg3'])
            pyautogui.click(1900,1040,duration=1)
            pyautogui.hotkey('shift','ctrl','left')
            pyautogui.press('delete')


        except Exception as e:
            logging.info('< Error > autogui : ' + str(e))
        finally:
            pass
    
    ##################
    # cb_modbus_tcp
    ##################
    def cb_modbus_tcp(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_jnc_cb)
        
        self.ui.btn_m_start.clicked.connect(self.timer_start_cb_modbus_tcp)
        self.ui.btn_m_stop.clicked.connect(self.timer_stop_cb_modbus_tcp)

    #############################
    # timer_stop_cb_modbus_tcp
    #############################
    def timer_stop_cb_modbus_tcp(self):
        try:
            self.ui.btn_m_start.setEnabled(True)
            self.ui.btn_m_stop.setEnabled(False)
            
            #self.t_run.stop()
            self.t_run2.stop()
            logging.info('stop cb modbusTCP')

        except Exception as e:
            logging.info('< Error > timer_stop_cb_modbus_tcp : ' + str(e))
        finally:
            pass

    ##############################
    # timer_start_cb_modbus_tcp
    ##############################
    def timer_start_cb_modbus_tcp(self):
        try:
            self.ui.btn_m_start.setEnabled(False)
            self.ui.btn_m_stop.setEnabled(True)
            
            #self.t_run = QTimer()
            #self.t_run.timeout.connect(self.cb_modbus_tcp2)
            #self.t_run.start(60000)

            self.t_run2 = QTimer()
            self.t_run2.timeout.connect(self.conn_modbudtcp)
            self.t_run2.start(5000)

            logging.info('start cb modbusTCP...')

        except Exception as e:
            logging.info('< Error > timer_start_cb_modbus_tcp : ' + str(e))
        finally:
            pass

    ###################
    # conn_modbudtcp
    ###################
    def conn_modbudtcp(self):
        try:
            ### variables
            s_ip     = self.ui.m_ip.text()
            s_port   = int(self.ui.m_port.text())
            s_item_1 = self.ui.m_i_1.text()
            s_item_2 = self.ui.m_i_2.text()
            s_item_3 = self.ui.m_i_3.text()
            s_item_4 = self.ui.m_i_4.text()
            s_item_5 = self.ui.m_i_5.text()
            self.s_item = {'temp':s_item_1 , 'rh':s_item_2 , 'pr':s_item_3 , 'nh3':s_item_4 , 'h2s':s_item_5}
            
            self.i6 = ModbusClient(host=s_ip,port=s_port,auto_open=True,auto_close=True,debug=False)
            
            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
            
            ### 溫度 temp
            self.i6_val1 = self.i6.read_input_registers(int(self.s_item['temp'],16),1)
            ### 濕度 rh
            self.i6_val2 = self.i6.read_input_registers(int(self.s_item['rh'],16),1)
            ### 大氣壓力 pr
            self.i6_val3 = self.i6.read_input_registers(int(self.s_item['pr'],16),1)
            ### 氨氣 nh3
            self.i6_val4 = self.i6.read_input_registers(int(self.s_item['nh3'],16),1)
            ### 硫化氫 
            self.i6_val5 = self.i6.read_input_registers(int(self.s_item['h2s'],16),1)
            
            self.ui.cb_tcp_realtime_list.setHeaderLabels(['日期','設備','TEMP','RH','PR','NH3','H2S'])
            self.ui.cb_tcp_realtime_list.setColumnWidth(0,180)
            self.ui.cb_tcp_realtime_list.setColumnWidth(1,80)
            self.ui.cb_tcp_realtime_list.setColumnWidth(2,80)
            self.ui.cb_tcp_realtime_list.setColumnWidth(3,80)
            self.ui.cb_tcp_realtime_list.setColumnWidth(4,80)
            self.ui.cb_tcp_realtime_list.setColumnWidth(5,80)
            self.ui.cb_tcp_realtime_list.setColumnWidth(6,80)

            self.root = QTreeWidgetItem(self.ui.cb_tcp_realtime_list)
            self.root.setText(0 , str(self.r_time))
            self.root.setText(1 , 'CB')
            self.root.setText(2 , str(self.i6_val1[0]/10) + ' °C')
            self.root.setText(3 , str(self.i6_val2[0]/10) + ' %')
            self.root.setText(4 , str(self.i6_val3[0]/10) + ' hPa')
            self.root.setText(5 , str(self.i6_val4[0]/10) + ' ppm')
            self.root.setText(6 , str(self.i6_val5[0]/10) + ' ppm')

            ##############
            # save file
            ##############
            add_txt = self.r_time + ' , ' + str(self.i6_val1[0]/10) + ' °C , ' + str(self.i6_val2[0]/10) + ' % , ' + str(self.i6_val3[0]/10) + ' hPa , ' + str(self.i6_val4[0]/10) + ' ppm , ' + str(self.i6_val5[0]/10) + ' ppm\n'
            if platform.system() == 'Linux':
                add     = open(txt['linux_path'] + self.r_day + '_CB' + '.txt','a')
                add.write(add_txt)
                add.close()
            elif platform.system() == 'Darwin':
                add     = open(txt['mac_path'] + self.r_day + '_CB' + '.txt','a')
                add.write(add_txt)
                add.close()
            
        except Exception as e:
            logging.info('< Error > conn_modbudtcp : ' + str(e) + '\n') 
        finally:
            self.i6.close()
    
    ##################
    # cb_modbus_tcp
    ##################
    def cb_modbus_tcp2(self):
        
        try:
            ### variables
            ip     = self.ui.m_ip.text()
            port   = self.ui.m_port.text()
            item_1 = self.ui.m_i_1.text()
            item_2 = self.ui.m_i_2.text()
            item_3 = self.ui.m_i_3.text()
            item_4 = self.ui.m_i_4.text()
            item_5 = self.ui.m_i_5.text()

            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y_%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 

            self.conn = pymysql.connect(host=tinfar_VM['host'],port=tinfar_VM['port'],user=tinfar_VM['user'],passwd=tinfar_VM['pwd'],database=tinfar_VM['db'],charset=tinfar_VM['charset'])    
            self.curr = self.conn.cursor()
            self.sql = "select r_time , s_kind , val_1 , val_2 , val_3 , val_4 , val_5 from {0} order by r_time desc limit 0,1".format(self.r_month)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.cb_tcp_list.setHeaderLabels(['日期','設備','TEMP','RH','PR','NH3','H2S'])
            self.ui.cb_tcp_list.setColumnWidth(0,180)
            self.ui.cb_tcp_list.setColumnWidth(1,80)
            self.ui.cb_tcp_list.setColumnWidth(2,80)
            self.ui.cb_tcp_list.setColumnWidth(3,80)
            self.ui.cb_tcp_list.setColumnWidth(4,80)
            self.ui.cb_tcp_list.setColumnWidth(5,80)
            self.ui.cb_tcp_list.setColumnWidth(6,80)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.cb_tcp_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2] + '°C'))
                self.root.setText(3 , str(val[3] + '%'))
                self.root.setText(4 , str(val[4] + 'hPa'))
                self.root.setText(5 , str(val[5] + 'ppm'))
                self.root.setText(6 , str(val[6] + 'ppm'))

        except Exception as e:
            logging.info('< Error > cb_modbus_tcp : ' + str(e))
        finally:
            self.conn.commit()
            self.conn.close()

    

########################################################################################################################
#
# login
#
########################################################################################################################
class login(QWidget):
    
    ############
    # logging
    ############
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format , level=logging.INFO , datefmt="%H:%M:%S")

    #########
    # init
    #########
    def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = Ui_login()
            self.ui.setupUi(self)
            self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
            
            self.login_init()

    ###############
    # login_init
    ###############
    def login_init(self):
        try:
            ### cancel 
            self.ui.btn_cancel.clicked.connect(self.login_cancel)

            ### login
            self.ui.btn_login.clicked.connect(self.login_submit)

        except Exception as e:
            logging.info('< Error > login_init : ' + str(e))

    #################
    # login_submit
    #################
    def login_submit(self):
        try:
            ### variables
            self.user = self.ui.login_user.text()
            self.pwd = self.ui.login_pwd.text()

            ### pwd encode MD5
            self.pwd_str = hashlib.md5()
            self.pwd_str.update(self.pwd.encode(encoding='utf8'))
            self.pwd_md5 = self.pwd_str.hexdigest()
            
            if len(self.user) == 0 or len(self.pwd) == 0:

                self.ui.login_msg.setStyleSheet('color:red;background-color:white;')
                self.ui.login_msg.setText('帳密不能空白 !!!')

                logging.info('帳密不能空白 !!!')

            elif self.user != 'rl8002002' or self.pwd_md5 != '274aca9430419de1a941eddcd4b647a0':

                self.ui.login_msg.setStyleSheet('color:red')
                self.ui.login_msg.setText('帳密不對 !!!')

                logging.info('帳密不對 !!!')

            else:
                self.close()
                self.main = main_content()
                self.main.show()

        except Exception as e:
            logging.info('< Error > login_submit : ' + str(e))
    
    #################
    # login_cancel
    #################
    def login_cancel(self):
        try:
            QApplication.closeAllWindows()
        except Exception as e:
            logging.info('< Error > login_cancel : ' + str(e))

########################################################################################################################
#
# main 
#
########################################################################################################################
def main(): 
    app = QApplication(sys.argv)
    main = login()
    main.show()
    app.exit(app.exec())

if __name__ == '__main__':
    main()


    