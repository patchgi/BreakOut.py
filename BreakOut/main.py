# coding: utf-8

# Python2.X encoding wrapper (Windows dedicated processing)
import codecs
import sys
import time

from BreakOut import*

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

map=BreakOut(20,10)

while True:

    map.update()
    time.sleep(0.1)




