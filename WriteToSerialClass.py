# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 19:22:11 2022

@author: Ryan
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:01:36 2022

@author: Ryan
"""
# Class for Handling the handling of Serial Data
# https://medium.com/vicara-hardware-university/a-guide-to-transmitting-structures-using-stm32-uart-and-python-56b67f806566

class WriteToSerial(object):
   
    def __init__(self, port):
        self.port = port
        self.vals = []
 
    def viewPorts(self):
        ports = ['COM%s' % (i + 1) for i in range(256)]
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        print(result)
        return result
            

                
# Program Loop
if __name__ == "__main__":
    import serial
    import time

    
    s = serial.Serial('COM6') # Check COM port in device manager

    s.baudrate = 230400  # set Baud rate to 230400
    s.bytesize = 8     # Number of data bits = 8
    s.parity   ='N'    # No parity
    s.stopbits = 1     # Number of Stop bits = 1
    s.timeout = 5.0  # set the read time out to 1 second    
    
    opClass = WriteToSerial(s)
    print(opClass.viewPorts())
    
    for x in range(0, 20):
        print(x)
        time.sleep(1) # Wait for 1 seconds
        s.write("%01#RDD0010000107**\r".encode())
    
    s.close() # Close Serial Port
