#!/usr/bin/env python

import curses
from time import sleep

globalWindow = curses.initscr()
globalWindow.nodelay(1)

val = -1
while 1:
   try:
      val = globalWindow.getkey(1,1)
      globalWindow.addstr( 0, 0, "Hello World {}".format( val ) )
      curses.doupdate()
   except curses.error:
      val = -1
   
   curses.doupdate()
   sleep( 1/30. )
   if val == 'Q':
      globalWindow.addstr(2,0,"Fin!")
      globalWindow.refresh()
      sleep(1)

      break

curses.endwin()




