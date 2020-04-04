#!/usr/bin/python

import json
import os
import pandas as pd
import ast


Queue_name = "QUEUE_NAME"
InstantenousFairResources1 = "InstantenousFairResources"
UsedResources1 = "UsedResources"

reports = os.system('curl -k  -u aanatha:phone@123 -H "Accept: application/json" -X GET -s -k http://resourcemanager.com/ws/v1/cluster/scheduler | python -m json.tool | more > out5.json')
with open('out5.json') as json_file:
     data = json.load(json_file)
     for p in data['scheduler']['schedulerInfo']['rootQueue']['childQueues']['queue']:
         QUEUE_NAME = p["queueName"]
         InstantenousFairResources = p["fairResources"]["memory"]
         UsedResources = p["usedResources"]["memory"]
         print("""%-15s %10s %10s \n""" % (QUEUE_NAME, InstantenousFairResources, UsedResources))
