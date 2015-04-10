#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 10/Apr/2015
# File: SortIPs.py
# Desc: sort ips according to the connection time
#
# Produced By CSRGXTU
from Connection import Connection
from time import time

class SortIPs(object):
  IPS = None
  RES = None

  def __init__(self, ips):
    self.IPS = ips
    self.RES = []
  
  # add connection times to the ips
  #
  # @return num int how many ips added times
  def addTimes(self):
    for ip in self.IPS:
      start = time()
      conn = Connection(ip)
      if conn.httpsConn():
        end = time()
        self.RES.append([ip, end - start])

    return len(self.RES)

  def asc(self):
    pass

  def desc(self):
    pass

  def getIPS(self):
    pass

  def getRES(self):
    pass

  def setIPS(self, ips):
    pass

  def setRES(self, lst):
    pass
