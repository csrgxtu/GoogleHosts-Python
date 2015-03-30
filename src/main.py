#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 30/Mar/2015
# File: main.py
# Desc: the entrance file of this project
#
# Produced By CSRGXTU
from Connection import Connection
import multiprocessing as mp
from math import ceil

class main(object):
  InputSource = None
  IPS = mp.Queue()

  def __init__(self, source):
    self.InputSource = source

  def worker(self, ips):
    for ip in ips:
      conn = Connection(ip)
      if conn.httpsConn():
        self.IPS.put(ip)

  def run(self):
    ips = self.loadIPS()
    for chunk in self.splitGenerator(ips, int(ceil(len(ips)/4.0))):
      print 'DEBUG: ', len(chunk)

    #processes = [mp.Process(target=self.worker, args=(x,)) for x in range(4)]

  def loadIPS(self):
    res = []
    with open(self.InputSource, 'r') as myFile:
      for line in myFile:
        res.append(line.rstrip())
    return res

  def saveIPS(self):
    with open(self.Output, 'w') as myFile:
      for ip in self.IPS:
        myFile.write(ip + '\n')

  def splitGenerator(self, lst, n):
    """ Yield successive n-sized chunks from lst."""
    for i in xrange(0, len(lst), n):
      yield lst[i:i+n]

m = main('../data/ips.txt')
m.run()
