from tree import RGBXmasTree
from colorzero import Color
from time import sleep
import random

tree = RGBXmasTree(brightness=0.1)
star = tree[3]

bot = (0,16,15,6,12,24,19,7);
mid = (17,14,5,23,20,8,1,11);
top = (18,13,10,22,21,9,4,2);

bottom = (tree[0], tree[16], tree [15], tree[6], tree[12], tree[24], tree[19], tree[7])
middle = (tree[17], tree[14], tree [5], tree[23], tree[20], tree[8], tree[1], tree[11])
top = (tree[18], tree[13], tree [10], tree[22], tree[21], tree[9], tree[4], tree[2])

firstSection = (0,1,2,18,17,16)
secondSection = (4,5,6,13,14,15)
thirdSection = (10,11,12,22,23,24)
fourthSection = (7,8,9,21,20,19)

First = (tree[0], tree[1], tree [2], tree[18], tree[17], tree[16])
Second = (tree[4], tree[5], tree [6], tree[13], tree[14], tree[15])
Third = (tree[10], tree[11], tree [12], tree[22], tree[23], tree[24])
Fourth = (tree[7], tree[8], tree [9], tree[21], tree[20], tree[19])

Lights = (0,16,15,6,12,24,19,7,17,14,5,23,20,8,1,11,18,13,10,22,21,9,4,2);

gold = Color(1,0.5,0.01)
silver = Color(0.8,0.65,0.8)
iceBlue = Color(0.35,0.5,0.91)
redGold =  Color(0.94,0.3,0.02)

tree.color = Color('green')
star.color = Color('yellow')

#Copied from myTree thats in use
# def mainTree():
#   for group in groups:
#     star.color = random_yellow();
#     star.brightness = random.choice([0.2, 0.4, 0.6, 0.8])
#     for j in group:
#       j.brightness = random.choice([0.2, 0.4, 0.6, 0.8])
#       j.color += Hue(deg=2)
#       sleep(0.05);
#   sparkle();

#print('Whole tree should be green now...')
#sleep(2)
#This function will create a random shade of yellow to be applied to the star.
def random_yellow():
    g = random.randint(80, 225)
    r = g + 30
    if (g > 175):
        b = random.randint(0, 125)
    else:
        b = 0
    R = r/255
    G = g/255
    B = b/255
    return Color(R, G, B)

#This function will use the random_yellow() function to keep generating random yellow tones
#and apply them to the star in quick but randomised succession to give a sparkling effect
def sparkle():
    star.color = random_yellow()
    sleep(0.1)
    star.color = random_yellow()
    sleep(0.1)
    star.color = random_yellow()
    sleep(0.1)
    star.color = random_yellow()
    sleep(0.1)
    star.color = random_yellow()
    sleep(0.1)
    star.color = random_yellow()
    sleep(0.1)
    star.color = random_yellow()
    sleep(0.1)
    star.color = random_yellow()
    sleep(0.1)

#This function will create a new shade of green at random and assign it to a light at random.
#Each light will only be changed once though and then be removed from the list of lights left to change.
def randomGreenRandomLight():
    lights = (0,16,15,6,12,24,19,7,17,14,5,23,20,8,1,11,18,13,10,22,21,9,4,2);
    while (len(lights) > 0):
        pos = random.randint(1, len(lights))
        i = pos - 1
        r = random.randint(0, 70)
        g = random.randint(127, 255)
        b = random.randint(0, 200)
        R = r/255
        G = g/255
        B = b/255
#        print('Changing the green of light ', lights[i])
        tree[lights[i]].color = Color(R, G, B)
        lightList = list(lights)
        lightList.pop(i)
        lights = tuple(lightList)

#This function will create a random shade of green and then apply it to every light
#in a random order.
def sameGreenRandomLight():
    lights = (0,16,15,6,12,24,19,7,17,14,5,23,20,8,1,11,18,13,10,22,21,9,4,2);
    r = random.randint(0, 70)
    g = random.randint(127, 255)
    b = random.randint(0, 200)
    R = r/255
    G = g/255
    B = b/255
    while (len(lights) > 0):
        pos = random.randint(1, len(lights))
        i = pos - 1
#        print('Changing the green of light ', lights[i])
        tree[lights[i]].color = Color(R, G, B)
        lightList = list(lights)
        lightList.pop(i)
        lights = tuple(lightList)

def addDecorations():
    colours = (gold, silver, iceBlue, redGold)
    col = random.randint(0, 3)
    i = random.randint(0, 5)
    
    tree[firstSection[i]].color = colours[col]
    tree[secondSection[i]].color = colours[col]
    tree[thirdSection[i]].color = colours[col]
    tree[fourthSection[i]].color = colours[col]

try:
    while True:
        num = random.randint(1, 11)
        if (num % 2 == 0):
#            print('num is even. Running randomGreenRandomLight()', num, 'times, then changing the stars colour once.')
            for i in range (0, num):
#                print(i+1)
                addDecorations()
                randomGreenRandomLight()
#                print('All green LED\'s updated. Round', i+1, 'complete!')
                sleep(2)
            star.color = random_yellow()
#            print('All rounds completed, star colour changed. Back to start.')
        else:
#            print('num is odd. Running sameGreenRandomLight()', num, 'times, then sparkle().')
            for i in range (0, num):
                print(i+1)
                addDecorations()
                sameGreenRandomLight()
#                print('All green LED\'s updated. Round', i+1, 'complete!')
                sleep(2)
            sparkle()
except KeyboardInterrupt:
    tree.close()
