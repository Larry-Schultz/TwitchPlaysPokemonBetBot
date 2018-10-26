# -*- coding: utf-8 -*-
from IRCManager import findUsername, findText, findDirectedUser, IRCManager, do_nothing
from ThatPokemonResearcher import BulbapediaResearcher
from Strategizers import UserScoreBettingStrategy, Bet, Better
from CommandQueue import CommandQueue,  random_from_set
from MarkovChainChatGenerator import MarkovChainChatter
from CommandLineArgumentParser import CommandLineArguments
from DatabaseManager import DatabaseConnectionFactory
from TrustedUserResearcher import TrustedUserResearcher

import socket #imports module allowing connection to IRC
import signal
import traceback

def quit_handler(signum,frame):
    traceback.print_stack()
signal.signal(signal.SIGINT,quit_handler)

#sets variables for connection to twitch chat
bot_owner = 'OtherBrand'
nick = 'OtherBrand'
channel = "#twitchplayspokemon"
server = 'irc.twitch.tv'
password = ''

print "connecting"
irc = socket.socket()
irc.connect((server, 6667)) #connects to the server
irc.send('PASS ' + password + '\r\n')
irc.send('USER ' + nick + '\r\n')
irc.send('NICK ' + nick + '\r\n')
irc.send('JOIN ' + channel + '\r\n')
print 'connected'

databaseConnectionFactory = DatabaseConnectionFactory(user='postgres', password='Start123', database='twitchplayspokemonbot')

userScoreBettingStrategizer = UserScoreBettingStrategy(dict(), dict(), '')
commandQueueThread = CommandQueue(irc)
markovChainChatter = MarkovChainChatter(commandQueueThread, 'E:\\TwitchIRCBot\\cobe.brain')
ircManager = IRCManager(irc)
betThread = Better(userScoreBettingStrategizer, commandQueueThread)
trustedUserResearcher = TrustedUserResearcher(databaseConnectionFactory)
#trustedUserResearcher.start()

print 'done found'
#irc.send("PRIVMSG #twitchplayspokemon :has joined the channel" +'\r\n')

