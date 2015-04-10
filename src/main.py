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
from Utility import isGoogleSearch, splitGenerator, appendLst2File
from Utility import loadIPS

class main(object):
  InputSource = None
  Output = None

  def __init__(self, source, output):
    self.InputSource = source
    self.Output = output

  def worker(self, name, ips):
    res = []
    for ip in ips:
      conn = Connection(ip)
      if conn.httpsConn():
        if isGoogleSearch('http', ip) or isGoogleSearch('https', ip):
          print 'Worker ' + name + ': ', ip
          res.append(ip)
    appendLst2File(self.Output, res)

  def run(self):
    processes = []
    ips = loadIPS(self.InputSource)
    i = 0
    for chunk in splitGenerator(ips, int(ceil(len(ips)/20.0))):
      processes.append(mp.Process(target=self.worker, args=(str(i), chunk)))
      i = i + 1

    for p in processes:
      p.start()

    for p in processes:
      p.join()
    
m = main('../data/ips.txt', '../data/ipsok.txt')
m.run()
