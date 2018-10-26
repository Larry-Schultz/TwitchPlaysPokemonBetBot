'''
Created on Aug 31, 2015

@author: derp
'''
import json
import pg8000

jsonString = '''{
    "1": {
        "stats": {
            "hp": 245,
            "atk": 168,
            "sdf": 190,
            "spd": 140,
            "def": 148,
            "sat": 148
        },
        "name": "Bulbasaur",
        "weight": 6.9,
        "gender": "m",
        "type2": "poison",
        "moves": [
            438,
            73,
            79,
            182
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "2": {
        "stats": {
            "hp": 267,
            "atk": 149,
            "sdf": 202,
            "spd": 162,
            "def": 168,
            "sat": 222
        },
        "name": "Ivysaur",
        "weight": 13,
        "gender": "f",
        "type2": "poison",
        "moves": [
            412,
            188,
            77,
            235
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "3": {
        "stats": {
            "hp": 296,
            "atk": 192,
            "sdf": 198,
            "spd": 220,
            "def": 187,
            "sat": 305
        },
        "name": "Venusaur",
        "weight": 100,
        "gender": "f",
        "type2": "poison",
        "moves": [
            124,
            72,
            267,
            320
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "4": {
        "stats": {
            "hp": 230,
            "atk": 223,
            "sdf": 136,
            "spd": 219,
            "def": 122,
            "sat": 140
        },
        "name": "Charmander",
        "weight": 8.5,
        "gender": "m",
        "moves": [
            394,
            200,
            261,
            14
        ],
        "type1": "fire",
        "ability": "Blaze"
    },
    "5": {
        "stats": {
            "hp": 320,
            "atk": 147,
            "sdf": 196,
            "spd": 203,
            "def": 196,
            "sat": 196
        },
        "name": "Charmeleon",
        "weight": 19,
        "gender": "f",
        "moves": [
            53,
            406,
            246,
            241
        ],
        "type1": "fire",
        "ability": "Solar Power"
    },
    "6": {
        "stats": {
            "hp": 323,
            "atk": 215,
            "sdf": 232,
            "spd": 212,
            "def": 218,
            "sat": 321
        },
        "name": "Charizard",
        "weight": 90.5,
        "gender": "f",
        "type2": "flying",
        "moves": [
            17,
            52,
            317,
            45
        ],
        "type1": "fire",
        "ability": "Blaze"
    },
    "7": {
        "stats": {
            "hp": 292,
            "atk": 118,
            "sdf": 164,
            "spd": 122,
            "def": 167,
            "sat": 218
        },
        "name": "Squirtle",
        "weight": 9,
        "gender": "m",
        "moves": [
            56,
            396,
            58,
            243
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "8": {
        "stats": {
            "hp": 280,
            "atk": 183,
            "sdf": 238,
            "spd": 155,
            "def": 217,
            "sat": 187
        },
        "name": "Wartortle",
        "weight": 22.5,
        "gender": "f",
        "moves": [
            291,
            91,
            92,
            240
        ],
        "type1": "water",
        "ability": "Rain Dish"
    },
    "9": {
        "stats": {
            "hp": 293,
            "atk": 157,
            "sdf": 276,
            "spd": 186,
            "def": 241,
            "sat": 200
        },
        "name": "Blastoise",
        "weight": 85.5,
        "gender": "f",
        "moves": [
            308,
            192,
            430,
            110
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "10": {
        "stats": {
            "hp": 245,
            "atk": 174,
            "sdf": 90,
            "spd": 147,
            "def": 120,
            "sat": 68
        },
        "name": "Caterpie",
        "weight": 2.9,
        "gender": "m",
        "moves": [
            450,
            33,
            81,
            173
        ],
        "type1": "bug",
        "ability": "Shield Dust"
    },
    "11": {
        "stats": {
            "hp": 241,
            "atk": 152,
            "sdf": 148,
            "spd": 96,
            "def": 148,
            "sat": 77
        },
        "name": "Metapod",
        "weight": 9.9,
        "gender": "m",
        "moves": [
            450,
            33,
            81,
            334
        ],
        "type1": "bug",
        "ability": "Shed Skin"
    },
    "12": {
        "stats": {
            "hp": 269,
            "atk": 134,
            "sdf": 204,
            "spd": 202,
            "def": 144,
            "sat": 183
        },
        "name": "Butterfree",
        "weight": 32,
        "gender": "f",
        "type2": "flying",
        "moves": [
            405,
            94,
            79,
            48
        ],
        "type1": "bug",
        "ability": "Compound Eyes"
    },
    "13": {
        "stats": {
            "hp": 235,
            "atk": 185,
            "sdf": 90,
            "spd": 157,
            "def": 110,
            "sat": 68
        },
        "name": "Weedle",
        "weight": 3.2,
        "gender": "m",
        "type2": "poison",
        "moves": [
            450,
            40,
            81
        ],
        "type1": "bug",
        "ability": "Shield Dust"
    },
    "14": {
        "stats": {
            "hp": 232,
            "atk": 163,
            "sdf": 86,
            "spd": 169,
            "def": 136,
            "sat": 77
        },
        "name": "Kakuna",
        "weight": 10,
        "gender": "m",
        "type2": "poison",
        "moves": [
            450,
            40,
            81,
            334
        ],
        "type1": "bug",
        "ability": "Shed Skin"
    },
    "15": {
        "stats": {
            "hp": 279,
            "atk": 224,
            "sdf": 204,
            "spd": 194,
            "def": 124,
            "sat": 120
        },
        "name": "Beedrill",
        "weight": 29.5,
        "gender": "m",
        "type2": "poison",
        "moves": [
            398,
            41,
            14,
            390
        ],
        "type1": "bug",
        "ability": "Swarm"
    },
    "16": {
        "stats": {
            "hp": 222,
            "atk": 207,
            "sdf": 106,
            "spd": 211,
            "def": 116,
            "sat": 95
        },
        "name": "Pidgey",
        "weight": 1.8,
        "gender": "m",
        "type2": "flying",
        "moves": [
            413,
            216,
            297,
            355
        ],
        "type1": "normal",
        "ability": "Tangled Feet"
    },
    "17": {
        "stats": {
            "hp": 268,
            "atk": 140,
            "sdf": 136,
            "spd": 241,
            "def": 146,
            "sat": 218
        },
        "name": "Pidgeotto",
        "weight": 30,
        "gender": "m",
        "type2": "flying",
        "moves": [
            403,
            257,
            445,
            355
        ],
        "type1": "normal",
        "ability": "Tangled Feet"
    },
    "18": {
        "stats": {
            "hp": 307,
            "atk": 196,
            "sdf": 187,
            "spd": 239,
            "def": 197,
            "sat": 139
        },
        "name": "Pidgeot",
        "weight": 39.5,
        "gender": "m",
        "type2": "flying",
        "moves": [
            416,
            143,
            119,
            355
        ],
        "type1": "normal",
        "ability": "Tangled Feet"
    },
    "19": {
        "stats": {
            "hp": 202,
            "atk": 211,
            "sdf": 106,
            "spd": 267,
            "def": 106,
            "sat": 77
        },
        "name": "Rattata",
        "weight": 3.5,
        "gender": "m",
        "moves": [
            38,
            242,
            91,
            98
        ],
        "type1": "normal",
        "ability": "Hustle"
    },
    "20": {
        "stats": {
            "hp": 260,
            "atk": 229,
            "sdf": 185,
            "spd": 239,
            "def": 165,
            "sat": 108
        },
        "name": "Raticate",
        "weight": 18.5,
        "gender": "m",
        "moves": [
            162,
            158,
            279,
            172
        ],
        "type1": "normal",
        "ability": "Guts"
    },
    "21": {
        "stats": {
            "hp": 222,
            "atk": 219,
            "sdf": 98,
            "spd": 262,
            "def": 96,
            "sat": 88
        },
        "name": "Spearow",
        "weight": 2,
        "gender": "m",
        "type2": "flying",
        "moves": [
            38,
            19,
            211,
            119
        ],
        "type1": "normal",
        "ability": "Sniper"
    },
    "22": {
        "stats": {
            "hp": 274,
            "atk": 219,
            "sdf": 177,
            "spd": 239,
            "def": 169,
            "sat": 144
        },
        "name": "Fearow",
        "weight": 38,
        "gender": "f",
        "type2": "flying",
        "moves": [
            65,
            416,
            211,
            45
        ],
        "type1": "normal",
        "ability": "Sniper"
    },
    "23": {
        "stats": {
            "hp": 232,
            "atk": 198,
            "sdf": 205,
            "spd": 146,
            "def": 145,
            "sat": 103
        },
        "name": "Ekans",
        "weight": 6.9,
        "gender": "m",
        "moves": [
            441,
            89,
            402,
            137
        ],
        "type1": "poison",
        "ability": "Intimidate"
    },
    "24": {
        "stats": {
            "hp": 264,
            "atk": 209,
            "sdf": 197,
            "spd": 199,
            "def": 177,
            "sat": 169
        },
        "name": "Arbok",
        "weight": 65,
        "gender": "f",
        "moves": [
            305,
            423,
            424,
            422
        ],
        "type1": "poison",
        "ability": "Intimidate"
    },
    "25": {
        "stats": {
            "hp": 229,
            "atk": 131,
            "sdf": 124,
            "spd": 246,
            "def": 104,
            "sat": 218
        },
        "name": "Pikachu",
        "weight": 6,
        "gender": "f",
        "moves": [
            85,
            57,
            324,
            417
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "26": {
        "stats": {
            "hp": 260,
            "atk": 215,
            "sdf": 195,
            "spd": 235,
            "def": 145,
            "sat": 215
        },
        "name": "Raichu",
        "weight": 30,
        "gender": "m",
        "moves": [
            87,
            19,
            91,
            393
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "27": {
        "stats": {
            "hp": 251,
            "atk": 239,
            "sdf": 149,
            "spd": 148,
            "def": 206,
            "sat": 68
        },
        "name": "Sandshrew",
        "weight": 12,
        "gender": "f",
        "moves": [
            89,
            157,
            404,
            14
        ],
        "type1": "ground",
        "ability": "Sand Veil"
    },
    "28": {
        "stats": {
            "hp": 293,
            "atk": 238,
            "sdf": 162,
            "spd": 168,
            "def": 258,
            "sat": 115
        },
        "name": "Sandslash",
        "weight": 29.5,
        "gender": "f",
        "moves": [
            89,
            70,
            398,
            201
        ],
        "type1": "ground",
        "ability": "Sand Veil"
    },
    "29": {
        "stats": {
            "hp": 266,
            "atk": 212,
            "sdf": 119,
            "spd": 161,
            "def": 143,
            "sat": 104
        },
        "name": "Nidoran-female",
        "weight": 7,
        "gender": "f",
        "moves": [
            398,
            91,
            332,
            142
        ],
        "type1": "poison",
        "ability": "Hustle"
    },
    "30": {
        "stats": {
            "hp": 291,
            "atk": 134,
            "sdf": 156,
            "spd": 137,
            "def": 180,
            "sat": 217
        },
        "name": "Nidorina",
        "weight": 20,
        "gender": "f",
        "moves": [
            162,
            188,
            59,
            260
        ],
        "type1": "poison",
        "ability": "Rivalry"
    },
    "31": {
        "stats": {
            "hp": 319,
            "atk": 178,
            "sdf": 204,
            "spd": 186,
            "def": 208,
            "sat": 202
        },
        "name": "Nidoqueen",
        "weight": 60,
        "gender": "f",
        "type2": "ground",
        "moves": [
            89,
            398,
            196,
            39
        ],
        "type1": "poison",
        "ability": "Poison Point"
    },
    "32": {
        "stats": {
            "hp": 265,
            "atk": 182,
            "sdf": 130,
            "spd": 188,
            "def": 130,
            "sat": 104
        },
        "name": "Nidoran-male",
        "weight": 9,
        "gender": "m",
        "moves": [
            398,
            457,
            389,
            32
        ],
        "type1": "poison",
        "ability": "Hustle"
    },
    "33": {
        "stats": {
            "hp": 273,
            "atk": 152,
            "sdf": 167,
            "spd": 155,
            "def": 171,
            "sat": 194
        },
        "name": "Nidorino",
        "weight": 19.5,
        "gender": "m",
        "moves": [
            188,
            87,
            32,
            260
        ],
        "type1": "poison",
        "ability": "Rivalry"
    },
    "34": {
        "stats": {
            "hp": 301,
            "atk": 218,
            "sdf": 202,
            "spd": 183,
            "def": 188,
            "sat": 204
        },
        "name": "Nidoking",
        "weight": 62,
        "gender": "m",
        "type2": "ground",
        "moves": [
            414,
            398,
            57,
            32
        ],
        "type1": "poison",
        "ability": "Rivalry"
    },
    "35": {
        "stats": {
            "hp": 313,
            "atk": 113,
            "sdf": 194,
            "spd": 106,
            "def": 164,
            "sat": 210
        },
        "name": "Clefairy",
        "weight": 7.5,
        "gender": "m",
        "moves": [
            304,
            58,
            347,
            118
        ],
        "type1": "normal",
        "ability": "Magic Guard"
    },
    "36": {
        "stats": {
            "hp": 331,
            "atk": 193,
            "sdf": 216,
            "spd": 156,
            "def": 203,
            "sat": 166
        },
        "name": "Clefable",
        "weight": 40,
        "gender": "f",
        "moves": [
            70,
            309,
            383,
            227
        ],
        "type1": "normal",
        "ability": "Magic Guard"
    },
    "37": {
        "stats": {
            "hp": 219,
            "atk": 106,
            "sdf": 198,
            "spd": 198,
            "def": 148,
            "sat": 183
        },
        "name": "Vulpix",
        "weight": 9.9,
        "gender": "f",
        "moves": [
            126,
            412,
            109,
            261
        ],
        "type1": "fire",
        "ability": "Drought"
    },
    "38": {
        "stats": {
            "hp": 284,
            "atk": 203,
            "sdf": 209,
            "spd": 233,
            "def": 183,
            "sat": 195
        },
        "name": "Ninetales",
        "weight": 19.9,
        "gender": "f",
        "moves": [
            315,
            91,
            288,
            384
        ],
        "type1": "fire",
        "ability": "Flash Fire"
    },
    "39": {
        "stats": {
            "hp": 372,
            "atk": 126,
            "sdf": 149,
            "spd": 76,
            "def": 152,
            "sat": 113
        },
        "name": "Jigglypuff",
        "weight": 5.5,
        "gender": "m",
        "moves": [
            69,
            195,
            113,
            115
        ],
        "type1": "normal",
        "ability": "Cute Charm"
    },
    "40": {
        "stats": {
            "hp": 442,
            "atk": 262,
            "sdf": 157,
            "spd": 126,
            "def": 147,
            "sat": 167
        },
        "name": "Wigglytuff",
        "weight": 12,
        "gender": "f",
        "moves": [
            1,
            264,
            247,
            47
        ],
        "type1": "normal",
        "ability": "Cute Charm"
    },
    "41": {
        "stats": {
            "hp": 222,
            "atk": 189,
            "sdf": 116,
            "spd": 229,
            "def": 106,
            "sat": 86
        },
        "name": "Zubat",
        "weight": 7.5,
        "gender": "m",
        "type2": "flying",
        "moves": [
            162,
            413,
            109,
            92
        ],
        "type1": "poison",
        "ability": "Inner Focus"
    },
    "42": {
        "stats": {
            "hp": 291,
            "atk": 165,
            "sdf": 186,
            "spd": 253,
            "def": 158,
            "sat": 180
        },
        "name": "Golbat",
        "weight": 55,
        "gender": "f",
        "type2": "flying",
        "moves": [
            403,
            202,
            109,
            269
        ],
        "type1": "poison",
        "ability": "Inner Focus"
    },
    "43": {
        "stats": {
            "hp": 290,
            "atk": 122,
            "sdf": 166,
            "spd": 128,
            "def": 150,
            "sat": 239
        },
        "name": "Oddish",
        "weight": 5.4,
        "gender": "m",
        "type2": "poison",
        "moves": [
            76,
            188,
            298,
            241
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "44": {
        "stats": {
            "hp": 268,
            "atk": 155,
            "sdf": 193,
            "spd": 135,
            "def": 183,
            "sat": 213
        },
        "name": "Gloom",
        "weight": 8.6,
        "gender": "f",
        "type2": "poison",
        "moves": [
            412,
            188,
            236,
            241
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "45": {
        "stats": {
            "hp": 313,
            "atk": 176,
            "sdf": 237,
            "spd": 136,
            "def": 227,
            "sat": 328
        },
        "name": "Vileplume",
        "weight": 18.6,
        "gender": "f",
        "type2": "poison",
        "moves": [
            72,
            51,
            409,
            236
        ],
        "type1": "grass",
        "ability": "Effect Spore"
    },
    "46": {
        "stats": {
            "hp": 212,
            "atk": 262,
            "sdf": 146,
            "spd": 149,
            "def": 146,
            "sat": 113
        },
        "name": "Paras",
        "weight": 5.4,
        "gender": "m",
        "type2": "grass",
        "moves": [
            402,
            404,
            147,
            14
        ],
        "type1": "bug",
        "ability": "Dry Skin"
    },
    "47": {
        "stats": {
            "hp": 282,
            "atk": 289,
            "sdf": 196,
            "spd": 151,
            "def": 196,
            "sat": 140
        },
        "name": "Parasect",
        "weight": 29.5,
        "gender": "f",
        "type2": "grass",
        "moves": [
            402,
            163,
            147,
            97
        ],
        "type1": "bug",
        "ability": "Dry Skin"
    },
    "48": {
        "stats": {
            "hp": 257,
            "atk": 126,
            "sdf": 141,
            "spd": 202,
            "def": 131,
            "sat": 174
        },
        "name": "Venonat",
        "weight": 30,
        "gender": "f",
        "type2": "poison",
        "moves": [
            188,
            94,
            79,
            234
        ],
        "type1": "bug",
        "ability": "Tinted Lens"
    },
    "49": {
        "stats": {
            "hp": 283,
            "atk": 151,
            "sdf": 188,
            "spd": 218,
            "def": 173,
            "sat": 218
        },
        "name": "Venomoth",
        "weight": 12.5,
        "gender": "m",
        "type2": "poison",
        "moves": [
            405,
            50,
            390,
            164
        ],
        "type1": "bug",
        "ability": "Tinted Lens"
    },
    "50": {
        "stats": {
            "hp": 162,
            "atk": 209,
            "sdf": 126,
            "spd": 317,
            "def": 86,
            "sat": 95
        },
        "name": "Diglett",
        "weight": 0.8,
        "gender": "m",
        "moves": [
            89,
            157,
            90,
            262
        ],
        "type1": "ground",
        "ability": "Sand Veil"
    },
    "51": {
        "stats": {
            "hp": 217,
            "atk": 202,
            "sdf": 182,
            "spd": 310,
            "def": 142,
            "sat": 127
        },
        "name": "Dugtrio",
        "weight": 33.3,
        "gender": "f",
        "moves": [
            91,
            444,
            90,
            446
        ],
        "type1": "ground",
        "ability": "Arena Trap"
    },
    "52": {
        "stats": {
            "hp": 237,
            "atk": 203,
            "sdf": 112,
            "spd": 256,
            "def": 102,
            "sat": 100
        },
        "name": "Meowth",
        "weight": 4.2,
        "gender": "m",
        "moves": [
            175,
            44,
            180,
            164
        ],
        "type1": "normal",
        "ability": "Technician"
    },
    "53": {
        "stats": {
            "hp": 274,
            "atk": 196,
            "sdf": 169,
            "spd": 269,
            "def": 143,
            "sat": 169
        },
        "name": "Persian",
        "weight": 32,
        "gender": "f",
        "moves": [
            252,
            29,
            85,
            352
        ],
        "type1": "normal",
        "ability": "Technician"
    },
    "54": {
        "stats": {
            "hp": 255,
            "atk": 138,
            "sdf": 150,
            "spd": 160,
            "def": 146,
            "sat": 198
        },
        "name": "Psyduck",
        "weight": 19.6,
        "gender": "m",
        "moves": [
            57,
            80,
            50,
            281
        ],
        "type1": "water",
        "ability": "Cloud Nine"
    },
    "55": {
        "stats": {
            "hp": 298,
            "atk": 216,
            "sdf": 193,
            "spd": 203,
            "def": 189,
            "sat": 200
        },
        "name": "Golduck",
        "weight": 76.6,
        "gender": "f",
        "moves": [
            401,
            428,
            238,
            39
        ],
        "type1": "water",
        "ability": "Cloud Nine"
    },
    "56": {
        "stats": {
            "hp": 237,
            "atk": 212,
            "sdf": 142,
            "spd": 211,
            "def": 122,
            "sat": 109
        },
        "name": "Mankey",
        "weight": 28,
        "gender": "f",
        "moves": [
            370,
            231,
            265,
            164
        ],
        "type1": "fighting",
        "ability": "Anger Point"
    },
    "57": {
        "stats": {
            "hp": 272,
            "atk": 222,
            "sdf": 177,
            "spd": 227,
            "def": 157,
            "sat": 172
        },
        "name": "Primeape",
        "weight": 32,
        "gender": "f",
        "moves": [
            238,
            315,
            37,
            116
        ],
        "type1": "fighting",
        "ability": "Vital Spirit"
    },
    "58": {
        "stats": {
            "hp": 272,
            "atk": 197,
            "sdf": 157,
            "spd": 217,
            "def": 147,
            "sat": 158
        },
        "name": "Growlithe",
        "weight": 19,
        "gender": "m",
        "moves": [
            394,
            370,
            261,
            234
        ],
        "type1": "fire",
        "ability": "Intimidate"
    },
    "59": {
        "stats": {
            "hp": 313,
            "atk": 248,
            "sdf": 206,
            "spd": 218,
            "def": 188,
            "sat": 205
        },
        "name": "Arcanine",
        "weight": 155,
        "gender": "f",
        "moves": [
            172,
            242,
            245,
            46
        ],
        "type1": "fire",
        "ability": "Intimidate"
    },
    "60": {
        "stats": {
            "hp": 230,
            "atk": 117,
            "sdf": 125,
            "spd": 255,
            "def": 125,
            "sat": 174
        },
        "name": "Poliwag",
        "weight": 12.4,
        "gender": "f",
        "moves": [
            57,
            95,
            207,
            74
        ],
        "type1": "water",
        "ability": "Damp"
    },
    "61": {
        "stats": {
            "hp": 279,
            "atk": 215,
            "sdf": 144,
            "spd": 224,
            "def": 174,
            "sat": 110
        },
        "name": "Poliwhirl",
        "weight": 20,
        "gender": "m",
        "moves": [
            291,
            358,
            301,
            95
        ],
        "type1": "water",
        "ability": "Damp"
    },
    "62": {
        "stats": {
            "hp": 318,
            "atk": 203,
            "sdf": 213,
            "spd": 173,
            "def": 200,
            "sat": 190
        },
        "name": "Poliwrath",
        "weight": 54,
        "gender": "f",
        "type2": "fighting",
        "moves": [
            56,
            223,
            170,
            339
        ],
        "type1": "water",
        "ability": "Water Absorb"
    },
    "63": {
        "stats": {
            "hp": 206,
            "atk": 63,
            "sdf": 161,
            "spd": 279,
            "def": 81,
            "sat": 261
        },
        "name": "Abra",
        "weight": 19.5,
        "gender": "m",
        "moves": [
            94,
            412,
            385,
            207
        ],
        "type1": "psychic",
        "ability": "Synchronize"
    },
    "64": {
        "stats": {
            "hp": 228,
            "atk": 92,
            "sdf": 201,
            "spd": 253,
            "def": 124,
            "sat": 254
        },
        "name": "Kadabra",
        "weight": 56.5,
        "gender": "f",
        "moves": [
            94,
            351,
            134,
            272
        ],
        "type1": "psychic",
        "ability": "Magic Guard"
    },
    "65": {
        "stats": {
            "hp": 249,
            "atk": 155,
            "sdf": 204,
            "spd": 274,
            "def": 136,
            "sat": 254
        },
        "name": "Alakazam",
        "weight": 48,
        "gender": "f",
        "moves": [
            60,
            324,
            134,
            118
        ],
        "type1": "psychic",
        "ability": "Inner Focus"
    },
    "66": {
        "stats": {
            "hp": 297,
            "atk": 233,
            "sdf": 122,
            "spd": 109,
            "def": 152,
            "sat": 122
        },
        "name": "Machop",
        "weight": 19.5,
        "gender": "f",
        "moves": [
            223,
            25,
            89,
            418
        ],
        "type1": "fighting",
        "ability": "No Guard"
    },
    "67": {
        "stats": {
            "hp": 307,
            "atk": 242,
            "sdf": 178,
            "spd": 118,
            "def": 182,
            "sat": 142
        },
        "name": "Machoke",
        "weight": 70.5,
        "gender": "f",
        "moves": [
            238,
            157,
            418,
            184
        ],
        "type1": "fighting",
        "ability": "No Guard"
    },
    "68": {
        "stats": {
            "hp": 318,
            "atk": 263,
            "sdf": 203,
            "spd": 143,
            "def": 193,
            "sat": 179
        },
        "name": "Machamp",
        "weight": 130,
        "gender": "f",
        "moves": [
            66,
            126,
            431,
            92
        ],
        "type1": "fighting",
        "ability": "No Guard"
    },
    "69": {
        "stats": {
            "hp": 242,
            "atk": 167,
            "sdf": 96,
            "spd": 196,
            "def": 106,
            "sat": 239
        },
        "name": "Bellsprout",
        "weight": 4,
        "gender": "f",
        "type2": "poison",
        "moves": [
            188,
            311,
            79,
            241
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "70": {
        "stats": {
            "hp": 293,
            "atk": 194,
            "sdf": 147,
            "spd": 146,
            "def": 157,
            "sat": 295
        },
        "name": "Weepinbell",
        "weight": 6.4,
        "gender": "m",
        "type2": "poison",
        "moves": [
            438,
            378,
            74,
            241
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "71": {
        "stats": {
            "hp": 322,
            "atk": 339,
            "sdf": 167,
            "spd": 197,
            "def": 177,
            "sat": 212
        },
        "name": "Victreebel",
        "weight": 15.5,
        "gender": "m",
        "item": "Big Root",
        "type2": "poison",
        "moves": [
            22,
            21,
            141,
            321
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "72": {
        "stats": {
            "hp": 234,
            "atk": 108,
            "sdf": 273,
            "spd": 189,
            "def": 88,
            "sat": 191
        },
        "name": "Tentacool",
        "weight": 45.5,
        "gender": "m",
        "type2": "poison",
        "moves": [
            56,
            188,
            59,
            243
        ],
        "type1": "water",
        "ability": "Clear Body"
    },
    "73": {
        "stats": {
            "hp": 297,
            "atk": 172,
            "sdf": 272,
            "spd": 232,
            "def": 162,
            "sat": 192
        },
        "name": "Tentacruel",
        "weight": 55,
        "gender": "f",
        "type2": "poison",
        "moves": [
            300,
            188,
            112,
            390
        ],
        "type1": "water",
        "ability": "Liquid Ooze"
    },
    "74": {
        "stats": {
            "hp": 284,
            "atk": 197,
            "sdf": 174,
            "spd": 76,
            "def": 236,
            "sat": 86
        },
        "name": "Geodude",
        "weight": 20,
        "gender": "m",
        "type2": "ground",
        "moves": [
            89,
            444,
            389,
            153
        ],
        "type1": "rock",
        "ability": "Sturdy"
    },
    "75": {
        "stats": {
            "hp": 263,
            "atk": 240,
            "sdf": 151,
            "spd": 118,
            "def": 278,
            "sat": 101
        },
        "name": "Graveler",
        "weight": 105,
        "gender": "f",
        "type2": "ground",
        "moves": [
            91,
            157,
            397,
            120
        ],
        "type1": "rock",
        "ability": "Sturdy"
    },
    "76": {
        "stats": {
            "hp": 333,
            "atk": 256,
            "sdf": 251,
            "spd": 126,
            "def": 295,
            "sat": 146
        },
        "name": "Golem",
        "weight": 300,
        "gender": "m",
        "type2": "ground",
        "moves": [
            222,
            205,
            111,
            201
        ],
        "type1": "rock",
        "ability": "Sand Veil"
    },
    "77": {
        "stats": {
            "hp": 247,
            "atk": 212,
            "sdf": 172,
            "spd": 244,
            "def": 152,
            "sat": 154
        },
        "name": "Ponyta",
        "weight": 30,
        "gender": "f",
        "moves": [
            394,
            231,
            95,
            234
        ],
        "type1": "fire",
        "ability": "Flame Body"
    },
    "78": {
        "stats": {
            "hp": 268,
            "atk": 233,
            "sdf": 193,
            "spd": 267,
            "def": 155,
            "sat": 193
        },
        "name": "Rapidash",
        "weight": 95,
        "gender": "f",
        "moves": [
            257,
            231,
            23,
            32
        ],
        "type1": "fire",
        "ability": "Flash Fire"
    },
    "79": {
        "stats": {
            "hp": 336,
            "atk": 181,
            "sdf": 144,
            "spd": 81,
            "def": 181,
            "sat": 117
        },
        "name": "Slowpoke",
        "weight": 36,
        "gender": "m",
        "type2": "psychic",
        "moves": [
            401,
            428,
            89,
            174
        ],
        "type1": "water",
        "ability": "Own Tempo"
    },
    "80": {
        "stats": {
            "hp": 329,
            "atk": 202,
            "sdf": 174,
            "spd": 94,
            "def": 254,
            "sat": 234
        },
        "name": "Slowbro",
        "weight": 78.5,
        "gender": "f",
        "type2": "psychic",
        "moves": [
            94,
            352,
            281,
            433
        ],
        "type1": "water",
        "ability": "Own Tempo"
    },
    "81": {
        "stats": {
            "hp": 205,
            "atk": 120,
            "sdf": 144,
            "spd": 140,
            "def": 190,
            "sat": 264
        },
        "name": "Magnemite",
        "weight": 6,
        "gender": "-",
        "type2": "steel",
        "moves": [
            85,
            430,
            48,
            86
        ],
        "type1": "electric",
        "ability": "Sturdy"
    },
    "82": {
        "stats": {
            "hp": 241,
            "atk": 171,
            "sdf": 158,
            "spd": 176,
            "def": 226,
            "sat": 276
        },
        "name": "Magneton",
        "weight": 60,
        "gender": "-",
        "type2": "steel",
        "moves": [
            435,
            429,
            319,
            48
        ],
        "type1": "electric",
        "ability": "Sturdy"
    },
    "83": {
        "stats": {
            "hp": 252,
            "atk": 177,
            "sdf": 171,
            "spd": 194,
            "def": 172,
            "sat": 127
        },
        "name": "Farfetch'd",
        "weight": 15,
        "gender": "m",
        "type2": "flying",
        "moves": [
            163,
            19,
            348,
            14
        ],
        "type1": "normal",
        "ability": "Inner Focus"
    },
    "84": {
        "stats": {
            "hp": 232,
            "atk": 227,
            "sdf": 138,
            "spd": 227,
            "def": 158,
            "sat": 95
        },
        "name": "Doduo",
        "weight": 39.2,
        "gender": "m",
        "type2": "flying",
        "moves": [
            19,
            263,
            67,
            114
        ],
        "type1": "normal",
        "ability": "Tangled Feet"
    },
    "85": {
        "stats": {
            "hp": 263,
            "atk": 212,
            "sdf": 178,
            "spd": 216,
            "def": 198,
            "sat": 172
        },
        "name": "Dodrio",
        "weight": 85.2,
        "gender": "f",
        "type2": "flying",
        "moves": [
            65,
            161,
            367,
            156
        ],
        "type1": "normal",
        "ability": "Early Bird"
    },
    "86": {
        "stats": {
            "hp": 303,
            "atk": 113,
            "sdf": 208,
            "spd": 126,
            "def": 195,
            "sat": 157
        },
        "name": "Seel",
        "weight": 90,
        "gender": "m",
        "moves": [
            57,
            196,
            227,
            195
        ],
        "type1": "water",
        "ability": "Hydration"
    },
    "87": {
        "stats": {
            "hp": 320,
            "atk": 157,
            "sdf": 225,
            "spd": 175,
            "def": 214,
            "sat": 175
        },
        "name": "Dewgong",
        "weight": 120,
        "gender": "f",
        "type2": "ice",
        "moves": [
            58,
            362,
            324,
            392
        ],
        "type1": "water",
        "ability": "Thick Fat"
    },
    "88": {
        "stats": {
            "hp": 315,
            "atk": 232,
            "sdf": 160,
            "spd": 100,
            "def": 160,
            "sat": 98
        },
        "name": "Grimer",
        "weight": 30,
        "gender": "m",
        "moves": [
            441,
            91,
            425,
            103
        ],
        "type1": "poison",
        "ability": "Stench"
    },
    "89": {
        "stats": {
            "hp": 348,
            "atk": 199,
            "sdf": 254,
            "spd": 133,
            "def": 183,
            "sat": 179
        },
        "name": "Muk",
        "weight": 30,
        "gender": "f",
        "moves": [
            124,
            87,
            202,
            151
        ],
        "type1": "poison",
        "ability": "Sticky Hold"
    },
    "90": {
        "stats": {
            "hp": 259,
            "atk": 193,
            "sdf": 124,
            "spd": 111,
            "def": 231,
            "sat": 108
        },
        "name": "Shellder",
        "weight": 4,
        "gender": "f",
        "moves": [
            291,
            419,
            350,
            420
        ],
        "type1": "water",
        "ability": "Skill Link"
    },
    "91": {
        "stats": {
            "hp": 236,
            "atk": 242,
            "sdf": 156,
            "spd": 171,
            "def": 333,
            "sat": 180
        },
        "name": "Cloyster",
        "weight": 132.5,
        "gender": "f",
        "type2": "ice",
        "moves": [
            57,
            333,
            131,
            191
        ],
        "type1": "water",
        "ability": "Skill Link"
    },
    "92": {
        "stats": {
            "hp": 216,
            "atk": 108,
            "sdf": 121,
            "spd": 232,
            "def": 111,
            "sat": 251
        },
        "name": "Gastly",
        "weight": 0.1,
        "gender": "m",
        "type2": "poison",
        "moves": [
            247,
            188,
            85,
            194
        ],
        "type1": "ghost",
        "ability": "Levitate"
    },
    "93": {
        "stats": {
            "hp": 237,
            "atk": 127,
            "sdf": 152,
            "spd": 255,
            "def": 132,
            "sat": 272
        },
        "name": "Haunter",
        "weight": 0.1,
        "gender": "f",
        "type2": "poison",
        "moves": [
            101,
            138,
            174,
            95
        ],
        "type1": "ghost",
        "ability": "Levitate"
    },
    "94": {
        "stats": {
            "hp": 258,
            "atk": 200,
            "sdf": 164,
            "spd": 253,
            "def": 153,
            "sat": 267
        },
        "name": "Gengar",
        "weight": 40.5,
        "gender": "f",
        "type2": "poison",
        "moves": [
            399,
            101,
            269,
            120
        ],
        "type1": "ghost",
        "ability": "Levitate"
    },
    "95": {
        "stats": {
            "hp": 209,
            "atk": 193,
            "sdf": 124,
            "spd": 184,
            "def": 364,
            "sat": 74
        },
        "name": "Onix",
        "weight": 210,
        "gender": "m",
        "type2": "ground",
        "moves": [
            89,
            444,
            103,
            397
        ],
        "type1": "rock",
        "ability": "Sturdy"
    },
    "96": {
        "stats": {
            "hp": 274,
            "atk": 124,
            "sdf": 229,
            "spd": 100,
            "def": 152,
            "sat": 177
        },
        "name": "Drowzee",
        "weight": 32.4,
        "gender": "m",
        "moves": [
            247,
            138,
            69,
            95
        ],
        "type1": "psychic",
        "ability": "Insomnia"
    },
    "97": {
        "stats": {
            "hp": 317,
            "atk": 144,
            "sdf": 272,
            "spd": 176,
            "def": 216,
            "sat": 160
        },
        "name": "Hypno",
        "weight": 75.6,
        "gender": "f",
        "moves": [
            149,
            171,
            95,
            274
        ],
        "type1": "psychic",
        "ability": "Insomnia"
    },
    "98": {
        "stats": {
            "hp": 257,
            "atk": 239,
            "sdf": 156,
            "spd": 130,
            "def": 209,
            "sat": 71
        },
        "name": "Krabby",
        "weight": 6.5,
        "gender": "m",
        "moves": [
            152,
            12,
            133,
            334
        ],
        "type1": "water",
        "ability": "Shell Armor"
    },
    "99": {
        "stats": {
            "hp": 250,
            "atk": 295,
            "sdf": 135,
            "spd": 185,
            "def": 291,
            "sat": 121
        },
        "name": "Kingler",
        "weight": 60,
        "gender": "f",
        "moves": [
            152,
            280,
            11,
            321
        ],
        "type1": "water",
        "ability": "Hyper Cutter"
    },
    "100": {
        "stats": {
            "hp": 234,
            "atk": 96,
            "sdf": 138,
            "spd": 297,
            "def": 115,
            "sat": 209
        },
        "name": "Voltorb",
        "weight": 10.4,
        "gender": "-",
        "moves": [
            87,
            113,
            240,
            153
        ],
        "type1": "electric",
        "ability": "Aftermath"
    },
    "101": {
        "stats": {
            "hp": 260,
            "atk": 160,
            "sdf": 195,
            "spd": 323,
            "def": 175,
            "sat": 195
        },
        "name": "Electrode",
        "weight": 66.6,
        "gender": "-",
        "moves": [
            87,
            103,
            268,
            120
        ],
        "type1": "electric",
        "ability": "Soundproof"
    },
    "102": {
        "stats": {
            "hp": 324,
            "atk": 116,
            "sdf": 184,
            "spd": 116,
            "def": 218,
            "sat": 140
        },
        "name": "Exeggcute",
        "weight": 2.5,
        "gender": "m",
        "type2": "psychic",
        "moves": [
            202,
            138,
            73,
            79
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "103": {
        "stats": {
            "hp": 326,
            "atk": 221,
            "sdf": 177,
            "spd": 141,
            "def": 201,
            "sat": 252
        },
        "name": "Exeggutor",
        "weight": 120,
        "gender": "f",
        "type2": "psychic",
        "moves": [
            452,
            94,
            121,
            275
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "104": {
        "stats": {
            "hp": 240,
            "atk": 180,
            "sdf": 165,
            "spd": 108,
            "def": 225,
            "sat": 130
        },
        "name": "Cubone",
        "weight": 6.5,
        "gender": "m",
        "moves": [
            155,
            196,
            195,
            69
        ],
        "type1": "ground",
        "ability": "Battle Armor"
    },
    "105": {
        "stats": {
            "hp": 289,
            "atk": 252,
            "sdf": 231,
            "spd": 140,
            "def": 270,
            "sat": 122
        },
        "name": "Marowak",
        "weight": 45,
        "gender": "f",
        "moves": [
            125,
            36,
            66,
            45
        ],
        "type1": "ground",
        "ability": "Rock Head"
    },
    "106": {
        "stats": {
            "hp": 242,
            "atk": 249,
            "sdf": 257,
            "spd": 211,
            "def": 143,
            "sat": 117
        },
        "name": "Hitmonlee",
        "weight": 49.8,
        "gender": "m",
        "moves": [
            136,
            410,
            299,
            364
        ],
        "type1": "fighting",
        "ability": "Limber"
    },
    "107": {
        "stats": {
            "hp": 242,
            "atk": 247,
            "sdf": 231,
            "spd": 189,
            "def": 214,
            "sat": 107
        },
        "name": "Hitmonchan",
        "weight": 50.2,
        "gender": "m",
        "moves": [
            183,
            8,
            4,
            68
        ],
        "type1": "fighting",
        "ability": "Iron Fist"
    },
    "108": {
        "stats": {
            "hp": 329,
            "atk": 229,
            "sdf": 173,
            "spd": 124,
            "def": 173,
            "sat": 143
        },
        "name": "Lickitung",
        "weight": 65.5,
        "gender": "m",
        "moves": [
            25,
            438,
            359,
            122
        ],
        "type1": "normal",
        "ability": "Cloud Nine"
    },
    "109": {
        "stats": {
            "hp": 254,
            "atk": 157,
            "sdf": 174,
            "spd": 87,
            "def": 238,
            "sat": 168
        },
        "name": "Koffing",
        "weight": 1,
        "gender": "f",
        "moves": [
            188,
            126,
            220,
            261
        ],
        "type1": "poison",
        "ability": "Levitate"
    },
    "110": {
        "stats": {
            "hp": 269,
            "atk": 214,
            "sdf": 174,
            "spd": 154,
            "def": 274,
            "sat": 204
        },
        "name": "Weezing",
        "weight": 9.5,
        "gender": "f",
        "moves": [
            188,
            87,
            399,
            120
        ],
        "type1": "poison",
        "ability": "Levitate"
    },
    "111": {
        "stats": {
            "hp": 322,
            "atk": 227,
            "sdf": 174,
            "spd": 86,
            "def": 247,
            "sat": 86
        },
        "name": "Rhyhorn",
        "weight": 115,
        "gender": "f",
        "type2": "rock",
        "moves": [
            89,
            444,
            66,
            46
        ],
        "type1": "ground",
        "ability": "Reckless"
    },
    "112": {
        "stats": {
            "hp": 373,
            "atk": 266,
            "sdf": 147,
            "spd": 137,
            "def": 276,
            "sat": 207
        },
        "name": "Rhydon",
        "weight": 120,
        "gender": "m",
        "type2": "rock",
        "moves": [
            350,
            224,
            126,
            57
        ],
        "type1": "ground",
        "ability": "Lightning Rod"
    },
    "113": {
        "stats": {
            "hp": 641,
            "atk": 46,
            "sdf": 246,
            "spd": 157,
            "def": 109,
            "sat": 148
        },
        "name": "Chansey",
        "weight": 34.6,
        "gender": "f",
        "moves": [
            58,
            426,
            451,
            47
        ],
        "type1": "normal",
        "ability": "Serene Grace"
    },
    "114": {
        "stats": {
            "hp": 274,
            "atk": 115,
            "sdf": 140,
            "spd": 159,
            "def": 295,
            "sat": 239
        },
        "name": "Tangela",
        "weight": 35,
        "gender": "f",
        "moves": [
            72,
            79,
            74,
            164
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "115": {
        "stats": {
            "hp": 349,
            "atk": 224,
            "sdf": 194,
            "spd": 192,
            "def": 194,
            "sat": 125
        },
        "name": "Kangaskhan",
        "weight": 80,
        "gender": "f",
        "moves": [
            252,
            146,
            200,
            179
        ],
        "type1": "normal",
        "ability": "Scrappy"
    },
    "116": {
        "stats": {
            "hp": 218,
            "atk": 119,
            "sdf": 103,
            "spd": 173,
            "def": 193,
            "sat": 212
        },
        "name": "Horsea",
        "weight": 8,
        "gender": "m",
        "moves": [
            56,
            58,
            108,
            240
        ],
        "type1": "water",
        "ability": "Swift Swim"
    },
    "117": {
        "stats": {
            "hp": 254,
            "atk": 169,
            "sdf": 129,
            "spd": 229,
            "def": 206,
            "sat": 229
        },
        "name": "Seadra",
        "weight": 25,
        "gender": "f",
        "moves": [
            330,
            225,
            92,
            108
        ],
        "type1": "water",
        "ability": "Sniper"
    },
    "118": {
        "stats": {
            "hp": 245,
            "atk": 202,
            "sdf": 150,
            "spd": 176,
            "def": 170,
            "sat": 108
        },
        "name": "Goldeen",
        "weight": 15,
        "gender": "f",
        "moves": [
            127,
            224,
            32,
            240
        ],
        "type1": "water",
        "ability": "Swift Swim"
    },
    "119": {
        "stats": {
            "hp": 303,
            "atk": 222,
            "sdf": 198,
            "spd": 147,
            "def": 168,
            "sat": 195
        },
        "name": "Seaking",
        "weight": 39,
        "gender": "f",
        "moves": [
            56,
            398,
            32,
            97
        ],
        "type1": "water",
        "ability": "Lightning Rod"
    },
    "120": {
        "stats": {
            "hp": 201,
            "atk": 113,
            "sdf": 183,
            "spd": 238,
            "def": 183,
            "sat": 218
        },
        "name": "Staryu",
        "weight": 34.5,
        "gender": "-",
        "moves": [
            56,
            87,
            94,
            220
        ],
        "type1": "water",
        "ability": "Illuminate"
    },
    "121": {
        "stats": {
            "hp": 256,
            "atk": 181,
            "sdf": 201,
            "spd": 261,
            "def": 221,
            "sat": 207
        },
        "name": "Starmie",
        "weight": 80,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            94,
            352,
            408,
            293
        ],
        "type1": "water",
        "ability": "Natural Cure"
    },
    "122": {
        "stats": {
            "hp": 222,
            "atk": 114,
            "sdf": 277,
            "spd": 217,
            "def": 183,
            "sat": 237
        },
        "name": "Mr. Mime",
        "weight": 54.5,
        "gender": "m",
        "moves": [
            60,
            411,
            345,
            115
        ],
        "type1": "psychic",
        "ability": "Filter"
    },
    "123": {
        "stats": {
            "hp": 278,
            "atk": 253,
            "sdf": 193,
            "spd": 243,
            "def": 193,
            "sat": 143
        },
        "name": "Scyther",
        "weight": 56,
        "gender": "f",
        "type2": "flying",
        "moves": [
            404,
            17,
            206,
            116
        ],
        "type1": "bug",
        "ability": "Technician"
    },
    "124": {
        "stats": {
            "hp": 272,
            "atk": 137,
            "sdf": 227,
            "spd": 249,
            "def": 107,
            "sat": 240
        },
        "name": "Jynx",
        "weight": 40.6,
        "gender": "f",
        "type2": "psychic",
        "moves": [
            94,
            196,
            122,
            186
        ],
        "type1": "ice",
        "ability": "Dry Skin"
    },
    "125": {
        "stats": {
            "hp": 269,
            "atk": 200,
            "sdf": 183,
            "spd": 268,
            "def": 148,
            "sat": 224
        },
        "name": "Electabuzz",
        "weight": 30,
        "gender": "f",
        "moves": [
            9,
            223,
            8,
            86
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "126": {
        "stats": {
            "hp": 269,
            "atk": 201,
            "sdf": 204,
            "spd": 242,
            "def": 148,
            "sat": 234
        },
        "name": "Magmar",
        "weight": 44.5,
        "gender": "f",
        "moves": [
            53,
            411,
            108,
            109
        ],
        "type1": "fire",
        "ability": "Flame Body"
    },
    "127": {
        "stats": {
            "hp": 268,
            "atk": 254,
            "sdf": 173,
            "spd": 203,
            "def": 256,
            "sat": 143
        },
        "name": "Pinsir",
        "weight": 55,
        "gender": "f",
        "moves": [
            404,
            233,
            88,
            12
        ],
        "type1": "bug",
        "ability": "Mold Breaker"
    },
    "128": {
        "stats": {
            "hp": 289,
            "atk": 257,
            "sdf": 174,
            "spd": 254,
            "def": 224,
            "sat": 102
        },
        "name": "Tauros",
        "weight": 88.4,
        "gender": "m",
        "moves": [
            30,
            428,
            157,
            203
        ],
        "type1": "normal",
        "ability": "Anger Point"
    },
    "129": {
        "stats": {
            "hp": 181,
            "atk": 50,
            "sdf": 76,
            "spd": 259,
            "def": 146,
            "sat": 141
        },
        "name": "Magikarp",
        "weight": 10,
        "gender": "m",
        "moves": [
            150,
            56,
            340,
            82
        ],
        "type1": "water",
        "ability": "Swift Swim"
    },
    "130": {
        "stats": {
            "hp": 300,
            "atk": 229,
            "sdf": 205,
            "spd": 179,
            "def": 163,
            "sat": 240
        },
        "name": "Gyarados",
        "weight": 235,
        "gender": "f",
        "type2": "flying",
        "moves": [
            401,
            63,
            239,
            269
        ],
        "type1": "water",
        "ability": "Intimidate"
    },
    "131": {
        "stats": {
            "hp": 395,
            "atk": 220,
            "sdf": 220,
            "spd": 150,
            "def": 190,
            "sat": 180
        },
        "name": "Lapras",
        "weight": 220,
        "gender": "f",
        "type2": "ice",
        "moves": [
            57,
            419,
            70,
            445
        ],
        "type1": "water",
        "ability": "Shell Armor"
    },
    "132": {
        "stats": {
            "hp": 296,
            "atk": 115,
            "sdf": 128,
            "spd": 210,
            "def": 128,
            "sat": 128
        },
        "name": "Ditto",
        "weight": 4,
        "gender": "-",
        "item": "Quick Powder",
        "moves": [
            144
        ],
        "type1": "normal",
        "ability": "Limber"
    },
    "133": {
        "stats": {
            "hp": 298,
            "atk": 209,
            "sdf": 166,
            "spd": 160,
            "def": 153,
            "sat": 113
        },
        "name": "Eevee",
        "weight": 6.5,
        "gender": "m",
        "moves": [
            36,
            231,
            98,
            174
        ],
        "type1": "normal",
        "ability": "Adaptability"
    },
    "134": {
        "stats": {
            "hp": 370,
            "atk": 135,
            "sdf": 195,
            "spd": 135,
            "def": 125,
            "sat": 225
        },
        "name": "Vaporeon",
        "weight": 29,
        "gender": "f",
        "moves": [
            330,
            247,
            313,
            151
        ],
        "type1": "water",
        "ability": "Water Absorb"
    },
    "135": {
        "stats": {
            "hp": 266,
            "atk": 161,
            "sdf": 221,
            "spd": 291,
            "def": 151,
            "sat": 251
        },
        "name": "Jolteon",
        "weight": 24.5,
        "gender": "m",
        "moves": [
            435,
            387,
            28,
            321
        ],
        "type1": "electric",
        "ability": "Volt Absorb"
    },
    "136": {
        "stats": {
            "hp": 266,
            "atk": 291,
            "sdf": 251,
            "spd": 161,
            "def": 166,
            "sat": 198
        },
        "name": "Flareon",
        "weight": 25,
        "gender": "m",
        "moves": [
            424,
            36,
            39,
            261
        ],
        "type1": "fire",
        "ability": "Flash Fire"
    },
    "137": {
        "stats": {
            "hp": 240,
            "atk": 156,
            "sdf": 249,
            "spd": 76,
            "def": 262,
            "sat": 206
        },
        "name": "Porygon",
        "weight": 36.5,
        "gender": "-",
        "moves": [
            161,
            231,
            176,
            220
        ],
        "type1": "normal",
        "ability": "Download"
    },
    "138": {
        "stats": {
            "hp": 230,
            "atk": 116,
            "sdf": 182,
            "spd": 145,
            "def": 245,
            "sat": 239
        },
        "name": "Omanyte",
        "weight": 7.5,
        "gender": "m",
        "type2": "water",
        "moves": [
            57,
            246,
            58,
            240
        ],
        "type1": "rock",
        "ability": "Swift Swim"
    },
    "139": {
        "stats": {
            "hp": 279,
            "atk": 154,
            "sdf": 174,
            "spd": 144,
            "def": 284,
            "sat": 264
        },
        "name": "Omastar",
        "weight": 35,
        "gender": "m",
        "type2": "water",
        "moves": [
            330,
            246,
            341,
            445
        ],
        "type1": "rock",
        "ability": "Shell Armor"
    },
    "140": {
        "stats": {
            "hp": 243,
            "atk": 238,
            "sdf": 184,
            "spd": 146,
            "def": 216,
            "sat": 131
        },
        "name": "Kabuto",
        "weight": 11.5,
        "gender": "m",
        "type2": "water",
        "moves": [
            127,
            157,
            453,
            109
        ],
        "type1": "rock",
        "ability": "Battle Armor"
    },
    "141": {
        "stats": {
            "hp": 274,
            "atk": 237,
            "sdf": 193,
            "spd": 194,
            "def": 244,
            "sat": 198
        },
        "name": "Kabutops",
        "weight": 40.5,
        "gender": "f",
        "type2": "water",
        "moves": [
            401,
            246,
            404,
            453
        ],
        "type1": "rock",
        "ability": "Battle Armor"
    },
    "142": {
        "stats": {
            "hp": 297,
            "atk": 242,
            "sdf": 182,
            "spd": 292,
            "def": 162,
            "sat": 152
        },
        "name": "Aerodactyl",
        "weight": 59,
        "gender": "f",
        "type2": "flying",
        "moves": [
            157,
            332,
            48,
            446
        ],
        "type1": "rock",
        "ability": "Pressure"
    },
    "143": {
        "stats": {
            "hp": 454,
            "atk": 350,
            "sdf": 249,
            "spd": 97,
            "def": 159,
            "sat": 149
        },
        "name": "Snorlax",
        "weight": 460,
        "gender": "f",
        "moves": [
            6,
            249,
            122,
            174
        ],
        "type1": "normal",
        "ability": "Thick Fat"
    },
    "144": {
        "stats": {
            "hp": 311,
            "atk": 196,
            "sdf": 276,
            "spd": 196,
            "def": 226,
            "sat": 216
        },
        "name": "Articuno",
        "weight": 55.4,
        "gender": "-",
        "type2": "flying",
        "moves": [
            59,
            365,
            246,
            54
        ],
        "type1": "ice",
        "ability": "Pressure"
    },
    "145": {
        "stats": {
            "hp": 290,
            "atk": 272,
            "sdf": 185,
            "spd": 238,
            "def": 175,
            "sat": 229
        },
        "name": "Zapdos",
        "weight": 52.6,
        "gender": "-",
        "type2": "flying",
        "moves": [
            87,
            64,
            249,
            197
        ],
        "type1": "electric",
        "ability": "Pressure"
    },
    "146": {
        "stats": {
            "hp": 311,
            "atk": 248,
            "sdf": 196,
            "spd": 206,
            "def": 206,
            "sat": 248
        },
        "name": "Moltres",
        "weight": 60,
        "gender": "-",
        "type2": "flying",
        "moves": [
            126,
            17,
            211,
            97
        ],
        "type1": "fire",
        "ability": "Pressure"
    },
    "147": {
        "stats": {
            "hp": 265,
            "atk": 203,
            "sdf": 141,
            "spd": 157,
            "def": 147,
            "sat": 136
        },
        "name": "Dratini",
        "weight": 3.3,
        "gender": "f",
        "moves": [
            200,
            245,
            127,
            349
        ],
        "type1": "dragon",
        "ability": "Shed Skin"
    },
    "148": {
        "stats": {
            "hp": 268,
            "atk": 188,
            "sdf": 181,
            "spd": 181,
            "def": 188,
            "sat": 181
        },
        "name": "Dragonair",
        "weight": 16.5,
        "gender": "m",
        "moves": [
            434,
            126,
            245,
            219
        ],
        "type1": "dragon",
        "ability": "Shed Skin"
    },
    "149": {
        "stats": {
            "hp": 292,
            "atk": 245,
            "sdf": 205,
            "spd": 165,
            "def": 195,
            "sat": 225
        },
        "name": "Dragonite",
        "weight": 210,
        "gender": "f",
        "type2": "flying",
        "moves": [
            407,
            192,
            57,
            432
        ],
        "type1": "dragon",
        "ability": "Inner Focus"
    },
    "150": {
        "stats": {
            "hp": 334,
            "atk": 237,
            "sdf": 197,
            "spd": 277,
            "def": 197,
            "sat": 325
        },
        "name": "Mewtwo",
        "weight": 122,
        "gender": "-",
        "moves": [
            427,
            382,
            50,
            357
        ],
        "type1": "psychic",
        "ability": "Pressure"
    },
    "151": {
        "stats": {
            "hp": 330,
            "atk": 225,
            "sdf": 225,
            "spd": 225,
            "def": 225,
            "sat": 225
        },
        "name": "Mew",
        "weight": 4,
        "gender": "-",
        "moves": [
            94,
            382,
            144,
            118
        ],
        "type1": "psychic",
        "ability": "Synchronize"
    },
    "152": {
        "stats": {
            "hp": 294,
            "atk": 120,
            "sdf": 251,
            "spd": 126,
            "def": 167,
            "sat": 134
        },
        "name": "Chikorita",
        "weight": 6.4,
        "gender": "m",
        "moves": [
            412,
            73,
            68,
            113
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "153": {
        "stats": {
            "hp": 300,
            "atk": 200,
            "sdf": 218,
            "spd": 178,
            "def": 218,
            "sat": 145
        },
        "name": "Bayleef",
        "weight": 15.8,
        "gender": "f",
        "moves": [
            402,
            34,
            267,
            14
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "154": {
        "stats": {
            "hp": 296,
            "atk": 214,
            "sdf": 231,
            "spd": 171,
            "def": 231,
            "sat": 197
        },
        "name": "Meganium",
        "weight": 100.5,
        "gender": "m",
        "moves": [
            338,
            231,
            200,
            230
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "155": {
        "stats": {
            "hp": 241,
            "atk": 126,
            "sdf": 157,
            "spd": 229,
            "def": 122,
            "sat": 194
        },
        "name": "Cyndaquil",
        "weight": 7.9,
        "gender": "m",
        "moves": [
            284,
            307,
            53,
            261
        ],
        "type1": "fire",
        "ability": "Blaze"
    },
    "156": {
        "stats": {
            "hp": 282,
            "atk": 189,
            "sdf": 193,
            "spd": 221,
            "def": 193,
            "sat": 176
        },
        "name": "Quilava",
        "weight": 19,
        "gender": "f",
        "moves": [
            394,
            179,
            203,
            336
        ],
        "type1": "fire",
        "ability": "Blaze"
    },
    "157": {
        "stats": {
            "hp": 295,
            "atk": 202,
            "sdf": 224,
            "spd": 234,
            "def": 190,
            "sat": 204
        },
        "name": "Typhlosion",
        "weight": 79.5,
        "gender": "f",
        "moves": [
            172,
            306,
            9,
            67
        ],
        "type1": "fire",
        "ability": "Blaze"
    },
    "158": {
        "stats": {
            "hp": 266,
            "atk": 212,
            "sdf": 157,
            "spd": 147,
            "def": 189,
            "sat": 111
        },
        "name": "Totodile",
        "weight": 9.5,
        "gender": "m",
        "moves": [
            127,
            8,
            14,
            349
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "159": {
        "stats": {
            "hp": 277,
            "atk": 202,
            "sdf": 168,
            "spd": 173,
            "def": 202,
            "sat": 144
        },
        "name": "Croconaw",
        "weight": 25,
        "gender": "f",
        "moves": [
            291,
            163,
            423,
            103
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "160": {
        "stats": {
            "hp": 305,
            "atk": 216,
            "sdf": 215,
            "spd": 186,
            "def": 230,
            "sat": 188
        },
        "name": "Feraligatr",
        "weight": 88.8,
        "gender": "m",
        "moves": [
            401,
            223,
            58,
            43
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "161": {
        "stats": {
            "hp": 274,
            "atk": 140,
            "sdf": 127,
            "spd": 76,
            "def": 167,
            "sat": 95
        },
        "name": "Sentret",
        "weight": 6,
        "gender": "m",
        "moves": [
            38,
            401,
            389,
            179
        ],
        "type1": "normal",
        "ability": "Keen Eye"
    },
    "162": {
        "stats": {
            "hp": 300,
            "atk": 193,
            "sdf": 135,
            "spd": 225,
            "def": 154,
            "sat": 172
        },
        "name": "Furret",
        "weight": 32.5,
        "gender": "f",
        "moves": [
            29,
            8,
            9,
            382
        ],
        "type1": "normal",
        "ability": "Keen Eye"
    },
    "163": {
        "stats": {
            "hp": 262,
            "atk": 86,
            "sdf": 148,
            "spd": 218,
            "def": 96,
            "sat": 171
        },
        "name": "Hoothoot",
        "weight": 21.2,
        "gender": "m",
        "type2": "flying",
        "moves": [
            403,
            97,
            95,
            18
        ],
        "type1": "normal",
        "ability": "Tinted Lens"
    },
    "164": {
        "stats": {
            "hp": 344,
            "atk": 125,
            "sdf": 231,
            "spd": 196,
            "def": 139,
            "sat": 191
        },
        "name": "Noctowl",
        "weight": 40.8,
        "gender": "f",
        "type2": "flying",
        "moves": [
            314,
            63,
            138,
            95
        ],
        "type1": "normal",
        "ability": "Tinted Lens"
    },
    "165": {
        "stats": {
            "hp": 220,
            "atk": 66,
            "sdf": 194,
            "spd": 227,
            "def": 94,
            "sat": 177
        },
        "name": "Ledyba",
        "weight": 10.8,
        "gender": "m",
        "type2": "flying",
        "moves": [
            405,
            314,
            113,
            115
        ],
        "type1": "bug",
        "ability": "Swarm"
    },
    "166": {
        "stats": {
            "hp": 283,
            "atk": 185,
            "sdf": 256,
            "spd": 206,
            "def": 168,
            "sat": 131
        },
        "name": "Ledian",
        "weight": 35.6,
        "gender": "m",
        "type2": "flying",
        "moves": [
            332,
            409,
            8,
            9
        ],
        "type1": "bug",
        "ability": "Iron Fist"
    },
    "167": {
        "stats": {
            "hp": 284,
            "atk": 189,
            "sdf": 140,
            "spd": 96,
            "def": 140,
            "sat": 104
        },
        "name": "Spinarak",
        "weight": 8.5,
        "gender": "m",
        "type2": "poison",
        "moves": [
            224,
            400,
            389,
            101
        ],
        "type1": "bug",
        "ability": "Sniper"
    },
    "168": {
        "stats": {
            "hp": 289,
            "atk": 246,
            "sdf": 175,
            "spd": 124,
            "def": 175,
            "sat": 143
        },
        "name": "Ariados",
        "weight": 33.5,
        "gender": "m",
        "type2": "poison",
        "moves": [
            398,
            450,
            91,
            97
        ],
        "type1": "bug",
        "ability": "Swarm"
    },
    "169": {
        "stats": {
            "hp": 305,
            "atk": 210,
            "sdf": 190,
            "spd": 290,
            "def": 190,
            "sat": 170
        },
        "name": "Crobat",
        "weight": 75,
        "gender": "f",
        "type2": "flying",
        "moves": [
            19,
            305,
            211,
            48
        ],
        "type1": "poison",
        "ability": "Inner Focus"
    },
    "170": {
        "stats": {
            "hp": 322,
            "atk": 100,
            "sdf": 185,
            "spd": 202,
            "def": 150,
            "sat": 153
        },
        "name": "Chinchou",
        "weight": 12,
        "gender": "m",
        "type2": "electric",
        "moves": [
            87,
            57,
            196,
            240
        ],
        "type1": "water",
        "ability": "Water Absorb"
    },
    "171": {
        "stats": {
            "hp": 392,
            "atk": 168,
            "sdf": 189,
            "spd": 171,
            "def": 137,
            "sat": 189
        },
        "name": "Lanturn",
        "weight": 22.5,
        "gender": "f",
        "type2": "electric",
        "moves": [
            61,
            209,
            340,
            268
        ],
        "type1": "water",
        "ability": "Volt Absorb"
    },
    "172": {
        "stats": {
            "hp": 181,
            "atk": 179,
            "sdf": 107,
            "spd": 240,
            "def": 66,
            "sat": 95
        },
        "name": "Pichu",
        "weight": 2,
        "gender": "m",
        "moves": [
            344,
            179,
            298,
            164
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "173": {
        "stats": {
            "hp": 297,
            "atk": 77,
            "sdf": 167,
            "spd": 70,
            "def": 153,
            "sat": 126
        },
        "name": "Cleffa",
        "weight": 3,
        "gender": "m",
        "moves": [
            69,
            247,
            86,
            207
        ],
        "type1": "normal",
        "ability": "Cute Charm"
    },
    "174": {
        "stats": {
            "hp": 384,
            "atk": 86,
            "sdf": 139,
            "spd": 66,
            "def": 72,
            "sat": 117
        },
        "name": "Igglybuff",
        "weight": 1,
        "gender": "m",
        "moves": [
            69,
            247,
            68,
            186
        ],
        "type1": "normal",
        "ability": "Cute Charm"
    },
    "175": {
        "stats": {
            "hp": 274,
            "atk": 68,
            "sdf": 207,
            "spd": 76,
            "def": 207,
            "sat": 116
        },
        "name": "Togepi",
        "weight": 1.5,
        "gender": "m",
        "moves": [
            69,
            281,
            193,
            135
        ],
        "type1": "normal",
        "ability": "Super Luck"
    },
    "176": {
        "stats": {
            "hp": 257,
            "atk": 122,
            "sdf": 252,
            "spd": 122,
            "def": 212,
            "sat": 202
        },
        "name": "Togetic",
        "weight": 3.2,
        "gender": "f",
        "type2": "flying",
        "moves": [
            161,
            314,
            246,
            118
        ],
        "type1": "normal",
        "ability": "Serene Grace"
    },
    "177": {
        "stats": {
            "hp": 284,
            "atk": 122,
            "sdf": 126,
            "spd": 239,
            "def": 126,
            "sat": 198
        },
        "name": "Natu",
        "weight": 2,
        "gender": "m",
        "type2": "flying",
        "moves": [
            94,
            101,
            109,
            273
        ],
        "type1": "psychic",
        "ability": "Synchronize"
    },
    "178": {
        "stats": {
            "hp": 271,
            "atk": 186,
            "sdf": 176,
            "spd": 226,
            "def": 193,
            "sat": 203
        },
        "name": "Xatu",
        "weight": 15,
        "gender": "f",
        "type2": "flying",
        "moves": [
            65,
            94,
            202,
            375
        ],
        "type1": "psychic",
        "ability": "Early Bird"
    },
    "179": {
        "stats": {
            "hp": 277,
            "atk": 101,
            "sdf": 141,
            "spd": 103,
            "def": 130,
            "sat": 248
        },
        "name": "Mareep",
        "weight": 7.8,
        "gender": "m",
        "moves": [
            85,
            324,
            86,
            115
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "180": {
        "stats": {
            "hp": 281,
            "atk": 229,
            "sdf": 188,
            "spd": 126,
            "def": 178,
            "sat": 176
        },
        "name": "Flaaffy",
        "weight": 13.3,
        "gender": "f",
        "moves": [
            9,
            264,
            7,
            260
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "181": {
        "stats": {
            "hp": 330,
            "atk": 195,
            "sdf": 247,
            "spd": 155,
            "def": 175,
            "sat": 247
        },
        "name": "Ampharos",
        "weight": 61.5,
        "gender": "f",
        "moves": [
            192,
            223,
            129,
            148
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "182": {
        "stats": {
            "hp": 290,
            "atk": 195,
            "sdf": 246,
            "spd": 102,
            "def": 216,
            "sat": 236
        },
        "name": "Bellossom",
        "weight": 5.8,
        "gender": "f",
        "moves": [
            80,
            290,
            409,
            298
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "183": {
        "stats": {
            "hp": 302,
            "atk": 152,
            "sdf": 157,
            "spd": 116,
            "def": 157,
            "sat": 68
        },
        "name": "Marill",
        "weight": 8.5,
        "gender": "m",
        "moves": [
            127,
            34,
            205,
            111
        ],
        "type1": "water",
        "ability": "Huge Power"
    },
    "184": {
        "stats": {
            "hp": 319,
            "atk": 120,
            "sdf": 183,
            "spd": 147,
            "def": 183,
            "sat": 176
        },
        "name": "Azumarill",
        "weight": 28.5,
        "gender": "f",
        "moves": [
            401,
            276,
            205,
            447
        ],
        "type1": "water",
        "ability": "Huge Power"
    },
    "185": {
        "stats": {
            "hp": 287,
            "atk": 242,
            "sdf": 172,
            "spd": 102,
            "def": 272,
            "sat": 102
        },
        "name": "Sudowoodo",
        "weight": 38,
        "gender": "f",
        "moves": [
            444,
            452,
            359,
            383
        ],
        "type1": "rock",
        "ability": "Rock Head"
    },
    "186": {
        "stats": {
            "hp": 318,
            "atk": 164,
            "sdf": 233,
            "spd": 173,
            "def": 201,
            "sat": 213
        },
        "name": "Politoed",
        "weight": 33.9,
        "gender": "f",
        "moves": [
            352,
            304,
            341,
            195
        ],
        "type1": "water",
        "ability": "Drizzle"
    },
    "187": {
        "stats": {
            "hp": 274,
            "atk": 95,
            "sdf": 181,
            "spd": 150,
            "def": 147,
            "sat": 106
        },
        "name": "Hoppip",
        "weight": 0.5,
        "gender": "m",
        "type2": "flying",
        "moves": [
            76,
            92,
            241,
            235
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "188": {
        "stats": {
            "hp": 243,
            "atk": 198,
            "sdf": 157,
            "spd": 250,
            "def": 127,
            "sat": 105
        },
        "name": "Skiploom",
        "weight": 1,
        "gender": "f",
        "type2": "flying",
        "moves": [
            340,
            402,
            79,
            262
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "189": {
        "stats": {
            "hp": 293,
            "atk": 185,
            "sdf": 208,
            "spd": 258,
            "def": 178,
            "sat": 114
        },
        "name": "Jumpluff",
        "weight": 3,
        "gender": "m",
        "type2": "flying",
        "moves": [
            340,
            29,
            73,
            77
        ],
        "type1": "grass",
        "ability": "Leaf Guard"
    },
    "190": {
        "stats": {
            "hp": 273,
            "atk": 239,
            "sdf": 167,
            "spd": 227,
            "def": 146,
            "sat": 116
        },
        "name": "Aipom",
        "weight": 11.5,
        "gender": "m",
        "moves": [
            3,
            280,
            421,
            321
        ],
        "type1": "normal",
        "ability": "Skill Link"
    },
    "191": {
        "stats": {
            "hp": 201,
            "atk": 86,
            "sdf": 128,
            "spd": 174,
            "def": 128,
            "sat": 96
        },
        "name": "Sunkern",
        "weight": 1.8,
        "gender": "m",
        "moves": [
            412,
            73,
            164,
            320
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "192": {
        "stats": {
            "hp": 312,
            "atk": 186,
            "sdf": 249,
            "spd": 117,
            "def": 167,
            "sat": 267
        },
        "name": "Sunflora",
        "weight": 8.5,
        "gender": "f",
        "moves": [
            202,
            414,
            416,
            117
        ],
        "type1": "grass",
        "ability": "Early Bird"
    },
    "193": {
        "stats": {
            "hp": 279,
            "atk": 174,
            "sdf": 134,
            "spd": 234,
            "def": 147,
            "sat": 174
        },
        "name": "Yanma",
        "weight": 38,
        "gender": "m",
        "type2": "flying",
        "moves": [
            405,
            403,
            95,
            197
        ],
        "type1": "bug",
        "ability": "Speed Boost"
    },
    "194": {
        "stats": {
            "hp": 272,
            "atk": 207,
            "sdf": 118,
            "spd": 66,
            "def": 137,
            "sat": 77
        },
        "name": "Wooper",
        "weight": 8.5,
        "gender": "m",
        "type2": "ground",
        "moves": [
            89,
            401,
            281,
            182
        ],
        "type1": "water",
        "ability": "Unaware"
    },
    "195": {
        "stats": {
            "hp": 335,
            "atk": 210,
            "sdf": 170,
            "spd": 110,
            "def": 210,
            "sat": 170
        },
        "name": "Quagsire",
        "weight": 75,
        "gender": "m",
        "type2": "ground",
        "moves": [
            330,
            91,
            58,
            133
        ],
        "type1": "water",
        "ability": "Damp"
    },
    "196": {
        "stats": {
            "hp": 266,
            "atk": 161,
            "sdf": 221,
            "spd": 251,
            "def": 166,
            "sat": 261
        },
        "name": "Espeon",
        "weight": 26.5,
        "gender": "m",
        "moves": [
            60,
            129,
            213,
            28
        ],
        "type1": "psychic",
        "ability": "Synchronize"
    },
    "197": {
        "stats": {
            "hp": 320,
            "atk": 192,
            "sdf": 285,
            "spd": 121,
            "def": 245,
            "sat": 200
        },
        "name": "Umbreon",
        "weight": 27,
        "gender": "m",
        "moves": [
            372,
            94,
            109,
            289
        ],
        "type1": "dark",
        "ability": "Synchronize"
    },
    "198": {
        "stats": {
            "hp": 267,
            "atk": 212,
            "sdf": 126,
            "spd": 246,
            "def": 113,
            "sat": 212
        },
        "name": "Murkrow",
        "weight": 2.1,
        "gender": "f",
        "type2": "flying",
        "moves": [
            19,
            389,
            257,
            297
        ],
        "type1": "dark",
        "ability": "Insomnia"
    },
    "199": {
        "stats": {
            "hp": 329,
            "atk": 202,
            "sdf": 254,
            "spd": 94,
            "def": 174,
            "sat": 234
        },
        "name": "Slowking",
        "weight": 79.5,
        "gender": "f",
        "type2": "psychic",
        "moves": [
            57,
            93,
            408,
            86
        ],
        "type1": "water",
        "ability": "Oblivious"
    },
    "200": {
        "stats": {
            "hp": 264,
            "atk": 159,
            "sdf": 209,
            "spd": 209,
            "def": 159,
            "sat": 209
        },
        "name": "Misdreavus",
        "weight": 1,
        "gender": "f",
        "moves": [
            247,
            85,
            220,
            195
        ],
        "type1": "ghost",
        "ability": "Levitate"
    },
    "201": {
        "stats": {
            "hp": 244,
            "atk": 154,
            "sdf": 140,
            "spd": 139,
            "def": 140,
            "sat": 258
        },
        "name": "Unown",
        "weight": 5,
        "gender": "-",
        "item": "Choice Specs",
        "moves": [
            237
        ],
        "type1": "psychic",
        "ability": "Levitate"
    },
    "202": {
        "stats": {
            "hp": 521,
            "atk": 134,
            "sdf": 136,
            "spd": 181,
            "def": 136,
            "sat": 134
        },
        "name": "Wobbuffet",
        "weight": 28.5,
        "gender": "f",
        "moves": [
            68,
            243,
            219,
            102
        ],
        "type1": "psychic",
        "ability": "Shadow Tag"
    },
    "203": {
        "stats": {
            "hp": 344,
            "atk": 196,
            "sdf": 198,
            "spd": 206,
            "def": 198,
            "sat": 216
        },
        "name": "Girafarig",
        "weight": 41.5,
        "gender": "f",
        "type2": "psychic",
        "moves": [
            60,
            458,
            24,
            45
        ],
        "type1": "normal",
        "ability": "Early Bird"
    },
    "204": {
        "stats": {
            "hp": 260,
            "atk": 251,
            "sdf": 151,
            "spd": 31,
            "def": 216,
            "sat": 106
        },
        "name": "Pineco",
        "weight": 7.2,
        "gender": "m",
        "moves": [
            360,
            89,
            174,
            153
        ],
        "type1": "bug",
        "ability": "Sturdy"
    },
    "205": {
        "stats": {
            "hp": 323,
            "atk": 185,
            "sdf": 219,
            "spd": 85,
            "def": 316,
            "sat": 125
        },
        "name": "Forretress",
        "weight": 125.8,
        "gender": "f",
        "type2": "steel",
        "moves": [
            42,
            191,
            390,
            120
        ],
        "type1": "bug",
        "ability": "Sturdy"
    },
    "206": {
        "stats": {
            "hp": 346,
            "atk": 181,
            "sdf": 171,
            "spd": 131,
            "def": 181,
            "sat": 171
        },
        "name": "Dunsparce",
        "weight": 14,
        "gender": "m",
        "moves": [
            70,
            91,
            157,
            137
        ],
        "type1": "normal",
        "ability": "Serene Grace"
    },
    "207": {
        "stats": {
            "hp": 334,
            "atk": 139,
            "sdf": 191,
            "spd": 269,
            "def": 246,
            "sat": 106
        },
        "name": "Gligar",
        "weight": 64.8,
        "gender": "m",
        "type2": "flying",
        "moves": [
            91,
            92,
            207,
            259
        ],
        "type1": "ground",
        "ability": "Hyper Cutter"
    },
    "208": {
        "stats": {
            "hp": 287,
            "atk": 181,
            "sdf": 162,
            "spd": 92,
            "def": 411,
            "sat": 179
        },
        "name": "Steelix",
        "weight": 400,
        "gender": "f",
        "type2": "ground",
        "moves": [
            231,
            91,
            401,
            159
        ],
        "type1": "steel",
        "ability": "Sturdy"
    },
    "209": {
        "stats": {
            "hp": 297,
            "atk": 196,
            "sdf": 182,
            "spd": 117,
            "def": 156,
            "sat": 104
        },
        "name": "Snubbull",
        "weight": 7.8,
        "gender": "f",
        "moves": [
            265,
            44,
            213,
            86
        ],
        "type1": "normal",
        "ability": "Intimidate"
    },
    "210": {
        "stats": {
            "hp": 323,
            "atk": 278,
            "sdf": 142,
            "spd": 140,
            "def": 188,
            "sat": 158
        },
        "name": "Granbull",
        "weight": 48.7,
        "gender": "m",
        "moves": [
            263,
            276,
            371,
            214
        ],
        "type1": "normal",
        "ability": "Quick Feet"
    },
    "211": {
        "stats": {
            "hp": 275,
            "atk": 253,
            "sdf": 135,
            "spd": 210,
            "def": 190,
            "sat": 150
        },
        "name": "Qwilfish",
        "weight": 3.9,
        "gender": "m",
        "type2": "poison",
        "moves": [
            127,
            398,
            42,
            107
        ],
        "type1": "water",
        "ability": "Poison Point"
    },
    "212": {
        "stats": {
            "hp": 250,
            "atk": 238,
            "sdf": 165,
            "spd": 148,
            "def": 205,
            "sat": 115
        },
        "name": "Scizor",
        "weight": 118,
        "gender": "f",
        "type2": "steel",
        "moves": [
            404,
            232,
            276,
            97
        ],
        "type1": "bug",
        "ability": "Technician"
    },
    "213": {
        "stats": {
            "hp": 244,
            "atk": 130,
            "sdf": 496,
            "spd": 13,
            "def": 496,
            "sat": 56
        },
        "name": "Shuckle",
        "weight": 20.5,
        "gender": "f",
        "type2": "rock",
        "moves": [
            444,
            360,
            117,
            379
        ],
        "type1": "bug",
        "ability": "Sturdy"
    },
    "214": {
        "stats": {
            "hp": 292,
            "atk": 229,
            "sdf": 216,
            "spd": 175,
            "def": 176,
            "sat": 93
        },
        "name": "Heracross",
        "weight": 54,
        "gender": "f",
        "type2": "fighting",
        "moves": [
            224,
            292,
            43,
            106
        ],
        "type1": "bug",
        "ability": "Swarm"
    },
    "215": {
        "stats": {
            "hp": 255,
            "atk": 253,
            "sdf": 190,
            "spd": 243,
            "def": 150,
            "sat": 110
        },
        "name": "Sneasel",
        "weight": 28,
        "gender": "m",
        "type2": "ice",
        "moves": [
            8,
            44,
            404,
            213
        ],
        "type1": "dark",
        "ability": "Keen Eye"
    },
    "216": {
        "stats": {
            "hp": 286,
            "atk": 221,
            "sdf": 161,
            "spd": 157,
            "def": 161,
            "sat": 122
        },
        "name": "Teddiursa",
        "weight": 8.8,
        "gender": "m",
        "moves": [
            175,
            9,
            281,
            203
        ],
        "type1": "normal",
        "ability": "Quick Feet"
    },
    "217": {
        "stats": {
            "hp": 343,
            "atk": 359,
            "sdf": 207,
            "spd": 160,
            "def": 186,
            "sat": 186
        },
        "name": "Ursaring",
        "weight": 125.8,
        "gender": "f",
        "moves": [
            10,
            122,
            339,
            46
        ],
        "type1": "normal",
        "ability": "Guts"
    },
    "218": {
        "stats": {
            "hp": 238,
            "atk": 104,
            "sdf": 162,
            "spd": 76,
            "def": 162,
            "sat": 212
        },
        "name": "Slugma",
        "weight": 35,
        "gender": "m",
        "moves": [
            53,
            281,
            182,
            105
        ],
        "type1": "fire",
        "ability": "Magma Armor"
    },
    "219": {
        "stats": {
            "hp": 247,
            "atk": 108,
            "sdf": 245,
            "spd": 81,
            "def": 283,
            "sat": 223
        },
        "name": "Magcargo",
        "weight": 55,
        "gender": "f",
        "type2": "rock",
        "moves": [
            126,
            246,
            414,
            262
        ],
        "type1": "fire",
        "ability": "Flame Body"
    },
    "220": {
        "stats": {
            "hp": 282,
            "atk": 173,
            "sdf": 128,
            "spd": 136,
            "def": 148,
            "sat": 86
        },
        "name": "Swinub",
        "weight": 6.5,
        "gender": "m",
        "type2": "ground",
        "moves": [
            89,
            419,
            420,
            283
        ],
        "type1": "ice",
        "ability": "Thick Fat"
    },
    "221": {
        "stats": {
            "hp": 401,
            "atk": 236,
            "sdf": 176,
            "spd": 122,
            "def": 216,
            "sat": 201
        },
        "name": "Piloswine",
        "weight": 55.8,
        "gender": "m",
        "type2": "ground",
        "moves": [
            196,
            341,
            44,
            317
        ],
        "type1": "ice",
        "ability": "Oblivious"
    },
    "222": {
        "stats": {
            "hp": 260,
            "atk": 175,
            "sdf": 215,
            "spd": 85,
            "def": 215,
            "sat": 192
        },
        "name": "Corsola",
        "weight": 5,
        "gender": "f",
        "type2": "rock",
        "moves": [
            444,
            57,
            243,
            213
        ],
        "type1": "water",
        "ability": "Hustle"
    },
    "223": {
        "stats": {
            "hp": 207,
            "atk": 144,
            "sdf": 101,
            "spd": 246,
            "def": 101,
            "sat": 224
        },
        "name": "Remoraid",
        "weight": 12,
        "gender": "f",
        "moves": [
            323,
            362,
            63,
            53
        ],
        "type1": "water",
        "ability": "Sniper"
    },
    "224": {
        "stats": {
            "hp": 314,
            "atk": 275,
            "sdf": 229,
            "spd": 113,
            "def": 209,
            "sat": 275
        },
        "name": "Octillery",
        "weight": 28.5,
        "gender": "m",
        "moves": [
            190,
            350,
            378,
            86
        ],
        "type1": "water",
        "ability": "Suction Cups"
    },
    "225": {
        "stats": {
            "hp": 253,
            "atk": 229,
            "sdf": 126,
            "spd": 228,
            "def": 126,
            "sat": 149
        },
        "name": "Delibird",
        "weight": 16,
        "gender": "m",
        "type2": "flying",
        "moves": [
            8,
            332,
            280,
            420
        ],
        "type1": "ice",
        "ability": "Hustle"
    },
    "226": {
        "stats": {
            "hp": 271,
            "atk": 150,
            "sdf": 295,
            "spd": 158,
            "def": 176,
            "sat": 196
        },
        "name": "Mantine",
        "weight": 220,
        "gender": "f",
        "type2": "flying",
        "moves": [
            61,
            340,
            60,
            114
        ],
        "type1": "water",
        "ability": "Water Veil"
    },
    "227": {
        "stats": {
            "hp": 271,
            "atk": 196,
            "sdf": 193,
            "spd": 176,
            "def": 284,
            "sat": 116
        },
        "name": "Skarmory",
        "weight": 50.5,
        "gender": "f",
        "type2": "flying",
        "moves": [
            211,
            92,
            18,
            191
        ],
        "type1": "steel",
        "ability": "Keen Eye"
    },
    "228": {
        "stats": {
            "hp": 253,
            "atk": 140,
            "sdf": 136,
            "spd": 228,
            "def": 117,
            "sat": 238
        },
        "name": "Houndour",
        "weight": 10.8,
        "gender": "m",
        "type2": "fire",
        "moves": [
            315,
            399,
            76,
            241
        ],
        "type1": "dark",
        "ability": "Flash Fire"
    },
    "229": {
        "stats": {
            "hp": 288,
            "atk": 213,
            "sdf": 193,
            "spd": 223,
            "def": 146,
            "sat": 227
        },
        "name": "Houndoom",
        "weight": 35,
        "gender": "f",
        "type2": "fire",
        "moves": [
            257,
            44,
            422,
            46
        ],
        "type1": "dark",
        "ability": "Early Bird"
    },
    "230": {
        "stats": {
            "hp": 325,
            "atk": 226,
            "sdf": 246,
            "spd": 227,
            "def": 246,
            "sat": 258
        },
        "name": "Kingdra",
        "weight": 152,
        "gender": "f",
        "type2": "dragon",
        "moves": [
            55,
            13,
            116,
            164
        ],
        "type1": "water",
        "ability": "Sniper"
    },
    "231": {
        "stats": {
            "hp": 321,
            "atk": 190,
            "sdf": 148,
            "spd": 160,
            "def": 187,
            "sat": 104
        },
        "name": "Phanpy",
        "weight": 33.5,
        "gender": "m",
        "moves": [
            89,
            34,
            104,
            201
        ],
        "type1": "ground",
        "ability": "Sand Veil"
    },
    "232": {
        "stats": {
            "hp": 318,
            "atk": 273,
            "sdf": 168,
            "spd": 133,
            "def": 273,
            "sat": 137
        },
        "name": "Donphan",
        "weight": 120,
        "gender": "f",
        "moves": [
            222,
            420,
            229,
            446
        ],
        "type1": "ground",
        "ability": "Sturdy"
    },
    "233": {
        "stats": {
            "hp": 307,
            "atk": 192,
            "sdf": 222,
            "spd": 152,
            "def": 212,
            "sat": 242
        },
        "name": "Porygon2",
        "weight": 32.5,
        "gender": "-",
        "moves": [
            161,
            435,
            92,
            277
        ],
        "type1": "normal",
        "ability": "Trace"
    },
    "234": {
        "stats": {
            "hp": 287,
            "atk": 226,
            "sdf": 166,
            "spd": 206,
            "def": 160,
            "sat": 206
        },
        "name": "Stantler",
        "weight": 71.2,
        "gender": "f",
        "moves": [
            23,
            247,
            428,
            95
        ],
        "type1": "normal",
        "ability": "Intimidate"
    },
    "235": {
        "stats": {
            "hp": 252,
            "atk": 152,
            "sdf": 126,
            "spd": 249,
            "def": 106,
            "sat": 68
        },
        "name": "Smeargle",
        "weight": 58,
        "gender": "m",
        "moves": [
            462,
            467,
            221,
            464
        ],
        "type1": "normal",
        "ability": "Technician"
    },
    "236": {
        "stats": {
            "hp": 211,
            "atk": 185,
            "sdf": 106,
            "spd": 169,
            "def": 106,
            "sat": 95
        },
        "name": "Tyrogue",
        "weight": 21,
        "gender": "m",
        "moves": [
            136,
            89,
            157,
            207
        ],
        "type1": "fighting",
        "ability": "Guts"
    },
    "237": {
        "stats": {
            "hp": 239,
            "atk": 224,
            "sdf": 254,
            "spd": 174,
            "def": 224,
            "sat": 104
        },
        "name": "Hitmontop",
        "weight": 48,
        "gender": "m",
        "moves": [
            167,
            332,
            418,
            228
        ],
        "type1": "fighting",
        "ability": "Technician"
    },
    "238": {
        "stats": {
            "hp": 263,
            "atk": 86,
            "sdf": 175,
            "spd": 217,
            "def": 98,
            "sat": 228
        },
        "name": "Smoochum",
        "weight": 6,
        "gender": "f",
        "type2": "psychic",
        "moves": [
            58,
            94,
            347,
            417
        ],
        "type1": "ice",
        "ability": "Oblivious"
    },
    "239": {
        "stats": {
            "hp": 221,
            "atk": 189,
            "sdf": 156,
            "spd": 236,
            "def": 108,
            "sat": 196
        },
        "name": "Elekid",
        "weight": 23.5,
        "gender": "m",
        "moves": [
            85,
            8,
            148,
            113
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "240": {
        "stats": {
            "hp": 231,
            "atk": 196,
            "sdf": 140,
            "spd": 233,
            "def": 120,
            "sat": 196
        },
        "name": "Magby",
        "weight": 21.4,
        "gender": "m",
        "moves": [
            53,
            238,
            109,
            108
        ],
        "type1": "fire",
        "ability": "Flame Body"
    },
    "241": {
        "stats": {
            "hp": 329,
            "atk": 259,
            "sdf": 174,
            "spd": 234,
            "def": 223,
            "sat": 83
        },
        "name": "Miltank",
        "weight": 75.5,
        "gender": "f",
        "moves": [
            217,
            205,
            208,
            117
        ],
        "type1": "normal",
        "ability": "Scrappy"
    },
    "242": {
        "stats": {
            "hp": 620,
            "atk": 22,
            "sdf": 284,
            "spd": 160,
            "def": 85,
            "sat": 175
        },
        "name": "Blissey",
        "weight": 46.8,
        "gender": "f",
        "moves": [
            63,
            59,
            356,
            287
        ],
        "type1": "normal",
        "ability": "Serene Grace"
    },
    "243": {
        "stats": {
            "hp": 300,
            "atk": 200,
            "sdf": 195,
            "spd": 235,
            "def": 170,
            "sat": 360
        },
        "name": "Raikou",
        "weight": 178,
        "gender": "-",
        "moves": [
            84,
            44,
            148,
            46
        ],
        "type1": "electric",
        "ability": "Pressure"
    },
    "244": {
        "stats": {
            "hp": 371,
            "atk": 239,
            "sdf": 186,
            "spd": 236,
            "def": 206,
            "sat": 306
        },
        "name": "Entei",
        "weight": 198,
        "gender": "-",
        "moves": [
            52,
            23,
            249,
            46
        ],
        "type1": "fire",
        "ability": "Pressure"
    },
    "245": {
        "stats": {
            "hp": 344,
            "atk": 189,
            "sdf": 269,
            "spd": 188,
            "def": 269,
            "sat": 240
        },
        "name": "Suicune",
        "weight": 187,
        "gender": "-",
        "moves": [
            55,
            16,
            54,
            46
        ],
        "type1": "water",
        "ability": "Pressure"
    },
    "246": {
        "stats": {
            "hp": 300,
            "atk": 207,
            "sdf": 136,
            "spd": 156,
            "def": 136,
            "sat": 113
        },
        "name": "Larvitar",
        "weight": 72,
        "gender": "f",
        "type2": "ground",
        "moves": [
            89,
            444,
            44,
            349
        ],
        "type1": "rock",
        "ability": "Guts"
    },
    "247": {
        "stats": {
            "hp": 344,
            "atk": 183,
            "sdf": 217,
            "spd": 138,
            "def": 217,
            "sat": 166
        },
        "name": "Pupitar",
        "weight": 152,
        "gender": "f",
        "type2": "ground",
        "moves": [
            91,
            157,
            156,
            397
        ],
        "type1": "rock",
        "ability": "Shed Skin"
    },
    "248": {
        "stats": {
            "hp": 310,
            "atk": 273,
            "sdf": 184,
            "spd": 154,
            "def": 225,
            "sat": 195
        },
        "name": "Tyranitar",
        "weight": 202,
        "gender": "f",
        "type2": "dark",
        "moves": [
            44,
            317,
            424,
            43
        ],
        "type1": "rock",
        "ability": "Sand Stream"
    },
    "249": {
        "stats": {
            "hp": 322,
            "atk": 203,
            "sdf": 281,
            "spd": 225,
            "def": 265,
            "sat": 185
        },
        "name": "Lugia",
        "weight": 216,
        "gender": "-",
        "type2": "flying",
        "moves": [
            177,
            248,
            432,
            102
        ],
        "type1": "psychic",
        "ability": "Pressure"
    },
    "250": {
        "stats": {
            "hp": 322,
            "atk": 265,
            "sdf": 313,
            "spd": 185,
            "def": 203,
            "sat": 202
        },
        "name": "Ho-Oh",
        "weight": 199,
        "gender": "-",
        "type2": "flying",
        "moves": [
            257,
            311,
            201,
            366
        ],
        "type1": "fire",
        "ability": "Pressure"
    },
    "251": {
        "stats": {
            "hp": 330,
            "atk": 225,
            "sdf": 225,
            "spd": 225,
            "def": 225,
            "sat": 225
        },
        "name": "Celebi",
        "weight": 5,
        "gender": "-",
        "type2": "grass",
        "moves": [
            345,
            93,
            352,
            118
        ],
        "type1": "psychic",
        "ability": "Natural Cure"
    },
    "252": {
        "stats": {
            "hp": 222,
            "atk": 113,
            "sdf": 146,
            "spd": 262,
            "def": 106,
            "sat": 229
        },
        "name": "Treecko",
        "weight": 5,
        "gender": "m",
        "moves": [
            437,
            412,
            225,
            203
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "253": {
        "stats": {
            "hp": 262,
            "atk": 228,
            "sdf": 187,
            "spd": 247,
            "def": 147,
            "sat": 185
        },
        "name": "Grovyle",
        "weight": 21.6,
        "gender": "f",
        "moves": [
            402,
            404,
            9,
            14
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "254": {
        "stats": {
            "hp": 275,
            "atk": 210,
            "sdf": 200,
            "spd": 270,
            "def": 160,
            "sat": 230
        },
        "name": "Sceptile",
        "weight": 52.2,
        "gender": "f",
        "moves": [
            348,
            337,
            332,
            219
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "255": {
        "stats": {
            "hp": 231,
            "atk": 198,
            "sdf": 122,
            "spd": 168,
            "def": 116,
            "sat": 240
        },
        "name": "Torchic",
        "weight": 2.5,
        "gender": "m",
        "moves": [
            315,
            91,
            67,
            182
        ],
        "type1": "fire",
        "ability": "Speed Boost"
    },
    "256": {
        "stats": {
            "hp": 282,
            "atk": 227,
            "sdf": 177,
            "spd": 167,
            "def": 177,
            "sat": 227
        },
        "name": "Combusken",
        "weight": 19.5,
        "gender": "f",
        "type2": "fighting",
        "moves": [
            53,
            327,
            400,
            157
        ],
        "type1": "fire",
        "ability": "Speed Boost"
    },
    "257": {
        "stats": {
            "hp": 295,
            "atk": 243,
            "sdf": 170,
            "spd": 209,
            "def": 170,
            "sat": 250
        },
        "name": "Blaziken",
        "weight": 52,
        "gender": "f",
        "type2": "fighting",
        "moves": [
            299,
            24,
            119,
            182
        ],
        "type1": "fire",
        "ability": "Speed Boost"
    },
    "258": {
        "stats": {
            "hp": 262,
            "atk": 262,
            "sdf": 157,
            "spd": 116,
            "def": 157,
            "sat": 122
        },
        "name": "Mudkip",
        "weight": 7.6,
        "gender": "m",
        "moves": [
            127,
            276,
            419,
            213
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "259": {
        "stats": {
            "hp": 287,
            "atk": 171,
            "sdf": 182,
            "spd": 142,
            "def": 182,
            "sat": 201
        },
        "name": "Marshtomp",
        "weight": 28,
        "gender": "f",
        "type2": "ground",
        "moves": [
            330,
            89,
            124,
            112
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "260": {
        "stats": {
            "hp": 335,
            "atk": 225,
            "sdf": 210,
            "spd": 150,
            "def": 210,
            "sat": 220
        },
        "name": "Swampert",
        "weight": 81.9,
        "gender": "f",
        "type2": "ground",
        "moves": [
            291,
            426,
            301,
            243
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "261": {
        "stats": {
            "hp": 232,
            "atk": 229,
            "sdf": 117,
            "spd": 106,
            "def": 127,
            "sat": 86
        },
        "name": "Poochyena",
        "weight": 13.6,
        "gender": "m",
        "moves": [
            162,
            389,
            289,
            207
        ],
        "type1": "dark",
        "ability": "Quick Feet"
    },
    "262": {
        "stats": {
            "hp": 286,
            "atk": 221,
            "sdf": 161,
            "spd": 199,
            "def": 181,
            "sat": 144
        },
        "name": "Mightyena",
        "weight": 37,
        "gender": "m",
        "moves": [
            242,
            424,
            46,
            336
        ],
        "type1": "dark",
        "ability": "Intimidate"
    },
    "263": {
        "stats": {
            "hp": 279,
            "atk": 174,
            "sdf": 119,
            "spd": 156,
            "def": 119,
            "sat": 86
        },
        "name": "Zigzagoon",
        "weight": 17.5,
        "gender": "m",
        "moves": [
            162,
            245,
            316,
            187
        ],
        "type1": "normal",
        "ability": "Gluttony"
    },
    "264": {
        "stats": {
            "hp": 302,
            "atk": 181,
            "sdf": 163,
            "spd": 265,
            "def": 163,
            "sat": 126
        },
        "name": "Linoone",
        "weight": 32.5,
        "gender": "f",
        "moves": [
            29,
            228,
            175,
            187
        ],
        "type1": "normal",
        "ability": "Pickup"
    },
    "265": {
        "stats": {
            "hp": 247,
            "atk": 207,
            "sdf": 112,
            "spd": 92,
            "def": 122,
            "sat": 68
        },
        "name": "Wurmple",
        "weight": 3.6,
        "gender": "m",
        "moves": [
            450,
            40,
            33,
            81
        ],
        "type1": "bug",
        "ability": "Shield Dust"
    },
    "266": {
        "stats": {
            "hp": 262,
            "atk": 185,
            "sdf": 107,
            "spd": 66,
            "def": 167,
            "sat": 77
        },
        "name": "Silcoon",
        "weight": 10,
        "gender": "m",
        "moves": [
            450,
            40,
            106,
            81
        ],
        "type1": "bug",
        "ability": "Shed Skin"
    },
    "267": {
        "stats": {
            "hp": 324,
            "atk": 158,
            "sdf": 136,
            "spd": 187,
            "def": 157,
            "sat": 260
        },
        "name": "Beautifly",
        "weight": 28.4,
        "gender": "f",
        "type2": "flying",
        "moves": [
            405,
            94,
            18,
            234
        ],
        "type1": "bug",
        "ability": "Rivalry"
    },
    "268": {
        "stats": {
            "hp": 262,
            "atk": 185,
            "sdf": 107,
            "spd": 66,
            "def": 167,
            "sat": 77
        },
        "name": "Cascoon",
        "weight": 11.5,
        "gender": "m",
        "moves": [
            450,
            40,
            106,
            81
        ],
        "type1": "bug",
        "ability": "Shed Skin"
    },
    "269": {
        "stats": {
            "hp": 284,
            "atk": 122,
            "sdf": 239,
            "spd": 189,
            "def": 199,
            "sat": 174
        },
        "name": "Dustox",
        "weight": 31.6,
        "gender": "f",
        "type2": "poison",
        "moves": [
            188,
            94,
            113,
            236
        ],
        "type1": "bug",
        "ability": "Shield Dust"
    },
    "270": {
        "stats": {
            "hp": 243,
            "atk": 86,
            "sdf": 149,
            "spd": 124,
            "def": 117,
            "sat": 173
        },
        "name": "Lotad",
        "weight": 2.6,
        "gender": "m",
        "type2": "grass",
        "moves": [
            57,
            412,
            59,
            240
        ],
        "type1": "water",
        "ability": "Swift Swim"
    },
    "271": {
        "stats": {
            "hp": 324,
            "atk": 122,
            "sdf": 239,
            "spd": 136,
            "def": 158,
            "sat": 156
        },
        "name": "Lombre",
        "weight": 32.5,
        "gender": "f",
        "type2": "grass",
        "moves": [
            56,
            73,
            240,
            182
        ],
        "type1": "water",
        "ability": "Rain Dish"
    },
    "272": {
        "stats": {
            "hp": 300,
            "atk": 175,
            "sdf": 235,
            "spd": 175,
            "def": 175,
            "sat": 215
        },
        "name": "Ludicolo",
        "weight": 55,
        "gender": "f",
        "type2": "grass",
        "moves": [
            61,
            202,
            73,
            118
        ],
        "type1": "water",
        "ability": "Own Tempo"
    },
    "273": {
        "stats": {
            "hp": 221,
            "atk": 196,
            "sdf": 96,
            "spd": 159,
            "def": 136,
            "sat": 86
        },
        "name": "Seedot",
        "weight": 4,
        "gender": "m",
        "moves": [
            402,
            241,
            14,
            153
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "274": {
        "stats": {
            "hp": 293,
            "atk": 151,
            "sdf": 128,
            "spd": 184,
            "def": 128,
            "sat": 188
        },
        "name": "Nuzleaf",
        "weight": 28,
        "gender": "f",
        "type2": "dark",
        "moves": [
            412,
            399,
            417,
            241
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "275": {
        "stats": {
            "hp": 320,
            "atk": 258,
            "sdf": 155,
            "spd": 195,
            "def": 155,
            "sat": 193
        },
        "name": "Shiftry",
        "weight": 59.6,
        "gender": "m",
        "type2": "dark",
        "moves": [
            437,
            185,
            267,
            18
        ],
        "type1": "grass",
        "ability": "Early Bird"
    },
    "276": {
        "stats": {
            "hp": 243,
            "atk": 229,
            "sdf": 96,
            "spd": 248,
            "def": 96,
            "sat": 86
        },
        "name": "Taillow",
        "weight": 2.3,
        "gender": "m",
        "type2": "flying",
        "moves": [
            413,
            216,
            211,
            48
        ],
        "type1": "normal",
        "ability": "Guts"
    },
    "277": {
        "stats": {
            "hp": 283,
            "atk": 185,
            "sdf": 157,
            "spd": 286,
            "def": 177,
            "sat": 218
        },
        "name": "Swellow",
        "weight": 19.8,
        "gender": "m",
        "type2": "flying",
        "moves": [
            403,
            63,
            257,
            466
        ],
        "type1": "normal",
        "ability": "Scrappy"
    },
    "278": {
        "stats": {
            "hp": 222,
            "atk": 86,
            "sdf": 96,
            "spd": 269,
            "def": 96,
            "sat": 229
        },
        "name": "Wingull",
        "weight": 9.5,
        "gender": "m",
        "type2": "flying",
        "moves": [
            403,
            352,
            59,
            366
        ],
        "type1": "water",
        "ability": "Rain Dish"
    },
    "279": {
        "stats": {
            "hp": 265,
            "atk": 107,
            "sdf": 200,
            "spd": 190,
            "def": 240,
            "sat": 210
        },
        "name": "Pelipper",
        "weight": 28,
        "gender": "m",
        "type2": "flying",
        "moves": [
            362,
            314,
            255,
            254
        ],
        "type1": "water",
        "ability": "Keen Eye"
    },
    "280": {
        "stats": {
            "hp": 198,
            "atk": 77,
            "sdf": 106,
            "spd": 196,
            "def": 86,
            "sat": 189
        },
        "name": "Ralts",
        "weight": 6.6,
        "gender": "m",
        "moves": [
            94,
            324,
            269,
            194
        ],
        "type1": "psychic",
        "ability": "Synchronize"
    },
    "281": {
        "stats": {
            "hp": 235,
            "atk": 111,
            "sdf": 164,
            "spd": 154,
            "def": 124,
            "sat": 202
        },
        "name": "Kirlia",
        "weight": 20.2,
        "gender": "f",
        "moves": [
            94,
            247,
            261,
            347
        ],
        "type1": "psychic",
        "ability": "Trace"
    },
    "282": {
        "stats": {
            "hp": 272,
            "atk": 177,
            "sdf": 261,
            "spd": 191,
            "def": 161,
            "sat": 252
        },
        "name": "Gardevoir",
        "weight": 48.4,
        "gender": "f",
        "moves": [
            94,
            345,
            425,
            277
        ],
        "type1": "psychic",
        "ability": "Trace"
    },
    "283": {
        "stats": {
            "hp": 263,
            "atk": 86,
            "sdf": 140,
            "spd": 166,
            "def": 122,
            "sat": 218
        },
        "name": "Surskit",
        "weight": 1.7,
        "gender": "m",
        "type2": "water",
        "moves": [
            56,
            324,
            58,
            240
        ],
        "type1": "bug",
        "ability": "Swift Swim"
    },
    "284": {
        "stats": {
            "hp": 286,
            "atk": 144,
            "sdf": 225,
            "spd": 161,
            "def": 165,
            "sat": 201
        },
        "name": "Masquerain",
        "weight": 3.6,
        "gender": "m",
        "type2": "flying",
        "moves": [
            405,
            403,
            56,
            355
        ],
        "type1": "bug",
        "ability": "Intimidate"
    },
    "285": {
        "stats": {
            "hp": 321,
            "atk": 196,
            "sdf": 158,
            "spd": 106,
            "def": 158,
            "sat": 104
        },
        "name": "Shroomish",
        "weight": 4.5,
        "gender": "m",
        "moves": [
            402,
            264,
            147,
            14
        ],
        "type1": "grass",
        "ability": "Poison Heal"
    },
    "286": {
        "stats": {
            "hp": 262,
            "atk": 276,
            "sdf": 157,
            "spd": 177,
            "def": 177,
            "sat": 195
        },
        "name": "Breloom",
        "weight": 39.2,
        "gender": "f",
        "type2": "fighting",
        "moves": [
            276,
            202,
            183,
            78
        ],
        "type1": "grass",
        "ability": "Technician"
    },
    "287": {
        "stats": {
            "hp": 283,
            "atk": 240,
            "sdf": 127,
            "spd": 117,
            "def": 156,
            "sat": 95
        },
        "name": "Slakoth",
        "weight": 24,
        "gender": "m",
        "moves": [
            38,
            359,
            400,
            281
        ],
        "type1": "normal",
        "ability": "Truant"
    },
    "288": {
        "stats": {
            "hp": 304,
            "atk": 218,
            "sdf": 149,
            "spd": 219,
            "def": 199,
            "sat": 134
        },
        "name": "Vigoroth",
        "weight": 46.5,
        "gender": "f",
        "moves": [
            163,
            421,
            67,
            269
        ],
        "type1": "normal",
        "ability": "Vital Spirit"
    },
    "289": {
        "stats": {
            "hp": 431,
            "atk": 346,
            "sdf": 156,
            "spd": 248,
            "def": 203,
            "sat": 216
        },
        "name": "Slaking",
        "weight": 130.5,
        "gender": "m",
        "moves": [
            70,
            386,
            281,
            303
        ],
        "type1": "normal",
        "ability": "Truant"
    },
    "290": {
        "stats": {
            "hp": 266,
            "atk": 207,
            "sdf": 97,
            "spd": 116,
            "def": 216,
            "sat": 86
        },
        "name": "Nincada",
        "weight": 5.5,
        "gender": "m",
        "type2": "ground",
        "moves": [
            404,
            91,
            400,
            207
        ],
        "type1": "bug",
        "ability": "Compound Eyes"
    },
    "291": {
        "stats": {
            "hp": 305,
            "atk": 216,
            "sdf": 178,
            "spd": 320,
            "def": 168,
            "sat": 149
        },
        "name": "Ninjask",
        "weight": 12,
        "gender": "f",
        "type2": "flying",
        "moves": [
            450,
            332,
            91,
            14
        ],
        "type1": "bug",
        "ability": "Speed Boost"
    },
    "292": {
        "stats": {
            "hp": 1,
            "atk": 260,
            "sdf": 117,
            "spd": 137,
            "def": 147,
            "sat": 105
        },
        "name": "Shedinja",
        "weight": 1.2,
        "gender": "-",
        "type2": "ghost",
        "moves": [
            404,
            425,
            261,
            174
        ],
        "type1": "bug",
        "ability": "Wonder Guard"
    },
    "293": {
        "stats": {
            "hp": 285,
            "atk": 124,
            "sdf": 98,
            "spd": 108,
            "def": 98,
            "sat": 221
        },
        "name": "Whismur",
        "weight": 16.3,
        "gender": "m",
        "moves": [
            304,
            59,
            126,
            247
        ],
        "type1": "normal",
        "ability": "Soundproof"
    },
    "294": {
        "stats": {
            "hp": 334,
            "atk": 160,
            "sdf": 147,
            "spd": 157,
            "def": 147,
            "sat": 225
        },
        "name": "Loudred",
        "weight": 40.5,
        "gender": "m",
        "moves": [
            304,
            315,
            326,
            313
        ],
        "type1": "normal",
        "ability": "Soundproof"
    },
    "295": {
        "stats": {
            "hp": 370,
            "atk": 196,
            "sdf": 183,
            "spd": 172,
            "def": 183,
            "sat": 309
        },
        "name": "Exploud",
        "weight": 84,
        "gender": "m",
        "moves": [
            359,
            173,
            313,
            156
        ],
        "type1": "normal",
        "ability": "Scrappy"
    },
    "296": {
        "stats": {
            "hp": 306,
            "atk": 240,
            "sdf": 117,
            "spd": 86,
            "def": 117,
            "sat": 68
        },
        "name": "Makuhita",
        "weight": 86.4,
        "gender": "m",
        "moves": [
            279,
            179,
            185,
            418
        ],
        "type1": "fighting",
        "ability": "Thick Fat"
    },
    "297": {
        "stats": {
            "hp": 408,
            "atk": 277,
            "sdf": 156,
            "spd": 172,
            "def": 156,
            "sat": 104
        },
        "name": "Hariyama",
        "weight": 253.8,
        "gender": "f",
        "moves": [
            358,
            265,
            290,
            371
        ],
        "type1": "fighting",
        "ability": "Guts"
    },
    "298": {
        "stats": {
            "hp": 262,
            "atk": 152,
            "sdf": 137,
            "spd": 76,
            "def": 137,
            "sat": 68
        },
        "name": "Azurill",
        "weight": 2,
        "gender": "m",
        "moves": [
            34,
            127,
            213,
            204
        ],
        "type1": "normal",
        "ability": "Huge Power"
    },
    "299": {
        "stats": {
            "hp": 264,
            "atk": 147,
            "sdf": 261,
            "spd": 86,
            "def": 306,
            "sat": 147
        },
        "name": "Nosepass",
        "weight": 97,
        "gender": "f",
        "moves": [
            444,
            192,
            223,
            356
        ],
        "type1": "rock",
        "ability": "Sturdy"
    },
    "300": {
        "stats": {
            "hp": 283,
            "atk": 156,
            "sdf": 150,
            "spd": 136,
            "def": 150,
            "sat": 95
        },
        "name": "Skitty",
        "weight": 11,
        "gender": "m",
        "moves": [
            428,
            213,
            207,
            86
        ],
        "type1": "normal",
        "ability": "Normalize"
    },
    "301": {
        "stats": {
            "hp": 281,
            "atk": 198,
            "sdf": 131,
            "spd": 239,
            "def": 166,
            "sat": 195
        },
        "name": "Delcatty",
        "weight": 32.6,
        "gender": "f",
        "moves": [
            274,
            383,
            204,
            47
        ],
        "type1": "normal",
        "ability": "Cute Charm"
    },
    "302": {
        "stats": {
            "hp": 304,
            "atk": 186,
            "sdf": 177,
            "spd": 122,
            "def": 197,
            "sat": 228
        },
        "name": "Sableye",
        "weight": 11,
        "gender": "f",
        "type2": "ghost",
        "moves": [
            371,
            190,
            277,
            289
        ],
        "type1": "dark",
        "ability": "Stall"
    },
    "303": {
        "stats": {
            "hp": 250,
            "atk": 215,
            "sdf": 155,
            "spd": 159,
            "def": 215,
            "sat": 139
        },
        "name": "Mawile",
        "weight": 11.5,
        "gender": "f",
        "moves": [
            442,
            424,
            254,
            256
        ],
        "type1": "steel",
        "ability": "Intimidate"
    },
    "304": {
        "stats": {
            "hp": 266,
            "atk": 201,
            "sdf": 141,
            "spd": 135,
            "def": 261,
            "sat": 104
        },
        "name": "Aron",
        "weight": 60,
        "gender": "m",
        "type2": "rock",
        "moves": [
            457,
            442,
            276,
            397
        ],
        "type1": "steel",
        "ability": "Rock Head"
    },
    "305": {
        "stats": {
            "hp": 324,
            "atk": 216,
            "sdf": 173,
            "spd": 158,
            "def": 316,
            "sat": 122
        },
        "name": "Lairon",
        "weight": 120,
        "gender": "m",
        "type2": "rock",
        "moves": [
            231,
            444,
            407,
            368
        ],
        "type1": "steel",
        "ability": "Sturdy"
    },
    "306": {
        "stats": {
            "hp": 286,
            "atk": 202,
            "sdf": 161,
            "spd": 139,
            "def": 379,
            "sat": 222
        },
        "name": "Aggron",
        "weight": 360,
        "gender": "f",
        "type2": "rock",
        "moves": [
            430,
            246,
            53,
            319
        ],
        "type1": "steel",
        "ability": "Sturdy"
    },
    "307": {
        "stats": {
            "hp": 219,
            "atk": 134,
            "sdf": 164,
            "spd": 191,
            "def": 164,
            "sat": 120
        },
        "name": "Meditite",
        "weight": 11.2,
        "gender": "m",
        "type2": "psychic",
        "moves": [
            136,
            428,
            418,
            96
        ],
        "type1": "fighting",
        "ability": "Pure Power"
    },
    "308": {
        "stats": {
            "hp": 267,
            "atk": 126,
            "sdf": 213,
            "spd": 202,
            "def": 234,
            "sat": 141
        },
        "name": "Medicham",
        "weight": 31.5,
        "gender": "f",
        "type2": "psychic",
        "moves": [
            252,
            427,
            395,
            379
        ],
        "type1": "fighting",
        "ability": "Pure Power"
    },
    "309": {
        "stats": {
            "hp": 242,
            "atk": 113,
            "sdf": 116,
            "spd": 229,
            "def": 116,
            "sat": 229
        },
        "name": "Electrike",
        "weight": 15.2,
        "gender": "m",
        "moves": [
            85,
            53,
            189,
            268
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "310": {
        "stats": {
            "hp": 296,
            "atk": 224,
            "sdf": 171,
            "spd": 261,
            "def": 171,
            "sat": 234
        },
        "name": "Manectric",
        "weight": 40.2,
        "gender": "f",
        "moves": [
            351,
            424,
            46,
            393
        ],
        "type1": "electric",
        "ability": "Static"
    },
    "311": {
        "stats": {
            "hp": 267,
            "atk": 127,
            "sdf": 192,
            "spd": 255,
            "def": 122,
            "sat": 212
        },
        "name": "Plusle",
        "weight": 4.2,
        "gender": "f",
        "moves": [
            435,
            447,
            451,
            227
        ],
        "type1": "electric",
        "ability": "Plus"
    },
    "312": {
        "stats": {
            "hp": 267,
            "atk": 109,
            "sdf": 212,
            "spd": 255,
            "def": 142,
            "sat": 192
        },
        "name": "Minun",
        "weight": 4.2,
        "gender": "m",
        "moves": [
            87,
            447,
            376,
            313
        ],
        "type1": "electric",
        "ability": "Minus"
    },
    "313": {
        "stats": {
            "hp": 278,
            "atk": 189,
            "sdf": 193,
            "spd": 213,
            "def": 153,
            "sat": 137
        },
        "name": "Volbeat",
        "weight": 17.7,
        "gender": "m",
        "moves": [
            318,
            428,
            294,
            236
        ],
        "type1": "bug",
        "ability": "Swarm"
    },
    "314": {
        "stats": {
            "hp": 278,
            "atk": 123,
            "sdf": 193,
            "spd": 234,
            "def": 153,
            "sat": 189
        },
        "name": "Illumise",
        "weight": 17.7,
        "gender": "f",
        "moves": [
            405,
            351,
            74,
            236
        ],
        "type1": "bug",
        "ability": "Tinted Lens"
    },
    "315": {
        "stats": {
            "hp": 248,
            "atk": 163,
            "sdf": 203,
            "spd": 155,
            "def": 146,
            "sat": 243
        },
        "name": "Roselia",
        "weight": 2,
        "gender": "f",
        "type2": "poison",
        "moves": [
            80,
            326,
            320,
            235
        ],
        "type1": "grass",
        "ability": "Poison Point"
    },
    "316": {
        "stats": {
            "hp": 297,
            "atk": 168,
            "sdf": 158,
            "spd": 132,
            "def": 158,
            "sat": 110
        },
        "name": "Gulpin",
        "weight": 10.3,
        "gender": "f",
        "moves": [
            441,
            223,
            220,
            281
        ],
        "type1": "poison",
        "ability": "Liquid Ooze"
    },
    "317": {
        "stats": {
            "hp": 341,
            "atk": 182,
            "sdf": 202,
            "spd": 131,
            "def": 202,
            "sat": 200
        },
        "name": "Swalot",
        "weight": 80,
        "gender": "f",
        "moves": [
            188,
            402,
            7,
            174
        ],
        "type1": "poison",
        "ability": "Liquid Ooze"
    },
    "318": {
        "stats": {
            "hp": 231,
            "atk": 232,
            "sdf": 113,
            "spd": 186,
            "def": 113,
            "sat": 166
        },
        "name": "Carvanha",
        "weight": 20.8,
        "gender": "f",
        "type2": "dark",
        "moves": [
            242,
            127,
            194,
            182
        ],
        "type1": "water",
        "ability": "Speed Boost"
    },
    "319": {
        "stats": {
            "hp": 282,
            "atk": 277,
            "sdf": 117,
            "spd": 227,
            "def": 117,
            "sat": 227
        },
        "name": "Sharpedo",
        "weight": 88.8,
        "gender": "f",
        "type2": "dark",
        "moves": [
            56,
            44,
            423,
            203
        ],
        "type1": "water",
        "ability": "Speed Boost"
    },
    "320": {
        "stats": {
            "hp": 408,
            "atk": 183,
            "sdf": 101,
            "spd": 179,
            "def": 113,
            "sat": 183
        },
        "name": "Wailmer",
        "weight": 130,
        "gender": "f",
        "moves": [
            323,
            59,
            90,
            120
        ],
        "type1": "water",
        "ability": "Water Veil"
    },
    "321": {
        "stats": {
            "hp": 481,
            "atk": 203,
            "sdf": 189,
            "spd": 112,
            "def": 189,
            "sat": 185
        },
        "name": "Wailord",
        "weight": 398,
        "gender": "f",
        "moves": [
            323,
            340,
            442,
            45
        ],
        "type1": "water",
        "ability": "Water Veil"
    },
    "322": {
        "stats": {
            "hp": 277,
            "atk": 140,
            "sdf": 142,
            "spd": 185,
            "def": 132,
            "sat": 182
        },
        "name": "Numel",
        "weight": 24,
        "gender": "f",
        "type2": "ground",
        "moves": [
            53,
            89,
            104,
            254
        ],
        "type1": "fire",
        "ability": "Simple"
    },
    "323": {
        "stats": {
            "hp": 282,
            "atk": 237,
            "sdf": 187,
            "spd": 117,
            "def": 177,
            "sat": 247
        },
        "name": "Camerupt",
        "weight": 220,
        "gender": "f",
        "type2": "ground",
        "moves": [
            284,
            53,
            222,
            90
        ],
        "type1": "fire",
        "ability": "Solid Rock"
    },
    "324": {
        "stats": {
            "hp": 344,
            "atk": 185,
            "sdf": 216,
            "spd": 76,
            "def": 316,
            "sat": 249
        },
        "name": "Torkoal",
        "weight": 80.4,
        "gender": "f",
        "item": "Grip Claw",
        "moves": [
            83,
            89,
            92,
            182
        ],
        "type1": "fire",
        "ability": "White Smoke"
    },
    "325": {
        "stats": {
            "hp": 283,
            "atk": 86,
            "sdf": 284,
            "spd": 177,
            "def": 106,
            "sat": 177
        },
        "name": "Spoink",
        "weight": 30.6,
        "gender": "m",
        "moves": [
            94,
            324,
            277,
            347
        ],
        "type1": "psychic",
        "ability": "Thick Fat"
    },
    "326": {
        "stats": {
            "hp": 301,
            "atk": 126,
            "sdf": 256,
            "spd": 196,
            "def": 166,
            "sat": 216
        },
        "name": "Grumpig",
        "weight": 71.5,
        "gender": "f",
        "moves": [
            411,
            412,
            408,
            115
        ],
        "type1": "psychic",
        "ability": "Own Tempo"
    },
    "327": {
        "stats": {
            "hp": 303,
            "atk": 194,
            "sdf": 177,
            "spd": 177,
            "def": 177,
            "sat": 140
        },
        "name": "Spinda",
        "weight": 5,
        "gender": "m",
        "moves": [
            37,
            389,
            409,
            298
        ],
        "type1": "normal",
        "ability": "Tangled Feet"
    },
    "328": {
        "stats": {
            "hp": 248,
            "atk": 278,
            "sdf": 143,
            "spd": 73,
            "def": 143,
            "sat": 128
        },
        "name": "Trapinch",
        "weight": 15,
        "gender": "m",
        "moves": [
            89,
            242,
            90,
            28
        ],
        "type1": "ground",
        "ability": "Hyper Cutter"
    },
    "329": {
        "stats": {
            "hp": 253,
            "atk": 206,
            "sdf": 148,
            "spd": 188,
            "def": 148,
            "sat": 133
        },
        "name": "Vibrava",
        "weight": 15.3,
        "gender": "f",
        "type2": "dragon",
        "moves": [
            200,
            91,
            19,
            366
        ],
        "type1": "ground",
        "ability": "Levitate"
    },
    "330": {
        "stats": {
            "hp": 296,
            "atk": 207,
            "sdf": 191,
            "spd": 254,
            "def": 191,
            "sat": 191
        },
        "name": "Flygon",
        "weight": 82,
        "gender": "m",
        "type2": "dragon",
        "moves": [
            434,
            89,
            16,
            201
        ],
        "type1": "ground",
        "ability": "Levitate"
    },
    "331": {
        "stats": {
            "hp": 254,
            "atk": 219,
            "sdf": 141,
            "spd": 107,
            "def": 129,
            "sat": 219
        },
        "name": "Cacnea",
        "weight": 51.3,
        "gender": "m",
        "moves": [
            402,
            264,
            189,
            201
        ],
        "type1": "grass",
        "ability": "Sand Veil"
    },
    "332": {
        "stats": {
            "hp": 280,
            "atk": 265,
            "sdf": 155,
            "spd": 145,
            "def": 155,
            "sat": 265
        },
        "name": "Cacturne",
        "weight": 77.4,
        "gender": "m",
        "type2": "dark",
        "moves": [
            302,
            371,
            178,
            201
        ],
        "type1": "grass",
        "ability": "Sand Veil"
    },
    "333": {
        "stats": {
            "hp": 273,
            "atk": 150,
            "sdf": 218,
            "spd": 136,
            "def": 188,
            "sat": 104
        },
        "name": "Swablu",
        "weight": 1.2,
        "gender": "m",
        "type2": "flying",
        "moves": [
            19,
            47,
            355,
            195
        ],
        "type1": "normal",
        "ability": "Cloud Nine"
    },
    "334": {
        "stats": {
            "hp": 275,
            "atk": 160,
            "sdf": 230,
            "spd": 180,
            "def": 200,
            "sat": 160
        },
        "name": "Altaria",
        "weight": 20.6,
        "gender": "f",
        "type2": "flying",
        "moves": [
            143,
            434,
            257,
            349
        ],
        "type1": "dragon",
        "ability": "Cloud Nine"
    },
    "335": {
        "stats": {
            "hp": 288,
            "atk": 267,
            "sdf": 157,
            "spd": 217,
            "def": 157,
            "sat": 157
        },
        "name": "Zangoose",
        "weight": 40.3,
        "gender": "f",
        "moves": [
            306,
            421,
            232,
            68
        ],
        "type1": "normal",
        "ability": "Immunity"
    },
    "336": {
        "stats": {
            "hp": 288,
            "atk": 260,
            "sdf": 157,
            "spd": 167,
            "def": 157,
            "sat": 213
        },
        "name": "Seviper",
        "weight": 52.5,
        "gender": "f",
        "moves": [
            342,
            401,
            137,
            103
        ],
        "type1": "poison",
        "ability": "Shed Skin"
    },
    "337": {
        "stats": {
            "hp": 284,
            "atk": 185,
            "sdf": 209,
            "spd": 143,
            "def": 169,
            "sat": 229
        },
        "name": "Lunatone",
        "weight": 168,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            94,
            246,
            347,
            433
        ],
        "type1": "rock",
        "ability": "Levitate"
    },
    "338": {
        "stats": {
            "hp": 284,
            "atk": 249,
            "sdf": 169,
            "spd": 143,
            "def": 209,
            "sat": 163
        },
        "name": "Solrock",
        "weight": 154,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            444,
            428,
            261,
            322
        ],
        "type1": "rock",
        "ability": "Levitate"
    },
    "339": {
        "stats": {
            "hp": 258,
            "atk": 163,
            "sdf": 135,
            "spd": 173,
            "def": 139,
            "sat": 130
        },
        "name": "Barboach",
        "weight": 1.9,
        "gender": "m",
        "type2": "ground",
        "moves": [
            401,
            222,
            90,
            349
        ],
        "type1": "water",
        "ability": "Oblivious"
    },
    "340": {
        "stats": {
            "hp": 361,
            "atk": 192,
            "sdf": 178,
            "spd": 156,
            "def": 182,
            "sat": 188
        },
        "name": "Whiscash",
        "weight": 23.6,
        "gender": "f",
        "type2": "ground",
        "moves": [
            330,
            222,
            209,
            445
        ],
        "type1": "water",
        "ability": "Oblivious"
    },
    "341": {
        "stats": {
            "hp": 248,
            "atk": 217,
            "sdf": 139,
            "spd": 148,
            "def": 187,
            "sat": 122
        },
        "name": "Corphish",
        "weight": 11.5,
        "gender": "m",
        "moves": [
            152,
            12,
            269,
            349
        ],
        "type1": "water",
        "ability": "Adaptability"
    },
    "342": {
        "stats": {
            "hp": 267,
            "atk": 276,
            "sdf": 131,
            "spd": 146,
            "def": 226,
            "sat": 216
        },
        "name": "Crawdaunt",
        "weight": 32.8,
        "gender": "f",
        "type2": "dark",
        "moves": [
            152,
            399,
            249,
            12
        ],
        "type1": "water",
        "ability": "Hyper Cutter"
    },
    "343": {
        "stats": {
            "hp": 284,
            "atk": 116,
            "sdf": 228,
            "spd": 103,
            "def": 178,
            "sat": 116
        },
        "name": "Baltoy",
        "weight": 21.5,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            89,
            94,
            433,
            153
        ],
        "type1": "ground",
        "ability": "Levitate"
    },
    "344": {
        "stats": {
            "hp": 258,
            "atk": 173,
            "sdf": 273,
            "spd": 183,
            "def": 243,
            "sat": 173
        },
        "name": "Claydol",
        "weight": 108,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            414,
            428,
            356,
            120
        ],
        "type1": "ground",
        "ability": "Levitate"
    },
    "345": {
        "stats": {
            "hp": 284,
            "atk": 116,
            "sdf": 243,
            "spd": 93,
            "def": 201,
            "sat": 169
        },
        "name": "Lileep",
        "weight": 23.8,
        "gender": "m",
        "type2": "grass",
        "moves": [
            412,
            246,
            109,
            105
        ],
        "type1": "rock",
        "ability": "Suction Cups"
    },
    "346": {
        "stats": {
            "hp": 311,
            "atk": 196,
            "sdf": 248,
            "spd": 120,
            "def": 228,
            "sat": 196
        },
        "name": "Cradily",
        "weight": 60.4,
        "gender": "f",
        "type2": "grass",
        "moves": [
            202,
            157,
            275,
            182
        ],
        "type1": "rock",
        "ability": "Suction Cups"
    },
    "347": {
        "stats": {
            "hp": 241,
            "atk": 238,
            "sdf": 130,
            "spd": 216,
            "def": 145,
            "sat": 131
        },
        "name": "Anorith",
        "weight": 12.5,
        "gender": "m",
        "type2": "bug",
        "moves": [
            404,
            157,
            397,
            14
        ],
        "type1": "rock",
        "ability": "Battle Armor"
    },
    "348": {
        "stats": {
            "hp": 289,
            "atk": 255,
            "sdf": 194,
            "spd": 124,
            "def": 234,
            "sat": 191
        },
        "name": "Armaldo",
        "weight": 68.2,
        "gender": "f",
        "type2": "bug",
        "moves": [
            404,
            350,
            414,
            300
        ],
        "type1": "rock",
        "ability": "Battle Armor"
    },
    "349": {
        "stats": {
            "hp": 182,
            "atk": 141,
            "sdf": 146,
            "spd": 259,
            "def": 76,
            "sat": 50
        },
        "name": "Feebas",
        "weight": 7.4,
        "gender": "m",
        "moves": [
            127,
            218,
            95,
            321
        ],
        "type1": "water",
        "ability": "Adaptability"
    },
    "350": {
        "stats": {
            "hp": 324,
            "atk": 149,
            "sdf": 279,
            "spd": 191,
            "def": 187,
            "sat": 229
        },
        "name": "Milotic",
        "weight": 162,
        "gender": "f",
        "moves": [
            352,
            406,
            243,
            300
        ],
        "type1": "water",
        "ability": "Marvel Scale"
    },
    "351": {
        "stats": {
            "hp": 286,
            "atk": 144,
            "sdf": 181,
            "spd": 221,
            "def": 181,
            "sat": 181
        },
        "name": "Castform",
        "weight": 0.8,
        "gender": "m",
        "moves": [
            311,
            258,
            240,
            241
        ],
        "type1": "normal",
        "ability": "Forecast"
    },
    "352": {
        "stats": {
            "hp": 306,
            "atk": 198,
            "sdf": 258,
            "spd": 89,
            "def": 221,
            "sat": 152
        },
        "name": "Kecleon",
        "weight": 22,
        "gender": "f",
        "moves": [
            421,
            409,
            60,
            285
        ],
        "type1": "normal",
        "ability": "Color Change"
    },
    "353": {
        "stats": {
            "hp": 230,
            "atk": 167,
            "sdf": 102,
            "spd": 207,
            "def": 106,
            "sat": 225
        },
        "name": "Shuppet",
        "weight": 2.3,
        "gender": "m",
        "moves": [
            247,
            87,
            289,
            194
        ],
        "type1": "ghost",
        "ability": "Insomnia"
    },
    "354": {
        "stats": {
            "hp": 270,
            "atk": 267,
            "sdf": 163,
            "spd": 167,
            "def": 150,
            "sat": 223
        },
        "name": "Banette",
        "weight": 12.5,
        "gender": "f",
        "moves": [
            421,
            389,
            269,
            288
        ],
        "type1": "ghost",
        "ability": "Insomnia"
    },
    "355": {
        "stats": {
            "hp": 240,
            "atk": 107,
            "sdf": 233,
            "spd": 89,
            "def": 256,
            "sat": 99
        },
        "name": "Duskull",
        "weight": 15,
        "gender": "m",
        "moves": [
            101,
            109,
            261,
            174
        ],
        "type1": "ghost",
        "ability": "Levitate"
    },
    "356": {
        "stats": {
            "hp": 222,
            "atk": 177,
            "sdf": 297,
            "spd": 87,
            "def": 297,
            "sat": 157
        },
        "name": "Dusclops",
        "weight": 30.6,
        "gender": "f",
        "moves": [
            325,
            8,
            174,
            433
        ],
        "type1": "ghost",
        "ability": "Pressure"
    },
    "357": {
        "stats": {
            "hp": 340,
            "atk": 155,
            "sdf": 211,
            "spd": 139,
            "def": 203,
            "sat": 199
        },
        "name": "Tropius",
        "weight": 100,
        "gender": "f",
        "type2": "flying",
        "moves": [
            76,
            403,
            241,
            235
        ],
        "type1": "grass",
        "ability": "Solar Power"
    },
    "358": {
        "stats": {
            "hp": 275,
            "atk": 126,
            "sdf": 200,
            "spd": 170,
            "def": 198,
            "sat": 230
        },
        "name": "Chimecho",
        "weight": 1,
        "gender": "m",
        "moves": [
            94,
            347,
            215,
            273
        ],
        "type1": "psychic",
        "ability": "Levitate"
    },
    "359": {
        "stats": {
            "hp": 271,
            "atk": 266,
            "sdf": 156,
            "spd": 186,
            "def": 156,
            "sat": 204
        },
        "name": "Absol",
        "weight": 47,
        "gender": "f",
        "moves": [
            400,
            276,
            351,
            261
        ],
        "type1": "dark",
        "ability": "Super Luck"
    },
    "360": {
        "stats": {
            "hp": 351,
            "atk": 102,
            "sdf": 152,
            "spd": 102,
            "def": 152,
            "sat": 102
        },
        "name": "Wynaut",
        "weight": 14,
        "gender": "m",
        "moves": [
            68,
            243,
            227,
            219
        ],
        "type1": "psychic",
        "ability": "Shadow Tag"
    },
    "361": {
        "stats": {
            "hp": 263,
            "atk": 216,
            "sdf": 158,
            "spd": 136,
            "def": 158,
            "sat": 122
        },
        "name": "Snorunt",
        "weight": 16.8,
        "gender": "f",
        "moves": [
            419,
            242,
            420,
            50
        ],
        "type1": "ice",
        "ability": "Ice Body"
    },
    "362": {
        "stats": {
            "hp": 300,
            "atk": 195,
            "sdf": 195,
            "spd": 195,
            "def": 195,
            "sat": 195
        },
        "name": "Glalie",
        "weight": 256.5,
        "gender": "m",
        "moves": [
            89,
            311,
            329,
            258
        ],
        "type1": "ice",
        "ability": "Ice Body"
    },
    "363": {
        "stats": {
            "hp": 298,
            "atk": 119,
            "sdf": 153,
            "spd": 103,
            "def": 153,
            "sat": 179
        },
        "name": "Spheal",
        "weight": 39.5,
        "gender": "m",
        "type2": "water",
        "moves": [
            162,
            362,
            258,
            182
        ],
        "type1": "ice",
        "ability": "Ice Body"
    },
    "364": {
        "stats": {
            "hp": 346,
            "atk": 156,
            "sdf": 201,
            "spd": 151,
            "def": 201,
            "sat": 213
        },
        "name": "Sealeo",
        "weight": 87.6,
        "gender": "f",
        "type2": "water",
        "moves": [
            62,
            352,
            324,
            46
        ],
        "type1": "ice",
        "ability": "Thick Fat"
    },
    "365": {
        "stats": {
            "hp": 355,
            "atk": 190,
            "sdf": 210,
            "spd": 160,
            "def": 210,
            "sat": 220
        },
        "name": "Walrein",
        "weight": 150.6,
        "gender": "f",
        "type2": "water",
        "moves": [
            291,
            301,
            111,
            227
        ],
        "type1": "ice",
        "ability": "Thick Fat"
    },
    "366": {
        "stats": {
            "hp": 274,
            "atk": 147,
            "sdf": 147,
            "spd": 100,
            "def": 206,
            "sat": 271
        },
        "name": "Clamperl",
        "weight": 52.5,
        "gender": "f",
        "moves": [
            330,
            58,
            109,
            112
        ],
        "type1": "water",
        "ability": "Shell Armor"
    },
    "367": {
        "stats": {
            "hp": 314,
            "atk": 244,
            "sdf": 246,
            "spd": 126,
            "def": 275,
            "sat": 224
        },
        "name": "Huntail",
        "weight": 27,
        "gender": "m",
        "item": "Grip Claw",
        "moves": [
            128,
            20,
            92,
            182
        ],
        "type1": "water",
        "ability": "Water Veil"
    },
    "368": {
        "stats": {
            "hp": 244,
            "atk": 216,
            "sdf": 179,
            "spd": 133,
            "def": 239,
            "sat": 231
        },
        "name": "Gorebyss",
        "weight": 22.6,
        "gender": "f",
        "moves": [
            401,
            362,
            94,
            240
        ],
        "type1": "water",
        "ability": "Swift Swim"
    },
    "369": {
        "stats": {
            "hp": 340,
            "atk": 166,
            "sdf": 165,
            "spd": 146,
            "def": 295,
            "sat": 160
        },
        "name": "Relicanth",
        "weight": 23.4,
        "gender": "m",
        "type2": "rock",
        "moves": [
            457,
            362,
            130,
            300
        ],
        "type1": "water",
        "ability": "Rock Head"
    },
    "370": {
        "stats": {
            "hp": 233,
            "atk": 166,
            "sdf": 172,
            "spd": 243,
            "def": 152,
            "sat": 97
        },
        "name": "Luvdisc",
        "weight": 8.7,
        "gender": "m",
        "moves": [
            127,
            340,
            213,
            186
        ],
        "type1": "water",
        "ability": "Swift Swim"
    },
    "371": {
        "stats": {
            "hp": 250,
            "atk": 214,
            "sdf": 143,
            "spd": 152,
            "def": 175,
            "sat": 117
        },
        "name": "Bagon",
        "weight": 42.1,
        "gender": "f",
        "moves": [
            337,
            424,
            56,
            349
        ],
        "type1": "dragon",
        "ability": "Rock Head"
    },
    "372": {
        "stats": {
            "hp": 276,
            "atk": 231,
            "sdf": 155,
            "spd": 141,
            "def": 241,
            "sat": 144
        },
        "name": "Shelgon",
        "weight": 110.5,
        "gender": "m",
        "moves": [
            407,
            242,
            428,
            334
        ],
        "type1": "dragon",
        "ability": "Rock Head"
    },
    "373": {
        "stats": {
            "hp": 300,
            "atk": 247,
            "sdf": 165,
            "spd": 225,
            "def": 165,
            "sat": 225
        },
        "name": "Salamence",
        "weight": 102.6,
        "gender": "f",
        "type2": "flying",
        "moves": [
            332,
            225,
            53,
            116
        ],
        "type1": "dragon",
        "ability": "Intimidate"
    },
    "374": {
        "stats": {
            "hp": 237,
            "atk": 205,
            "sdf": 172,
            "spd": 108,
            "def": 212,
            "sat": 90
        },
        "name": "Beldum",
        "weight": 95.2,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            442,
            428,
            36,
            334
        ],
        "type1": "steel",
        "ability": "Clear Body"
    },
    "375": {
        "stats": {
            "hp": 266,
            "atk": 210,
            "sdf": 201,
            "spd": 141,
            "def": 241,
            "sat": 135
        },
        "name": "Metang",
        "weight": 202.5,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            309,
            428,
            9,
            97
        ],
        "type1": "steel",
        "ability": "Clear Body"
    },
    "376": {
        "stats": {
            "hp": 270,
            "atk": 275,
            "sdf": 185,
            "spd": 159,
            "def": 265,
            "sat": 175
        },
        "name": "Metagross",
        "weight": 550,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            94,
            232,
            63,
            393
        ],
        "type1": "steel",
        "ability": "Clear Body"
    },
    "377": {
        "stats": {
            "hp": 280,
            "atk": 225,
            "sdf": 215,
            "spd": 115,
            "def": 365,
            "sat": 125
        },
        "name": "Regirock",
        "weight": 230,
        "gender": "-",
        "moves": [
            88,
            359,
            7,
            244
        ],
        "type1": "rock",
        "ability": "Clear Body"
    },
    "378": {
        "stats": {
            "hp": 280,
            "atk": 125,
            "sdf": 365,
            "spd": 115,
            "def": 215,
            "sat": 215
        },
        "name": "Regice",
        "weight": 175,
        "gender": "-",
        "moves": [
            59,
            192,
            430,
            199
        ],
        "type1": "ice",
        "ability": "Clear Body"
    },
    "379": {
        "stats": {
            "hp": 275,
            "atk": 160,
            "sdf": 310,
            "spd": 110,
            "def": 310,
            "sat": 160
        },
        "name": "Registeel",
        "weight": 205,
        "gender": "-",
        "moves": [
            442,
            411,
            205,
            397
        ],
        "type1": "steel",
        "ability": "Clear Body"
    },
    "380": {
        "stats": {
            "hp": 270,
            "atk": 165,
            "sdf": 265,
            "spd": 225,
            "def": 185,
            "sat": 225
        },
        "name": "Latias",
        "weight": 40,
        "gender": "f",
        "type2": "psychic",
        "moves": [
            296,
            337,
            375,
            272
        ],
        "type1": "dragon",
        "ability": "Levitate"
    },
    "381": {
        "stats": {
            "hp": 270,
            "atk": 185,
            "sdf": 225,
            "spd": 225,
            "def": 165,
            "sat": 265
        },
        "name": "Latios",
        "weight": 60,
        "gender": "m",
        "type2": "psychic",
        "moves": [
            295,
            225,
            377,
            262
        ],
        "type1": "dragon",
        "ability": "Levitate"
    },
    "382": {
        "stats": {
            "hp": 310,
            "atk": 225,
            "sdf": 285,
            "spd": 185,
            "def": 185,
            "sat": 275
        },
        "name": "Kyogre",
        "weight": 352,
        "gender": "-",
        "item": "Grip Claw",
        "moves": [
            250,
            87,
            442,
            258
        ],
        "type1": "water",
        "ability": "Drizzle"
    },
    "383": {
        "stats": {
            "hp": 310,
            "atk": 305,
            "sdf": 185,
            "spd": 203,
            "def": 285,
            "sat": 184
        },
        "name": "Groudon",
        "weight": 950,
        "gender": "-",
        "moves": [
            414,
            436,
            184,
            201
        ],
        "type1": "ground",
        "ability": "Drought"
    },
    "384": {
        "stats": {
            "hp": 320,
            "atk": 274,
            "sdf": 185,
            "spd": 205,
            "def": 185,
            "sat": 346
        },
        "name": "Rayquaza",
        "weight": 206.5,
        "gender": "-",
        "type2": "flying",
        "moves": [
            337,
            253,
            249,
            184
        ],
        "type1": "dragon",
        "ability": "Air Lock"
    },
    "385": {
        "stats": {
            "hp": 310,
            "atk": 185,
            "sdf": 205,
            "spd": 225,
            "def": 205,
            "sat": 225
        },
        "name": "Jirachi",
        "weight": 1.1,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            353,
            93,
            34,
            182
        ],
        "type1": "steel",
        "ability": "Serene Grace"
    },
    "386": {
        "stats": {
            "hp": 250,
            "atk": 275,
            "sdf": 145,
            "spd": 335,
            "def": 145,
            "sat": 305
        },
        "name": "Deoxys",
        "weight": 60.8,
        "gender": "-",
        "moves": [
            428,
            63,
            409,
            259
        ],
        "type1": "psychic",
        "ability": "Pressure"
    },
    "387": {
        "stats": {
            "hp": 314,
            "atk": 224,
            "sdf": 146,
            "spd": 98,
            "def": 196,
            "sat": 113
        },
        "name": "Turtwig",
        "weight": 10.2,
        "gender": "m",
        "moves": [
            402,
            242,
            174,
            235
        ],
        "type1": "grass",
        "ability": "Shell Armor"
    },
    "388": {
        "stats": {
            "hp": 313,
            "atk": 214,
            "sdf": 187,
            "spd": 97,
            "def": 227,
            "sat": 229
        },
        "name": "Grotle",
        "weight": 97,
        "gender": "f",
        "moves": [
            412,
            414,
            276,
            73
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "389": {
        "stats": {
            "hp": 363,
            "atk": 254,
            "sdf": 238,
            "spd": 133,
            "def": 278,
            "sat": 238
        },
        "name": "Torterra",
        "weight": 310,
        "gender": "m",
        "type2": "ground",
        "moves": [
            75,
            189,
            317,
            110
        ],
        "type1": "grass",
        "ability": "Overgrow"
    },
    "390": {
        "stats": {
            "hp": 250,
            "atk": 194,
            "sdf": 124,
            "spd": 220,
            "def": 146,
            "sat": 136
        },
        "name": "Chimchar",
        "weight": 6.2,
        "gender": "f",
        "moves": [
            7,
            9,
            67,
            339
        ],
        "type1": "fire",
        "ability": "Iron Fist"
    },
    "391": {
        "stats": {
            "hp": 294,
            "atk": 174,
            "sdf": 171,
            "spd": 197,
            "def": 171,
            "sat": 174
        },
        "name": "Monferno",
        "weight": 22,
        "gender": "f",
        "type2": "fighting",
        "moves": [
            370,
            126,
            417,
            14
        ],
        "type1": "fire",
        "ability": "Blaze"
    },
    "392": {
        "stats": {
            "hp": 272,
            "atk": 223,
            "sdf": 157,
            "spd": 231,
            "def": 172,
            "sat": 200
        },
        "name": "Infernape",
        "weight": 55,
        "gender": "f",
        "type2": "fighting",
        "moves": [
            257,
            280,
            269,
            347
        ],
        "type1": "fire",
        "ability": "Blaze"
    },
    "393": {
        "stats": {
            "hp": 268,
            "atk": 124,
            "sdf": 148,
            "spd": 158,
            "def": 142,
            "sat": 243
        },
        "name": "Piplup",
        "weight": 5.2,
        "gender": "m",
        "moves": [
            56,
            58,
            447,
            97
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "394": {
        "stats": {
            "hp": 275,
            "atk": 156,
            "sdf": 194,
            "spd": 142,
            "def": 195,
            "sat": 204
        },
        "name": "Prinplup",
        "weight": 23,
        "gender": "f",
        "moves": [
            57,
            29,
            196,
            297
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "395": {
        "stats": {
            "hp": 303,
            "atk": 224,
            "sdf": 232,
            "spd": 135,
            "def": 206,
            "sat": 227
        },
        "name": "Empoleon",
        "weight": 84.5,
        "gender": "f",
        "type2": "steel",
        "moves": [
            211,
            453,
            365,
            54
        ],
        "type1": "water",
        "ability": "Torrent"
    },
    "396": {
        "stats": {
            "hp": 222,
            "atk": 229,
            "sdf": 96,
            "spd": 219,
            "def": 96,
            "sat": 86
        },
        "name": "Starly",
        "weight": 2,
        "gender": "m",
        "type2": "flying",
        "moves": [
            413,
            38,
            283,
            366
        ],
        "type1": "normal",
        "ability": "Reckless"
    },
    "397": {
        "stats": {
            "hp": 276,
            "atk": 211,
            "sdf": 141,
            "spd": 245,
            "def": 161,
            "sat": 104
        },
        "name": "Staravia",
        "weight": 15.5,
        "gender": "f",
        "type2": "flying",
        "moves": [
            19,
            290,
            279,
            445
        ],
        "type1": "normal",
        "ability": "Intimidate"
    },
    "398": {
        "stats": {
            "hp": 290,
            "atk": 220,
            "sdf": 115,
            "spd": 240,
            "def": 155,
            "sat": 105
        },
        "name": "Staraptor",
        "weight": 24.9,
        "gender": "m",
        "type2": "flying",
        "moves": [
            36,
            370,
            310,
            18
        ],
        "type1": "normal",
        "ability": "Reckless"
    },
    "399": {
        "stats": {
            "hp": 275,
            "atk": 190,
            "sdf": 163,
            "spd": 98,
            "def": 132,
            "sat": 95
        },
        "name": "Bidoof",
        "weight": 20,
        "gender": "m",
        "moves": [
            162,
            98,
            174,
            316
        ],
        "type1": "normal",
        "ability": "Simple"
    },
    "400": {
        "stats": {
            "hp": 317,
            "atk": 201,
            "sdf": 174,
            "spd": 196,
            "def": 174,
            "sat": 193
        },
        "name": "Bibarel",
        "weight": 31.5,
        "gender": "f",
        "type2": "water",
        "moves": [
            130,
            352,
            451,
            269
        ],
        "type1": "normal",
        "ability": "Simple"
    },
    "401": {
        "stats": {
            "hp": 278,
            "atk": 86,
            "sdf": 176,
            "spd": 86,
            "def": 139,
            "sat": 77
        },
        "name": "Kricketot",
        "weight": 2.2,
        "gender": "m",
        "moves": [
            450,
            189,
            283,
            81
        ],
        "type1": "bug",
        "ability": "Shed Skin"
    },
    "402": {
        "stats": {
            "hp": 303,
            "atk": 214,
            "sdf": 146,
            "spd": 191,
            "def": 146,
            "sat": 138
        },
        "name": "Kricketune",
        "weight": 25.5,
        "gender": "m",
        "moves": [
            404,
            280,
            47,
            14
        ],
        "type1": "bug",
        "ability": "Swarm"
    },
    "403": {
        "stats": {
            "hp": 252,
            "atk": 251,
            "sdf": 125,
            "spd": 126,
            "def": 126,
            "sat": 104
        },
        "name": "Shinx",
        "weight": 9.5,
        "gender": "f",
        "moves": [
            422,
            216,
            44,
            86
        ],
        "type1": "electric",
        "ability": "Intimidate"
    },
    "404": {
        "stats": {
            "hp": 286,
            "atk": 256,
            "sdf": 167,
            "spd": 165,
            "def": 167,
            "sat": 140
        },
        "name": "Luxio",
        "weight": 30.5,
        "gender": "m",
        "moves": [
            209,
            400,
            113,
            268
        ],
        "type1": "electric",
        "ability": "Intimidate"
    },
    "405": {
        "stats": {
            "hp": 285,
            "atk": 234,
            "sdf": 178,
            "spd": 160,
            "def": 178,
            "sat": 231
        },
        "name": "Luxray",
        "weight": 42,
        "gender": "f",
        "moves": [
            351,
            276,
            423,
            214
        ],
        "type1": "electric",
        "ability": "Guts"
    },
    "406": {
        "stats": {
            "hp": 222,
            "atk": 86,
            "sdf": 176,
            "spd": 209,
            "def": 106,
            "sat": 218
        },
        "name": "Budew",
        "weight": 1.2,
        "gender": "m",
        "type2": "poison",
        "moves": [
            437,
            188,
            326,
            79
        ],
        "type1": "grass",
        "ability": "Poison Point"
    },
    "407": {
        "stats": {
            "hp": 258,
            "atk": 190,
            "sdf": 243,
            "spd": 213,
            "def": 143,
            "sat": 254
        },
        "name": "Roserade",
        "weight": 14.5,
        "gender": "f",
        "type2": "poison",
        "moves": [
            80,
            398,
            311,
            240
        ],
        "type1": "grass",
        "ability": "Poison Point"
    },
    "408": {
        "stats": {
            "hp": 286,
            "atk": 297,
            "sdf": 107,
            "spd": 179,
            "def": 127,
            "sat": 96
        },
        "name": "Cranidos",
        "weight": 31.5,
        "gender": "m",
        "moves": [
            457,
            89,
            70,
            184
        ],
        "type1": "rock",
        "ability": "Mold Breaker"
    },
    "409": {
        "stats": {
            "hp": 334,
            "atk": 308,
            "sdf": 179,
            "spd": 150,
            "def": 167,
            "sat": 143
        },
        "name": "Rampardos",
        "weight": 102.5,
        "gender": "m",
        "moves": [
            157,
            431,
            249,
            397
        ],
        "type1": "rock",
        "ability": "Mold Breaker"
    },
    "410": {
        "stats": {
            "hp": 264,
            "atk": 155,
            "sdf": 233,
            "spd": 58,
            "def": 306,
            "sat": 120
        },
        "name": "Shieldon",
        "weight": 57,
        "gender": "m",
        "type2": "steel",
        "moves": [
            231,
            444,
            90,
            368
        ],
        "type1": "rock",
        "ability": "Soundproof"
    },
    "411": {
        "stats": {
            "hp": 298,
            "atk": 140,
            "sdf": 281,
            "spd": 58,
            "def": 341,
            "sat": 155
        },
        "name": "Bastiodon",
        "weight": 149.5,
        "gender": "m",
        "type2": "steel",
        "moves": [
            430,
            126,
            368,
            319
        ],
        "type1": "rock",
        "ability": "Sturdy"
    },
    "412": {
        "stats": {
            "hp": 221,
            "atk": 172,
            "sdf": 125,
            "spd": 96,
            "def": 126,
            "sat": 156
        },
        "name": "Burmy",
        "weight": 3.4,
        "gender": "f",
        "moves": [
            450,
            237,
            33,
            182
        ],
        "type1": "bug",
        "ability": "Shed Skin"
    },
    "413": {
        "stats": {
            "hp": 265,
            "atk": 123,
            "sdf": 250,
            "spd": 133,
            "def": 231,
            "sat": 198
        },
        "name": "Wormadam",
        "weight": 6.5,
        "gender": "f",
        "type2": "grass",
        "moves": [
            437,
            324,
            94,
            74
        ],
        "type1": "bug",
        "ability": "Anticipation"
    },
    "414": {
        "stats": {
            "hp": 313,
            "atk": 224,
            "sdf": 168,
            "spd": 199,
            "def": 168,
            "sat": 224
        },
        "name": "Mothim",
        "weight": 23.3,
        "gender": "m",
        "type2": "flying",
        "moves": [
            403,
            450,
            293,
            355
        ],
        "type1": "bug",
        "ability": "Tinted Lens"
    },
    "415": {
        "stats": {
            "hp": 222,
            "atk": 86,
            "sdf": 141,
            "spd": 216,
            "def": 141,
            "sat": 138
        },
        "name": "Combee",
        "weight": 5.5,
        "gender": "m",
        "type2": "flying",
        "moves": [
            405,
            314,
            189,
            456
        ],
        "type1": "bug",
        "ability": "Honey Gather"
    },
    "416": {
        "stats": {
            "hp": 282,
            "atk": 157,
            "sdf": 241,
            "spd": 170,
            "def": 241,
            "sat": 197
        },
        "name": "Vespiquen",
        "weight": 38.5,
        "gender": "f",
        "type2": "flying",
        "moves": [
            454,
            314,
            408,
            455
        ],
        "type1": "bug",
        "ability": "Pressure"
    },
    "417": {
        "stats": {
            "hp": 267,
            "atk": 99,
            "sdf": 218,
            "spd": 232,
            "def": 182,
            "sat": 172
        },
        "name": "Pachirisu",
        "weight": 3.9,
        "gender": "f",
        "moves": [
            162,
            85,
            447,
            207
        ],
        "type1": "electric",
        "ability": "Volt Absorb"
    },
    "418": {
        "stats": {
            "hp": 264,
            "atk": 196,
            "sdf": 109,
            "spd": 219,
            "def": 107,
            "sat": 169
        },
        "name": "Buizel",
        "weight": 29.5,
        "gender": "m",
        "moves": [
            127,
            58,
            280,
            240
        ],
        "type1": "water",
        "ability": "Swift Swim"
    },
    "419": {
        "stats": {
            "hp": 309,
            "atk": 219,
            "sdf": 147,
            "spd": 264,
            "def": 144,
            "sat": 204
        },
        "name": "Floatzel",
        "weight": 33.5,
        "gender": "f",
        "moves": [
            401,
            242,
            269,
            339
        ],
        "type1": "water",
        "ability": "Water Veil"
    },
    "420": {
        "stats": {
            "hp": 252,
            "atk": 95,
            "sdf": 147,
            "spd": 139,
            "def": 131,
            "sat": 245
        },
        "name": "Cherubi",
        "weight": 3.3,
        "gender": "m",
        "moves": [
            76,
            311,
            73,
            241
        ],
        "type1": "grass",
        "ability": "Chlorophyll"
    },
    "421": {
        "stats": {
            "hp": 306,
            "atk": 201,
            "sdf": 217,
            "spd": 231,
            "def": 201,
            "sat": 189
        },
        "name": "Cherrim",
        "weight": 9.3,
        "gender": "f",
        "moves": [
            402,
            218,
            321,
            241
        ],
        "type1": "grass",
        "ability": "Flower Gift"
    },
    "422": {
        "stats": {
            "hp": 318,
            "atk": 174,
            "sdf": 185,
            "spd": 129,
            "def": 157,
            "sat": 135
        },
        "name": "Shellos",
        "weight": 6.3,
        "gender": "m",
        "moves": [
            291,
            90,
            156,
            214
        ],
        "type1": "water",
        "ability": "Storm Drain"
    },
    "423": {
        "stats": {
            "hp": 362,
            "atk": 201,
            "sdf": 199,
            "spd": 113,
            "def": 171,
            "sat": 219
        },
        "name": "Gastrodon",
        "weight": 29.9,
        "gender": "m",
        "type2": "ground",
        "moves": [
            89,
            127,
            68,
            106
        ],
        "type1": "water",
        "ability": "Storm Drain"
    },
    "424": {
        "stats": {
            "hp": 290,
            "atk": 235,
            "sdf": 167,
            "spd": 265,
            "def": 167,
            "sat": 155
        },
        "name": "Ambipom",
        "weight": 20.3,
        "gender": "f",
        "moves": [
            252,
            15,
            332,
            103
        ],
        "type1": "normal",
        "ability": "Technician"
    },
    "425": {
        "stats": {
            "hp": 321,
            "atk": 122,
            "sdf": 145,
            "spd": 240,
            "def": 125,
            "sat": 198
        },
        "name": "Drifloon",
        "weight": 1.2,
        "gender": "f",
        "type2": "flying",
        "moves": [
            247,
            314,
            85,
            194
        ],
        "type1": "ghost",
        "ability": "Aftermath"
    },
    "426": {
        "stats": {
            "hp": 410,
            "atk": 165,
            "sdf": 145,
            "spd": 197,
            "def": 125,
            "sat": 216
        },
        "name": "Drifblim",
        "weight": 15,
        "gender": "f",
        "type2": "flying",
        "moves": [
            466,
            87,
            311,
            240
        ],
        "type1": "ghost",
        "ability": "Aftermath"
    },
    "427": {
        "stats": {
            "hp": 252,
            "atk": 254,
            "sdf": 148,
            "spd": 269,
            "def": 124,
            "sat": 111
        },
        "name": "Buneary",
        "weight": 5.5,
        "gender": "m",
        "moves": [
            218,
            26,
            8,
            204
        ],
        "type1": "normal",
        "ability": "Limber"
    },
    "428": {
        "stats": {
            "hp": 263,
            "atk": 207,
            "sdf": 220,
            "spd": 245,
            "def": 196,
            "sat": 143
        },
        "name": "Lopunny",
        "weight": 33.3,
        "gender": "f",
        "moves": [
            146,
            26,
            445,
            193
        ],
        "type1": "normal",
        "ability": "Cute Charm"
    },
    "429": {
        "stats": {
            "hp": 259,
            "atk": 192,
            "sdf": 233,
            "spd": 245,
            "def": 143,
            "sat": 219
        },
        "name": "Mismagius",
        "weight": 4.4,
        "gender": "f",
        "moves": [
            247,
            389,
            86,
            286
        ],
        "type1": "ghost",
        "ability": "Levitate"
    },
    "430": {
        "stats": {
            "hp": 331,
            "atk": 248,
            "sdf": 130,
            "spd": 184,
            "def": 130,
            "sat": 236
        },
        "name": "Honchkrow",
        "weight": 27.3,
        "gender": "f",
        "type2": "flying",
        "moves": [
            19,
            400,
            269,
            18
        ],
        "type1": "dark",
        "ability": "Super Luck"
    },
    "431": {
        "stats": {
            "hp": 247,
            "atk": 203,
            "sdf": 118,
            "spd": 243,
            "def": 128,
            "sat": 102
        },
        "name": "Glameow",
        "weight": 3.9,
        "gender": "f",
        "moves": [
            252,
            387
        ],
        "type1": "normal",
        "ability": "Limber"
    },
    "432": {
        "stats": {
            "hp": 285,
            "atk": 202,
            "sdf": 156,
            "spd": 288,
            "def": 166,
            "sat": 149
        },
        "name": "Purugly",
        "weight": 43.8,
        "gender": "f",
        "moves": [
            34,
            91,
            185,
            274
        ],
        "type1": "normal",
        "ability": "Thick Fat"
    },
    "433": {
        "stats": {
            "hp": 294,
            "atk": 86,
            "sdf": 168,
            "spd": 126,
            "def": 184,
            "sat": 166
        },
        "name": "Chingling",
        "weight": 0.6,
        "gender": "m",
        "moves": [
            94,
            324,
            347,
            105
        ],
        "type1": "psychic",
        "ability": "Levitate"
    },
    "434": {
        "stats": {
            "hp": 291,
            "atk": 222,
            "sdf": 142,
            "spd": 199,
            "def": 154,
            "sat": 106
        },
        "name": "Stunky",
        "weight": 19.2,
        "gender": "m",
        "type2": "dark",
        "moves": [
            389,
            386,
            91,
            207
        ],
        "type1": "poison",
        "ability": "Aftermath"
    },
    "435": {
        "stats": {
            "hp": 346,
            "atk": 221,
            "sdf": 157,
            "spd": 182,
            "def": 169,
            "sat": 194
        },
        "name": "Skuntank",
        "weight": 38,
        "gender": "m",
        "type2": "dark",
        "moves": [
            400,
            53,
            139,
            114
        ],
        "type1": "poison",
        "ability": "Aftermath"
    },
    "436": {
        "stats": {
            "hp": 287,
            "atk": 121,
            "sdf": 208,
            "spd": 45,
            "def": 208,
            "sat": 156
        },
        "name": "Bronzor",
        "weight": 60.5,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            326,
            360,
            377,
            433
        ],
        "type1": "steel",
        "ability": "Levitate"
    },
    "437": {
        "stats": {
            "hp": 274,
            "atk": 213,
            "sdf": 267,
            "spd": 90,
            "def": 267,
            "sat": 212
        },
        "name": "Bronzong",
        "weight": 187,
        "gender": "-",
        "type2": "psychic",
        "moves": [
            93,
            360,
            451,
            104
        ],
        "type1": "steel",
        "ability": "Heatproof"
    },
    "438": {
        "stats": {
            "hp": 285,
            "atk": 259,
            "sdf": 169,
            "spd": 56,
            "def": 226,
            "sat": 50
        },
        "name": "Bonsly",
        "weight": 15,
        "gender": "m",
        "moves": [
            157,
            389,
            174,
            153
        ],
        "type1": "rock",
        "ability": "Sturdy"
    },
    "439": {
        "stats": {
            "hp": 206,
            "atk": 77,
            "sdf": 216,
            "spd": 200,
            "def": 128,
            "sat": 255
        },
        "name": "Mime Jr.",
        "weight": 13,
        "gender": "f",
        "moves": [
            94,
            85,
            115,
            298
        ],
        "type1": "psychic",
        "ability": "Filter"
    },
    "440": {
        "stats": {
            "hp": 404,
            "atk": 41,
            "sdf": 167,
            "spd": 96,
            "def": 119,
            "sat": 66
        },
        "name": "Happiny",
        "weight": 24.4,
        "gender": "f",
        "moves": [
            352,
            68,
            92,
            135
        ],
        "type1": "normal",
        "ability": "Serene Grace"
    },
    "441": {
        "stats": {
            "hp": 299,
            "atk": 154,
            "sdf": 126,
            "spd": 246,
            "def": 132,
            "sat": 226
        },
        "name": "Chatot",
        "weight": 1.9,
        "gender": "m",
        "type2": "flying",
        "moves": [
            304,
            448,
            102,
            47
        ],
        "type1": "normal",
        "ability": "Keen Eye"
    },
    "442": {
        "stats": {
            "hp": 240,
            "atk": 219,
            "sdf": 225,
            "spd": 115,
            "def": 251,
            "sat": 219
        },
        "name": "Spiritomb",
        "weight": 108,
        "gender": "m",
        "type2": "dark",
        "moves": [
            399,
            425,
            174,
            180
        ],
        "type1": "ghost",
        "ability": "Pressure"
    },
    "443": {
        "stats": {
            "hp": 279,
            "atk": 239,
            "sdf": 147,
            "spd": 141,
            "def": 147,
            "sat": 104
        },
        "name": "Gible",
        "weight": 20.5,
        "gender": "f",
        "type2": "ground",
        "moves": [
            200,
            89,
            444,
            203
        ],
        "type1": "dragon",
        "ability": "Rough Skin"
    },
    "444": {
        "stats": {
            "hp": 283,
            "atk": 222,
            "sdf": 152,
            "spd": 206,
            "def": 172,
            "sat": 142
        },
        "name": "Gabite",
        "weight": 56,
        "gender": "f",
        "type2": "ground",
        "moves": [
            407,
            91,
            201,
            446
        ],
        "type1": "dragon",
        "ability": "Rough Skin"
    },
    "445": {
        "stats": {
            "hp": 343,
            "atk": 238,
            "sdf": 192,
            "spd": 209,
            "def": 212,
            "sat": 181
        },
        "name": "Garchomp",
        "weight": 95,
        "gender": "f",
        "type2": "ground",
        "moves": [
            225,
            341,
            317,
            201
        ],
        "type1": "dragon",
        "ability": "Sand Veil"
    },
    "446": {
        "stats": {
            "hp": 419,
            "atk": 214,
            "sdf": 235,
            "spd": 68,
            "def": 124,
            "sat": 103
        },
        "name": "Munchlax",
        "weight": 105,
        "gender": "m",
        "moves": [
            34,
            7,
            133,
            174
        ],
        "type1": "normal",
        "ability": "Thick Fat"
    },
    "447": {
        "stats": {
            "hp": 246,
            "atk": 201,
            "sdf": 141,
            "spd": 201,
            "def": 141,
            "sat": 95
        },
        "name": "Riolu",
        "weight": 20.2,
        "gender": "m",
        "moves": [
            136,
            299,
            9,
            14
        ],
        "type1": "fighting",
        "ability": "Steadfast"
    },
    "448": {
        "stats": {
            "hp": 276,
            "atk": 251,
            "sdf": 171,
            "spd": 211,
            "def": 171,
            "sat": 261
        },
        "name": "Lucario",
        "weight": 54,
        "gender": "m",
        "type2": "steel",
        "moves": [
            396,
            418,
            198,
            382
        ],
        "type1": "fighting",
        "ability": "Inner Focus"
    },
    "449": {
        "stats": {
            "hp": 311,
            "atk": 180,
            "sdf": 154,
            "spd": 121,
            "def": 212,
            "sat": 129
        },
        "name": "Hippopotas",
        "weight": 49.5,
        "gender": "m",
        "moves": [
            89,
            317,
            174,
            281
        ],
        "type1": "ground",
        "ability": "Sand Stream"
    },
    "450": {
        "stats": {
            "hp": 389,
            "atk": 355,
            "sdf": 212,
            "spd": 117,
            "def": 272,
            "sat": 141
        },
        "name": "Hippowdon",
        "weight": 300,
        "gender": "m",
        "item": "Grip Claw",
        "moves": [
            328,
            352,
            92,
            203
        ],
        "type1": "ground",
        "ability": "Sand Stream"
    },
    "451": {
        "stats": {
            "hp": 243,
            "atk": 178,
            "sdf": 167,
            "spd": 228,
            "def": 216,
            "sat": 86
        },
        "name": "Skorupi",
        "weight": 12,
        "gender": "m",
        "type2": "bug",
        "moves": [
            404,
            440,
            91,
            109
        ],
        "type1": "poison",
        "ability": "Sniper"
    },
    "452": {
        "stats": {
            "hp": 278,
            "atk": 191,
            "sdf": 183,
            "spd": 223,
            "def": 253,
            "sat": 168
        },
        "name": "Drapion",
        "weight": 61.5,
        "gender": "f",
        "type2": "dark",
        "moves": [
            188,
            400,
            390,
            367
        ],
        "type1": "poison",
        "ability": "Sniper"
    },
    "453": {
        "stats": {
            "hp": 262,
            "atk": 203,
            "sdf": 141,
            "spd": 161,
            "def": 141,
            "sat": 142
        },
        "name": "Croagunk",
        "weight": 23,
        "gender": "f",
        "type2": "fighting",
        "moves": [
            441,
            238,
            389,
            207
        ],
        "type1": "poison",
        "ability": "Dry Skin"
    },
    "454": {
        "stats": {
            "hp": 305,
            "atk": 221,
            "sdf": 164,
            "spd": 204,
            "def": 164,
            "sat": 226
        },
        "name": "Toxicroak",
        "weight": 44.4,
        "gender": "f",
        "type2": "fighting",
        "moves": [
            252,
            411,
            188,
            260
        ],
        "type1": "poison",
        "ability": "Dry Skin"
    },
    "455": {
        "stats": {
            "hp": 290,
            "atk": 237,
            "sdf": 192,
            "spd": 129,
            "def": 192,
            "sat": 196
        },
        "name": "Carnivine",
        "weight": 27,
        "gender": "f",
        "moves": [
            438,
            290,
            78,
            380
        ],
        "type1": "grass",
        "ability": "Levitate"
    },
    "456": {
        "stats": {
            "hp": 261,
            "atk": 216,
            "sdf": 179,
            "spd": 168,
            "def": 169,
            "sat": 120
        },
        "name": "Finneon",
        "weight": 7,
        "gender": "m",
        "moves": [
            127,
            340,
            371,
            240
        ],
        "type1": "water",
        "ability": "Swift Swim"
    },
    "457": {
        "stats": {
            "hp": 293,
            "atk": 164,
            "sdf": 222,
            "spd": 232,
            "def": 202,
            "sat": 206
        },
        "name": "Lumineon",
        "weight": 24,
        "gender": "f",
        "moves": [
            291,
            60,
            318,
            204
        ],
        "type1": "water",
        "ability": "Water Veil"
    },
    "458": {
        "stats": {
            "hp": 243,
            "atk": 79,
            "sdf": 288,
            "spd": 148,
            "def": 148,
            "sat": 184
        },
        "name": "Mantyke",
        "weight": 65,
        "gender": "f",
        "type2": "flying",
        "moves": [
            57,
            58,
            109,
            92
        ],
        "type1": "water",
        "ability": "Water Veil"
    },
    "459": {
        "stats": {
            "hp": 274,
            "atk": 155,
            "sdf": 169,
            "spd": 129,
            "def": 163,
            "sat": 173
        },
        "name": "Snover",
        "weight": 50.5,
        "gender": "m",
        "type2": "ice",
        "moves": [
            59,
            202,
            320,
            329
        ],
        "type1": "grass",
        "ability": "Snow Warning"
    },
    "460": {
        "stats": {
            "hp": 319,
            "atk": 218,
            "sdf": 204,
            "spd": 154,
            "def": 184,
            "sat": 218
        },
        "name": "Abomasnow",
        "weight": 135.5,
        "gender": "f",
        "type2": "ice",
        "moves": [
            402,
            196,
            411,
            275
        ],
        "type1": "grass",
        "ability": "Snow Warning"
    },
    "461": {
        "stats": {
            "hp": 277,
            "atk": 244,
            "sdf": 187,
            "spd": 282,
            "def": 162,
            "sat": 150
        },
        "name": "Weavile",
        "weight": 34,
        "gender": "f",
        "type2": "ice",
        "moves": [
            8,
            400,
            411,
            43
        ],
        "type1": "dark",
        "ability": "Pressure"
    },
    "462": {
        "stats": {
            "hp": 275,
            "atk": 170,
            "sdf": 210,
            "spd": 165,
            "def": 260,
            "sat": 261
        },
        "name": "Magnezone",
        "weight": 180,
        "gender": "-",
        "type2": "steel",
        "moves": [
            351,
            429,
            161,
            393
        ],
        "type1": "electric",
        "ability": "Sturdy"
    },
    "463": {
        "stats": {
            "hp": 357,
            "atk": 202,
            "sdf": 222,
            "spd": 132,
            "def": 222,
            "sat": 192
        },
        "name": "Lickilicky",
        "weight": 140,
        "gender": "f",
        "moves": [
            63,
            223,
            205,
            378
        ],
        "type1": "normal",
        "ability": "Own Tempo"
    },
    "464": {
        "stats": {
            "hp": 344,
            "atk": 279,
            "sdf": 161,
            "spd": 121,
            "def": 269,
            "sat": 161
        },
        "name": "Rhyperior",
        "weight": 282.8,
        "gender": "f",
        "type2": "rock",
        "moves": [
            350,
            222,
            32,
            446
        ],
        "type1": "ground",
        "ability": "Lightning Rod"
    },
    "465": {
        "stats": {
            "hp": 339,
            "atk": 209,
            "sdf": 149,
            "spd": 134,
            "def": 284,
            "sat": 228
        },
        "name": "Tangrowth",
        "weight": 128.6,
        "gender": "f",
        "moves": [
            76,
            246,
            78,
            241
        ],
        "type1": "grass",
        "ability": "Leaf Guard"
    },
    "466": {
        "stats": {
            "hp": 284,
            "atk": 247,
            "sdf": 218,
            "spd": 219,
            "def": 163,
            "sat": 219
        },
        "name": "Electivire",
        "weight": 138.6,
        "gender": "f",
        "moves": [
            9,
            27,
            98,
            43
        ],
        "type1": "electric",
        "ability": "Motor Drive"
    },
    "467": {
        "stats": {
            "hp": 284,
            "atk": 219,
            "sdf": 219,
            "spd": 195,
            "def": 179,
            "sat": 251
        },
        "name": "Magmortar",
        "weight": 68,
        "gender": "f",
        "moves": [
            7,
            94,
            2,
            123
        ],
        "type1": "fire",
        "ability": "Flame Body"
    },
    "468": {
        "stats": {
            "hp": 280,
            "atk": 115,
            "sdf": 235,
            "spd": 165,
            "def": 195,
            "sat": 220
        },
        "name": "Togekiss",
        "weight": 38,
        "gender": "f",
        "type2": "flying",
        "moves": [
            245,
            314,
            396,
            381
        ],
        "type1": "normal",
        "ability": "Hustle"
    },
    "469": {
        "stats": {
            "hp": 309,
            "atk": 202,
            "sdf": 144,
            "spd": 222,
            "def": 183,
            "sat": 264
        },
        "name": "Yanmega",
        "weight": 51.5,
        "gender": "f",
        "type2": "flying",
        "moves": [
            403,
            318,
            98,
            18
        ],
        "type1": "bug",
        "ability": "Tinted Lens"
    },
    "470": {
        "stats": {
            "hp": 266,
            "atk": 225,
            "sdf": 161,
            "spd": 221,
            "def": 291,
            "sat": 166
        },
        "name": "Leafeon",
        "weight": 25.5,
        "gender": "m",
        "moves": [
            348,
            247,
            98,
            445
        ],
        "type1": "grass",
        "ability": "Leaf Guard"
    },
    "471": {
        "stats": {
            "hp": 266,
            "atk": 166,
            "sdf": 221,
            "spd": 161,
            "def": 251,
            "sat": 261
        },
        "name": "Glaceon",
        "weight": 25.9,
        "gender": "f",
        "moves": [
            59,
            129,
            44,
            243
        ],
        "type1": "ice",
        "ability": "Snow Cloak"
    },
    "472": {
        "stats": {
            "hp": 281,
            "atk": 194,
            "sdf": 176,
            "spd": 216,
            "def": 303,
            "sat": 116
        },
        "name": "Gliscor",
        "weight": 42.5,
        "gender": "f",
        "type2": "flying",
        "moves": [
            91,
            332,
            269,
            379
        ],
        "type1": "ground",
        "ability": "Hyper Cutter"
    },
    "473": {
        "stats": {
            "hp": 355,
            "atk": 261,
            "sdf": 150,
            "spd": 190,
            "def": 190,
            "sat": 187
        },
        "name": "Mamoswine",
        "weight": 291,
        "gender": "m",
        "type2": "ground",
        "moves": [
            414,
            423,
            420,
            258
        ],
        "type1": "ice",
        "ability": "Snow Cloak"
    },
    "474": {
        "stats": {
            "hp": 305,
            "atk": 209,
            "sdf": 180,
            "spd": 210,
            "def": 170,
            "sat": 270
        },
        "name": "Porygon-Z",
        "weight": 34,
        "gender": "-",
        "moves": [
            129,
            247,
            168,
            160
        ],
        "type1": "normal",
        "ability": "Adaptability"
    },
    "475": {
        "stats": {
            "hp": 272,
            "atk": 252,
            "sdf": 261,
            "spd": 191,
            "def": 177,
            "sat": 161
        },
        "name": "Gallade",
        "weight": 52,
        "gender": "m",
        "type2": "fighting",
        "moves": [
            427,
            409,
            425,
            262
        ],
        "type1": "psychic",
        "ability": "Steadfast"
    },
    "476": {
        "stats": {
            "hp": 256,
            "atk": 141,
            "sdf": 331,
            "spd": 111,
            "def": 321,
            "sat": 181
        },
        "name": "Probopass",
        "weight": 340,
        "gender": "m",
        "type2": "steel",
        "moves": [
            408,
            443,
            192,
            356
        ],
        "type1": "rock",
        "ability": "Sturdy"
    },
    "477": {
        "stats": {
            "hp": 293,
            "atk": 328,
            "sdf": 307,
            "spd": 85,
            "def": 307,
            "sat": 166
        },
        "name": "Dusknoir",
        "weight": 106.6,
        "gender": "f",
        "moves": [
            310,
            249,
            269,
            433
        ],
        "type1": "ghost",
        "ability": "Pressure"
    },
    "478": {
        "stats": {
            "hp": 296,
            "atk": 167,
            "sdf": 191,
            "spd": 271,
            "def": 191,
            "sat": 234
        },
        "name": "Froslass",
        "weight": 26.6,
        "gender": "f",
        "type2": "ghost",
        "moves": [
            466,
            181,
            50,
            194
        ],
        "type1": "ice",
        "ability": "Snow Cloak"
    },
    "479": {
        "stats": {
            "hp": 244,
            "atk": 139,
            "sdf": 212,
            "spd": 221,
            "def": 173,
            "sat": 229
        },
        "name": "Rotom",
        "weight": 0.3,
        "gender": "-",
        "type2": "ghost",
        "moves": [
            247,
            451,
            109,
            220
        ],
        "type1": "electric",
        "ability": "Levitate"
    },
    "480": {
        "stats": {
            "hp": 281,
            "atk": 158,
            "sdf": 286,
            "spd": 216,
            "def": 314,
            "sat": 176
        },
        "name": "Uxie",
        "weight": 0.3,
        "gender": "-",
        "moves": [
            428,
            8,
            207,
            244
        ],
        "type1": "psychic",
        "ability": "Levitate"
    },
    "481": {
        "stats": {
            "hp": 275,
            "atk": 220,
            "sdf": 220,
            "spd": 170,
            "def": 220,
            "sat": 220
        },
        "name": "Mesprit",
        "weight": 0.3,
        "gender": "-",
        "moves": [
            326,
            9,
            115,
            383
        ],
        "type1": "psychic",
        "ability": "Levitate"
    },
    "482": {
        "stats": {
            "hp": 265,
            "atk": 260,
            "sdf": 150,
            "spd": 240,
            "def": 150,
            "sat": 260
        },
        "name": "Azelf",
        "weight": 0.3,
        "gender": "-",
        "moves": [
            326,
            7,
            113,
            272
        ],
        "type1": "psychic",
        "ability": "Levitate"
    },
    "483": {
        "stats": {
            "hp": 310,
            "atk": 245,
            "sdf": 205,
            "spd": 205,
            "def": 245,
            "sat": 275
        },
        "name": "Dialga",
        "weight": 683,
        "gender": "-",
        "type2": "dragon",
        "moves": [
            232,
            239,
            368,
            46
        ],
        "type1": "steel",
        "ability": "Pressure"
    },
    "484": {
        "stats": {
            "hp": 290,
            "atk": 220,
            "sdf": 245,
            "spd": 205,
            "def": 205,
            "sat": 335
        },
        "name": "Palkia",
        "weight": 336,
        "gender": "-",
        "type2": "dragon",
        "moves": [
            291,
            239,
            189,
            433
        ],
        "type1": "water",
        "ability": "Pressure"
    },
    "485": {
        "stats": {
            "hp": 292,
            "atk": 203,
            "sdf": 217,
            "spd": 159,
            "def": 217,
            "sat": 238
        },
        "name": "Heatran",
        "weight": 430,
        "gender": "f",
        "item": "Grip Claw",
        "type2": "steel",
        "moves": [
            463,
            249,
            269,
            203
        ],
        "type1": "fire",
        "ability": "Flash Fire"
    },
    "486": {
        "stats": {
            "hp": 361,
            "atk": 292,
            "sdf": 319,
            "spd": 206,
            "def": 319,
            "sat": 181
        },
        "name": "Regigigas",
        "weight": 420,
        "gender": "-",
        "moves": [
            416,
            428,
            409,
            462
        ],
        "type1": "normal",
        "ability": "Slow Start"
    },
    "487": {
        "stats": {
            "hp": 410,
            "atk": 184,
            "sdf": 245,
            "spd": 185,
            "def": 245,
            "sat": 225
        },
        "name": "Giratina",
        "weight": 750,
        "gender": "-",
        "type2": "dragon",
        "moves": [
            421,
            239,
            163,
            377
        ],
        "type1": "ghost",
        "ability": "Pressure"
    },
    "488": {
        "stats": {
            "hp": 350,
            "atk": 145,
            "sdf": 265,
            "spd": 175,
            "def": 245,
            "sat": 164
        },
        "name": "Cresselia",
        "weight": 85.6,
        "gender": "f",
        "moves": [
            94,
            62,
            375,
            461
        ],
        "type1": "psychic",
        "ability": "Levitate"
    },
    "489": {
        "stats": {
            "hp": 300,
            "atk": 175,
            "sdf": 195,
            "spd": 214,
            "def": 195,
            "sat": 195
        },
        "name": "Phione",
        "weight": 3.1,
        "gender": "-",
        "moves": [
            127,
            412,
            246,
            240
        ],
        "type1": "water",
        "ability": "Hydration"
    },
    "490": {
        "stats": {
            "hp": 341,
            "atk": 236,
            "sdf": 268,
            "spd": 212,
            "def": 268,
            "sat": 328
        },
        "name": "Manaphy",
        "weight": 1.4,
        "gender": "-",
        "moves": [
            145,
            253,
            391,
            294
        ],
        "type1": "water",
        "ability": "Hydration"
    },
    "491": {
        "stats": {
            "hp": 250,
            "atk": 185,
            "sdf": 185,
            "spd": 229,
            "def": 185,
            "sat": 302
        },
        "name": "Darkrai",
        "weight": 50.5,
        "gender": "-",
        "moves": [
            168,
            464,
            171,
            114
        ],
        "type1": "dark",
        "ability": "Bad Dreams"
    },
    "492": {
        "stats": {
            "hp": 310,
            "atk": 205,
            "sdf": 225,
            "spd": 205,
            "def": 205,
            "sat": 185
        },
        "name": "Shaymin",
        "weight": 2.1,
        "gender": "-",
        "moves": [
            465,
            129,
            312,
            388
        ],
        "type1": "grass",
        "ability": "Natural Cure"
    }
}'''
    

