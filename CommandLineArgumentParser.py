# -*- coding: utf-8 -*-
'''
Created on Sep 1, 2015

@author: derp
'''

import argparse

class CommandLineArguments:
    bot_owner = 'OtherBrand'
    ircNick = 'OtherBrand'
    ircChannel = "#twitchplayspokemon"
    ircServer = 'irc.twitch.tv'
    ircPort = 6667
    password = ''
    databaseUser='postgres'
    databasePassword='Start123'
    databaseDBName='twitchplayspokemonbot'
    
    
def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ircNick', help='irc nickname')
    parser.add_argument('ircChannel', help='irc channel to connect to')
    parser.add_argument('ircServer', help='irc server to connect to')
    parser.add_argument('ircPort', help='irc port to connect to')
    parser.add_argument('databasePassword', help = 'password for database')
    args = parser.parse_args()