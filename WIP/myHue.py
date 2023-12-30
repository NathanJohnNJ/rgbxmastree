from rgbxmastree.tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep
import random

tree = RGBXmasTree(brightness=0.1);
star = tree[3]

firstSection = (0,1,2,18,17,16)
secondSection = (4,5,6,13,14,15)
thirdSection = (10,11,12,22,23,24)
fourthSection = (7,8,9,21,20,19)

First = (tree[0], tree[1], tree [2], tree[18], tree[17], tree[16])
Second = (tree[4], tree[5], tree [6], tree[13], tree[14], tree[15])
Third = (tree[10], tree[11], tree [12], tree[22], tree[23], tree[24])
Fourth = (tree[7], tree[8], tree [9], tree[21], tree[20], tree[19])

tree.color = Color('green');
tree[3].color = Color(0.7, 0.3, 0);

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

def sparkle():
  for i in range(8):
    star.color = random_yellow();
    tree.brightness = i/10;
    sleep(random.choice([0.5, 1.5]))
  for i in range(0, 7, -1):
    star.color = random_yellow();
    tree.brightness = i/10;
    sleep(random.choice([0.5, 1.5]))

def mainTree(section):
    for i in section:
      tree[i].color += Hue(deg=1);
      sleep(0.3)

def hueTree():
    tree.color += Hue(deg=1);

while True:
  sparkle();
#  mainTree(firstSection);
#  mainTree(secondSection);
#  mainTree(thirdSection);
#  mainTree(fourthSection);
  hueTree()
