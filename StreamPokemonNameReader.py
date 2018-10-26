'''
Created on Sep 1, 2015

@author: derp
'''
import time
import Image
import os
import subprocess

#import cv2
from livestreamer import Livestreamer

#import wand.api
#import wand.image
import ctypes
import pg8000

def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]


start_time = time.time()

conn = pg8000.connect(user='postgres', password='Start123', database='twitchplayspokemonbot')
# change to a stream that is actually online

livestreamer = Livestreamer()
plugin = livestreamer.resolve_url("http://www.twitch.tv/twitchplayspokemon")
streams = plugin.get_streams()
stream = streams['high']

# download enough data to make sure the first frame is there
fd = stream.open()
data = ''
while len(data) < 3e5:
    data += fd.read(10245)
    time.sleep(0.1)
fd.close()

fname = 'C:\\Users\\derp\\workspace\\TPPBot\\images\\stream.bin'
fileHandle = open(fname, 'wb')
fileHandle.write(data)
fileHandle.close()

ffmpegOutputFileName = 'C:\\Users\\derp\\workspace\\TPPBot\\images\\output.avi'
executeCall = "H:\\ffmpeg\\bin\\ffmpeg.exe -y -i " + fname + " -codec:v msmpeg4v2 " + ffmpegOutputFileName
print executeCall
subprocess.call(executeCall)


capture = cv2.VideoCapture(ffmpegOutputFileName)
success, imgdata = capture.read()
if not success:
    print 'failed again :('
frameFileName = 'images' + os.path.sep + 'frame.png'
cv2.imwrite(frameFileName, imgdata)
#img.save('frame.png')
# img.show()

frameFileName = 'images' + os.path.sep + 'frame.png'
croppedBlueFileName = 'C:\\Users\derp\\workspace\\TPPBot\\images\\cropped-blue.png'
thresheldBlueFileName = 'C:\\Users\\derp\\workspace\\TPPBot\\images\\thresheld-blue.png'
croppedRedFileName = 'C:\\Users\derp\\workspace\\TPPBot\\images\\cropped-red.png'
thresheldRedFileName = 'C:\\Users\\derp\\workspace\\TPPBot\\images\\thresheld-red.png'
croppedImg = cv2.imread(frameFileName)
crop_img_blue = croppedImg[190:230, 100:660]
crop_img_red = croppedImg[190:230, 610:1120]
cv2.imwrite(croppedBlueFileName, crop_img_blue)
cv2.imwrite(croppedRedFileName,crop_img_red)

processBlue = subprocess.Popen("C:\Users\derp\workspace\TPPBot\images\\callImageMagick.bat")
processBlue.wait()

tesseractBlueCall = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract ' + thresheldBlueFileName + ' C:\Users\derp\workspace\TPPBot\images\output-blue'
tesseractRedCall = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract ' + thresheldRedFileName + ' C:\Users\derp\workspace\TPPBot\images\output-red'
tesseractBlueExecution= subprocess.Popen(tesseractBlueCall)
tesseractRedExecution = subprocess.Popen(tesseractRedCall)

tesseractBlueExecution.wait()
tesseractRedExecution.wait()

pokemonNames = []
curr = conn.cursor()
curr.execute("SELECT name FROM pokemon WHERE name IS NOT NULL and name <> 'Mew'")
pokemonNameTuples = curr.fetchall()
for pokemonNameTuple in pokemonNameTuples:
    if str(pokemonNameTuple).lower() != str('mew'):
        pokemonNames.append(str(pokemonNameTuple).lower())

potentialNames = []
with open("images/output-red.txt") as potentialPokemonNamesString:
    potentialNamesValues = potentialPokemonNamesString.read().split(' ')
    for potentialName in potentialNamesValues:
        potentialName = str(potentialName).lower()
        potentialNames.append(potentialName)
       
with open("images/output-blue.txt") as potentialPokemonNamesString:
    potentialNamesValues = potentialPokemonNamesString.read().split(' ')
    for potentialName in potentialNamesValues:
        potentialName = str(potentialName).lower()
        potentialNames.append(potentialName)

print 'done parsing'
pokemonDistanceDict = dict()
for potentialName in potentialNames:
    for pokemonName in pokemonNames:
        pokemonDistanceDict[pokemonName] = abs(levenshtein(pokemonName, potentialName))
    bestFit = min(pokemonDistanceDict.keys(), key = lambda pokemonName: pokemonDistanceDict[pokemonName])
    print 'bestFit for: ' + str(potentialName) + ' was ' + bestFit
    otherPotentialNames = [name for name in pokemonDistanceDict.keys() if pokemonDistanceDict[name] == pokemonDistanceDict[bestFit]]
    print 'other potential names are: ' + str(otherPotentialNames)
    
print("--- %s seconds ---" % (time.time() - start_time))