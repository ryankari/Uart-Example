# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 17:58:09 2022

@author: Ryan
# Class for Handling the handling of Serial Data
# https://medium.com/vicara-hardware-university/a-guide-to-transmitting-structures-using-stm32-uart-and-python-56b67f806566

Uses a start indicator of 'S' and end indicator of 'Z'
0x0A ends the session, but needs to be sent from dsPIC between 'S' and 'Z'. 
"""

def readUART(SerialObj,vals):
    readIndicator = False

    while not readIndicator:
        myByte = SerialObj.read(1)
        if myByte == b'S':  # Look for Start indicator 
    
            ReceivedString = SerialObj.read_until(b'Z')
            print(ReceivedString)
            try:
                new_values = struct.unpack('<ff', ReceivedString[0:len(ReceivedString)-1])
                vals.append(list(new_values))
                readIndicator = True
                return True,vals,ReceivedString
            except KeyboardInterrupt:
                   return False,vals,ReceivedString # Stop Program  
            except:
                   return False,vals,ReceivedString # To ignore struct error

from serial import Serial
import struct
import numpy as np
import matplotlib.pyplot as plt

SerialObj = Serial('COM6')

SerialObj.baudrate = 230400  # set Baud rate to 115200
SerialObj.bytesize = 8     # Number of data bits = 8
SerialObj.parity   ='N'    # No parity
SerialObj.stopbits = 1     # Number of Stop bits = 1
SerialObj.timeout = 1.0  # set the read time out to 1 second

state = True
vals = []
while state:
    state,vals,ReceivedString = readUART(SerialObj,vals)


SerialObj.close()

npArray = np.array(vals)
plt.plot(npArray[:,0])
