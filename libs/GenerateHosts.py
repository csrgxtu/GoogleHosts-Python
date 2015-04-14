#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 13/Apr/2015
# File: GenerateHosts.py
# Desc: generate hosts file for Operating system
#
# Produced By CSRGXTU
from SortIPs import SortIPs
from Utility import loadLst

class GenerateHosts(object):
  Input = None
  Output = None

  IPS = None
  DOMAINS = None

  def __init__(self, domainFile, hostFile, ipFile):
    self.Input = domainFile
    self.Output = hostFile

    self.IPS = loadLst(ipFile)
    self.DOMAINS = loadLst(domainFile)
  
  def run(self):
    # get quickest ip
    s = SortIPs(self.IPS)
    IP = s.getTopNIPs(1)
    
    res = []
    for domain in self.DOMAINS:
      res.append(IP + '  ' + domain)

    saveLst2File(self.Output, res)

  def getInput(self):
    return self.Input

  def getOutput(self):
    return self.Output
  
  def getIPS(self):
    return self.IPS
  
  def getDOMAINS(self):
    return self.DOMAINS

  def setInput(self, Input):
    self.Input = Input

  def setOutput(self, Output):
    self.Output = Output

  def setIPS(self, lst):
    self.IPS = lst

  def setDOMAINS(self, lst):
    self.DOMAINS = lst
