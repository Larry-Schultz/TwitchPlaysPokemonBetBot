# -*- coding: utf-8 -*-
'''
Created on Aug 29, 2015

@author: derp
'''
from lxml import html
import requests
import urllib
import json

bulbapediaURL = 'http://bulbapedia.bulbagarden.net/w/index.php'

class BulbapediaResearcher:
    text = None
    
    def __init__(self, pokemonText):
        self.text = pokemonText
        
    def pokemonResult(self):
        dict = {'title': 'Special:Search', 'search' : self.text }
        queryParameters = urllib.urlencode(dict)
        page = response = requests.get(bulbapediaURL + '?' + queryParameters)
        tree = html.fromstring(page.text)
        results = tree.xpath('//div[@class="mw-search-result-heading"]/a[@title]/text()')
        if(len(results) > 0):
            resultsSplit = results[0].split('(')
            if len(resultsSplit) > 0:
                pokemon = resultsSplit[0].replace(' ', '').replace('(', '')
                print pokemon
                return pokemon 
        else:
            return None
        
class CurrentMatchPokemonResearcher:
    requestUrl = 'https://ws.twitchplaysleaderboard.info:8080/socket.io/'
    
    #get SID for communication with the websocket
    def getSID(self):
        sid = ''
        url = self.requestUrl
        urlParams = {"EIO": "3", "transport": "polling", "t":  "1441685265906-0"}
        r = requests.get(url, params = urlParams, verify=False)

        location = r.text.find("{")
        jsonValue = json.loads(r.text[location:(len(r.text))])
        return jsonValue["sid"]
    
    #perform the request to the websocket with the given SID
    def sendInformationRequest(self, SID):
        url = self.requestUrl
        urlParams = {"EIO": "3", "transport": "polling", "t":  "1441685265906-0", "sid": SID}
        requestStr = '''17:420["get_battle"]'''
        r = requests.post(url, params = urlParams, verify=False, data=requestStr)
        
        return
    
    def lookupPokemon(self):
        SID = self.getSID()
        self.sendInformationRequest(SID)
        
        url = self.requestUrl
        urlParams = {"EIO": "3", "transport": "polling", "t":  "1441685265906-0", "sid": SID}
        
        r = requests.get(url, params = urlParams, verify=False)
        location = r.text.find("[{")
        jsonData = json.loads(r.text[location:(len(r.text))])
        print jsonData
        
        pokemonIds = {"blue": [], "red": []}
        if jsonData[0]["phase"] == "betting":
            for bluePokemonJson in jsonData[0]["data"]["tentative_mons"]["blue"]:
                pokemonIds["blue"].append( {"id": bluePokemonJson["id"], "name": bluePokemonJson["name"]} )
            for redPokemonJson in jsonData[0]["data"]["tentative_mons"]["red"]:
                pokemonIds["red"].append( {"id": redPokemonJson["id"], "name": redPokemonJson["name"] } )
        elif jsonData[0]["phase"] == "battle":
            for bluePokemonJson in jsonData[0]["data"]["teams"]["blue"]["team"]:
                pokemonIds["blue"].append( {"id": bluePokemonJson["id"], "name": bluePokemonJson["name"]} )
            for redPokemonJson in jsonData[0]["data"]["teams"]["red"]["team"]:
                pokemonIds["red"].append( {"id": redPokemonJson["id"], "name": redPokemonJson["name"] } )
        elif jsonData[0]["phase"] == "result":
            for bluePokemonJson in jsonData[0]["data"]["teams"]["blue"]["team"]:
                pokemonIds["blue"].append( {"id": bluePokemonJson["id"], "name": bluePokemonJson["name"]} )
            for redPokemonJson in jsonData[0]["data"]["teams"]["red"]["team"]:
                pokemonIds["red"].append( {"id": redPokemonJson["id"], "name": redPokemonJson["name"] } ) 
        print pokemonIds
        return pokemonIds
        
#matcher = CurrentMatchPokemonResearcher()
#matcher.lookupPokemon()