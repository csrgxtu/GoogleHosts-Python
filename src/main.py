#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 30/Mar/2015
# File: main.py
# Desc: the entrance file of this project
#
# Produced By CSRGXTU
from Connection import Connection

class main(object):
  InputSource = None
  IPS = []

  def __init__(self, source):
    self.InputSource = source

  def run(self):
    ips = self.loadIPS()
    for ip in ips:
      conn = Connection(ip)
      if conn.httpsConn():
        print ip

  def loadIPS(self):
    res = []
    with open(self.InputSource, 'r') as myFile:
      for line in myFile:
        res.append(line.rstrip())
    return res

m = main('../data/ips.txt')
m.run()
