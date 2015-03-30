#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 30/Mar/2015
# File: Connection.py
# Desc: testing the connection to a host
#
# Produced By CSRGXTU
import socket
import os

class Connection(object):
  IP = None

  def __init__(self, ip):
    self.IP = ip

  def httpConn(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex((self.IP, 80))
    sock.close()
    if res == 0:
      return True
    return False

  def httpsConn(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex((self.IP, 443))
    sock.close()
    if res == 0:
      return True
    return False

  def socketConn(self, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect.ex((self.IP, port))
    sock.close()
    if res == 0:
      return True
    return False

  def icmpConn(self):
    res = os.system("ping -c 5 " + self.IP)
    if res == 0:
      return True
    return False
