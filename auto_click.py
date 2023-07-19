#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20230220
# Update   : 20230220
# Function : auto click


import sys , pymysql , hashlib , time , os , platform , pyautogui , cv2 , keyboard , signal

from control.dao import *

################################################################################################################################  
#
# main_content
#
################################################################################################################################  
class main_content():

    r_time = time.strftime("%Y-%m-%d" , time.localtime())

    ###############################
    # class var and function var
    ###############################
    def show(self):
        
        n = 'show'
        self.n = 'test'
        print(self.r_time)

        '''
        for i in range(60):
            r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            
            print(n)
            print(self.n)

            if platform.system() == 'Darwin':
                try:
                    add_content = r_time + str(' , function\'s var : r_time , use r_time , class\'s var : r_time , use self.r_time \n')
                    save_txt = open(txt['mac_path'] + self.r_time + '_test.txt' , 'a')
                    save_txt.write(add_content)
                    save_txt.close()
                except Exception as e:
                    print('< Error > save txt : ' + str(e))

            time.sleep(1)
        '''



    ###########
    # click1
    ###########
    def click1(self):

        n = 'show click1'

        try:

            x , y = pyautogui.position()

            r_time3 = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            pyautogui.click(1812 , 8 , duration=1)
            print('1).' + r_time3 + ' click 新聞')
            
            r_time3 = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            pyautogui.click(1817 , 42 , duration=1)
            print('2).' + r_time3 + ' click 新聞/news , wait 20 sec')
            time.sleep(20)

            r_time3 = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            pyautogui.click(3454 , 155 , duration=1)
            print('3).' + r_time3 + ' click 新聞/news/ET news statistics , wait 30 sec')
            time.sleep(30)

            r_time3 = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            pyautogui.click(2256 , 240 , duration=1)
            print('4).' + r_time3 + ' click close 新聞/news/ET news statistics')
                
        except KeyboardInterrupt:
            pass
class main_content2():
    n = 'class var'

    def show2(self):
        n = 'function show2 - var'
        self.n = 'function show2 - self var'
        print(self.n)
        print(n)
    
    def show3(self):
        self.n = 'function show3 - self var'
        print(self.n)
        
################################################################################################################################  
#
# main
#
################################################################################################################################  
if __name__ == '__main__':
    main = main_content()
    main.click1()
    #main.show()
    #print(main.n)
    #print(main.r_time)

    main2 = main_content2()
