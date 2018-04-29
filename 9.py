import time
print time.ctime()
print time.ctime()
print'_____________________'
print time.ctime()
time.sleep(1)
print time.ctime()
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))