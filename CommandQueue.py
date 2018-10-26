# -*- coding: utf-8 -*-
'''
Created on Aug 30, 2015

@author: derp
'''
from Queue import Queue
from random import randint
import math
import time
import threading

def log(string):
    print string
    
def random_from_set(listValue):
    index = randint(0, len(listValue)-1)
    return listValue[index]

#current strategy is to wait +/- 10% of the expected wait time
def wait_randomization_strategy_result(waitTime):
    boundDeterminer = int(round(math.ceil(int(waitTime)/5)))
    if(boundDeterminer < 1):
        boundDeterminer = 1
    
    lowerBound = waitTime - boundDeterminer
    if lowerBound < 1:
        lowerBound = 2
    
    upperBound = waitTime + boundDeterminer
    if(upperBound < 4):
        upperBound = 4
    
    listValue = range(int(lowerBound), int(upperBound))
    return random_from_set(listValue)

class CommandQueueObject:
    waitTime = 0
    command = ''  
    def __init__(self, command, waitTime):
        self.waitTime = waitTime
        self.command = command

class CommandQueue:
    commandQueue = Queue()
    ircRef = None
    quieteMode = False
    
    def __init__(self, ircRef):
        self.ircRef = ircRef
        self.commandThread = threading.Thread(target=self.command_worker)
        self.commandThread.start()
        
    def __del__(self):
        self.commandThread.join()
    
    def sendCommandToQueue(self, commandValue, waitTime):
        self.commandQueue.put(CommandQueueObject(commandValue, waitTime))
        
    def join(self):
        self.commandThread.join()

    def command_worker(self):
        while True:
            commandValue = self.commandQueue.get(block=True)
            if not (self.quieteMode and commandValue.command != 'PONG'):
                self.send_timed_command(commandValue)
            else:
                print 'command to irc ommitted due to quiet mode: ' + commandValue.command
                commandValue = None

    def send_timed_command(self, commandValue):
        time.sleep(wait_randomization_strategy_result(commandValue.waitTime))
        print 'sending command: ' + commandValue.command
        self.ircRef.send(commandValue.command)