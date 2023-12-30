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
  for i in range(4):
    star.color = random_yellow();
    star.brightness = (i+1)/10;
    sleep(0.05);
    star.color = random_yellow();
    star.brightness = i/10;
    sleep(0.05);



first = (tree[0], tree[23],  tree[5])
second = (tree[1], tree[22], tree[4])
others = (tree[21], tree[19], tree[6], tree[20],  tree[2], tree[16], tree[15], tree[12], tree[24], tree[7], tree[17], tree[14], tree[8], tree[11], tree[18], tree[13], tree[10], tree[21], tree[9]);
groups = (first, second, others)

def mainFunc(hueDeg):
    tree.brightness = 0.15;
    for i in others:
      i.color = Color('green') + Hue(deg=hueDeg);
      sleep(0.05);

tree.color = Color('green');
star.color = random_yellow();
sleep(2)
for i in first:
  i.color = Color(0.94,0.3,0.02);
for i in second:
  i.color = Color(0.35,0.5,0.91)
sleep(2)

while True:
  sparkle();
  for hueDeg in range(-120, 240, 1):
    for i in first:
      i.color += Hue(deg=hueDeg)
      sleep(0.05)
    for i in second:
      i.color += Hue(deg=hueDeg)
      sleep(0.05)
    mainFunc(hueDeg+120)