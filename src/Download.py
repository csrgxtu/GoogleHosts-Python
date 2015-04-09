#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 05-Aug-2014
# File: Download.py
# Description: download a webpage according to the url you
# specified.
# WebSite: http://csrgxtu.blog.com/
# Produced By CSRGXTU.
import urllib2
import socket
import re

class Download(object):
  
  URL = None
  REDIRECTED_URL = None
  HTTP_CODE = 403
  SOURCE = None
  TIME_OUT = 20
  HEAD = None
  
  USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
  REQ_HEAD = {"Referer": "http://www.google.com",
    "User-Agent": USER_AGENT
  }
  
  def __init__(self, url):
    self.setURL(url)
  
  def doRequest(self):
    try:
      req = urllib2.Request(self.getURL(), headers = self.REQ_HEAD)
      handler = urllib2.urlopen(url = req, timeout = self.getTIMEOUT())
      #handler = urllib2.urlopen(self.getURL(), timeout = self.getTIMEOUT())
      
      self.setREDIRECTEDURL(handler.geturl())
      self.setHTTPCODE(handler.getcode())
      self.setSOURCE(handler.read())
      self.setHEAD(handler.info())
      return 0
    except Exception, e:
      if isinstance(e, urllib2.HTTPError):
        print 'http error: {0}'.format(e.code)
        return 1
      elif isinstance(e, urllib2.URLError)  and isinstance(e.reason, socket.timeout):
        print 'url error: socket timeout {0}'.format(e.__str__())
        return 1
      else:
        print 'misc error: ' + e.__str__()
        return 1
 
  def getURL(self):
    return self.URL
  
  def getREDIRECTEDURL(self):
    return self.REDIRECTED_URL
  
  def getHTTPCODE(self):
    return self.HTTP_CODE
  
  def getSOURCE(self):
    return self.SOURCE;
  
  def getTIMEOUT(self):
    return self.TIME_OUT
  
  def getHEAD(self):
    return self.HEAD
  
  def getUSERAGENT(self):
    return self.USER_AGENT
  
  def getREQHEAD(self):
    return self.REQHEAD
  
  # @parameter url (string)
  def setURL(self, url):
    self.URL = url
  
  # @parameter url (string)
  def setREDIRECTEDURL(self, url):
    self.REDIRECTED_URL = url
  
  # @parameter http_code (int)
  def setHTTPCODE(self, http_code):
    self.HTTP_CODE = http_code
  
  # @parameter source (string)
  def setSOURCE(self, source):
    self.SOURCE = source
  
  # @parameter time_out (int)
  def setTIMEOUT(self, time_out):
    self.TIME_OUT = time_out;
  
  # @parameter head (string)
  def setHEAD(self, head):
    self.HEAD = head
  
  # @parameter user_agent (string)
  def setUSERAGENT(self, user_agent):
    self.USER_AGENT = user_agent
  
  # @parameter req_head
  def setREQHEAD(self, req_head):
    self.REQ_HEAD = req_head
  
  def __str__(self):
    return self.URL
