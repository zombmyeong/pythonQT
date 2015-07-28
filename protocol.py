#name, data info
#number 8000 ~
#connect 8000
#close 8001
#disconnection or somthing 8003
#recv disconnection 8004

#send start 8010
#recv success 8011

class protocol () :
	CLIENT_CONNECT = '8000'
	CLIENT_DISCONNECT_REQUEST = '8001'
	CLIENT_DISCONNECT = '8002'

	SERVER_DISCONNECT_REQUEST = '8003'
	CLIENT_DISCONNECT_REPLY = '8004'

	CLIENT_SEND_REQUEST = '8010'