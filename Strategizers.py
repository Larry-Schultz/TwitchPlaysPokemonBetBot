# -*- coding: utf-8 -*-
'''
Created on Aug 30, 2015

@author: derp
'''
from DatabaseManager import sqliteManager, databaseUpdater
from CommandQueue import random_from_set, wait_randomization_strategy_result
from ThatPokemonResearcher import CurrentMatchPokemonResearcher
from BBP_TPPBR_py.BBP_PBR_20 import MatchMaker

import threading
import time
import math


class Bet:
    user = None
    color = None
    value = 0
    score = 0
    
    def __init__(self, user, color, value):
        self.user = user
        self.color = color
        self.value = value
        
    def __str__(self):
        return 'user: ' + self.user + ' color: ' + self.color + ' value: ' + str(self.value)
    
    def __repr__(self):
        return self.__str__()


class UserScoreBettingStrategy:
    redBets = dict()
    blueBets = dict()
    
    redBetsLock = threading.Lock()
    blueBetsLock = threading.Lock()
    
    dbManager = None
    dbUpdater = None
    
    currentSide = None
    currentSideLock = threading.Lock()
    
    leader = None
    bettingAllowed = True
    
    addarashMode = False
    
    def __init__(self, redBets, blueBets, currentSide):
        self.redBets = redBets
        self.blueBets = blueBets
        self.dbManager = sqliteManager() #manages database
        self.dbUpdater = databaseUpdater(self.dbManager) #manages database updates
        self.currentSide = currentSide
    
    def addBet(self, bet):
        if self.bettingAllowed:
            if bet.value < 3000000: #if value makes sense
                if(bet.color == 'red'):
                    if bet.user not in self.blueBets.keys() : #don't send a user already in the other set
                        self.blueBetsLock.acquire()
                        self.redBets[bet.user] = bet
                        self.blueBetsLock.release()
                    #self.betRedAmount = self.betRedAmount + bet.value
                elif(bet.color == 'blue'):
                    if bet.user not in self.redBets.keys() : #don't send a user already in the other set
                        self.redBetsLock.acquire()
                        self.blueBets[bet.user] = bet
                        self.redBetsLock.release()
                    #self.betBlueAmount = self.betBlueAmount + bet.value
            #print 'added bet: ' + str(bet)
    
    #score should never equal 0
    #get score based on database call
    def getScore(self, color):
        score = 1
        if color == 'red':
            scoreValue = self.dbManager.getScore(self.redBets)
            if scoreValue != 0:
                score = scoreValue
        elif color == 'blue':
            scoreValue = self.dbManager.getScore(self.blueBets)
            if scoreValue != 0:
                score = scoreValue
        return score
    
    def getRecentScore(self, color):
        score = 1
        if color == 'red':
            scoreValue = self.dbManager.getRecentScores(self.redBets)
            if scoreValue != 0:
                score = scoreValue
        elif color == 'blue':
            scoreValue = self.dbManager.getRecentScores(self.blueBets)
            if scoreValue != 0:
                score = scoreValue
        return score
    
    #clear fields and send database updates
    def bettingDone(self, winningColor):
        print 'betting done with winning color = ' + str(winningColor)
        if winningColor is not None:
            if 'addarash1' in [lower_bet.lower() for lower_bet in self.redBets.keys() + self.blueBets.keys()]:
                self.addarashMode = True
            else:
                self.adderashMode = False
            if len(self.redBets) > 0 and len(self.blueBets) > 0:
                self.dbManager.updateWins(self.redBets, self.blueBets, winningColor)
        return
        
    def clearBettingInfo(self):
        self.blueBetsLock.acquire()
        self.blueBets = dict()
        self.blueBetsLock.release()
        
        self.redBetsLock.acquire()
        self.redBets = dict()
        self.redBetsLock.release()
        
        self.currentSide = None
        self.leader = None
        
    def getRedBetAmount(self):
        sumValue = 0
        self.redBetsLock.acquire()
        for key in self.redBets:
            bet = self.redBets[key]
            if bet.value > 0:
                sumValue = sumValue + bet.value
        self.redBetsLock.release()
        return sumValue
    
    def getBlueBetAmount(self):
        sumValue = 0
        self.blueBetsLock.acquire()
        for key in self.blueBets:
            bet = self.blueBets[key]
            if bet.value > 0:
                sumValue = sumValue + bet.value
        self.blueBetsLock.release()
        return sumValue
    
    def getCurrentSideLeader(self):
        if self.currentSide is None:
            return None
        
        if self.leader is None:
            self.leader = self.determineLeader()
        return self.leader
            
    def determineLeader(self):
        if self.currentSide == 'red':
            self.dbManager.getHighestScorerFromDict(self.redBets)
        elif self.currentSide == 'blue':
            self.dbManager.getHighestScorerFromDict(self.blueBets)
        else:
            return None
        
    def checkCurrentSide(self):
        self.currentSideLock.acquire()
        if self.currentSide == 'red':
            self.currentSideLock.release()
            return 'red'
        elif self.currentSide == 'blue':
            self.currentSideLock.release()
            return 'blue'
        else:
            self.currentSideLock.release()
            return None
        
        
