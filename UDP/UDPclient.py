from socket import *
import time
import requests
import eventlet

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(2)
count = 0
while count<10:
	message = "ping: "+ str(count)
	start_time = time.time()
	print "Sending " + message + " to the server at time " + str(start_time) 
	clientSocket.sendto(message.encode(),(serverName, serverPort))
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
		print "Recieved " + str(modifiedMessage.decode()) + " from the server at time "+str(time.time())
	except:
		print "Request timed out!!"
	count+=1
clientSocket.close()
