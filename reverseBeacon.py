import sys
import telnetlib

HOST = "telnet.reversebeacon.net"
call = "in3aqk"
port = 7000
tn = telnetlib.Telnet(HOST,port,timeout=5)

tn.read_until("call: ",10)
tn.write(call + "\n")
while True:
    line=tn.read_until("\n",10)
    if 'DX' in line:
        lineArr =  line.split()
        try:
            speed = int(lineArr[8])
            if speed <= 14 and lineArr[10] == 'CQ':
                result = "%s\t\t%s\t%s\t%s wpm\t%s\t%s" % (lineArr[3],lineArr[4],lineArr[5],lineArr[8],lineArr[10],lineArr[11])
                print result
        except ValueError:
            print "Conversion error"

tn.close()