class moveStrategizer:
    UserScoreBettingStrategyRef = None
    run = False
    currentColor = ''
    lastSentMoveDict = dict()
    runLock = threading.Lock()
    
    workerThread = None
    
    a_move = '!a'
    b_move = '!b'
    c_move = '!c'
    d_move = '!d'
    
    lastSentCommand = ''
    
    def __init__(self, userScoreBettingStrategy):
        self.UserScoreBettingStrategyRef = userScoreBettingStrategy
        self.workerThread = threading.Thread(target=self.worker)
        self.workerThread.start()
        
    def stopThread(self):
        self.runLock.acquire()
        self.run = False
        self.runLock.release()

    def worker(self):
        while self.checkRun():
            next_move = ''
            time.sleep(30)
            a_movesList = [name for name in self.lastSentMoveDict.keys() if self.lastSentMoveDict[name] == self.a_move]
            b_movesList = [name for name in self.lastSentMoveDict.keys() if self.lastSentMoveDict[name] == self.b_move]
            c_movesList = [name for name in self.lastSentMoveDict.keys() if self.lastSentMoveDict[name] == self.c_move]
            d_movesList = [name for name in self.lastSentMoveDict.keys() if self.lastSentMoveDict[name] == self.d_move]
            
            if self.UserScoreBettingStrategyRef.getCurrentSide() == 'red':
                sumsDict = dict()
                self.UserScoreBettingStrategyRef.redBetsLock.acquire()
                sumsDict[self.a_move] = sum(a_movesList, lambda name : self.UserScoreBettingStrategyRef.redBets[name].value)
                sumsDict[self.b_move] = sum(b_movesList, lambda name : self.UserScoreBettingStrategyRef.redBets[name].value)
                sumsDict[self.c_move] = sum(c_movesList, lambda name : self.UserScoreBettingStrategyRef.redBets[name].value)
                sumsDict[self.d_move] = sum(d_movesList, lambda name : self.UserScoreBettingStrategyRef.redBets[name].value)
                self.UserScoreBettingStrategyRef.redBetsLock.release()
                next_move = max(sumsDict.keys(), lambda sumKey: sumsDict[sumKey])
                
            elif self.UserScoreBettingStrategyRef.getCurrentSide() == 'blue':
                sumsDict = dict()
                self.UserScoreBettingStrategyRef.blueBetsLock.acquire()
                sumsDict[self.a_move] = sum(a_movesList, lambda name : self.UserScoreBettingStrategyRef.blueBets[name].value)
                sumsDict[self.b_move] = sum(b_movesList, lambda name : self.UserScoreBettingStrategyRef.blueBets[name].value)
                sumsDict[self.c_move] = sum(c_movesList, lambda name : self.UserScoreBettingStrategyRef.blueBets[name].value)
                sumsDict[self.d_move] = sum(d_movesList, lambda name : self.UserScoreBettingStrategyRef.blueBets[name].value)
                self.UserScoreBettingStrategyRef.blueBetsLock.release()
                next_move = max(sumsDict.keys(), lambda sumKey: sumsDict[sumKey])
                
            else: #nothing to see here, move on out of here
                return
            
            if next_move != self.lastSentCommand:
                self.lastSentCommand = next_move
                print 'next move should be: ' + next_move
                
            
    def checkRun(self):
        self.runLock.acquire()
        value = self.run
        if value:
            self.runLock.release
            return True
        else:
            self.runLock.release
            return False

