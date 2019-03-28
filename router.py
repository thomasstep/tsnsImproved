#!/usr/bin/python

import grpc
from concurrent import futures
import time
import os
import json
import copy
import sys

# Import grpc classes
import sns_pb2
import sns_pb2_grpc 

# Get the masters from command line
servers = []
for i in range(3,len(sys.argv)):
	servers.append(sys.argv[i])

class snsServicer(sns_pb2_grpc.SNSServiceServicer):

	def __init__(self):
		# Contains the IP:Port of all machines
		self.servers = servers
		# This is the master that all new clients are routed to
		self.availableMaster = ""

	def GetAvailable(self, request, context):
		available = ""
		for server in self.servers:
			# Check if the available server is still alive
			channel = grpc.insecure_channel(server)
			stub = sns_pb2_grpc.SNSServiceStub(channel)
			request = Alive(notdead=True)
			response = stub.KeepAlive(request)
			if response.notdead:
				available = server
				break
			# Server is down, move to the next
			self.servers.pop(server)
			# Want to keep track of that server just move it to last priority
			self.servers.append(server)
		response = Reply()
		if available == "":
			response.msg = "No available server"
		else:
			response.msg = available
		return response
			

# Create the server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Add class to server
sns_pb2_grpc.add_SNSServiceServicer_to_server(snsServicer(), server)

# Listen on port given
server.add_insecure_port(sys.argv[1] + ":" + sys.argv[2])
server.start()

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop(0)