class pokemon:
    id = 0
    name = ''
    weight = 0
    gender = ''
    hp = ''
    atk = ''
    sdf = ''
    spd = ''
    defValue = ''
    sat = ''
    type1 = ''
    type2 = 'null'
    move1 = 0
    move2 = 0
    move3 = 0
    move4 = 0
    ability = ''

jsonObject = json.loads(jsonString)
pokemonList = []
for key in jsonObject.keys():
    pokemonJsonObject = jsonObject[key]
    pokemonPythonObject = pokemon()
    pokemonPythonObject.id = int(key)
    pokemonPythonObject.ability = pokemonJsonObject['ability']
    pokemonPythonObject.name = pokemonJsonObject['name'].replace('\'', '\\\'')
    pokemonPythonObject.type1 = pokemonJsonObject['type1']
    try:
        pokemonPythonObject.type2 = pokemonJsonObject['type2']
    except KeyError, e:
        a = 1 #ignore key errors
    pokemonPythonObject.weight = pokemonJsonObject['weight']
    pokemonPythonObject.gender = pokemonJsonObject['gender']
    
    statsJsonObject = pokemonJsonObject['stats']
    pokemonPythonObject.hp = statsJsonObject['hp']
    pokemonPythonObject.atk = statsJsonObject['atk']
    pokemonPythonObject.sdf = statsJsonObject['sdf']
    pokemonPythonObject.spd = statsJsonObject['spd']
    pokemonPythonObject.defValue = statsJsonObject['def']
    pokemonPythonObject.sat = statsJsonObject['sat']
    
    movesJsonObject = pokemonJsonObject['moves']
    if len(movesJsonObject) > 0:
        pokemonPythonObject.move1 = movesJsonObject[0]
    if len(movesJsonObject) > 1:
        pokemonPythonObject.move2 = movesJsonObject[1]
    if len(movesJsonObject) > 2:
        pokemonPythonObject.move3 = movesJsonObject[2]
    if len(movesJsonObject) > 3:
        pokemonPythonObject.move4 = movesJsonObject[3]
    
    pokemonList.append(pokemonPythonObject)
            
