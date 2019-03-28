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

class snsServicer(sns_pb2_grpc.snsServiceServicer):

	def __init__(self):
		self.masterAlive = True
		#spawn a thread 

	def KeepAlive(self, request, context):
		time.sleep(3)

# Create the server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Add class to server
sns_pb2_grpc.add_SNSServiceServicer_to_server(snsServicer(), server)

# Listen on port 8888
print("Starting server on port 8888")
server.add_insecure_port("[::]:" + sys.argv[1])
server.start()

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop(0)
