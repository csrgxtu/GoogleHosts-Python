#!/usr/bin/env python
#
# Author: Archer Reilly
# File: Utility.py
# Date: 09/Apr/2015
# Desc: some utility functions
#
# Produced By CSRGXTU
from Download import Download
import Utility

# check if is the Google search page
#
# @param schema string
# @param ip string
# @return boolean
def isGoogleSearch(schema, ip):
  d = Download(schema + '://' + ip)
  if d.doRequest():
    return False

  if Utility.containsGoogle(d.getSOURCE()):
    return True
  
  return False

# check if a string contains <title>Google</title>
#
# @param html string
# @return boolean
def containsGoogle(html):
  item = '<title>Google</title>'
  if item in html:
    return True
  else:
    return False

# split a list into m equal chunked
#
# @param lst list
# @param n int
# @return yield list
def splitGenerator(lst, n):
  """ Yield successive n-sized chunks from lst."""
  for i in xrange(0, len(lst), n):
    yield lst[i:i+n]

# append list 2 file
#
# @param outFile string
# @param lst list
# @return void
def appendLst2File(outFile, lst):
  with open(outFile, 'a') as myFile:
    for item in lst:
      myFile.write(item + '\n')

    myFile.close()

# load IPs from file into list
#
# @param inputFile string
# @return lst list
def loadIPS(inputFile):
  res = []

  with open(inputFile, 'r') as myFile:
    for line in myFile:
      res.append(line.rstrip())
    myFile.close()

  return res