conn = pg8000.connect(user='postgres', password='Start123', database='twitchplayspokemonbot')

query = 'INSERT INTO pokemon (pokemon_id, name, weight, gender, type1, type2, hp, atk, sdf, spd, def, sat, move1_id, move2_id, move3_id, move4_id) VALUES '
for i in range(0, len(pokemonList)):
    pokemon = pokemonList[i]
    query = query + '( ' + str(pokemon.id) + ' , ' + '\'' +  pokemon.name + '\'' + ', ' + str(pokemon.weight) + ' , ' + '\'' + pokemon.gender + '\'' + ' , ' + '\'' + pokemon.type1 + '\''
    query = query +  ' , ' + '\'' + pokemon.type2 + '\'' + ' , ' + str(pokemon.hp) + ' , ' + str(pokemon.atk) + ' , ' + str(pokemon.sdf) + ' , ' + str(pokemon.spd) 
    query = query + ' , ' + str(pokemon.defValue) + ' , ' + str(pokemon.sat) + ' , ' + str(pokemon.move1) + ' , ' + str(pokemon.move2) + ' , ' + str(pokemon.move3)
    query = query + ' , ' + str(pokemon.move4) + ' ) '
    if i != (len(pokemonList) - 1):
        query = query + ' , '

fileHandle = open('pokemonSql.sql', 'w')
fileHandle.write(query)
fileHandle.close()

print query
curr = conn.cursor()
curr.execute(query)
conn.commit()
conn.close()