# -*- coding: utf-8 -*-
'''
Created on Sep 1, 2015

@author: derp
'''
from CommandQueue import wait_randomization_strategy_result

from Queue import Queue, Empty
from threading import Thread, Lock
import time
import json
import requests
import pg8000

conn = pg8000.connect(user='postgres', password='Start123', database='twitchplayspokemonbot')

class user:
    name = ''
    wins = 0
    losses = 0
    
    def __init__(self, name, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses
        
    def __repr__(self):
        return 'name: ' + self.name + ' wins: ' + str(self.wins) + ' losses: ' + str(self.losses)

untrustedQuery = '''
    SELECT name
    FROM users
    WHERE trusted = FALSE
    ORDER BY wins DESC;'''
   
untrustedQueryInOperation = '''
    SELECT name
    FROM users
    WHERE trusted = FALSE AND name IN (?)
    ORDER BY wins DESC;'''

class TrustedUserResearcher:
    sleepTimeBetweenUsers = 120
    
    connFactory = None
    threadConn = None
    researcherThread = None
    researcherQueue = Queue()
    
    continueBool = True
    continueBoolLock = Lock()
    
    def __init__(self, dbConnFactory):
        self.connFactory = dbConnFactory
        self.threadConn = dbConnFactory.createDatabaseConnection()
        for name in self.pullCurrentUntrustedUsers():
            self.researcherQueue.put(name)
            
    def start(self):
        self.researcherThread = Thread(target=self.research)
        self.researcherThread.start()
    
    def pullCurrentUntrustedUsers(self):
        conn = self.connFactory.createDatabaseConnection()
        curr = conn.cursor()
        curr.execute(untrustedQuery)
        nameTuples = curr.fetchall()
        names = []
        for nameTuple in nameTuples:
            names.append(nameTuple[0])
        print 'starting untrusted users loading queue with ' + str(len(names)) + ' users'
        conn.close()
        return names
    
    def pushNewUntrustedUsers(self, strategizer, winningColor):
        redBetDict = strategizer.redBets
        blueBetDict = strategizer.blueBets
        connManager = self.connFactory.createSqliteManager()
        conn = connManager.conn
        curr = conn.cursor()
        redBetList = redBetDict.values()
        blueBetList = blueBetDict.values()
        aggregattedList = redBetList + blueBetList
        inStatement = connManager.generateInStatementFromBetList(aggregattedList)
        if len(aggregattedList) == 0:
            return
        userQuery = untrustedQueryInOperation.replace('?', inStatement)
        print userQuery
        curr.execute(userQuery)
        namesAlreadyInDatabase = []
        for name in curr.fetchall():
            namesAlreadyInDatabase.append(str(name[0])) #convert list of string tuples with size 1 to strings
        for name in namesAlreadyInDatabase:
            self.researcherQueue.put(name)
        print 'loaded ' + str(len(namesAlreadyInDatabase)) + ' new users into the untrusted users queue'
        return
    
    def checkContinue(self):
        self.continueBoolLock.acquire()
        if self.continueBool:
            self.continueBoolLock.release()
            return True
        else:
            self.continueBoolLock.release()
            return False
        
    def stopThread(self):
        self.continueBoolLock.acquire()
        self.continueBool = False
        self.continueBoolLock.release()
        self.threadConn.close()
    
    def research(self):
        while self.checkContinue():
            try:
                time.sleep(wait_randomization_strategy_result(self.sleepTimeBetweenUsers))
                name = None
                name = self.researcherQueue.get(block=True, timeout=self.sleepTimeBetweenUsers)
                if name is not None:
                    self.pollLeaderboard(name)
            except Empty:
                pass
            
    def pollLeaderboard(self, username):
        print 'updating: ' + username
        url = 'http://twitchplaysleaderboard.info/search/?user=' + username
        header = {'X-Requested-With': 'XMLHttpRequest'}
        print url
        
        try:
            curr = self.threadConn.cursor()
            userData = str(requests.get(url, headers=header).text)
            userJson = json.loads(userData)
            userObj = user(username, userJson["summary"]["win"], userJson["summary"]["lose"])
            
            updateQuery = 'UPDATE users SET trusted = TRUE, wins = wins +' + str(userObj.wins) + ', losses = losses +' + str(userObj.losses) + ' where name = ' + '\'' + username + '\''
            print 'sending update: ' + updateQuery
            curr.execute(updateQuery)
            self.threadConn.commit()
            print 'updated: ' + username
        except Exception, e:
            print 'exception happened with reason: ' + str(e)
        
        return


def main():
    while True:
        curr = conn.cursor()
        curr.execute(untrustedQuery)
        nameTuples = curr.fetchall()
        names = []
        for nameTuple in nameTuples:
            names.append(nameTuple[0])
        
        print 'updating: ' + str(names)
        
        #escape if there are no users, probably because I stopped running the Bot
        if len(names) == 0:
            return
        
        for username in names:
            time.sleep(120)
            print 'updating: ' + username
            url = 'http://twitchplaysleaderboard.info/search/?user=' + username
            header = {'X-Requested-With': 'XMLHttpRequest'}
            print url
            
            try:
                userData = str(requests.get(url, headers=header).text)
                userJson = json.loads(userData)
                userObj = user(username, userJson["summary"]["win"], userJson["summary"]["lose"])
                
                updateQuery = 'UPDATE users SET trusted = TRUE, wins = wins +' + str(userObj.wins) + ', losses = losses +' + str(userObj.losses) + ' where name = ' + '\'' + username + '\''
                print 'sending update: ' + updateQuery
                curr.execute(updateQuery)
                conn.commit()
                print 'updated: ' + username
            except Exception, e:
                print 'exception happened with reason: ' + str(e)
            
        print 'done'
    
if __name__ == '__main__':
    main()