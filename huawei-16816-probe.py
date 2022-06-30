#!/usr/bin/python
"""Copyright 2008 Orbitz WorldWide

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

import htcondor 
import classad
import sys
import time
import os
import platform 
import subprocess
from socket import socket
from pysnmp.hlapi import *

CARBON_SERVER = '90.147.169.209'
CARBON_PORT = 2003
now = int( time.time() )



def getBGPRoutes():

  lines = []

  errorIndication, errorStatus, errorIndex, varBinds = next(
  getCmd(
     SnmpEngine(),
     CommunityData('ReCaScoreSwitch'),
     UdpTransportTarget(('90.147.169.124', 161)),
     ContextData(),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.177.9.1.0')),
  ))

  for varBind in varBinds:
    lines.append("network.huawei.bgp.routes %d %d" % (int(varBind[1]), now))
  sendData(lines)

def getCpuUsage():
  
  lines = []

  slots = {
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17694721': 'CE-MPUA-14',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17629185': 'CE-MPUA-13',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.16842753': 'CE-L48XS-EA-1',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.16908289': 'CE-L48XS-EA-2',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.16973825': 'CE-L48XS-EA-3',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17039361': 'CE-L48XS-EA-4',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17104897': 'CE-L48XS-EA-5',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17170433': 'CE-L48XS-EA-6',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17235969': 'CE-L48XS-EA-7',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17301505': 'CE-L48XS-EA-8',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17367041': 'CE-L48XS-EA-9',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17432577': 'CE-L48XS-EA-10',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17891329': 'CE-SFU12A-17',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17956865': 'CE-SFU12A-18',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.18022401': 'CE-SFU12A-19',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.18087937': 'CE-SFU12A-20',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.18153473': 'CE-SFU12A-21',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.18219009': 'CE-SFU12A-22'
  }

  errorIndication, errorStatus, errorIndex, varBinds = next(
  getCmd(
     SnmpEngine(),
     CommunityData('ReCaScoreSwitch'),
     UdpTransportTarget(('90.147.168.1', 161)),
     ContextData(),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17694721')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17629185')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.16842753')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.16908289')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.16973825')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17039361')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17104897')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17170433')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17235969')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17301505')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17367041')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17432577')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17891329')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.17956865')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.18022401')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.18087937')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.18153473')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.18219009')),
  ))

  for varBind in varBinds:
    lines.append("network.huawei.cpu.%s %d %d" % (slots[str(varBind[0])], int(varBind[1]), now))
  sendData(lines)

def getIPv6IfSpeed():

  lines = []

  slots = {
    '1.3.6.1.2.1.55.1.6.1.1.515': 'IPv6-T2-Farm-Uplink'
  }

  errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(
    SnmpEngine(),
    CommunityData('ReCaScoreSwitch'),
    UdpTransportTarget(('90.147.168.1', 161)),
    ContextData(),ObjectType(ObjectIdentity('IPV6-MIB','ipv6IfStatsInReceives', 515)),
  ))

  for varBind in varBinds:
     lines.append("network.huawei.throughput.input.%s %d %d" % (slots[str(varBind[0])], int(varBind[1]), now))
  sendData(lines)

  slots = {
    '1.3.6.1.2.1.55.1.6.1.11.515': 'IPv6-T2-Farm-Uplink'
  }

  errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(
    SnmpEngine(),
    CommunityData('ReCaScoreSwitch'),
    UdpTransportTarget(('90.147.168.1', 161)),
    ContextData(),ObjectType(ObjectIdentity('IPV6-MIB','ipv6IfStatsOutRequests', 515)),
  ))


  for varBind in varBinds:
     lines.append("network.huawei.throughput.output.%s %d %d" % (slots[str(varBind[0])], int(varBind[1]), now))
  sendData(lines)

def getIfSpeed():

  lines = []

  slots = {
    '1.3.6.1.2.1.31.1.1.1.6.303': '12812-Uplink_VLAN-1100'
  }

  errorIndication, errorStatus, errorIndex, varBinds = next(
  getCmd(
     SnmpEngine(),
     CommunityData('ReCaScoreSwitch'),
     UdpTransportTarget(('90.147.169.124', 161)),
     ContextData(),
     ObjectType(ObjectIdentity('IF-MIB','ifHCInOctets', 303)),
  ))

  print(errorStatus)
  for varBind in varBinds:
     lines.append("network.huawei16816.throughput.input.%s %d %d" % (slots[str(varBind[0])], int(varBind[1]), now))
  sendData(lines)
  
  slots = {
    '1.3.6.1.2.1.31.1.1.1.10.303': '12812-Uplink_VLAN-1100'
  }

  errorIndication, errorStatus, errorIndex, varBinds = next(
  getCmd(
     SnmpEngine(),
     CommunityData('ReCaScoreSwitch'),
     UdpTransportTarget(('90.147.169.124', 161)),
     ContextData(),
     ObjectType(ObjectIdentity('IF-MIB','ifHCOutOctets', 303)),
  ))
   

  for varBind in varBinds:
     lines.append("network.huawei16816.throughput.output.%s %d %d" % (slots[str(varBind[0])], int(varBind[1]), now))
  sendData(lines)


def getTemperature():

  lines = []

  slots = {
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.16842753': 'CE-L48XS-EA-1',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.16908289': 'CE-L48XS-EA-2',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.16973825': 'CE-L48XS-EA-3',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17039361': 'CE-L48XS-EA-4',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17104897': 'CE-L48XS-EA-5',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17170433': 'CE-L48XS-EA-6',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17235969': 'CE-L48XS-EA-7',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17301505': 'CE-L48XS-EA-8',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17367041': 'CE-L48XS-EA-9',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17432577': 'CE-L48XS-EA-10',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19398657': 'POWER-1',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19464193': 'POWER-2',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19529729': 'POWER=3',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19595265': 'POWER-4',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19660801': 'POWER-5',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19726337': 'POWER-6',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19791873': 'POWER-7',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19922945': 'POWER-9',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19988481': 'POWER-10',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17629185': 'CE-MPUA-13',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17694721': 'CE-MPUA-14',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17760257': 'CE-CMUA-15',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17825793': 'CE-CMUA-16',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17891329': 'CE-SFU12A-17',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17956865': 'CE-SFU12A-18',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.18022401': 'CE-SFU12A-19',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.18087937': 'CE-SFU12A-20',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.18153473': 'CE-SFU12A-21',
     '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.18219009': 'CE-SFU12A-22'

  }

  errorIndication, errorStatus, errorIndex, varBinds = next(
  getCmd(
     SnmpEngine(),
     CommunityData('ReCaScoreSwitch'),
     UdpTransportTarget(('90.147.168.1', 161)),
     ContextData(),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.16842753')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.16908289')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.16973825')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17039361')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17104897')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17170433')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17235969')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17301505')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17367041')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17432577')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17629185')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17694721')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17760257')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17825793')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17891329')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.17956865')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.18022401')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.18087937')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.18153473')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.18219009')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19398657')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19464193')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19529729')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19595265')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19660801')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19726337')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19791873')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19922945')),
     ObjectType(ObjectIdentity('1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.19988481')),
  ))

  for varBind in varBinds:
     lines.append("network.huawei.temperature.%s %d %d" % (slots[str(varBind[0])], int(varBind[1]), now))
  sendData(lines)





def sendData(lines):
  
  sock = socket()
  try:
    sock.connect( (CARBON_SERVER,CARBON_PORT) )
  except:
    print "Couldn't connect to %(server)s on port %(port)d, is carbon-agent.py running?" % { 'server':CARBON_SERVER, 'port':CARBON_PORT }
    sys.exit(1)

  message = '\n'.join(lines) + '\n' #all lines must end in a newline
  #for g in lines: print g
  #print message
  #sys.exit(0)
  sock.sendall(message)

#a = getCpuUsage()
b = getIfSpeed()
#c = getBGPRoutes()
#d = getTemperature()
#e = getIPv6IfSpeed()

