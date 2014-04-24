#!/usr/bin/env python
import os

# 111.txt is the raw copied content from some webpage

file= open("111.txt")
ay_lines= file.readlines()

for line in ay_lines:
    if(line.strip()!=""):
        if(line.strip()[0]!="0" and line.strip()[0]!="1"):
            print line
