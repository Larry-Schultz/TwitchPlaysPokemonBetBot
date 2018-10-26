# -*- coding: utf-8 -*-
'''
Created on Aug 30, 2015

@author: derp
'''
import Queue
import threading
#import sqlite3
import pg8000

class databaseUpdateRequest:
    winningColor = ''
    blueBetList = []
    redBetList = []
    
    def __init__(self, winningColor, blueBetList, redBetList):
        self.winningColor = winningColor
        self.blueBetList = blueBetList
        self.redBetList = redBetList
        
class databaseUpdater:
    dbRef = None
    updatedThread = None
    databaseUpdateQueue = Queue.Queue()
    
    def updater(self):
        while True:
            databaseUpdate = self.databaseUpdateQueue.get(block=True)
            self.dbRef.updateWins(databaseUpdate.redBetList, databaseUpdate.blueBetList, databaseUpdate.winningColor)
    
    def __init__(self, dbRef):
        self.dbRef = dbRef
        self.updatedThread = threading.Thread(target=self.updater)
        self.updatedThread.start()
        
    def addToQueue(self, dbUpdateRequst):
        self.databaseUpdateQueue.put(dbUpdateRequst)
        
class user:
    name = None
    wins = 0
    losses = 0

scoreQueryTemplate = '''SELECT name, (users.wins + 1) /  (users.losses + 1) AS score
                FROM users
                WHERE users.name IN (?)'''
    
userExistenceQuery = '''SELECT name
                        FROM users
                        WHERE name IN ( ? )''' 
                        
userIdsQuery = '''SELECT user_id, name
             FROM users
             WHERE users.name IN(?)'''
             
recentMatchesScoreQuery = '''
SELECT users.name, SUM(win_history.win) AS recent_wins, SUM(win_history.loss) AS recent_losses, 
    (SUM(win_history.win) + 1)/(SUM(win_history.loss) + 1) AS score
FROM win_history LEFT JOIN users
    ON win_history.user_id = users.user_id
WHERE win_history.win_timestamp > (win_history.win_timestamp - INTERVAL '8 hours')
    AND users.name IN (?)
GROUP BY users.name
ORDER BY recent_wins DESC;
'''

class DatabaseConnectionFactory:
    user = ''
    password = ''
    database = ''
    currentModule = pg8000
    
    
    def __init__(self, user, password, database):
        self.user = user
        self.password = password
        self.database = database
    
    def createSqliteManager(self):
        return sqliteManager(user=self.user, password=self.password, database=self.database)
    
    def createDatabaseConnection(self):
        return self.currentModule.connect(user=self.user, password=self.password, database=self.database)