directionList = ['start', 'select', 'a', 'b', 'down', 'up', 'right', 'left']
while True:
    data = ircManager.ircDataQueue.get(block=True)
    username = findUsername(data)
    text = findText(data)
    directedUser = findDirectedUser(text)

    if data.find('PING') > 0:
        print 'PONG sent'
        ircCommand = 'PONG'
        irc.send(ircCommand)
    elif data.find('tppbankbot@tppbankbot.tmi.twitch.tv') > 0:
        if data.find("@otherbrand") > 0:
            if data.find('outbid') > 0:
                print 'the song/match you attempted to bid on was outbid'
            elif data.find('tokens') > 0 and data.find('you have') > 0:
                print 'tokens found'
                splitString = data.split(':tppbankbot!tppbankbot@tppbankbot.tmi.twitch.tv PRIVMSG #twitchplayspokemon :@otherbrand you have')
                print splitString[1].replace(' tokens', '').replace(' ', '')
            elif data.find('balance') > 0:
                try:
                    print 'balance found'
                    print data
                    value =  data.split('your balance is')
                    if(len(value) > 1):
                        balance = value[1].replace(' ', '').replace('\r\n', '').replace(',', '')
                        balance = int(balance)
                        print 'starting bet thread'
                        betThread.start(balance)
                except Exception, e:
                    print 'balance value exception: ' + str(e)
    elif data.find('tppinfobot@tppinfobot.tmi.twitch.tv') > 0:
        if data.find('new match') > 0:
            print 'new match found'
            print data
            userScoreBettingStrategizer.bettingAllowed = True
            userScoreBettingStrategizer.clearBettingInfo()
            ircCommand = 'PRIVMSG ' + channel + ' :' + '!balance' + '\r\n'
            commandQueueThread.sendCommandToQueue(ircCommand, 35)
        elif data.find('won') > 0 or data.find('draw') > 0:
            print 'match end found'
            print data
            direction = random_from_set(['start', 'select', 'a', 'b', 'down', 'up', 'right'])
            ircCommand = 'PRIVMSG ' + channel + ' :' + direction + '\r\n'
            commandQueueThread.sendCommandToQueue(ircCommand, 50)
            if direction == 'select':
                ircCommand = 'PRIVMSG ' + channel + ' :' + 'deIlluminati Select Sect deIlluminati' + '\r\n' #send a cool message when select comes up
                commandQueueThread.sendCommandToQueue(ircCommand, 33)
            elif direction == 'right':
                ircCommand = 'PRIVMSG ' + channel + ' :' + '┌༼ຈل͜ຈ༽¤=[]:::::> right knights unite' + '\r\n' #send a cool message when select comes up
                commandQueueThread.sendCommandToQueue(ircCommand, 33)
            winningColor = ''
            if data.find('draw') > 0 or data.find('Draw') > 0:
                winningColor = None
                userScoreBettingStrategizer.bettingDone(winningColor)
                userScoreBettingStrategizer.clearBettingInfo()
            elif data.find('Red') > 0 or data.find('red') > 0:
                winningColor = 'red'
                userScoreBettingStrategizer.bettingDone(winningColor)
                trustedUserResearcher.pushNewUntrustedUsers(userScoreBettingStrategizer, winningColor)
                userScoreBettingStrategizer.clearBettingInfo()
            elif data.find('Blue') > 0 or data.find('blue') > 0:
                winningColor = 'blue'
                userScoreBettingStrategizer.bettingDone(winningColor)
                trustedUserResearcher.pushNewUntrustedUsers(userScoreBettingStrategizer, winningColor)
                userScoreBettingStrategizer.clearBettingInfo()
        elif data.find('that Pokemon:') > 0:
            try:
                print 'searching for pokemon'
                splitStr = data.replace('\r\n', '').split('Who\'s that Pokemon: ')
                if len(splitStr) > 0:
                    researcherObj = BulbapediaResearcher(splitStr[1])
                    pokemon = researcherObj.pokemonResult()
                    ircCommand = 'PRIVMSG' + channel + ' :' + pokemon + '\r\n'
                    commandQueueThread.sendCommandToQueue(ircCommand, 35)
            except Exception, e:
                print 'pokemon lookup failed'
                z = e
                print str(z)
        elif data.find('has just begun!') > 0:
            print data
            userScoreBettingStrategizer.bettingAllowed = False
            print 'final tallies'
            print 'blue has: ' + str(userScoreBettingStrategizer.getBlueBetAmount())
            print 'blue has score of: ' + str(userScoreBettingStrategizer.getScore('blue'))
            print 'red has: ' + str(userScoreBettingStrategizer.getRedBetAmount())
            print 'red has score of: ' + str(userScoreBettingStrategizer.getScore('red'))
    elif data.find('otherbrand.tmi.twitch.tv') > 0:
        if data.find('!forcetoken') > 0:
            print data
            print 'force token command found'
            ircCommand = "PRIVMSG " + channel + " :" + "!tokens" + '\r\n'
            commandQueueThread.sendCommandToQueue(ircCommand, 35) 
        elif data.find('!forcebalance') > 0:
            print 'force balance command found'
            print data
            ircCommand = "PRIVMSG " + channel + " :" + "!balance" + '\r\n'
            commandQueueThread.sendCommandToQueue(ircCommand, 35)
        elif data.find('!forcedirection') > 0:
            print 'force direction command found'
            print data
            direction = random_from_set(directionList)
            ircCommand = 'PRIVMSG ' + channel + ' :' + direction + '\r\n'
            commandQueueThread.sendCommandToQueue(ircCommand, 40)
    elif data.find('!bet') > 0:
        if data.find('red') > 0:
            try:
                amountSplitList = data.split('!bet')
                if(len(amountSplitList) > 1): 
                    amountSplitList = amountSplitList[1].split('red')
                    if(len(amountSplitList) > 1): 
                        amount = int(amountSplitList[0].replace(' ', '').replace('\r\n', ''))
                        if username is not None:
                            userScoreBettingStrategizer.addBet(Bet(username, 'red', amount))
                            #print 'red: ' + str(betRedAmount)
            except Exception, e:
                z = e
                print 'value exception found'
                print str(z)
        elif data.find('blue') > 0:
            try:
                amountSplitList = data.split('!bet')
                if(len(amountSplitList) > 1): 
                    amountSplitList = amountSplitList[1].split('blue')
                    if(len(amountSplitList) > 1): 
                        amount = int(amountSplitList[0].replace(' ', '').replace('\r\n', ''))
                        if username is not None:
                            userScoreBettingStrategizer.addBet(Bet(username, 'blue', amount))
                            #print 'blue: ' + str(betBlueAmount)
            except Exception, e:
                z = e
                print 'value exception found'
                print str(z)
    
    #do nothing with move data yet
    elif data.find('!a') > 0 or data.find('!b') > 0 or data.find('!c') > 0 or data.find('!d') > 0 or data.find('!move') > 0:
        leader = userScoreBettingStrategizer.getCurrentSideLeader()
        if leader is not None and data.find(leader) > 0:
            if data.find('!a') > 0 or (data.find('!move') > 0 and data.find('a') > 0):
                print 'leader: ' + leader + ' sent command: ' + '!a'
            elif data.find('!b') > 0 or (data.find('!move') > 0 and data.find('b') > 0):
                print 'leader: ' + leader.getCurrentSideLeader + ' sent command: ' + '!b'
            elif data.find('!c') > 0 or (data.find('!move') > 0 and data.find('c') > 0):
                print 'leader: ' + leader.getCurrentSideLeader + ' sent command: ' + '!c'
            elif data.find('!d') > 0 or (data.find('!move') > 0 and data.find('d') > 0):
                print 'leader: ' + leader.getCurrentSideLeader + ' sent command: ' + '!c'
    elif data.find('!visualize') > 0:
        pass
    elif data.find('!slots') > 0:
        pass
    elif data.find('!tokens') > 0:
        pass
    elif data.find('!balance') > 0:
        pass
    elif data.find('!match') > 0:
        pass
    else:
        storedText = text
        textIsNotDirection = True
        storedText = markovChainChatter.cleanString(storedText)
        for direction in directionList:
            if storedText.lower() == direction:
                textIsNotDirection = False
                break
        if directedUser is not None:
            storedText = storedText.replace('@' + directedUser + ' ', '') #remove directed user strings
        if textIsNotDirection and storedText.find('@') < 0: #don't bother to include replies
            if len(storedText.split(' ')) > (markovChainChatter.chain_length + 1): #if not a blank string
                #print storedText
                markovChainChatter.add_to_brain(storedText)
                #pass

    #print data

print "finished" 