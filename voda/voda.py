#!/usr/bin/python
#
# Vodafone SMS + Gammu fallback
#
# user: vf_test_msmt
# pass: Fgh58s6HvfS
#

import httplib
import urllib
import sys
import socket
import os

header={'Content-type' : 'application/x-www-form-urlencoded','Accept' : 'text/plain'}

form=['<?xml version="1.0"?><SmsServices><DataHeader><DataType>SMS</DataType><UserName>vf_test_msmt</UserName><Password>Fgh58s6HvfS</Password></DataHeader><DataArray><DataTemplate><DataItem><MobileTerminate>','</MobileTerminate><Text>','</Text></DataItem></DataTemplate></DataArray></SmsServices>']

if len(sys.argv)==3:

	data = form[0] + sys.argv[2] + form[1] + sys.argv[1] + form[2]
	param = urllib.urlencode({'xml':data})
	
	try:
		conn=httplib.HTTPSConnection('www.sms-operator.cz','443',timeout=10)
		conn.request('POST','/webservices/webservice.aspx', param, header)
	
		r=conn.getresponse()
		if not r.status == 200:
                        sys.exit('Gateway error.')
		conn.close()

	except socket.error:
		cmd ='/usr/bin/printf "%b" "' + sys.argv[1] + '" | /usr/bin/gammu sendsms TEXT ' + sys.argv[2]
		os.system(cmd)	
else:
	print('Wrong number of arguments.')

