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

  def __init__(self, source):
    self.InputSource = source

  def run(self):
    IPBlocks = self.loadIPBlocks()

    for block in IPBlocks:
      ips = IPNetwork(block)
      for ip in list(ips):
        print str(ip)

  def loadIPBlocks(self):
    IPBlocks = []

    with open(self.InputSource, 'r') as myFile:
      for line in myFile:
        IPBlocks.append(line.rstrip())

    return IPBlocks
