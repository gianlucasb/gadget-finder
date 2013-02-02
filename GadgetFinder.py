#!/usr/bin/env python

import sys
import os

start = 0x08048134

if len(sys.argv) < 3:
  print "Enter an input file and a number of bytes to look back"
  sys.exit(1)

offset = int(sys.argv[2])

with os.popen("objdump -D %s | head"%sys.argv[1]) as f:
  for line in f:
    if line.startswith("0"):
      start = int(line.split()[0],16)

binary = ""

with open(sys.argv[1],"rb") as f:
  binary = f.read()

count = 0

rets = []

for letter in binary:
  if letter == '\xc3':
    rets.append(count)
  count += 1
 
for ret in rets:
  with open("dump","wb") as f:
    for i in range(0,offset+1)[::-1]:
      f.write(binary[ret-i])
  output = ""
  with os.popen("objdump -D -b binary -mi386 dump") as f:
    for line in f:
      output += line
  if output.find("ret") > 0:
    print output.replace("00000000","%s"%hex(start+ret-315))
