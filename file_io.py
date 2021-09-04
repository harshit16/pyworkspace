import os
import sys
import re
from datetime import datetime


fileName = "/Users/harshitgupta/UsbTest_x64_Win10_20.2.33.log"

if os.path.exists(fileName):
    start_time = "Test Run Beginning:"
    end_time = "Test Run Ended"
    d = {}
    mfile = open(fileName, 'r')
    file_name = os.path.basename(fileName)
    filedata =[]
    filedata = file_name.split("_") 
    d["Utility Tested: "] = filedata[0]
    d["OS Arch: "] = filedata[1]
    d["OS Flavour :"] = filedata[2]
    d["Product Version: "] = filedata[3].split(".l")[0]
    data = mfile.read()
    Testfailed = data.count("Failing Test:") 
    Testpassed = data.count("Test Passed!!!!")  
    total_test = Testfailed + Testpassed
    d["Total Tests Run: "] = total_test
    d["Total Tests Failed: "] = Testfailed
    d["Total Tests Passed: "] = Testpassed
    mfile = open(fileName, 'r')
    for line in mfile:
        if start_time in line:
            itime_stamp = ''.join([char for char in line.casefold() if char not in 'ampqwertyuiosdfghjklnbvcxz']).split(": ")[1]
        if end_time in line:
            etime_stamp = ''.join([char for char in line.casefold() if char not in 'ampqwertyuiosdfghjklnbvcxz']).split(": ")[1]
    date_time_format = '%d/%m/%Y %I:%M:%S'
    tdelta = datetime.strptime(etime_stamp.strip(), date_time_format) - datetime.strptime(itime_stamp.strip(), date_time_format)
    for i in d:
        print(i, d[i], sep = ' ')
    print("Total execution time: ", tdelta)    
