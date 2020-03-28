import os
import codecs
from os.path import expanduser

# cd into user home directory
home = expanduser("~")
# find all namebench files
fileList = []
path = home + '\\AppData\\Local\\Temp'
keyword = 'namebench'

for fname in os.listdir(path):
    if fname.endswith('.html'):
        if keyword in fname:
            fileList.append(fname)

# take latest file so that the newest run is used
fileList.sort()
fileUsed = path + "\\" + fileList[-1]

# line with all the server names and IP
primaryServer = ""
secondServer = ""
thirdServer = ""

f = codecs.open(fileUsed, 'r')
lines = f.readlines()

# reads file and finds 1st, 2nd
for i in range(len(lines)):
    if '<td>Primary Server</td>' in lines[i]:
        primaryServer = lines[i+1]
    if '<td>Secondary Server</td>' in lines[i]:
        secondServer = lines[i+1]

# parses substrings for IP address only
primaryServerIP = ""
index1 = primaryServer.find('ip') + 4
primaryServerIP = primaryServer[index1:]
index2 = primaryServerIP.find('</div>')
primaryServerIP = primaryServerIP[:index2]

secondServerIP = ""
index1 = secondServer.find('ip') + 4
secondServerIP = secondServer[index1:]
index2 = secondServerIP.find('</div>')
secondServerIP = secondServerIP[:index2]

# PLEASE READ: primaryServerIP and secondaryServerIP are the IP addresses only
print primaryServerIP
print secondServerIP
