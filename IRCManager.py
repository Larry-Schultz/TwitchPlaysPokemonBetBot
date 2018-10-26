'''
Created on Aug 30, 2015

@author: derp
'''
import socket
from Queue import Queue
from threading import Thread

def findUsername(data):
    splitStr = data.split("!")
    if len(splitStr) > 0:
        result = splitStr[0].replace(' ', '').replace(':', '').lower()
        return result
    else:
        return None
    
def findText(data):
    firstIndex = data[1:].replace('str:', '').find(':')
    lastIndex = data[1:].replace('str:', '').rfind(':')
    if firstIndex > 0 and lastIndex > 0:
        result = data[lastIndex+1:].replace('str:', '').replace(':', '').replace('\r\n', '')
        return result
    else:
        return ''
    
def findDirectedUser(text):
    directedUser = ''
    if text is not None:
        findResult = text.find('@')
        if findResult >= 0:
            for i in range(1, len(text)):
                if text[i] != ' ':
                    directedUser = directedUser + text[i]
                else:
                    break
    
    #if still default, set it to None
    if directedUser == '':
        directedUser = None
    return directedUser

def do_nothing():
    return

class IRCManager(object):
    irc = None
    readingIRCThread = None
    ircDataQueue = Queue()
    
    def __init__(self, ircRef):
        self.irc = ircRef
        self.readingIRCThread = Thread(target=self.ircReader)
        self.readingIRCThread.start()
    
    #add all lines from irc into a queue that the main thread can read
    #helps prevent loss of irc commands due to event handling that too long
    def ircReader(self):
        while True:
            data = self.irc.recv(1024)
            if len(data.replace(' ', '')) > 0:
                self.ircDataQueue.put(data)
        