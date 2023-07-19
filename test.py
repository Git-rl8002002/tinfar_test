#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20230220
# Update   : 20230411
# Function : test 

import threading , time , logging , requests , json , socket , cv2 , sys , pymysql , paho.mqtt.client as mqtt
from bs4 import BeautifulSoup

from control.dao import *

#########################################################################################################
#
# MQTT API
#
#########################################################################################################
class mqtt_server:
    ### log 
    log_format = "%(asctime)s %(message)s"
    logging.basicConfig(format=log_format,level=logging.INFO,datefmt="%Y-%m-%d %H:%M:%S")

    def __init__(self):
        self.main()

    def on_connect(self , client , userdata , flags , rc):
        logging.info("connection with result code : " + str(rc))
        client.subscribe("Try / MQTT")
    
    def on_message(client , userdata , msg):
        logging.info(msg.topic + " " + msg.payload.decode("utf-8"))

    def main(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect()
        client.on_message = self.on_message()

        client.username_pw_set("try","xxxx")
        client.connect("61.220.205.143",1883,60)
        client.loop_forever()


#########################################################################################################
#
# 根基營造 JNC Server JSON API
#
#########################################################################################################
class kedge:
    
    ### log 
    log_format = "%(asctime)s %(message)s"
    logging.basicConfig(format=log_format,level=logging.INFO,datefmt="%Y-%m-%d %H:%M:%S")
    
    #########
    # init
    #########
    def __init__(self):
        self.main()
    
    #################
    # add_kedge_db
    #################
    def add_kedge_db(self , position , val1 , val2 , val3 , status):
        
        ### record time
        r_time  = time.strftime("%H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())
        r_day   = time.strftime("%d" , time.localtime()) 
        b_month = time.strftime("%Y_%m" , time.localtime())

        #############
        # kedge DB
        #############
        conn = pymysql.connect(host=kedge_connect['host'] , port=kedge_connect['port'] , user=kedge_connect['user'] , passwd=kedge_connect['pwd'] , database=kedge_connect['db'] , charset=kedge_connect['charset'])
        curr = conn.cursor()

        try:
            b_sql = "create table {0}(no int not null primary key AUTO_INCREMENT,r_time time null,r_year varchar(100) null,r_month varchar(100) null,r_day varchar(100) null,s_kind varchar(200) null,s_content varchar(200) null,s_protocol varchar(200) null,tag_name varchar(200) null,val varchar(200) null,unit varchar(200) null,r_status varchar(50) null)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci".format(b_month)
            curr.execute(b_sql)

        except Exception as e:
            b_sql = "insert into {0}(r_time,r_year,r_month,r_day,s_protocol,s_kind,s_content,tag_name,val,unit,r_status) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(b_month , r_time , r_year , r_month , r_day , 'HTTP JSON' , 'CB' , position , val1 , val2 , val3 , status)
            curr.execute(b_sql)
            
        finally:
            conn.commit()
            conn.close()
    
    #########
    # main
    #########
    def main(self):

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

        for val in data_val_1["Device"]:
            logging.info(str(d_data_val_1['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_1['Connect']))
            self.add_kedge_db(d_data_val_1['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_1['Connect'])

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

        for val in data_val_2["Device"]:
            logging.info(str(d_data_val_2['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_2['Connect']))
            self.add_kedge_db(d_data_val_2['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_2['Connect'])

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

        for val in data_val_3["Device"]:
            logging.info(str(d_data_val_3['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_3['Connect']))
            self.add_kedge_db(d_data_val_3['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_3['Connect'])

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

        for val in data_val_4["Device"]:
            logging.info(str(d_data_val_4['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_4['Connect']))
            self.add_kedge_db(d_data_val_4['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_4['Connect'])

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

        for val in data_val_5["Device"]:
            logging.info(str(d_data_val_5['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_5['Connect']))
            self.add_kedge_db(d_data_val_5['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_5['Connect'])

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

        for val in data_val_6["Device"]:
            logging.info(str(d_data_val_6['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_6['Connect']))
            self.add_kedge_db(d_data_val_6['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_6['Connect'])

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

        for val in data_val_7["Device"]:
            logging.info(str(d_data_val_7['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_7['Connect']))
            self.add_kedge_db(d_data_val_7['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_7['Connect'])

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

        for val in data_val_8["Device"]:
            logging.info(str(d_data_val_8['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_8['Connect']))
            self.add_kedge_db(d_data_val_8['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_8['Connect'])

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

        for val in data_val_9["Device"]:
            logging.info(str(d_data_val_9['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_9['Connect']))
            self.add_kedge_db(d_data_val_9['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_9['Connect'])

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

        for val in data_val_10["Device"]:
            logging.info(str(d_data_val_10['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_10['Connect']))
            self.add_kedge_db(d_data_val_10['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_10['Connect'])

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

        for val in data_val_11["Device"]:
            logging.info(str(d_data_val_11['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_11['Connect']))
            self.add_kedge_db(d_data_val_11['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_11['Connect'])

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

        for val in data_val_12["Device"]:
            logging.info(str(d_data_val_12['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_12['Connect']))
            self.add_kedge_db(d_data_val_12['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_12['Connect'])

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

        for val in data_val_13["Device"]:
            logging.info(str(d_data_val_13['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_13['Connect']))
            self.add_kedge_db(d_data_val_13['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_13['Connect'])

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

        for val in data_val_14["Device"]:
            logging.info(str(d_data_val_14['DeviceName']) + ' : ' + val['TagName'] + ' , ' + val['Value'] + ' ' +  val['Unit'] + str(' , 連線(0:斷線 , 1:連線) : ') + str(d_data_val_14['Connect']))
            self.add_kedge_db(d_data_val_14['DeviceName'] , val['TagName'] , val['Value'] , val['Unit'] , d_data_val_14['Connect'])


#########################################################################################################
#
# 北醫大圖書館 sd api
#
#########################################################################################################
class library_sd:
    
    ### log 
    log_format = "%(asctime)s %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")
    
    def __init__(self):
        self.main()
    
    def main(self):
        
        url      = "http://61.220.205.143:9001/sd" # 雙和
        url2     = "http://61.220.205.143:9002/sd" # 萬芳

        try:
            data     = requests.get(url)
            r_data   = data.text.replace('&#34;', '"')
            data_val = json.loads(r_data)

            #######################
            # write txt in linux
            #######################
            if sys.platform == "linux":
                
                with open('/var/www/html/tinfar_test/txt/library_sd.txt' , 'a') as w_txt :
                    w_content =  str(data_val['date']) + ' : ' + str(data_val['sd-co2']) + '\n'
                    w_txt.write(w_content)
            
            print(str(data_val['date']) + ' : ' + str(data_val['sd-co2']))    

        except Exception as e:
            logging.info('< Error > library_sd : ' + str(e))
        finally:
            data.close()

#########################################################################################################
#
# opencv
#
#########################################################################################################
class open_cv:
    def __init__(self):
        self.main()

    def show_xy(self , event , x , y , flags , userdata):
        if event == 0:
            print(event , x , y ,flags)
        if event == 1:
            color = self.img[y,x]
            print(color)


    def main(self):
        self.img = cv2.imread('/Users/user/eclipse-workspace/tinfar/tinfar_test/icon/camera.png')
        cv2.imshow('test img' , self.img)
        cv2.setMouseCallback('test img' , self.show_xy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



#########################################################################################################
#
# 彰化縣避難處
#
#########################################################################################################
class position_item:
    def __init__(self):
        self.main()
    def main(self):
        url = "https://www.chpb.gov.tw/opendata/8sGgzAHD40Kr1kYg7GSSAw/json"
        data = requests.get(url)
        data_val = data.json()

        for val in data_val:
            print(val['類別'] + ' , ' + val['地址'] + ' , 容納 ' + val['可容納人數'])

#########################################################################################################
#
# 空氣品質 AQI API
#
#########################################################################################################
class air_aqi:
    def __init__(self):
        self.main()
    def main(self):
        url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=JSON"
        data = requests.get(url)
        data_val = data.json()

        for val in data_val['records']:
            print(val['publishtime'] + ' : ' + val['county'] + ' ( ' + val['sitename'] + ' ) , AQI : ' + val['aqi'] + ' , pm2.5 : ' + val['pm2.5'] + ' ug/m3')
            


#########################################################################################################
#
# e_socket
#
#########################################################################################################
class e_socket:

    def __init__(self):
        self.monitor_network()

    def monitor_network():
        
        # 建立socket並監聽所有網路流量
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sniffer.bind(('0.0.0.0', 0))
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        # 監聽網路流量
        while True:
            raw_data, addr = sniffer.recvfrom(65535)
            print(f'Packet: {raw_data}')

        # 停止監聽網路流量
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

#########################################################################################################
#
# file try-except-finally , with
#
#########################################################################################################
class try_except:

    log_format = '%(asctime)s : %(message)s'
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")

    def __init__(self):
        
        txt_path   = '/Users/user/eclipse-workspace/tinfar/tinfar_test/txt/try_except.txt'
        jason_path = 'http://61.220.205.1/read?callbacl?'
        
        with requests.get(jason_path) as json_content:
            json_val = json_content.text.strip('(').strip(')')
            json_data = json.loads(json_val)
            logging.info(json_data['date'] + ' , ' + json_data['PID'] + ' , ' + str(json_data['RH']))


        try:
            json_content = requests.get(jason_path)
            json_val = json_content.text.strip('(').strip(')')
            json_data = json.loads(json_val)
            logging.info(json_data['date'] + ' , ' + json_data['PID'] + ' , ' + str(json_data['RH']))
        except Exception as e:
            logging.info('< Error > load iAeris52 failed.' + str(e))
        finally:
            pass

#########################################################################################################
#
# analysis_json
#
#########################################################################################################
class analysis_json:

    log_format = '%(asctime)s : %(message)s'
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S ")

    def __init__(self):
        self.main()

    def main(self):
        r_time    = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        json_url1 = 'http://192.168.111.12/JSONDeviceCH?DeviceIdx=0&Key=JNC&val=235478'
        json_url2 = 'http://192.168.111.12/JSONDeviceCH?DeviceIdx=1&Key=JNC&val=235478'
        json_url3 = "http://192.168.111.12/JSONDevice?Idx=0&Key=JNC&val=123545'"
        json_url4 = "http://192.168.111.12/JSONDevice?Idx=1&Key=JNC&val=123545'"
        
        print('\n')

        f = requests.get(json_url3)
        f = json.loads(f.text)
        logging.info(f['DeviceName'] + ' , channel count : ' + f['ChannelCount'])
        
        f = requests.get(json_url1)
        f = json.loads(f.text)
        for val in f['Device']:
            logging.info(val['TagName'] + ' : ' + val['Value'] + val['Unit'])

        f = requests.get(json_url4)
        f = json.loads(f.text)
        logging.info(f['DeviceName'] + ' , channel count : ' + f['ChannelCount'])

        f = requests.get(json_url2)
        f = json.loads(f.text)
        for val in f['Device']:
            logging.info(val['TagName'] + ' : ' + val['Value'] + val['Unit'])


#########################################################################################################
#
# ddos attack
#
#########################################################################################################
class ddos_attack:
    def __init__(self):
        self.main()

    def main(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        url  = "https://whatismyipaddress.com/ip/8.208.113.83"
        data = requests.get(url , headers=headers)
        data.encoding = "utf-8"
        
        print(data.text)
        
        
        #data_val = data.json()
        #print(data_val)
        

#########################################################################################################
#
# class : scraping
#
#########################################################################################################
class scraping:
    ########
    # log
    ########
    log_foramt = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_foramt , level=logging.INFO , datefmt="%H:%M:%S")

    def __init__(self):
        self.main()    

    def main(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        
        url = requests.get('https://technews.tw/category/finance/finance-report/' , headers=headers)
        url.encoding = 'utf8'
        #url = requests.get('https://mops.twse.com.tw/nas/t21/sii/t21sc03_103_2_0.html' , headers=headers)
        #url.encoding = 'big5'
        
        data = BeautifulSoup(url.text , 'html.parser')
        content = data.find_all('a')

        for val in content:
            title = val.get('title')
            href = val.get('href')

            logging.info(str(title) + ' , ' + str(href))



#########################################################################################################
#
# class : test
#
#########################################################################################################
class test_thread:
    
    ########
    # log
    ########
    log_foramt = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_foramt , level=logging.INFO , datefmt="%H:%M:%S")

    def r_timer(self):
        time.sleep(5)
        print('Wake up.')

    def run_thread(self):
        r_thread = threading.Thread(target=self.r_timer)    
        if r_thread.is_alive() == False:
            r_thread.start()
        else:
            logging.info(r_thread.is_alive())


#########################################################################################################
#
# class : people
#
#########################################################################################################
class people:
    def __init__(self):
        self.name = "people name"
        data = person()
        self.age = data.age
        self.address = data.person_parm().address
    def show(self):
       print(str(self.name) + ' / ' + str(self.age) + ' / ' + str(self.address))

class person:
    def __init__(self):
        self.name = "person name"
        self.age = 22
    def person_parm(self):
        self.address = "new taipei"

#########################################################################################################
#
# start
#
#########################################################################################################
if __name__ == "__main__":      
    
    ### usage
    if len(sys.argv) < 2:
        print("#############################################################################################################")
        print("#")
        print("# Example : ")
        print("# \t ( 北醫大圖書館SD CO2 : library ) ./text.py library ")
        print("# \t ( 根基營造 JNC SERVER : kedge ) ./text.py kedge ")
        print("# \t ( DDOS attack : ddos ) ./text.py ddos ")
        print("#")
        print("#############################################################################################################")
    
    ### 北醫大圖書館 SD CO2
    elif sys.argv[1] == "library":
        run = library_sd()

    ### 根基營造 JNC Server CB
    elif sys.argv[1] == 'kedge':
        run = kedge()

    ### MQTT server
    elif sys.argv[1] == 'mqtt':
        run = mqtt_server()
    
    ### DDOS attack
    elif sys.argv[1] == 'ddos':
        run = ddos_attack()