from rgbxmastree.tree import RGBXmasTree, TreeBottom, TreeMiddle, TreeTop
from colorzero import Color, Hue

tree = RGBXmasTree(brightness=0.1)
#bottom = (tree[0], tree[16], tree [15], tree[6], tree[12], tree[24], tree[19], tree[7])
#middle = (tree[17], tree[14], tree [5], tree[23], tree[20], tree[8], tree[1], tree[11])
#top = (tree[18], tree[13], tree [10], tree[22], tree[21], tree[9], tree[4], tree[2])

bottom = TreeBottom(brightness=0.1)
middle = TreeMiddle(brightness=0.1)
top = TreeTop(brightness=0.1)

bottom.color = Color('green')
middle.color = Color('blue')
top.color = Color('yellow')

try:
    while True:
        tree.color += Hue(deg=1)
except KeyboardInterrupt:
    tree.close()
