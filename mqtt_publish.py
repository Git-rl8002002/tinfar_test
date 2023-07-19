#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20230413
# Update   : 20230413
# Function : MQTT publish

import paho.mqtt.client as mqtt , random , json , datetime , time

#########################################################################################################
#
# mqtt_publish
#
#########################################################################################################
class mqtt_publish:
    
    def __init__(self):
        pass

    def main(self):
        ISOTIMEFORMAT = '%m/%d %H:%M:%S'

        client = mqtt.Client()
        client.username_pw_set("try","xxxx")
    


#########################################################################################################
#
# start
#
#########################################################################################################
if __name__ == "__main__":
    run = mqtt_publish()


