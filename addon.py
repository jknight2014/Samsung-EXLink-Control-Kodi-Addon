import xbmcaddon
import xbmcgui
import serial
import time

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
	ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)
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

elif mode[0] == 'on':
	ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)
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
					ser.write("\x08\x22\x00\x00\x00\x01\xd5")
					data = ser.read(24)
					resp=data.encode('hex')
					print resp
					count = count +1
					time.sleep(1)
	print "finished"

elif mode[0] == 'off':
	ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)
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
					ser.write("\x08\x22\x00\x00\x00\x02\xd4")
					data = ser.read(24)
					resp=data.encode('hex')
					print resp
					count = count +1
					time.sleep(1)
	print "finished"