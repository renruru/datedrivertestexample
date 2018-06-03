import os
import time

def getscreenshordDir():
    # a = os.path.abspath(__file__)
    # b = os.path.dirname(os.path.abspath(__file__))
    c = os.path.dirname(__file__)
    # print(c)
    rootDir = os.path.split(c)[0]
    # print('root = ' + rootDir)
    newDir = os.path.join(rootDir,'screenshorts')

    if os.path.exists(newDir):
        print('ok')
    else:
        os.mkdir(newDir)
    # print('new = '+ newDir)
    return newDir


def getPngFileName():
    screenshotsDir = getscreenshordDir()
    current_time = time.time()
    filename = os.path.join(screenshotsDir,str(current_time)+'.png')
    return filename
    