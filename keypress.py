#!/usr/bin/env python

import curses
from time import sleep
import logging

class KeyDetect():
   
   def __init__( s ):
      s.Logger = logging.getLogger( '' )
      s.Logger.info("Fin __init__()")
   
   def CheckForKey( s, window, cursor=(0,0), runUpdates = True ):
      s.Logger.debug("Start of CheckForKey()")
      try:
         s.Logger.debug("Get a Key")
         #val = window.getkey( *cursor )
         val = window.getch( *cursor )
         s.Logger.debug("Got a Key")
         if runUpdates:
            curses.doupdate()

      except curses.error:
         val = -1
         s.Logger.exception("Got Expection")
      except:
         s.Logger.exception("Got Expection")

      
      return val
      




