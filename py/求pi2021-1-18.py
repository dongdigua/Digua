#求π
from random import *
from math import sqrt
from time import *
DARTS = 120000
hits = 0
#clock()             #为什么没有这个模块???
for i in range(1,DARTS):
    x,y = random(),random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4*(hits/DARTS)
print('pi is %s' % pi)    #那个 % 到底是什么意思呀啊啊啊!!!
#print('time i %-5.5s' % clock)
