#!/usr/bin/python
#
# O2 SMS Connector
#

import httplib
import urllib
import sys
import socket

CERT_FILE='/etc/nagios/o2/o2.pem'
baID='1992428'

if len(sys.argv)==3:
	try:
		conn=httplib.HTTPSConnection('smsconnector.cz.o2.com','443', cert_file=CERT_FILE)   
		conn.request('POST','/smsconnector/getpost/GP?action=send&baID=%s&toNumber=%s&text=%s' % (baID,urllib.quote(sys.argv[2]),urllib.quote(sys.argv[1])))
		resp=conn.getresponse()
		#print r.status,r.reason,r.msg
		#data = r.read()
		#print data
		if not resp.status == 200:
			sys.exit('Gateway error.')
		conn.close()
	except socket.error:
		sys.exit('Connection error.')
else: print('Wrong number of arguments.')


