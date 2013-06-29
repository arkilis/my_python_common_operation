# Read and Write file
# Ben Liu
# arkilis@gmail.com
# 2012-02-29


# Read a file line by line
# Remember in this way, but the output will keep the '\n' of each line
import os

def readfile1(filePath):
    szList=[]
    if(os.path.exists(filePath)==False):
        return False
    fp= open(filePath, "r")
    r= fp.readline()
    while(r!='\n'):
        print r
        r= fp.readline()
        szList.append(r)
    return szList


# To avoid the problem, there are two ways
# The 1st is use readlines()
# But this will consume a lot memory in practise

def readfile2(filePath):
    if(os.path.exists(filePath)==False):
        return False
    fp= open(filePath, "r")
    for line in lines:
        print line
    fp.close()

# 2nd way to solve this to use the replace(), similar with readfile1()

def readfile3(filePath):
    szList=[]
    if(os.path.exists(filePath)==False):
        return False
    fp= open(filePath, "r")
    r= fp.readline()
    while(r!='\n'):
        print r.replace("\n", "")
        r= fp.readline()
        szList.append(r)
    return szList

# Read all the content of a file
def readAll(filePath):
    if(os.path.exists(filePath)==False):
        return False
    fp= open(filePath, "r") # Support only after python 2.2
    print fp



if(__name__=="__main__"):
    print readfile("1.txt")





