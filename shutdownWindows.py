import os

def shutdown():
    #calling os.system func. with parameters
    #/s for shutdown and /t parameter that specifies a time interva, 1 for 1 sec
    #Without the /t parameter, the default is 30 seconds before initiating shutdown.
    os.system("shutdown /s /t 1")

shutdown()
