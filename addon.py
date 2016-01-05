import xbmcaddon
import xbmcgui
import serial
import time
import urlparse

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
resp=""
loop="true"
string="030cf100"
count=0
while loop:
        if count == 10:
                break
                print "TV Did Not Respond Success"
        if string in resp:
                print "found it"
                break
                ser.close()
        else:
                ser.write("\x08\x22\x00\x00\x00\x00\xd6")
                data = ser.read(24)
                resp=data.encode('hex')
                print resp
                count = count +1
                time.sleep(1)
        print "finished"