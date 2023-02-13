
import datetime
import wmi
import time
import os

time_now  = datetime.datetime.now().strftime('%d_%m_%Y') 

print(time_now)

f = wmi.WMI()

import psutil
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if checkIfProcessRunning('steam.exe'):
    print('Yes a steam process was running')
else:
    print('No steam process was running')
    print('Running it...')
    time.sleep(1)
    os.startfile('D:\\Personal\\Gaming\\Steam\\steam.exe')
    print(f"Steam run")
    
# Displaying the output
#print(output)

# print("pid   Process name")

# for process in f.Win32_Process():
#     print(f"{process.ProcessId:<10} {process.Name}")
#     if(process.Name == "steam.exe"):
#         print(f"{process.ProcessId:<10} {process.Name}")
#         break
#     else:
#         print(f"Not there")
#         time.sleep(2)
#         print(f"Running it...")
#         os.startfile('D:\\Personal\\Gaming\\Steam\\steam.exe')
#         print(f"Steam run")
#         break

