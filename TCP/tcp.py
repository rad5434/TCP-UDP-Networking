#import socket module
from socket import *
import sys # In order to terminate the program
from bs4 import BeautifulSoup

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(("", 12000))
serverSocket.listen(1)
#Fill in end
while True:
#Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024).decode()
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = BeautifulSoup(f,"lxml")
		outputdata = outputdata.body.text
		#outputdata.feed(f)
		#Send one HTTP header line into socket
		#Fill in start
		connectionSocket.send('HTTP/1.0 200 OK\r\n')
		#Fill in end
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		#Fill in start
		connectionSocket.send('HTTP/1.0 408 FILE NOT FOUND\r\n')
		#Fill in end
		#Close client socket
		#Fill in start
		connectionSocket.close()
		#Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data