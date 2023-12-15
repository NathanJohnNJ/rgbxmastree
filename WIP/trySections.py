from colorzero import Color
from sections import TreeBottom, TreeMiddle, TreeTop

bottom = TreeBottom()
middle = TreeMiddle()
top = TreeTop()


while True:
	bottom.color = Color('red')
	bottom.close()
	middle.color = Color('blue')
	middle.close()
	top.color = Color('green')
	top.close()

