import datetime
import logging
import os
import sys

from tkinter import filedialog
from tkinter import *
from win10toast import ToastNotifier

root = Tk()
root.withdraw()

steamConfigPath = "configs/steamConfig.txt"
steamPath = "null"

if(os.path.exists(steamConfigPath)):
    if(os.stat(steamConfigPath).st_size == 0):
        configFile = open(steamConfigPath,"w+")
        toast = ToastNotifier()
        toast.show_toast(
        f"Steam Location",
        f"Select steam.exe",
        duration = 5,
        threaded = True,
        )
        steamExe = filedialog.askopenfilename()
        configFile.write(steamExe)
        configFile.close()
        steamExeLoc = open(steamConfigPath,"r+")
        steamPath = steamExeLoc.readline()
        new_steamPath = steamPath.replace( '/', '\\' )
        configFile = open(steamConfigPath,"w+")
        configFile.write(new_steamPath)
        configFile.close()
    else:
        steamExeLoc = open(steamConfigPath,"r+")
        steamPath = steamExeLoc.readline()
        new_steamPath = steamPath.replace( '/', '\\' )
        configFile = open(steamConfigPath,"w+")
        configFile.write(new_steamPath)
        configFile.close()
else:
    configFile = open(steamConfigPath,"w+")
    configFile.close()
    print("DEBUG: SteamLocation not set, automatically set it.")


print("After:" + new_steamPath)
    
date_now  = datetime.datetime.now().strftime('%d_%m_%Y')
log_path = f"logs\{date_now}_var.log" 
LOG_FILENAME = log_path


if(os.path.exists(log_path)):
    format_string = '%(levelname)s: %(asctime)s > %(message)s;'
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
    logging.info("Verified, log file exists.")
else:
    fp = open(f'{date_now}.log', 'w+')
    fp.close()
    format_string = '%(levelname)s: %(asctime)s > %(message)s;'
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
    logging.info("Verified failed, create log file")

if(os.path.exists(log_path)):
    format_string = '%(levelname)s: %(asctime)s > %(message)s;'
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
    logging.info("Script start running... ")
else:
    print("Close script.")
    sys.exit()