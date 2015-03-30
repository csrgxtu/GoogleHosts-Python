#!/bin/sh
#
# Author: Archer Reilly
# Date: 28/Mar/2015
# File: IpCount.sh
# Desc: count how many ips does Google have
#
# Produced By CSRGXTU
total=0
for slash in $(dig TXT +short _netblocks{,2,3}.google.com | tr ' ' '\n' | grep '^ip4:' | cut -d '/' -f 2); do
  total=$((total+$(echo "2^(32-$slash)" | bc -l)))
done
echo $total
