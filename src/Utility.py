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
  
