
from __future__ import division
import random
import json
import logging
import os

log = logging.getLogger("pbrmm")

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
LOSSES_FILE_PATH = os.path.join(SCRIPT_DIR, "Losses PBRMM.txt")
WINS_FILE_PATH = os.path.join(SCRIPT_DIR, "Wins PBRMM.txt")
MOVES_FILE_PATH = os.path.join(SCRIPT_DIR, "Moves PBR.txt")
GAMES_PLAYED_FILE_PATH = os.path.join(SCRIPT_DIR, "Games Played.txt")
# JSON_FILE_PATH = os.path.join(SCRIPT_DIR, "../pokemon.json")
JSON_FILE_PATH = os.path.join(SCRIPT_DIR, "json.json")

dmg = [0, 0, 0, 0, 0]
move = ['', '', '', '', '']
text = ['', '', '', 0, '']
temphpr = 1
temphpb = 1

class MatchMaker(object):
    def __init__(self):
        self.log = log

        self._Types = {"normal":  0, "fire":  1, "water":  2, "electric":  3, "grass":  4,
                       "ice":  5, "fighting":  6, "poison":  7, "ground":  8, "flying":  9,
                       "psychic": 10, "bug": 11, "rock": 12, "ghost": 13, "dragon": 14,
                       "dark": 15, "steel": 16, "u": 17}

        self._tableTypeEffs = [                            # Fe1k's Design
                        #                                     Defenders
                        # NOR  FIR  WAT  ELE  GRA  ICE  FIG  POI  GRO  FLY  PSY  BUG  ROC  GHO  DRA  DAR  STE
                        [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 0.5,   0,   1,   1, 0.5],  # NOR
                        [1, 0.5, 0.5,   1,   2,   2,   1,   1,   1,   1,   1,   2, 0.5,   1, 0.5,   1,   2],  # FIR
                        [1,   2, 0.5,   1, 0.5,   1,   1,   1,   2,   1,   1,   1,   2,   1, 0.5,   1,   1],  # WAT
                        [1,   1,   2, 0.5, 0.5,   1,   1,   1,   0,   2,   1,   1,   1,   1, 0.5,   1,   1],  # ELE
                        [1, 0.5,   2,   1, 0.5,   1,   1, 0.5,   2, 0.5,   1, 0.5,   2,   1, 0.5,   1, 0.5],  # GRA
                        [1, 0.5, 0.5,   1,   2, 0.5,   1,   1,   2,   2,   1,   1,   1,   1,   2,   1, 0.5],  # ICE
                        [2,   1,   1,   1,   1,   2,   1, 0.5,   1, 0.5, 0.5, 0.5,   2,   0,   1,   2,   2],  # FIG
                        [1,   1,   1,   1,   2,   1,   1, 0.5, 0.5,   1,   1,   1, 0.5, 0.5,   1,   1,   0],  # POI
                        [1,   2,   1,   2, 0.5,   1,   1,   2,   1,   0,   1, 0.5,   2,   1,   1,   1,   2],  # GRO   Attackers
                        [1,   1,   1, 0.5,   2,   1,   2,   1,   1,   1,   1,   2, 0.5,   1,   1,   1, 0.5],  # FLY
                        [1,   1,   1,   1,   1,   1,   2,   2,   1,   1, 0.5,   1,   1,   1,   1,   0, 0.5],  # PSY
                        [1, 0.5,   1,   1,   2,   1, 0.5, 0.5,   1, 0.5,   2,   1,   1, 0.5,   1,   2, 0.5],  # BUG
                        [1,   2,   1,   1,   1,   2, 0.5,   1, 0.5,   2,   1,   2,   1,   1,   1,   1, 0.5],  # ROC
                        [0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,   2,   1, 0.5, 0.5],  # GHO
                        [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1, 0.5],  # DRA
                        [1,   1,   1,   1,   1,   1, 0.5,   1,   1,   1,   2,   1,   1,   2,   1, 0.5, 0.5],  # DAR
                        [1, 0.5, 0.5, 0.5,   1,   2,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1, 0.5],  # STE
                        [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1],  # U
                        ]

        self.jsonlist = json.loads(open(JSON_FILE_PATH).read(), encoding="utf-8")
        self._stats = []
        for i in range(0, 540):
            temptext = (str(self.jsonlist[i]['dexNumber'])+'_'+self.jsonlist[i]['ability']+'_')
            for i2 in range(0, 4):
                if i2 <= len(self.jsonlist[i]['moves'])-1:
                    temptext = temptext+self.jsonlist[i]['moves'][i2]['name']+'_'
                else:
                    temptext = temptext+'_'
            temptext = (temptext+str(self.jsonlist[i]['stats']['hp'])+'_'+str(self.jsonlist[i]['stats']['atk'])+'_'+str(self.jsonlist[i]['stats']['def'])+'_'+str(self.jsonlist[i]['stats']['spa'])+'_'+str(self.jsonlist[i]['stats']['spd'])+'_'+str(self.jsonlist[i]['stats']['spe'])+'_'+self.jsonlist[i]['name']+'_')
            temptext = temptext+self.jsonlist[i]['types'][0]+'_'
            if len(self.jsonlist[i]['types']) > 1:
                temptext = temptext+self.jsonlist[i]['types'][1]+'_'
            else:
                temptext = temptext+'_'
            temptext = temptext.lower()
            temptext = temptext.replace(' ', '')
            temptext = temptext.replace('.', '')
            temptext = temptext.replace('.', '')
            temptext = temptext.replace('-', '')
            temptext = temptext.replace("'", "")
            temptext = temptext.encode('ascii', 'ignore')
            self._stats.append(temptext)

        with open(MOVES_FILE_PATH, 'r') as tempX:
            self._moves = tempX.read().split('//')

    def getEff(self, type1name, type2name, defenderability):
        if (type2name == '') or (type1name == 'u') or (type1name == 'default') or (type1name == ''):
            return(1)

        type1 = self._Types[type1name]
        type2 = self._Types[type2name]
        tempx = self._tableTypeEffs[type1][type2]
        if defenderability.lower() == 'wonderguard':
            for i2 in range(0, 18):
                if tempx < 2:
                    tempx = 0
        if (defenderability.lower() == 'waterabsorb') and (type1name == 'water'):
            tempx = 0
        if (defenderability.lower() == 'voltabsorb') and (type1name == 'electric'):
            tempx = 0
        if (defenderability.lower() == 'levitate') and (type1name == 'ground'):
            tempx = 0
        if (defenderability.lower() == 'motordrive') and (type1name == 'electric'):
            tempx = 0
        if (defenderability.lower() == 'flashfire') and (type1name == 'fire'):
            tempx = 0
        if (defenderability.lower() == 'dryskin') and (type1name == 'water'):
            tempx = 0
        if (defenderability.lower() == 'dryskin') and (type1name == 'fire'):
            tempx = tempx * 1.25
        if (defenderability.lower() == 'thickfat') and (type1name == 'ice'):
            tempx = tempx * 0.5
        if (defenderability.lower() == 'thickfat') and (type1name == 'fire'):
            tempx = tempx * 0.5
        if (defenderability.lower() == 'heatproof') and (type1name == 'fire'):
            tempx = tempx * 0.5
        if (defenderability.lower() == 'filter') and (tempx > 1):
            tempx = tempx*0.75
        if (defenderability.lower() == 'solidrock') and (tempx > 1):
            tempx = tempx*0.75
        return tempx

    def DamageDealt(self, Attacker, Defender, moveset2, position2, StoredMoves, bathp, batatk, batdef, batsatk, batsdef, dmg, enemyhp):
        tempdamage = self._stats[position2[Attacker]].split('_')
        tempdamage2 = self._stats[position2[Defender]].split('_')
        text[0] = StoredMoves[Attacker][moveset2][0]
        text[1] = StoredMoves[Attacker][moveset2][1]
        text[2] = StoredMoves[Attacker][moveset2][2]
        basebp = StoredMoves[Attacker][moveset2][3]
        if text[0].lower() == 'weatherball':
            text[1] = 'normal'
            StoredMoves[Attacker][moveset2][1] = 'normal'
            basebp = 50
            if StoredMoves[Attacker][0][0] == "sunnyday" or StoredMoves[Attacker][1][0] == "sunnyday" or StoredMoves[Attacker][2][0] == "sunnyday" or StoredMoves[Attacker][3][0] == "sunnyday" or tempdamage2[1].lower() == 'drought':
                text[1] = 'fire'
                basebp = 100
            if StoredMoves[Attacker][0][0] == "raindance" or StoredMoves[Attacker][1][0] == "raindance" or StoredMoves[Attacker][2][0] == "raindance" or StoredMoves[Attacker][3][0] == "raindance" or tempdamage2[1].lower() == 'drizzle':
                text[1] = 'water'
                basebp = 100
            if StoredMoves[Attacker][0][0] == "sandstorm" or StoredMoves[Attacker][1][0] == "sandstorm" or StoredMoves[Attacker][2][0] == "sandstorm" or StoredMoves[Attacker][3][0] == "sandstorm" or tempdamage2[1].lower() == 'sandstream':
                text[1] = 'rock'
                basebp = 80
            if StoredMoves[Attacker][0][0] == "hail" or StoredMoves[Attacker][1][0] == "hail" or StoredMoves[Attacker][2][0] == "hail" or StoredMoves[Attacker][3][0] == "hail" or tempdamage2[1].lower() == 'snowwarning':
                text[1] = 'ice'
                basebp = 80
            StoredMoves[Attacker][moveset2][1] = text[1]
            StoredMoves[Attacker][moveset2][3] = basebp
        if text[0].lower() == 'gyroball':
            basebp = 25 * (float(tempdamage2[11])/float(tempdamage[11]))
            if basebp > 150:
                basebp = 150
        if tempdamage[1].lower() == 'technician':
            if basebp <= 60:
                basebp = basebp * 1.5
        if tempdamage[1].lower() == 'normalize':
            text[1] = 'normal'
        if text[1].lower() == tempdamage[13].lower():
            basebp = basebp*1.5
        if text[1].lower() == tempdamage[14].lower():
            basebp = basebp*1.5
        if tempdamage[1].lower() == 'adaptability':
            if float(StoredMoves[Attacker][moveset2][3]) < basebp:
                basebp = float(StoredMoves[Attacker][moveset2][3]) * 2
        if text[2].lower() == 'status':
            basebp = 0
        temp1 = ((((0.84 * (batsatk[Attacker] / batsdef[Defender]) * basebp)+2) * 0.88) / bathp[Defender])
        temp2 = ((((0.84 * (batatk[Attacker] / batdef[Defender]) * basebp)+2) * 0.88) / bathp[Defender])
        effmulti = 1
        it = True
        if text[2].lower() == 'physical':
            it = False
        temptext = tempdamage2[1]
        if tempdamage[1] == 'moldbreaker':
            temptext = 'moldbreaker'
        effmulti = self.getEff(text[1], tempdamage2[13], temptext) * self.getEff(text[1], tempdamage2[14], temptext)
        if tempdamage[1].lower() == 'tintedlens':
            if effmulti < 1:
                effmulti = effmulti*2
        if it is True:
            temp3 = effmulti*temp1
        if it is False:
            temp3 = effmulti*temp2
        if text[1].lower() == 'fire' and tempdamage[1].lower() == 'drought':
            temp3 = temp3 * 1.5
        if text[1].lower() == 'water' and tempdamage[1].lower() == 'drizzle':
            temp3 = temp3 * 1.5
        if text[1].lower() == 'water' and tempdamage2[1].lower() == 'drought':
            temp3 = temp3 * 0.5
        if text[1].lower() == 'fire' and tempdamage2[1].lower() == 'drizzle':
            temp3 = temp3 * 0.5
        if tempdamage[1].lower() == 'sandstream' and (tempdamage2[13].lower() != 'rock' or tempdamage2[13].lower() != 'steel' or tempdamage2[13].lower() != 'ground' or tempdamage2[14].lower() != 'rock' or tempdamage2[14].lower() != 'steel' or tempdamage2[14].lower() != 'ground'):
            temp3 = temp3 + 0.0625
        if tempdamage[1].lower() == 'hail' and (tempdamage2[13].lower() != 'ice' or tempdamage2[14].lower() != 'ice'):
            temp3 = temp3 + 0.0625
        if ((text[0].lower() == 'horndrill') or (text[0].lower() == 'sheercold') or (text[0].lower() == 'fissure') or (text[0].lower() == 'guillotine')) and (tempdamage2[1].lower() != 'sturdy'):
            temp3 = enemyhp / 3
        if ((text[0].lower() == 'horndrill') or (text[0].lower() == 'sheercold') or (text[0].lower() == 'fissure') or (text[0].lower() == 'guillotine')) and (tempdamage2[1].lower() == 'noguard' or tempdamage[1].lower() == 'noguard'):
            temp3 = 1
        if ((text[0].lower() == 'fly') or (text[0].lower() == 'dive') or (text[0].lower() == 'dig') or (text[0].lower() == 'bounce') or (text[0].lower() == 'shadowforce')) and (tempdamage2[1].lower() == 'noguard' or tempdamage[1].lower() == 'noguard'):
            temp3 = temp3 / 2
        if ((text[0].lower() == 'flareblitz') or (text[0].lower() == 'bravebird') or (text[0].lower() == 'doubleedge') or (text[0].lower() == 'jumpkick') or (text[0].lower() == 'highjumpkick')) and (tempdamage[1].lower() == 'reckless'):
            temp3 = temp3 * 1.2
        if (text[0].lower() == 'seismictoss') or (text[0].lower() == 'nightshade') or (text[0].lower() == 'psywave'):
            temp3 = 100 / bathp[Defender]
        if text[0].lower() == 'dragonrage':
            temp3 = 40 / bathp[Defender]
        if text[0].lower() == 'sonicboom':
            temp3 = 20 / bathp[Defender]
        if text[0].lower() == 'superfang':
            temp3 = 0.34
        if text[0].lower() == 'toxic':
            temp3 = 0.21
        if effmulti < 0.125:
            temp3 = 0
        if text[0].lower() == 'curse':
            if tempdamage[13].lower() == 'ghost':
                temp3 = 0.24
            if tempdamage[14].lower() == 'ghost':
                temp3 = 0.24

        if tempdamage2[1].lower() == 'wonderguard':
            if (text[0].lower() == 'willowisp') or (text[0].lower() == 'poisonpowder') or (text[0].lower() == 'supersonic') or (text[0].lower() == 'perishsong'):
                temp3 = 0.34
            if ((text[0].lower() == 'sandstorm') or (text[0].lower() == 'hail') or (text[0].lower() == 'confuseray') or (text[0].lower() == 'swagger') or
               (text[0].lower() == 'worryseed') or (text[0].lower() == 'toxic') or (text[0].lower() == 'gastroacid') or (text[0].lower() == 'nightmare') or
               (text[0].lower() == 'leechseed') or (text[0].lower() == 'teeterdance')):
                temp3 = 0.51
            if text[0].lower() == 'metronome':
                temp3 = 0.26

        if Attacker < 3:
            dmg[moveset2] = temp3
        if Attacker > 2:
            dmg[4+moveset2] = temp3
        return(dmg)

    def Predictor(self, names=None):
        text = []
        tempdamage = []
        tempweak = []
        tempresist = []
        tempdamage2 = []
        tempweak2 = []
        tempresist2 = []
        temptype = []
        temptype2 = []
        ttype = []
        tempextra = []
        battlers = []
        winpere = []
        winorder = []
        gamesplayed = []
        newmovesname = []

        passes = 0
        rng = 0
        batnames = []
        batnumber = []
        batper = []
        batmatch = []
        batspeed = []
        batatk = []
        bathp = []
        batsatk = []
        batsdef = []
        batdef = []
        position = []
        batresist = []
        batweak = []
        for i in range(0, 6):
            batnames.append(-1)
            batnumber.append(-1)
            batper.append(-1)
            batmatch.append(-1)
            position.append(-1)
            batspeed.append(-1)
            batatk.append(-1)
            bathp.append(-1)
            batsatk.append(-1)
            batsdef.append(-1)
            batdef.append(-1)
            batresist.append(-1)
            batweak.append(-1)
        #print(stats)
        for i2 in range(0,6):
            #Now, find the pokemon the user entered
            found=False
            while not found:
                theinput = None
                if names is not None:
                    theinput=names[i2]
                else:
                    theinput = (str(raw_input('Pokemon name ' +str(i2+1)+":").strip()).title()) 
                # the .strip() removes whitespace, and .title() makes the first letter capitalized
                if theinput == '' :   
                    print('Script Terminated')
                    exit()
                #Now find that pokemon!
                tempx = 0
                temptext = ''
                for i in range(0 , len(self._stats)):
                    text = self._stats[i].split('_')
                    if text[0] == '29':
                        text[12] = 'nidoranf'
                    if text[0] == '32':
                        text[12] = 'nidoranm'
                    if theinput.lower() == text[12].lower() : 
                        batnumber[i2] = text[0]
                        position[i2] = i
                        batnames[i2] = text[12]
                        found=True
                        break
                    if theinput.lower() == text[0].lower() : 
                        batnumber[i2] = text[0]
                        position[i2] = i
                        batnames[i2] = text[12] 
                        found=True
                        break
                    if text[12].lower().startswith(theinput.lower()): 
                        batnumber[i2] = text[0]
                        position[i2] = i
                        batnames[i2] = text[12] 
                        tempx= tempx + 1
                        temptext= temptext + text[12] + ', '
                if tempx == 1:
                    found = True
                if tempx > 1:
                    print('There are multiple pokemon that start with "'+theinput+'" please narrow it down, possible pokemon are: '+temptext)
                if found:
                    pass #Great; we found it!
                elif tempx < 1:
                    print("Pokemon "+theinput+" was not found for pokemon #"+str(i2+1)+". Please try again.")
            #Print the results!
        print(batnames[0]+' '+batnames[1]+' '+ batnames[2]+' '+ batnames[3]+' '+ batnames[4]+' '+ batnames[5])
        print(str(batnumber[0])+' '+str(batnumber[1])+' '+str(batnumber[2])+' '+str(batnumber[3])+' '+ str(batnumber[4])+' '+str(batnumber[5]))
        # figures out self._stats for all mons in the theoretical match
        for allmons in range(0, 6):
            text = self._stats[position[allmons]].split('_')
            bathp[allmons] = int(text[6].strip(", '[]{}_:"))
            batatk[allmons] = int(text[7].strip(", '[]{}_:"))
            batdef[allmons] = int(text[8].strip(", '[]{}_:"))
            batsatk[allmons] = int(text[9].strip(", '[]{}_:"))
            batsdef[allmons] = int(text[10].strip(", '[]{}_:"))
            batspeed[allmons] = int(text[11].strip(", '[]{}_:"))
            # unown is a special case (choice specs - this is a hardcoded way around it)
            if text[12].lower() == 'unown':
                batsatk[allmons] = round(batsatk[allmons] * 1.5)
            # abilities that effect skills that i deemed important
            if text[1].lower() == 'hugepower':
                batatk[allmons] = round(batatk[allmons] * 2)
            if text[1].lower() == 'purepower':
                batatk[allmons] = round(batatk[allmons] * 2)
            if text[1].lower() == 'hustle':
                batatk[allmons] = round(batatk[allmons] * 1.25)
            if text[1].lower() == 'speedboost':
                batspeed[allmons] = round(batspeed[allmons] * 1.7)
            if text[1].lower() == 'slowstart':
                batspeed[allmons] = round(batspeed[allmons] * 0.5)
            if text[1].lower() == 'slowstart':
                batatk[allmons] = round(batatk[allmons] * 0.5)
            if text[1].lower() == 'truant':
                batatk[allmons] = round(batatk[allmons] * 0.5)
            if text[1].lower() == 'truant':
                batsatk[allmons] = round(batsatk[allmons] * 0.5)
        i2 = 0

        # fill StoredMoves with junk so i can use it properly
        StoredMoves = self._stats[0].split('_')
        for allmons in range(0, 6):
            StoredMoves[allmons] = self._stats[0].split('_')
            for moveset in range(0, 4):
                StoredMoves[allmons][moveset] = self._stats[0].split('_')

        for allmons in range(0, 6):
            tempdamage = self._stats[position[allmons]].split('_')
            for moveset in range(0, 4):
                for movelist in range(0, len(self._moves)):
                    text = self._moves[movelist].split('_')
                    # systematically checks every move in the moves.txt
                    if tempdamage[moveset+2].lower() == text[0].lower():
                        StoredMoves[allmons][moveset][0] = text[0]
                        StoredMoves[allmons][moveset][1] = text[1]
                        StoredMoves[allmons][moveset][2] = text[2]
                        StoredMoves[allmons][moveset][3] = float(text[3])
                        if text[0].lower() == 'judgment':
                            StoredMoves[allmons][moveset][1] = tempdamage[13]
                            if tempdamage[13] != 'normal':
                                StoredMoves[allmons][moveset][3] = StoredMoves[allmons][moveset][3] * 1.2
                            if self.jsonlist[position[allmons]]['moves'][moveset]['type'].lower() == 'normal':
                                StoredMoves[allmons][moveset][1] = self.jsonlist[position[allmons]]['moves'][3]['type'].lower()
                        if text[0].lower() == 'hiddenpower':
                            StoredMoves[allmons][moveset][1] = self.jsonlist[position[allmons]]['moves'][moveset]['type'].lower()
                            if self.jsonlist[position[allmons]]['moves'][moveset]['type'].lower() == 'normal':
                                StoredMoves[allmons][moveset][1] = 'u'
                        break
        matchn = 0
        for allmons in range(0, 6):
            # prevents dividing by 0
            batper[allmons] = 50
        i6 = 3
        # setup hp percents of both teams(100% == 1)
        temphpr = 1
        temphpb = 1
        error = ''
        print('')
        print('~Play By Play~')
        for blumons in range(0, 3):
            # setting up blumons
            tempdamage = self._stats[position[blumons]].split('_')
            for redmons in range(i6, 6):
                # setting up redmons
                tempdamage2 = self._stats[position[redmons]].split('_')
                # resetting variables, temporary damage for current move
                temp3 = 0
                # used for charging attacks [xxx, highest blue damaging move, highest red damaging move, second blue, second red]
                dmg = [0, 0, 0, 0, 0, 0, 0, 0]
                move = ['', '', '', '', '', '', '', '']
                for moveset in range(0, 4):
                    dmg = self.DamageDealt(blumons, redmons, moveset, position, StoredMoves, bathp, batatk, batdef, batsatk, batsdef, dmg, temphpr)
                temp3 = 0
                for moveset in range(0, 4):
                    dmg = self.DamageDealt(redmons, blumons, moveset, position, StoredMoves, bathp, batatk, batdef, batsatk, batsdef, dmg, temphpb)

                bestblu = -1
                bestred = -1
                for moveset in range(0, 4):
                    if dmg[moveset] > bestblu:
                        bestblu = dmg[moveset]
                        bestblui = moveset
                        move[moveset] = StoredMoves[blumons][moveset][0]
                    if dmg[4+moveset] > bestred:
                        bestred = dmg[4+moveset]
                        bestredi = 4+moveset
                        move[4+moveset] = StoredMoves[redmons][moveset][0]

                # if any move deals more than 100% damage, make it deal only 100%
                if redmons != 5:
                    if bestblu > 1:
                        bestblu = 1
                    if bestblu > temphpr:
                        bestblu = temphpr + ((bestblu - temphpr) / 2)
                if blumons != 2:
                    if bestred > 1:
                        bestred = 1
                    if bestred > temphpb:
                        bestred = temphpb + ((bestred - temphpb) / 2)

                it = False

                # if a pokemon would be killed before they could use a charging move, use a different move, foo
                if (move[bestblui] == 'solarbeam') or (move[bestblui] == 'skyattack') or (move[bestblui] == 'razorwind') or (move[bestblui] == 'skullbash'):
                    if batspeed[blumons] > batspeed[redmons]:
                        if bestred == 1:
                            bestblu = 0
                            for moveset in range(0, 4):
                                if dmg[moveset] > bestblu and moveset != bestblui:
                                    bestblu = dmg[moveset]
                                    bestblui = moveset
                    if batspeed[blumons] <= batspeed[redmons]:
                        if bestred >= 0.5:
                            bestblu = 0
                            for moveset in range(0, 4):
                                if dmg[moveset] > bestblu and moveset != bestblui:
                                    bestblu = dmg[moveset]
                                    bestblui = moveset

                if (move[bestredi] == 'solarbeam') or (move[bestredi] == 'skyattack') or (move[bestredi] == 'razorwind') or (move[bestredi] == 'skullbash'):
                    if batspeed[blumons] < batspeed[redmons]:
                        if bestblu == 1:
                            bestred = 0
                            for moveset in range(0, 4):
                                if dmg[4+moveset] > bestred and moveset != bestredi:
                                    bestred = dmg[4+moveset]
                                    bestredi = 4+moveset
                    if batspeed[blumons] >= batspeed[redmons]:
                        if bestblu >= 0.5:
                            bestred = 0
                            for moveset in range(0, 4):
                                if dmg[4+moveset] > bestred and moveset != bestredi:
                                    bestred = dmg[4+moveset]
                                    bestredi = 4+moveset

                i3 = 0
                # code to figure out who wins in ideal conditions, blue faster
                if batspeed[blumons] > batspeed[redmons]:
                    it = False
                    while it is False:
                        i3 = i3+1
                        temphpr = temphpr - bestblu
                        batper[blumons] = batper[blumons]+bestblu*100
                        if temphpr > 0:
                            temphpb = temphpb - bestred
                            batper[redmons] = batper[redmons]+bestred*100
                        if temphpr <= 0:
                            print('red died: '+str(tempdamage[12])+', '+str(move[bestblui])+' has killed '+str(tempdamage2[12])+', '+str(move[bestredi])+' in '+str(i3)+' turns with {0:6.2f}'.format(temphpb*100)+'% hp left')
                            i6 = i6+1
                            it = True
                        if temphpb <= 0:
                            print('blue died: '+str(tempdamage2[12])+', '+str(move[bestredi])+' has killed '+str(tempdamage[12])+', '+str(move[bestblui])+' in '+str(i3)+' turns with {0:6.2f}'.format(temphpr*100)+'% hp left')
                            it = True
                # same as above, just red is faster, and attacks first
                if batspeed[blumons] < batspeed[redmons]:
                    it = False
                    while it is False:
                        i3 = i3+1
                        temphpb = temphpb - bestred
                        batper[redmons] = batper[redmons]+bestred*100
                        if temphpb > 0:
                            temphpr = temphpr - bestblu
                            batper[blumons] = batper[blumons]+bestblu*100
                        if temphpr <= 0:
                            print('red died: '+str(tempdamage[12])+', '+str(move[bestblui])+' has killed '+str(tempdamage2[12])+', '+str(move[bestredi])+' in '+str(i3)+' turns with {0:6.2f}'.format(temphpb*100)+'% hp left')
                            i6 = i6+1
                            it = True
                        if temphpb <= 0:
                            print('blue died: '+str(tempdamage2[12])+', '+str(move[bestredi])+' has killed '+str(tempdamage[12])+', '+str(move[bestblui])+' in '+str(i3)+' turns with {0:6.2f}'.format(temphpr*100)+'% hp left')
                            it = True
                # Speed tie
                if batspeed[blumons] == batspeed[redmons]:
                    it = False
                    while it is False:
                        i3 = i3+1
                        temphpb = temphpb - bestred
                        temphpr = temphpr - bestblu
                        batper[blumons] = batper[blumons]+bestblu*100
                        batper[redmons] = batper[redmons]+bestred*100
                        if temphpr <= 0:
                            print('red died: '+str(tempdamage[12])+', '+str(move[bestblui])+' has killed '+str(tempdamage2[12])+', '+str(move[bestredi])+' in '+str(i3)+' turns with {0:6.2f}'.format(temphpb*100)+'% hp left')
                            i6 = i6+1
                            it = True
                        if temphpb <= 0:
                            print('blue died: '+str(tempdamage2[12])+', '+str(move[bestredi])+' has killed '+str(tempdamage[12])+', '+str(move[bestblui])+' in '+str(i3)+' turns with {0:6.2f}'.format(temphpr*100)+'% hp left')
                            it = True
                # Sweeping Clause
                if temphpr <= 0:
                    if redmons == 5:
                        if temphpb > 0:
                            while temphpb > 0:
                                batper[blumons] = batper[blumons]+(bestblu*100)+20
                                temphpb = temphpb - bestred - 1
                            if blumons == 0:
                                batper[1] = batper[1]+50
                            if blumons == 0:
                                batper[2] = batper[2]+50
                            if blumons == 1:
                                batper[2] = batper[2]+50
                if(temphpb <= 0) and(temphpr > 0):
                    if blumons == 2:
                        if temphpr > 0:
                            while temphpr > 0:
                                batper[redmons] = batper[redmons]+(bestred*100)+20
                                temphpr = temphpr - bestblu - 1
                            if redmons == 3:
                                batper[4] = batper[4]+50
                            if redmons == 3:
                                batper[5] = batper[5]+50
                            if redmons == 4:
                                batper[5] = batper[5]+50
                # whatever mon died, increase that teams for loop by one and reset hp to 100%
                if temphpr <= 0:
                    temphpr = 1
                if temphpb <= 0:
                    temphpb = 1
                    break
        print('~Play By Play~')
        print('')
        # if any mon has a rating less than 0, make it 0.01
        for allmons in range(0, 6):
            if batper[allmons] < 0:
                batper[allmons] = 0.01

        # figure out the average
        blueper = (batper[0]+batper[1]+batper[2]) / 3
        redper = (batper[3]+batper[4]+batper[5]) / 3

        # ditto == the average of the opposing team
        for blumons in range(0, 3):
            if batnumber[blumons] == 132:
                batper[blumons] = redper
                blueper = (batper[0]+batper[1]+batper[2]) / 3
        # ditto == the average of the opposing team
        for redmons in range(3, 6):
            if batnumber[redmons] == 132:
                batper[redmons] = blueper
                redper = (batper[3]+batper[4]+batper[5]) / 3

        for i in range(0, 6):
            tempdamage = self._stats[position[i]].split('_')
            for i3 in range(0, 4):
                for i2 in range(0, len(self._moves)):
                    text = self._moves[i2].split('_')
                    if tempdamage[i3+2].lower() == text[0].lower():
                        break
                if text[2].lower() == 'status':
                    batper[i] = batper[i]+(int(text[3]) * 3)

        blueper = (batper[0]+batper[1]+batper[2]) / 3
        redper = (batper[3]+batper[4]+batper[5]) / 3

        temptext = ''
        temptext2 = ''
        if blueper > redper :
            winPer= blueper/(blueper+redper) * 100
            print('Battle Rating: '+batnames[0]+' {0:6.2f}, '.format(batper[0])+batnames[1]+' {0:6.2f}, '.format(batper[1])+batnames[2]+' {0:6.2f}'.format(batper[2])+' -VERSUS- '+batnames[3]+' {0:6.2f}, '.format(batper[3])+batnames[4]+' {0:6.2f}, '.format(batper[4])+batnames[5]+' {0:6.2f} '.format(batper[5])+' ---  {0:6.2f}'.format(winPer)+'% BLUE Wins')
        elif blueper < redper :
            winPer= redper/(blueper+redper) * 100
            print('Battle Rating: '+batnames[0]+' {0:6.2f}, '.format(batper[0])+batnames[1]+' {0:6.2f}, '.format(batper[1])+batnames[2]+' {0:6.2f}'.format(batper[2])+' -VERSUS- '+batnames[3]+' {0:6.2f}, '.format(batper[3])+batnames[4]+' {0:6.2f}, '.format(batper[4])+batnames[5]+' {0:6.2f} '.format(batper[5])+' ---  {0:6.2f}'.format(winPer)+'% RED Wins')
        elif blueper == redper :
            winPer= blueper/(blueper+redper) * 100
            print('Battle Rating: '+batnames[0]+' {0:6.2f}, '.format(batper[0])+batnames[1]+' {0:6.2f}, '.format(batper[1])+batnames[2]+' {0:6.2f}'.format(batper[2])+' -VERSUS- '+batnames[3]+' {0:6.2f}, '.format(batper[3])+batnames[4]+' {0:6.2f}, '.format(batper[4])+batnames[5]+' {0:6.2f} '.format(batper[5])+' ---  {0:6.2f}'.format(winPer)+'% EITHER Wins')      
        
        return ({"blueScore": blueper, "redScore": redper})








def main():
    logging.basicConfig(level=logging.DEBUG)
    matchmaker = MatchMaker()
    results = matchmaker.Predictor(['kabuto', 'pidgey', 'clefairy', 'jigglyp54456', 'ivysaur', 'squirtle'])
    print 'printing results'
    print results


if __name__ == '__main__':
    main()
