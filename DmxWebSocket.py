from websocket import create_connection

class DmxWebSocket(object):
	def __init__(self):
		address = "ws://127.0.0.1:9999"
		self.ws = create_connection(address)
		print "Connected to DMX."

	def __del__(self):
		self.ws.close()
		print "Disconnected."

	def sendColor(self, color):
		self.ws.send("CH|2|" + str(color[0])) #R
		self.ws.send("CH|3|" + str(color[1])) #G
		self.ws.send("CH|4|" + str(color[2])) #B