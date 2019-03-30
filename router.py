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

	def GetAvailable(self, request, context):
		available = ""
		for server in self.servers:
			# Check if the available server is still alive
			print("Checking if " + server + " is still alive")
			try:
				channel = grpc.insecure_channel(server)
				stub = sns_pb2_grpc.SNSServiceStub(channel)
				request = sns_pb2.Alive(notDead=True)
				response = stub.KeepAlive(request)
				if response.notDead:
					available = server
					break
			except grpc.RpcError as e:
				print("Caught could not connect")
				print(e.code())
				# Server is down, move to the next
				self.servers.pop(server)
				# Want to keep track of that server just move it to last priority
				self.servers.append(server)
		response = sns_pb2.Reply(msg="")
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
print("Router started on " + sys.argv[1] + ":" + sys.argv[2])

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop(0)