class Better:
    weights = {"amount": .15, "score": .35, "recentScore": .35, "random": .05, "matcherWeight": .50}
    
    userScoreBettingStrategizer = None
    userScoreBettngStrategizerLocalThreadCopy = None
    commandQueueThread = None
    channel = "#twitchplayspokemon"
    currentBetThread = None
    
    def __init__(self, userScoreBettingStrategyRef, commandQueueRef):
        self.userScoreBettingStrategizer = userScoreBettingStrategyRef
        self.commandQueueThread = commandQueueRef
        
    def start(self, balance):
        self.userScoreBettingStrategizerLocalThreadCopy = UserScoreBettingStrategy(self.userScoreBettingStrategizer.redBets, self.userScoreBettingStrategizer.blueBets, self.userScoreBettingStrategizer.currentSide)
        self.currentBetThread = threading.Thread(target=self.wait_to_send_bet, args=(balance,self.userScoreBettingStrategizer.addarashMode))
        self.currentBetThread.start()
    
    def bet_strategy_result(self, balance, color):
        if balance > 10000:
            if color == 'red':
                maxRedBetKeyValue = max(self.userScoreBettingStrategizerLocalThreadCopy.redBets.keys(), key = lambda betKey: int(self.userScoreBettingStrategizerLocalThreadCopy.redBets[betKey].value))
                maxRedBetValue = int(self.userScoreBettingStrategizerLocalThreadCopy.redBets[maxRedBetKeyValue].value)
                return min([int(math.floor((balance-500) / 3)) + int(500), maxRedBetValue])
            elif color == 'blue':
                maxBlueBetKeyValue = max(self.userScoreBettingStrategizerLocalThreadCopy.blueBets.keys(), key = lambda betKey: int(self.userScoreBettingStrategizerLocalThreadCopy.blueBets[betKey].value))
                maxBlueBetValue = int(self.userScoreBettingStrategizerLocalThreadCopy.blueBets[maxBlueBetKeyValue].value)
                return min([int(math.floor((balance-500) / 3)) + int(500), maxBlueBetValue])
            else:
                print 'no color found :/'
                maxBlueBetKeyValue = max(self.userScoreBettingStrategizerLocalThreadCopy.blueBets.keys(), key = lambda betKey: int(self.userScoreBettingStrategizerLocalThreadCopy.blueBets[betKey].value))
                maxBlueBetValue = int(self.userScoreBettingStrategizerLocalThreadCopy.blueBets[maxBlueBetKeyValue].value)
                return min([int(math.floor((balance-500) / 3)) + int(500), maxBlueBetValue])
        elif(balance > 500 and balance < 10000):
            return int(math.floor((balance-500) / 3)) + int(500)
        else:
            return balance
    
    def bet_color_strategy_higher_bet(self):
        print 'determining bet now'
        #gets its own sql connection 
        
        betRedAmount = self.userScoreBettingStrategizerLocalThreadCopy.getRedBetAmount()
        betBlueAmount = self.userScoreBettingStrategizerLocalThreadCopy.getBlueBetAmount()
        
        print 'blue has: ' + str(betBlueAmount)
        print 'red has: ' + str(betRedAmount)
        #trying an inverse strategy, where I go for the group with the fewest tokens.
        # I think that someone is intentionally gaming the bet counts with false positives.
        color = None
        if(betRedAmount >= betBlueAmount):
            color = 'red'
        elif(betBlueAmount > betRedAmount):
            color = 'blue'
        else:
            color = 'blue'
            print 'no deciding color found'
        return color
    
    def bet_color_strategy_trusted_users(self):
        print 'determing bet now '
        #gets its own sql connection
        
        redScore = self.userScoreBettingStrategizerLocalThreadCopy.getScore('red')
        recentRedScore = self.userScoreBettingStrategizerLocalThreadCopy.getRecentScore('red')
        betRedAmount = self.userScoreBettingStrategizerLocalThreadCopy.getRedBetAmount()
        blueScore = self.userScoreBettingStrategizerLocalThreadCopy.getScore('blue')
        recentBlueScore = self.userScoreBettingStrategizerLocalThreadCopy.getRecentScore('blue')
        betBlueAmount = self.userScoreBettingStrategizerLocalThreadCopy.getBlueBetAmount()
        
        print 'blue has: ' + str(betBlueAmount)
        print 'blue has score of: ' + str(blueScore)
        print 'blue has recent score of: ' + str(recentBlueScore)
        print 'red has: ' + str(betRedAmount)
        print 'red has score of: ' + str(redScore)
        print 'red has recent score of: ' + str(recentRedScore)
        
        color = None
        if redScore >= blueScore:
            color = 'red'
        elif blueScore > redScore:
            color = 'blue'
        else:
            color = 'blue'
            print 'no deciding color found'
            
        return color
    
    def messagePokemonNameForMatchMakerCall(self, pokemonName):
        if pokemonName == 'Mr. Mime':
            return 'MrMime'
        elif pokemonName == 'Mime Jr.':
            return 'MimeJr'
        elif pokemonName == "Farfetch'd":
            return 'Farfetchd'
        elif pokemonName == 'Ho-Oh':
            return 'HoOh'
        elif pokemonName == 'Porygon-Z':
            return 'PorygonZ'
        elif pokemonName == 'Nidoran-F':
            return 'NidoranF'
        elif pokemonName == 'Nidoran-M' or pokemonName == 'Nidoran\xe2\x99\x80':
            return 'NidoranM'
        elif pokemonName.find('Nidoran') > 0 or pokemonName.find('Nidaran') > 0:
            return 'Nidorina'
        else:
            return pokemonName

    def bet_color_strategy_multi_attribute(self, pokemonDict):
        print 'determing bet now '
        
        redScore = self.userScoreBettingStrategizerLocalThreadCopy.getScore('red')
        recentRedScore = self.userScoreBettingStrategizerLocalThreadCopy.getRecentScore('red')
        betRedAmount = self.userScoreBettingStrategizerLocalThreadCopy.getRedBetAmount()
        blueScore = self.userScoreBettingStrategizerLocalThreadCopy.getScore('blue')
        recentBlueScore = self.userScoreBettingStrategizerLocalThreadCopy.getRecentScore('blue')
        betBlueAmount = self.userScoreBettingStrategizerLocalThreadCopy.getBlueBetAmount()
        
        print 'blue has: ' + str(betBlueAmount)
        print 'blue has score of: ' + str(blueScore)
        print 'blue has recent score of: ' + str(recentBlueScore)
        print 'red has: ' + str(betRedAmount)
        print 'red has score of: ' + str(redScore)
        print 'red has recent score of: ' + str(recentRedScore)
        
        totalAmount = betRedAmount + betBlueAmount
        totalScore = redScore + blueScore
        totalRecentScore = recentBlueScore + recentRedScore
        
        pokemonResults = None
        pokemonNames = []
        if pokemonDict is not None and len(pokemonDict["red"]) == 3 and len(pokemonDict["blue"]) == 3:
            for pokemonInfoDict in pokemonDict["blue"]:
                pokemonNames.append(self.messagePokemonNameForMatchMakerCall(pokemonInfoDict["name"]))
            for pokemonInfoDict in pokemonDict["red"]:
                pokemonNames.append(self.messagePokemonNameForMatchMakerCall(pokemonInfoDict["name"]))

            pokemonMatcher = MatchMaker()
            pokemonResults = pokemonMatcher.Predictor(pokemonNames)
            print 'red has a: ' + str(((pokemonResults["redScore"] + 1)/(pokemonResults["redScore"] + pokemonResults["blueScore"] + 1))) + '% chance of victory'
            print 'blue has a ' + str((pokemonResults["blueScore"] + 1)/(pokemonResults["redScore"] + pokemonResults["blueScore"] + 1)) + '% chance of victory'
        
        redHueristic = float(((betRedAmount+1)/(totalAmount+1)) * self.weights["amount"] + ((redScore+1)/(totalScore+1))* self.weights["score"] +((recentRedScore+1)/(totalRecentScore+1))*self.weights["recentScore"] + random_from_set([0,1])*self.weights["random"])
        if pokemonDict is not None and len(pokemonDict["red"]) == 3 and len(pokemonDict["blue"]) == 3:
            redHueristic = float(redHueristic + (((pokemonResults["redScore"] + 1)/(pokemonResults["redScore"] + pokemonResults["blueScore"] + 1)) * self.weights["matcherWeight"]))
        blueHueristic = float(((betBlueAmount+1)/(totalAmount+1)) * self.weights["amount"] + ((blueScore+1)/(totalScore+1))* self.weights["score"] +((recentBlueScore+1)/(totalRecentScore+1))*self.weights["recentScore"] + random_from_set([0,1])*self.weights["random"])
        if pokemonDict is not None and len(pokemonDict["red"]) == 3 and len(pokemonDict["blue"]) == 3:
            blueHueristic = float(blueHueristic + (((pokemonResults["blueScore"] + 1)/(pokemonResults["redScore"] + pokemonResults["blueScore"] + 1)) * self.weights["matcherWeight"]))
        color = None
        
        print 'red hueristic is: ' + str.format('{0:.15f}',redHueristic)
        print 'blue hueristic is: ' + str.format('{0:.15f}',blueHueristic)
        
        if redHueristic >= blueHueristic:
            color = 'red'
        elif blueHueristic > redHueristic:
            color = 'blue'
        else: #red has a usually higher chance of victory.  When in doubt red it out
            color = 'red'
            print 'no deciding color found'
            
        return (color, redHueristic, blueHueristic)
    
    def calculateWeightedBetAmount(self, winningHueristic, losingHueristic, betAmount):
        #formula is p(winning, losing) = slope * (winning - losing)
        slope = float(10) #this slope assumes max difference is .10
        value = float(betAmount - 500) * min(float(1), slope*(winningHueristic-losingHueristic)) + 500 #bound multiplier by 1
        return int(value)
    
    def wait_to_send_bet(self, balance, addarashMode=False):
        print 'bet thread started with balance: ' + str(balance)
        time.sleep(170)
        
        #you can wait longer with lower balances, due to betting amount thresholds that change over time
        if balance < 10000:
            time.sleep(10)
        if balance < 1000:
            time.sleep(20)
        
        #get Pokemon data
        pokemonDict = None
        try:
            pokemonRetriever = CurrentMatchPokemonResearcher()
            pokemonDict = pokemonRetriever.lookupPokemon()
            print 'pokemonIds: ' + str(pokemonDict)
            
        except Exception, e:
            print 'No pokemon data found'
        
        
        color, redHueristic, blueHueristic = self.bet_color_strategy_multi_attribute(pokemonDict)
        betAmount = self.bet_strategy_result(balance, color)
        
        print 'original bet amount: ' + str(betAmount)
        
        #take a percentage of the bet amount based on the relative hueristic values of the colors
        if color == 'red':
            betAmount = self.calculateWeightedBetAmount(redHueristic, blueHueristic, betAmount)
        else:
            betAmount = self.calculateWeightedBetAmount(blueHueristic, redHueristic, betAmount)
            
        '''
        if addarashMode:
            #if addarash is in play, then reverse logic
            if color == 'red':
                color = 'blue'
            elif color == 'blue':
                color = 'red'
            #if Addarash is in play, limit the bet amount to 999 so that more time can be waited to see where he bets
            betAmount = min(999, betAmount)
            print 'Addarash mode engaged'
        '''
        
        print 'weighted bet amount: ' + str(betAmount)
        
        self.userScoreBettingStrategizer.currentSide = color
        
        command = '!bet' + ' ' + str(betAmount) + ' ' + color
        command = command.replace('\n', '').replace('\r', '')
        ircCommand = 'PRIVMSG ' + self.channel + ' :' + command + '\r\n'
        self.commandQueueThread.sendCommandToQueue(ircCommand, 5)
        self.userScoreBettingStrategizerLocalThreadCopy.dbManager.close()
