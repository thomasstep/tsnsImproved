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

channel = grpc.insecure_channel(sys.argv[1]+":"+sys.argv[2])
stub = sns_pb2_grpc.SNSServiceStub(channel)
request = sns_pb2.Alive(notDead=True)
response = stub.GetAvailable(request)
print(response.msg)
