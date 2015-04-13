#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 30/Mar/2015
# File: PrepareIPS.py
# Desc: preparing the IP address
#
# Produced By CSRGXTU
from netaddr import *

class PrepareIPS(object):
  InputSource = None
  Output = None
  IPS = []

  def __init__(self, source, output):
    self.InputSource = source
    self.Output = output

  def run(self):
    IPBlocks = self.loadIPBlocks()

    for block in IPBlocks:
      ips = IPNetwork(block)
      for ip in list(ips):
        self.IPS.append(str(ip))

    self.saveIPS()

  def loadIPBlocks(self):
    IPBlocks = []

    with open(self.InputSource, 'r') as myFile:
      for line in myFile:
        IPBlocks.append(line.rstrip())

    return IPBlocks

  def saveIPS(self):
    with open(self.Output, 'w') as myFile:
      for ip in self.IPS:
        myFile.write(ip + '\n')
