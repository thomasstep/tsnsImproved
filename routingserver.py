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


class snsServicer(sns_pb2_grpc.SNSServiceServicer):

	def __init__(self):
		#need to create list for Masters' IP and PORT num
		self.masterInfo = {}

	def GetAvailable(self, request, context):
		response = sns_pb2.Reply()
		# if the client initiates a GetAvailable call, do I need to look at the notDead msg
		# can I just check to see which server is alive, then reply with that servers
		# port # and IP
	
	def findRouting(self, request, context):
		# will populate masterInfo

	def Election(self, request, context):
		response = sns_pb2.Alive()
		# need to know other masters IP and Port to send client msg

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

sns_pb2_grpc.add_SNSServiceServicer_to_server(snsServicer(), server)

print("Starting server on port 8080")
server.add_insecure_port("[::]:" + sys.argv[1])
server.start()

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop(0)
		
