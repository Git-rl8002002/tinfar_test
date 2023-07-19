#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20230315
# Update   : 20230315
# Function : sqlite3

import logging , sqlite3 , minimalmodbus , time
from control.dao import *


################################################################################################################################################
#
# main
#
################################################################################################################################################
class main_content:

    ########
    # log
    ########
    log_format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%H:%M:%S")

    def __init__(self):
        self.get_cw9_m_rtu()
    
    #########
    # main
    #########
    def main(self):
        try:
            conn = sqlite3.connect('test.db')
            logging.info("sqlite3 db connection success.")
        except Exception as e:
            logging.info(str(e))
        finally:
            pass
    #######################
    # get cw9 mosbus RTU
    #######################
    def get_cw9_m_rtu(self):
            
            try:
                #while True:
                    
                    #########
                    #
                    # ID 1
                    #
                    #########
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())
                    self.n_time  = time.strftime("%H:%M:%S" , time.localtime())
                    ### port 
                    self.cw9  = minimalmodbus.Instrument(port=i6_rtu_connect['mac_port2'] , slaveaddress=3 , mode=minimalmodbus.MODE_RTU)
                    #self.cw9  = minimalmodbus.Instrument(port=i6_rtu_connect['linux_port'] , slaveaddress=1 , mode=minimalmodbus.MODE_RTU)
                
                    self.cw9.serial.baudrate = i6_rtu_para['br']
                    self.cw9.serial.timeout = 1
                    self.cw9.clear_buffers_before_each_transaction = True
                    self.cw9.close_port_after_each_call = True
                    self.cw9.debug = False
                
                    ###  show CW9 read register val
                    self.cw9_val1 = self.cw9.read_register(int(i6_rtu_sensor['temp'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val2 = self.cw9.read_register(int(i6_rtu_sensor['rh'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val3 = self.cw9.read_register(int(i6_rtu_sensor['co2'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val4 = self.cw9.read_register(int(i6_rtu_sensor['pm2.5'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val5 = self.cw9.read_register(int(i6_rtu_sensor['hcho'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val6 = self.cw9.read_register(int(i6_rtu_sensor['tvoc'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val7 = self.cw9.read_register(int(i6_rtu_sensor['o3'],16),functioncode=int(i6_rtu_para['fc']))
                    self.cw9_val8 = self.cw9.read_register(int(i6_rtu_sensor['pm10'],16),functioncode=int(i6_rtu_para['fc']))
                    
                    print('ID : 1')
                    print(self.r_time + ' , modbudRTU , CW9-TEMP  : ' + str(self.cw9_val1/10) + ' °C')
                    print(self.r_time + ' , modbudRTU , CW9-RH    : ' + str(self.cw9_val2/10) + ' %')
                    print(self.r_time + ' , modbudRTU , CW9-CO2   : ' + str(self.cw9_val3/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-PM2.5 : ' + str(self.cw9_val4/10) + ' ug/m3')
                    print(self.r_time + ' , modbudRTU , CW9-HCHO  : ' + str(self.cw9_val5/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-TVOC  : ' + str(self.cw9_val6/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-O3    : ' + str(self.cw9_val7/10) + ' ppm')
                    print(self.r_time + ' , modbudRTU , CW9-PM10  : ' + str(self.cw9_val8/10) + ' ug/m3')

                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , modbusRTU , A , ID : 1 , TEMP : ' + str(self.cw9_val1/10) + ' °C , RH : ' + str(self.cw9_val2/10) + ' ％ , CO2 : ' +  str(self.cw9_val3/10) + ' ppm , PM2.5 : ' + str(self.cw9_val4/10) + ' ppm , HCHO : ' + str(self.cw9_val5/10) + ' ppm \n'
                    #self.db_insert_file(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.n_time , 'modbusRTU' , 'A' , '1', 'TEMP , RH , CO2 , PM2.5 , HCHO' , self.cw9_val1/10 , self.cw9_val2/10 , self.cw9_val3/10 , self.cw9_val4/10 , self.cw9_val5/10 , 'ok')    
                    
                    print('\n')
                    
                    time.sleep(1)

            except IOError as e:
                print('< IOError > : ' + str(e))
            finally:
                pass

################################################################################################################################################
#
# start
#
################################################################################################################################################
if __name__  == "__main__":
    main = main_content()
