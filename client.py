import socket
import threading

class sendMsg(threading.Thread):
	
	def __init__(self, s):
		threading.Thread.__init__(self)
		self.s = s
		self.closed = False
		
	def run(self):
#		print "sending thread started"
		while not self.closed:
			msg = raw_input()
			self.s.send(msg)
			if msg == "quit":
				self.closed = True
				break
#		print "sending thread closed"
	
class recvMsg(threading.Thread):
	def __init__(self, s, p):
		threading.Thread.__init__(self)
		self.s = s
		self.p = p
		
	def run(self):
#		print "recieving thread started"
		while not self.p.closed:
			msg = self.s.recv(1024)
			print msg
#		print "recieving thread closed"
			
s = socket.socket()
print "socket created"
ip = "127.0.0.1"
port = 8456
s.connect((ip, port))
print "connected to ip ", ip, "and port ", port
#closed = False
go = sendMsg(s)
get = recvMsg(s, go)
go.start()
get.start()
while not go.closed:
	pass
s.close()
print "socket closed"
