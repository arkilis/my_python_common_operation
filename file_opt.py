# Read and Write file
# Ben Liu
# arkilis@gmail.com
# 2012-02-29


# Read a file line by line
# Remember in this way, the output will keep the '\n' of each line
import os

def readfile(filePath):
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


# 



if(__name__=="__main__"):
    print readfile("1.txt")





