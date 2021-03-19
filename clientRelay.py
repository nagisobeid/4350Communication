import socket 
import threading 
from tkinter import *
from tkinter import font 
from tkinter import ttk 


PORT = 5000
SERVER = 'localhost'
ADDRESS = (SERVER, PORT) 
FORMAT = "utf-8"


############## BREAK AND FIX
try:
	client = socket.socket(socket.AF_INET, 
						socket.SOCK_STREAM) 
	client.connect(ADDRESS) 
except socket.error as err:
	print("********************************************************")
	print("Server is DOWN or has NOT been Started <------------ ERR")
	print("****Please start server and try Running client again****")
	exit()
###########################

class GUI: 
	def __init__(self): 
		self.Window = Tk() 
		self.Window.withdraw() 
		
		self.login = Toplevel() 
		self.login.title("Login") 
		self.login.resizable(width = False, 
							height = False) 

		self.login.configure(width = 400, 
							height = 300,
							bg = "#659ea8") 
		
		self.pls = Label(self.login, 
					text = "LOGIN", 
					justify = CENTER, 
					font = "Times-Roman 14 bold") 
					
		self.pls.place(relheight = 0.12, 
					relx = 0.2, 
					rely = 0.2) 
		
		self.entryName = Entry(self.login)
								
		self.entryName.place(relwidth = 0.4, 
							relheight = 0.12, 
							relx = 0.35, 
							rely = 0.2) 
		
		self.entryName.focus() 
		
		self.go = Button(self.login, 
						text = "CONTINUE", 
						bg = "#00ff00",
						font = "Times-Roman 14 bold", 
						command = lambda: self.runClient(self.entryName.get())) 
		
		self.go.place(relx = 0.4, 
					rely = 0.35) 
		self.Window.mainloop() 



	def runClient(self, name): 
		self.login.destroy() 
		self.layout(name) 
		
		rcv = threading.Thread(target=self.receive) 
		rcv.start() 

	def layout(self,name): 
		self.name = name 
		self.Window.deiconify() 
		self.Window.title("RELAY") 
		self.Window.resizable(width = False, 
							height = False) 
		self.Window.configure(width = 470, 
							height = 450, 
							bg = "black") 
		
		self.textCons = Text(self.Window, 
							width = 20, 
							height = 2, 
							bg = "#0c7045", 
							fg = "#EAECEE", 
							font = "Times-Roman 14", 
							padx = 5, 
							pady = 5) 
		
		self.textCons.place(relheight = 1, 
							relwidth = 1, 
							rely = 0.00) 
		
		self.labelBottom = Label(self.Window, 
								bg = "#29383b", 
								height = 40) 
		
		self.labelBottom.place(relwidth = 1, 
							rely = 0.825) 
		
		self.entryMsg = Entry(self.labelBottom, 
							bg = "#5e5e5e", 
							fg = "#EAECEE", 
							font = "Times-Roman 13") 
		
		self.entryMsg.place(relwidth = 0.74, 
							relheight = 0.06, 
							rely = 0.008, 
							relx = 0.011) 
		
		self.entryMsg.focus() 
		
		self.buttonMsg = Button(self.labelBottom, 
								text = "Send", 
								font = "Times-Roman 10 bold", 
								width = 20, 
								bg = "#2aeb44", 
								fg = "#2aeb44",
								command = lambda : self.sendButton(self.entryMsg.get())) 
		
		self.buttonMsg.place(relx = 0.77, 
							rely = 0.008, 
							relheight = 0.06, 
							relwidth = 0.22) 
		
		self.textCons.config(cursor = "arrow") 
		
		scrollbar = Scrollbar(self.textCons) 
		
		scrollbar.place(relheight = 1, 
						relx = 0.974) 
		
		scrollbar.config(command = self.textCons.yview) 
		
		self.textCons.config(state = DISABLED) 

	def sendButton(self, msg): 
		self.textCons.config(state = DISABLED) 
		self.msg=msg 
		self.entryMsg.delete(0, END) 
		snd= threading.Thread(target = self.sendMessage)
		snd.start()


	def receive(self): 
		while True: 
			print("loop")

			try: 
				message = client.recv(1024).decode(FORMAT) 
				
				if message == 'NAME': 
					client.send(self.name.encode(FORMAT)) 
				else: 
					self.textCons.config(state = NORMAL) 
					self.textCons.insert(END, 
										message+"\n\n") 
					
					self.textCons.config(state = DISABLED) 
					self.textCons.see(END) 
			except: 
				print("An error occured!")
				client.close()
				break
		
	def sendMessage(self):
		self.textCons.config(state=DISABLED)
		while True:
			message = (f"{self.name}: {self.msg}")
			client.send(message.encode(FORMAT))
			break

g = GUI() 