class sqliteManager:
    conn = None
    def __init__(self, user='postgres', password='Start123', database='twitchplayspokemonbot'):
        self.conn = pg8000.connect(user=user, password=password, database=database)
        
    def __del__(self):
        self.conn.close()
        
    def getScore(self, betDict):
        betList = betDict.values()
        if len(betList) == 0:
            return 0
        inOperatorTupleString = self.generateInStatementFromBetList(betList)
        
        curr = self.conn.cursor()
        scoreQuery = scoreQueryTemplate.replace('?', inOperatorTupleString)
        #print 'sending query of: ' + scoreQuery
        curr.execute(scoreQuery);
        
        score = 0
        scoreTuples = curr.fetchall()
        for scoreTuple in scoreTuples:
            name = str(scoreTuple[0])
            scoreRatio = int(scoreTuple[1])
            totalScore = int(betDict[name].value) * scoreRatio
            score = score + totalScore
        
        #print 'sql result is: ' + str(scoreTuples)
        #print 'score is: ' + str(score)
        return score
    
    def getRecentScores(self, betDict):
        betList = betDict.values()
        if len(betList) == 0:
            return 0
        inOperatorTupleString = self.generateInStatementFromBetList(betList)
        
        curr = self.conn.cursor()
        scoreQuery = recentMatchesScoreQuery.replace('?', inOperatorTupleString)
        #print 'sending query of: ' + scoreQuery
        curr.execute(scoreQuery);
        
        score = 0
        scoreTuples = curr.fetchall()
        for scoreTuple in scoreTuples:
            name = str(scoreTuple[0])
            scoreRatio = int(scoreTuple[3])
            totalScore = int(betDict[name].value) * scoreRatio
            score = score + totalScore
        return score
    
    def getHighestScorerFromDict(self, betDict):
        betList = betDict.values()
        inOperatorTupleString = self.generateInStatementFromBetList(betList)
        
        curr = self.conn.cursor()
        scoreQuery = scoreQueryTemplate.replace('?', inOperatorTupleString)
        curr.execute(scoreQuery);
        
        scoreTuples = curr.fetchall()
        sorted(scoreTuples, key = lambda tupleValue: betDict[str(tupleValue[0])].value * int(tupleValue[1]))
        leader = str(scoreTuples[0][0])
        #print 'leader is: ' + leader
        return leader
    
    def updateWins(self, redBetDict, blueBetDict, winningColor):
        redBetList = redBetDict.values()
        blueBetList = blueBetDict.values()
        
        curr = self.conn.cursor()
        
        aggregattedList = redBetList + blueBetList
        inStatement = self.generateInStatementFromBetList(aggregattedList)
        userQuery = userExistenceQuery.replace('?', inStatement)
        print 'query for user existence is: ' + userQuery
        curr.execute(userQuery)
        namesAlreadyInDatabase = []
        for name in curr.fetchall():
            namesAlreadyInDatabase.append(str(name[0])) #convert list of string tuples with size 1 to strings 
        
        print namesAlreadyInDatabase
        
        betsToUpdateWin = [bet for bet in aggregattedList if bet.color == winningColor and bet.user in namesAlreadyInDatabase]
        betsToUpdateLoss = [bet for bet in aggregattedList if bet.color != winningColor and bet.user in namesAlreadyInDatabase]
        betsToInsertWin = [bet for bet in aggregattedList if bet.color == winningColor and bet.user not in namesAlreadyInDatabase]
        betsToInsertLoss = [bet for bet in aggregattedList if bet.color != winningColor and bet.user not in namesAlreadyInDatabase]
        
        if len(betsToUpdateWin) > 0:
            updateStatement = self.generateBulkUpdateWinStatement(betsToUpdateWin)
            print 'update win Statement is: ' + updateStatement
            curr.execute(updateStatement)
        if len(betsToUpdateLoss) > 0:
            updateStatement = self.generateBulkUpdateLossStatement(betsToUpdateLoss)
            print 'update loss Statement is: ' + updateStatement
            curr.execute(updateStatement)
        
        if len(betsToInsertWin + betsToInsertLoss) > 0:
            bulkInsertStatement = self.generateBulkInsertStatement(betsToInsertWin, betsToInsertLoss)
            print 'insert statement is: ' + bulkInsertStatement
            curr.execute(bulkInsertStatement)
        
        print 'recoring match histories'
        curr.execute(userIdsQuery.replace('?', self.generateInStatementFromBetList(betsToUpdateWin + betsToInsertWin)))
        winnerTuples = curr.fetchall()
        curr.execute(userIdsQuery.replace('?', self.generateInStatementFromBetList(betsToUpdateLoss + betsToInsertLoss)))
        loserTuples = curr.fetchall()
        curr.execute(self.generateBulkWinHistoryInsertStatement(winnerTuples, loserTuples))
        
        self.conn.commit()
        
        print 'done updating wins'
        return
    
    
    def generateBulkInsertStatement(self, winners, losers):
        query = ' INSERT INTO users (name, wins, losses) VALUES'
        values = []
        for i in range(0, len(winners)):
            bet = winners[i]
            queryValue = ' (' + '\'' + bet.user + '\'' + ' , ' + str(1) + ' , ' + str(0) + ' ) '
            values.append(queryValue)
        for i in range(0, len(losers)):
            bet = losers[i]
            queryValue = ' (' + '\'' + bet.user + '\'' + ' , ' + str(0) + ' , ' + str(1) + ' ) '
            values.append(queryValue)
        for i in range(0, len(values)):   
            query = query + values[i]
            if i != len(values) -1:
                query = query + ', '
        return query
    
    def generateBulkWinHistoryInsertStatement(self, winnerTuples, loserTuples):
        query = 'INSERT INTO win_history (user_id, win_timestamp, win, loss) VALUES '
        values = []
        for winnerTuple in winnerTuples:
            user_id = winnerTuple[0]
            name = winnerTuple[1]
            queryValue = ' ( ' + str(user_id) + ', ' + 'current_timestamp'  + ' , ' + str(1) + ' , ' + str(0) + ' ) '
            values.append(queryValue)
        for loserTuple in loserTuples:
            user_id = loserTuple[0]
            name = loserTuple[1]
            queryValue = ' ( ' + str(user_id) + ', ' + 'current_timestamp'  + ' , ' + str(0) + ' , ' + str(1) + ' ) '
            values.append(queryValue)
        for i in range(0, len(values)):   
            query = query + values[i]
            if i != len(values) -1:
                query = query + ', '
        return query
    
    def generateBulkUpdateWinStatement(self, winners):
        query = ' UPDATE users '
        if len(winners) > 0:
            query = query + ' SET wins = CASE name '
            for bet in winners:
                query = query + 'WHEN ' + '\'' + bet.user + '\'' + ' THEN ' + ' wins + 1 '
            query = query + ' END '
        query = query + ' WHERE name IN '
        updateInStatement = self.generateInStatementFromBetList(winners)  
        query = query + '( ' + updateInStatement + ' )'
        return query
    
    def generateBulkUpdateLossStatement(self, losers):
        query = ' UPDATE users '
        if len(losers) > 0:
            query = query +' SET losses = CASE name '
            for bet in losers:
                query = query + ' WHEN ' + '\'' + bet.user + '\'' + ' THEN ' + ' losses + 1 '
            query = query + ' END '
        query = query + ' WHERE name IN '
        updateInStatement = self.generateInStatementFromBetList(losers)
        query = query + '( ' + updateInStatement + ' )'
        return query
    '''
    def generateBulkInsertStatement(self, winners, losers):
        query = 'INSERT INTO users '
        for i in range(0, len(winners)):
            bet = winners[i]
            if i == 0:
                query = query + ' SELECT ' + '\'' + bet.user + '\' AS name, ' + str(1) + ' AS wins, ' + str(0) + ' AS losses '
            else:
                query = query + ' UNION SELECT ' + '\'' +  bet.user + '\', ' + str(1) + ', ' + str(0) + ' '
        for bet in losers:
            query = query + ' UNION SELECT ' + '\'' + bet.user + '\', ' + str(0) + ', ' + str(1) + ' '
        return query
    '''
    def generateInStatementFromBetList(self, betList):
        inOperatorTupleString = ''
        for i in range(0, len(betList)):
            bet = betList[i]
            inOperatorTupleString = inOperatorTupleString + '\'' + bet.user
            if i != len(betList) - 1:
                inOperatorTupleString = inOperatorTupleString + '\', '
            else:
                inOperatorTupleString = inOperatorTupleString + '\''
        #print inOperatorTupleString
        return inOperatorTupleString
     
    def close(self):
        self.conn.close()