from rgbxmastree.tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep
import random

tree = RGBXmasTree(brightness=0.1);
star = tree[3]
tree.color = Color('green');
star.color = Color(0.7, 0.3, 0);

def random_yellow():
    g = random.randint(80, 225)
    r = g + 30
    if (g > 150):
        b = random.randint(0, 80)
    else:
        b = 0
    R = r/255
    G = g/255
    B = b/255
    return Color(R, G, B);

def sparkle():
  for i in range(6):
    star.color = random_yellow();
    star.brightness = 5/(10+i);
    sleep(0.05);

lights = (tree[0], tree[16], tree[15], tree[6], tree[12], tree[24], tree[19], tree[7], tree[17], tree[14], tree[5], tree[23], tree[20], tree[8], tree[1], tree[11], tree[18], tree[13], tree[10], tree[22], tree[21], tree[9], tree[2], tree[4]);

def mainFunc(hueDeg):
    sparkle();
    tree.brightness = 0.3;
    for i in lights:
      i.color = Color('green') + Hue(deg=hueDeg);
      sleep(0.1);

first = (tree[2], tree[1], tree[0], tree[22], tree[23], tree[24])
second = (tree[21], tree[20], tree[19], tree[4], tree[5], tree[6])
third = (tree[10], tree[11], tree[12], tree[18], tree[17], tree[16])
fourth = (tree[13], tree[14], tree[15], tree[9], tree[8], tree[7])
groups = (first, second, third, fourth)

def fadeDown():
    tree.brightness = 0.5
    star.brightness = 0.3
    sleep(0.25)
    star.brightness = 0.4
    sleep(0.25)
    star.brightness = 0.1
    for group in groups:
      for i in group:
         i.brightness = 0.1
         sleep(0.05)

upFirst = (tree[0], tree[24], tree[23], tree[1], tree[22], tree[2])
upSecond = (tree[6], tree[19], tree[5], tree[20], tree[4], tree[21])
upThird = (tree[16], tree[12], tree[17], tree[11], tree[18], tree[10])
upFourth = (tree[7], tree[15], tree[14], tree[8], tree[13], tree[9])
upGroups = (upFirst, upSecond, upThird, upFourth)

def brightUp(hueDeg):
   sparkle()
   for group in upGroups:
      star.brightness = 0.3
      sleep(0.25)
      star.brightness = 0.1
      sleep(0.25)
      star.brightness = 0.4
      for i in group:
         i.color = Color('green') + Hue(deg=hueDeg)
      for i in group:
         i.brightness = 0.4


while True:
  for hueDeg in range(0, 120, 10):
    fadeDown();
    brightUp(hueDeg);
  for hueDeg in range(120, 240, 15):
    mainFunc(hueDeg);
  for hueDeg in range(-120, 0, 20):
    mainFunc(hueDeg);