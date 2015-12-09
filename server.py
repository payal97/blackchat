import socket
import threading

'''
class recvMsg(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.closed = False

	def run(self):
		while not self.closed:
			msg = self.s.recv(1024)
'''

def operate(conn_cl):
	for client in conn_cl:
		c, addr = client[0], client[1]
		msg = c.recv(1024)
		for cl in conn_cl:
			s, addrs = cl[0], cl[1]
			if s != c:
				s.send(msg)
		if msg == "quit":
			c.close()
			conn_cl.remove(client)
			print "client", c, "closed"
			break


s = socket.socket()
print "socket created"

ip = ''
port = 8456
s.bind((ip, port))
print "port ", port, " binded to socket"

connected_clients = []

s.listen(2)
print "listening for clients..."
while True:
	c, addr = s.accept()
	connected_clients.append((c,addr))
	print "connected to ", addr


	c.close()
	print "client socket closed"
