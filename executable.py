import logging, time, os, sys, datetime
import tkinter as tk
from tkinter import filedialog,simpledialog
import os, sys
import subprocess, pyautogui, webbrowser, wmi
from win10toast import ToastNotifier
import psutil
from tldextract import extract



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

# ~ 35 secunde pana la lansarea Steam completa

def launchGame():
    date_now  = datetime.datetime.now().strftime('%d_%m_%Y')

    if(os.path.exists(f'logs\{date_now}.log')):
        print("File exist.")
    else:
        fp = open(f'{date_now}.log', 'w+')
        fp.close()
        print("File doesn't exist.")

    if(os.path.exists(f'logs\{date_now}.log')):
        LOG_FILENAME = f'logs\{date_now}.log'
        format_string = '%(levelname)s: %(asctime)s > %(message)s;'
        logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
        logging.info("Start running Script")
    else:
        print("Close script.")
        sys.exit()

    logging.info("Start running Don't Starve Together")
    subprocess.run("start steam://run/322330", shell=True)

    logging.info("Wait 60 seconds")
    time.sleep(60)

    logging.info("Finish running Don't Starve Together")

    time.sleep(1)
    pyautogui.moveTo(960, 555, duration = 1)
    logging.info("Move mouse in position x = 1164, y = 555 for open first part of the gift")
    pyautogui.click(960, 555)
    logging.info("Click mouse in position x = 960, y = 555 for open first part of the gift")

    time.sleep(3)
    pyautogui.moveTo(871, 728, duration = 1)
    logging.info("Move mouse in position x = 871, y = 728 for open second part of the gift")
    pyautogui.click(871, 728)
    logging.info("Click mouse in position x = 871, y = 728 for open first part of the gift")

    pyautogui.moveTo(183, 870, duration = 1)
    logging.info("Move mouse in position x = 183, y = 870 for QUIT Button")

    pyautogui.click(183, 870)
    time.sleep(1)
    pyautogui.click(183, 870)
    logging.info("Click mouse in position x = 183, y = 870 for QUIT Button")

    time.sleep(2)
    pyautogui.click(794, 621)
    logging.info("Click mouse around position x = 794, y = 621 for YES Button")

    time.sleep(1)
    pyautogui.moveTo(792, 621, duration = 1)
    logging.info("Move mouse around position x = 794, y = 621 for YES Button")
    pyautogui.click(792, 621)
    logging.info("Click mouse in position x = 794, y = 621 for YES Button")

    time.sleep(1)
    logging.info("Don't Starve Together closed")
    toast = ToastNotifier()
    toast.show_toast(
    f"Everything done",
    f"{date_now}",
    duration = 2,
    threaded = True,
    )
       
    customUrlConfigPath = 'configs/customUrl.txt'
    date_now  = datetime.datetime.now().strftime('%d_%m_%Y') 
    log_path = f"logs\{date_now}.log"
    LOG_FILENAME = log_path

    if(os.stat(customUrlConfigPath).st_size == 0):
        configFile = open(customUrlConfigPath,"w+")
        toast = ToastNotifier()
        toast.show_toast(
        f"Input Custom URL",
        f"Insert Custom URL",
        duration = 5,
        threaded = True,
        )
        USER_INP = simpledialog.askstring(title="Custom URL", prompt="Insert custom URL:")
        if(USER_INP == '' and os.stat(customUrlConfigPath).st_size == 0):
            USER_INP = 'https://axbecher.com/'
            inputURL = USER_INP
        else:
            inputURL = USER_INP
        configFile.write(inputURL)
        configFile.close()
        customUrlOpen = open(customUrlConfigPath,"r+")
        customUrlPath = customUrlOpen.readline()
        tsd, td, tsu = extract(customUrlPath)
        extractName = td 
        configFile = open(customUrlConfigPath,"w+") #open config file for process
        configFile.write(customUrlPath) #write new value in customUrlConfigPath
        configFile.close()
        date_now  = datetime.datetime.now().strftime('%d_%m_%Y')
        format_string = '%(levelname)s: %(asctime)s > %(message)s;' # Log file format
        LOG_FILENAME = log_path
        logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string) #logConfig
        logging.info("Custom URL not found, need to update it") #logMessage
    else:
        customUrlOpen = open(customUrlConfigPath,"r+")
        customUrlPath = customUrlOpen.readline()
        tsd, td, tsu = extract(customUrlPath) # prints abc, hostname, com
        extractName = td # will prints as hostname.com
        date_now  = datetime.datetime.now().strftime('%d_%m_%Y')
        format_string = '%(levelname)s: %(asctime)s > %(message)s;'
        LOG_FILENAME = log_path
        logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
        logging.info("Custom URL found, it is: "+customUrlPath)
    webbrowser.open(customUrlPath, new=2)

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 220)
canvas1.pack()

