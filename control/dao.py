#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20230220
# Update   : 20230302
# Function : Tinfar test dao parm

################
# sqlite_path
################
sqlite_path = {'linux':'/var/www/html/tinfar_test/control/monitor_jnc.db'}

###########
# tinfar
###########
tinfar_VM = {'host':'61.220.205.143','port':5306,'user':'backup','pwd':'SLbackup#123','db':'tinfar_test', 'db2':'tinfar_network_attack' , 'charset':'utf8'}
tinfar_NB = {'host':'61.220.205.143','port':3306,'user':'backup','pwd':'SLbackup#123','db':'tinfar_test', 'charset':'utf8'}
kedge_connect = {'host':'61.220.205.143' , 'port':5306,'user':'backup' , 'pwd':'SLbackup#123' , 'db':'tinfar_kedge' , 'charset':'utf8'}

################
# tinfar sftp
################
tinfar_sftp = {'host':'61.220.205.143','port':5906,'user':'jason-tinfar','pwd':'1qaz#123','path':'/var/www/html'}

###############
#
# modbus RTU
#
###############

### tinfar test CW9 - modbus RTU
i6_rtu_connect = {'mac_port1':'/dev/tty.usbserial-1410','mac_port2':'/dev/tty.usbserial-AB0LZ3NC','linux_port':'/dev/ttyUSB0','win_port':'COM4'} 
i6_rtu_para    = {'br':'9600','fc':'4','kind':'cw9','tb':'modbus_sensor','protocol':'modbusRTU'}
i6_rtu_sensor  = {'temp':'0x0000','rh':'0x0001','co2':'0x0002','pm2.5':'0x0003','hcho':'0x0004','co':'0x0005','tvoc':'0x0006','o3':'0x0007','pm10':'0x0008' , 'nh3':'0x000A' , 'h2s':'0x000B' , 'pr':'0x0010'}

#################
# 維新 iAeris52
#################
iaeris52 = {'json_url':'http://61.220.205.1/read?callbacl?'}

#############
# 連大興 I6
#############
lds_i6 = {'ip':'60.248.16.152' , 'port':502 , 'ph':'0x0000' , 'ec':'0x0001' , 'temp':'0x0002' , 'mt':'0x0003' , 'cf':'0x0004' , 'other':'0x0005'}

############
# 富泰 I6
############
ft_i6 = {'ip':'60.250.232.118' , 'port':502 , 'ph':'0x0000' , 'ec':'0x0001' , 'temp':'0x0002' , 'mt':'0x0003' , 'cf':'0x0004' , 'other':'0x0005'}

########
# txt
########
txt = {'mac_path':'/Users/user/eclipse-workspace/tinfar/tinfar_test/txt/',
       'win_path':'d:/money_manager/txt/',
       'linux_path':'/var/www/html/tinfar_test/txt/',
       'network_attack_linux':'/var/www/html/scraping/txt/network_attack/',
       'network_attack_mac':'/Users/user/eclipse-workspace/tinfar/scraping/txt/network_attack/'}