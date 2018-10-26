# -*- coding: utf-8 -*-
'''
Created on Aug 30, 2015

@author: derp
'''
from collections import defaultdict
from cobe.brain import Brain
import random
import time
import threading
import gc

class MarkovChainChatter:
    chattiness = 300
    chain_length = 2
    commandQueueRef = None
    chatGeneratorThread = None
    initialWaitTime = 10
    
    markov = defaultdict(list)
    STOP_WORD = "\n"
    write_to_file = False
    fileLocation = ''
    max_words = 10000
    
    filteredCharacters = ['\\', '!', '.', '?', '/', ')', '(', '*', '-', '~', '\n', '\r', '\t', '>']
    emotes = [':)', ':(', ':o', ':z', 'B)', ':\\', ';)', ';p', ':p', 'R)', 'o_O', ':D', '>(', '<3', '<3', 'R)', ':>', '<]', ':7', ':(', ':P', ';P', ':O', ':\\', ':|', ':s'
              ,':D', '>(', '#/', 'KappaHD', 'MiniK', 'MiniK', 'imGlitch', 'copyThis', 'pastaThat', '<3', '͡°', 'ʖ' ]
    faceEmotes = ['tppCrit', 'tppMiss', 'tppHax', 'tppRng', 'tppHelix', 'tppPokeyen', 'tppRobored', 'tppRiot', 'tppPc', 'tppDome']
    wordsToFilter = ['raid', 'fuck', 'shit', 'bitch']
    
    brain = None
    brainCache = []
    sendChatMessageLock = threading.Lock()
    
    def __init__(self, commandQueueRef, trainingTextFileLocation):
        self.commandQueueRef = commandQueueRef
        self.fileLocation = trainingTextFileLocation
        
        self.chatGeneratorThread = threading.Thread(target=self.workerThread)
        self.chatGeneratorThread.start()
        
        emotesFileHandle = open('faceEmotes.txt', 'r')
        for line in emotesFileHandle.readlines():
            self.faceEmotes.append(line.replace(' ', '').replace('\n', ''))
        emotesFileHandle.close()
        
        '''
        trainingFileHandle = open(self.fileLocation)
        for line in trainingFileHandle.readlines():
            line = line.replace('\n', '').replace('\r', '')
            if len(line.split(' ')) > (self.chain_length + 1) and line.find('@') < 0:
                self.brain.learn(line)
        trainingFileHandle.close()
        '''

    def add_to_brain(self, msg):
        #self.sendChatMessageLock.acquire()
        currentMsg = self.cleanString(msg)
        if len(currentMsg.split(' ')) > 2 and currentMsg.find('@') < 0: #add new message if it meets certain criteria
            self.brainCache.append(currentMsg)
        #self.sendChatMessageLock.release()
        '''
        if self.write_to_file and len(msg.split(' ')) > (self.chain_length + 1):
            f = open(self.fileLocation, 'a')
            f.write(msg + '\n')
            f.close()
        buf = [self.STOP_WORD] * self.chain_length
        if len(msg.split(' ')) > (self.chain_length + 1): #must be enough words to store anything
            for word in msg.split():
                self.markov[tuple(buf)].append(word)
                del buf[0]
                buf.append(word)
            self.markov[tuple(buf)].append(self.STOP_WORD)
            '''
        
    def generate_sentence(self, msg):
        if self.brain is not None:
            return self.brain.reply(text=msg, max_len=30)
        '''
        buf = msg.split()[:self.chain_length]
        if len(msg.split()) > self.chain_length:
            message = buf[:]
        else:
            message = []
            for i in xrange(self.chain_length):
                message.append(random.choice(self.markov[random.choice(self.markov.keys())]))
        for i in xrange(self.max_words):
            try:
                next_word = random.choice(self.markov[tuple(buf)])
            except IndexError:
                continue
            if next_word == self.STOP_WORD:
                break
            message.append(next_word)
            del buf[0]
            buf.append(next_word)
        return ' '.join(message)
        '''
        
    def cleanString(self, msg):
        result = msg.lower()
        for character in self.filteredCharacters:
            result = result.replace(character, '')
        for emote in self.emotes:
            result = result.replace(emote.lower(), '')
        for faceEmote in self.faceEmotes:
            result = result.replace(faceEmote.lower(), '')
        for word in self.wordsToFilter:
            result = result.replace(word.lower(), '')
        return result
    
    def join(self):
        self.chatGeneratorThread.join()
    
    def workerThread(self):
        self.brain = Brain(self.fileLocation)
        #wait a few minutes to load enough information
        time.sleep(self.initialWaitTime)
        while True:
            time.sleep(self.chattiness)
            if len(self.brainCache) == 0:
                '''
                try:
                    self.sendChatMessageLock.release()
                except Exception, e:
                    z = e
                    print 'release exception: ' + str(z)
                    '''
                print 'there was nothing to reply to'
                pass
            else:
                print 'adding new info from cache: ' + str(self.brainCache)
                for msg in self.brainCache: #add all current messages to the brain
                    self.brain.learn(msg)
                usedMessage = max(self.brainCache, key = lambda msg: len(msg))
                print 'replying to message: ' + usedMessage
                message = (usedMessage + '.')[:-1] #get a copy of the longest message
                del self.brainCache[:] #clear cache after storing the messages in the brain
                self.brainCache = list()
                gc.collect()
                #release lock after making copy
                '''
                try:
                    self.sendChatMessageLock.release()
                except Exception, e:
                    z = e
                    print 'release exception: ' + str(z)
                 '''
                   
                
                sentence = ''
                try:
                    sentence = self.generate_sentence(message) #make new message
                    print 'generated sentence: ' + sentence
                except IndexError, e:
                    a = 1
                if len(sentence.split(' ')) > 2 and sentence.find('@') < 0: #send new message if it meets certain criteria
                    self.cleanString(sentence)
                    #print 'chatter says: ' + sentence
                    command = 'PRIVMSG #otherbrand ' + " :" + sentence + '\r\n'
                    self.commandQueueRef.sendCommandToQueue(command, self.initialWaitTime)
                
        