f = wmi.WMI()

date_now  = datetime.datetime.now().strftime('%d_%m_%Y') 
log_path = f"logs\{date_now}.log"
LOG_FILENAME = log_path

if(os.path.exists(log_path)):
    format_string = '%(levelname)s: %(asctime)s > %(message)s;'
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
    logging.info("Verified, log file exists.")
    
    toast = ToastNotifier()
    toast.show_toast(
    f"File exist, abort.",
    f"Log file found for {date_now}",
    duration = 4,
    threaded = True,
    )

    
else:
    fp = open(log_path, 'w+')
    fp.close()
    format_string = '%(levelname)s: %(asctime)s > %(message)s;'
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
    logging.info("Verified failed, create log file")
    

    def LansareJoc():
        customUrlConfigPath = 'configs/customUrl.txt'
        date_now  = datetime.datetime.now().strftime('%d_%m_%Y') 
        log_path = f"logs\{date_now}.log"
        LOG_FILENAME = log_path

        if(os.stat(customUrlConfigPath).st_size == 0):
            configFile = open(customUrlConfigPath,"w+")
            toast = ToastNotifier()
            toast.show_toast(
            f"Input Custom URL",
            f"Insert Custom URL",
            duration = 5,
            threaded = True,
            )
            USER_INP = simpledialog.askstring(title="Custom URL", prompt="Insert custom URL:")
            if(USER_INP == '' and os.stat(customUrlConfigPath).st_size == 0):
                USER_INP = 'https://axbecher.com/'
                inputURL = USER_INP
            else:
                inputURL = USER_INP
            configFile.write(inputURL)
            configFile.close()
            customUrlOpen = open(customUrlConfigPath,"r+")
            customUrlPath = customUrlOpen.readline()
            tsd, td, tsu = extract(customUrlPath)
            extractName = td 
            configFile = open(customUrlConfigPath,"w+") #open config file for process
            configFile.write(customUrlPath) #write new value in customUrlConfigPath
            configFile.close()
            date_now  = datetime.datetime.now().strftime('%d_%m_%Y')
            format_string = '%(levelname)s: %(asctime)s > %(message)s;' # Log file format
            LOG_FILENAME = log_path
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string) #logConfig
            logging.info("Custom URL not found, need to update it") #logMessage
        else:
            customUrlOpen = open(customUrlConfigPath,"r+")
            customUrlPath = customUrlOpen.readline()
            tsd, td, tsu = extract(customUrlPath) # prints abc, hostname, com
            extractName = td # will prints as hostname.com
            date_now  = datetime.datetime.now().strftime('%d_%m_%Y')
            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            LOG_FILENAME = log_path
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Custom URL found, it is: "+customUrlPath)
        
        
        steamConfigPath = "configs/steamConfig.txt"
        
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
            steamLocation = new_steamPath
            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            LOG_FILENAME = log_path
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam Location not found, need to update it")
        else:
            steamExeLoc = open(steamConfigPath,"r+")
            steamPath = steamExeLoc.readline()
            new_steamPath = steamPath.replace( '/', '\\' )
            configFile = open(steamConfigPath,"w+")
            configFile.write(new_steamPath)
            configFile.close()
            steamLocation = new_steamPath
            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            LOG_FILENAME = log_path
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam Location found")
        

        if checkIfProcessRunning('steam.exe'):
            canvas1.pack()
            time.sleep(1)

            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam verified passed, launch script..")

            launchGame()
            sys.exit()
        else:
            time.sleep(1)
            os.startfile(steamLocation)

            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam verified failed, locate and launch Steam..")

            time.sleep(12)
            launchGame()

            format_string = '%(levelname)s: %(asctime)s > %(message)s;'
            logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
            logging.info("Steam verified passed, launch script..")
            
            canvas1.pack()
            sys.exit()
        
    def HelpMe():
        readmeLocation = "readme.txt"
        os.startfile(readmeLocation)

    def LogsLocation():
        logsLocation = "logs"
        os.startfile(logsLocation)
        
    def Habitica():
        webbrowser.open(customUrlPath, new=2)

    customUrlConfigPath = 'configs/customUrl.txt'
    date_now  = datetime.datetime.now().strftime('%d_%m_%Y') 
    log_path = f"logs\{date_now}.log"
    LOG_FILENAME = log_path

    if(os.stat(customUrlConfigPath).st_size == 0):
        configFile = open(customUrlConfigPath,"w+")
        toast = ToastNotifier()
        toast.show_toast(
        f"Input Custom URL",
        f"Insert Custom URL",
        duration = 5,
        threaded = True,
        )
        USER_INP = simpledialog.askstring(title="Custom URL", prompt="Insert custom URL:")
        if(USER_INP == '' and os.stat(customUrlConfigPath).st_size == 0):
            USER_INP = 'https://axbecher.com/'
            inputURL = USER_INP
        else:
            inputURL = USER_INP
        configFile.write(inputURL)
        configFile.close()
        customUrlOpen = open(customUrlConfigPath,"r+")
        customUrlPath = customUrlOpen.readline()
        tsd, td, tsu = extract(customUrlPath)
        extractName = td 
        configFile = open(customUrlConfigPath,"w+") #open config file for process
        configFile.write(customUrlPath) #write new value in customUrlConfigPath
        configFile.close()
        date_now  = datetime.datetime.now().strftime('%d_%m_%Y')
        format_string = '%(levelname)s: %(asctime)s > %(message)s;' # Log file format
        LOG_FILENAME = log_path
        logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string) #logConfig
        logging.info("Custom URL not found, need to update it") #logMessage
    else:
        customUrlOpen = open(customUrlConfigPath,"r+")
        customUrlPath = customUrlOpen.readline()
        tsd, td, tsu = extract(customUrlPath) # prints abc, hostname, com
        extractName = td # will prints as hostname.com
        date_now  = datetime.datetime.now().strftime('%d_%m_%Y')
        format_string = '%(levelname)s: %(asctime)s > %(message)s;'
        LOG_FILENAME = log_path
        logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format=format_string)
        logging.info("Custom URL found, it is: "+customUrlPath)

    debugInfo = "(!) Welcome."
    button1 = tk.Button (root, text="1. START",command=LansareJoc,bg='brown',fg='white')
    button2 = tk.Button (root, text="2. HELP",command=HelpMe,bg='grey',fg='black')
    button3 = tk.Button (root, text="3. "+extractName.upper()+"",command=Habitica,bg='purple',fg='white')
    button4 = tk.Button (root, text="4. LOGS",command=LogsLocation,bg='grey',fg='white')

    canvas1.create_window(150, 30, window=button1) #DontStarveTogether
    canvas1.create_window(150, 70, window=button2) #Help
    canvas1.create_window(150, 110, window=button3) #Habitica
    canvas1.create_window(150, 150, window=button4) #Habitica
    
    root.resizable(False, False)
    root.mainloop()