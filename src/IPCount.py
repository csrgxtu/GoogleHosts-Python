#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 28/Mar/2015
# File: IPCount.py
# Desc: count Google ip addresses
#
# Produced By CSRGXTU
import os
import re

# first, get the ip blocks
res = os.popen('nslookup -q=TXT _netblocks.google.com 8.8.8.8').read()
IPBlocks = []
for item in res.split(':'):
  matchObj = re.match(r'^([\d|.]+)(/\d+)', item, re.M|re.I)
  if matchObj:
    IPBlocks.append(matchObj.group(1) + matchObj.group(2))
print IPBlocks

# count how many ip are there
IPCounts = 0
for item in IPBlocks:
  IPCounts = IPCounts + (2 ** (32 - int(item[item.index('/') + 1: ])) - 2)
print IPCounts
