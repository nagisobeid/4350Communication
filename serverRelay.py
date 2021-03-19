
import socket 
import threading 
import random
import requests


PORT = 5000
SERVER = "localhost"
ADDRESS = (SERVER, PORT) 
FORMAT = "utf-8"
clients, names = [], [] 

server = socket.socket(socket.AF_INET, 
					socket.SOCK_STREAM) 

 
server.bind(ADDRESS) 

def startChat(): 
	
	server.listen()

	#----------TESTING-----------
	#test(FORMAT) 
	
	while True: 
		conn, addr = server.accept() 
		conn.send("NAME".encode(FORMAT)) 
		name = conn.recv(1024).decode(FORMAT) 
		names.append(name) 
		clients.append(conn) 
		
		broadcastMessage(f"WELCOME {name}".encode(FORMAT)) 
		
		# Start the handling thread 
		thread = threading.Thread(target = handle, 
								args = (conn, addr)) 
		thread.start() 
		


def handle(conn, addr): 
	connected = True
	
	while connected: 
		message = conn.recv(1024) 
		broadcastMessage(message) 
	
	conn.close() 


def broadcastMessage(message): 
	for client in clients: 
		client.send(message) 

def test(FORMAT):

	success = 0
	unsuccess = 0
	WORDS = []

	with open('wordlist','r') as file:  
		for line in file:      
			for word in line.split(): 
				# displaying the words  
				WORDS.append(word)            

	testing = 0
	while testing < 20:
		st = random.randint(0,1) #0 = decode, 1 = encode
		msg = WORDS[testing]

		if (st == 0):
			#msg = WORDS[testing].decode(FORMAT)
			print ("UN-SUCCESSFUL <------ MESSAGE IS NOT-ENCODED - MSG = ", msg, " <--TYPE = ", type(msg))
			unsuccess+=1
		elif (st == 1):
			msg = WORDS[testing].encode(FORMAT)
			print ("SUCCESSFUL <------ MESSAGE IS ENCODED - MSG = ", msg, " <--TYPE = ", type(msg))
			success+=1
	
		testing += 1

	print ("===========================================")
	print ("SUCCESSFUL-------", success )
	print ("UN-SUCCESSFUL----", unsuccess )
	print ("TOTAL TESTS -----", testing )
	
	exit()




startChat() 

