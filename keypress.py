#!/usr/bin/env python

import curses
from time import sleep
import logging

class KeyDetect():
   
   def __init__( s ):
      s.Logger = logging.getLogger( '' )
      s.Logger.info("Fin __init__()")
      s.State = 0
   
   def CheckForKey( s, window, cursor=None, runUpdates = True ):
      s.Logger.debug("Start of CheckForKey()")

      try:
         s.Logger.debug("Get a Key")
         if cursor:
            val = window.getkey( *cursor )
         else:
            val = window.getkey( )
         s.Logger.debug("Got Key {}".format(ord(val)))
         s.Logger.debug("Key == chr(27): {}".format(val==chr(27)))
         if runUpdates:
            curses.doupdate()
      except curses.error:
         val = -1
         #s.Logger.exception("Raised Exception")
         s.Logger.debug("Got Key Error")
      except:
         s.Logger.exception("Got Expection")
         raise
      s.Logger.debug( "Middle Key Value: {}".format( val ))      

      if s.State == 0:
         if val == chr(27):
            s.State = 1

      elif s.State == 1:
         if val == chr(91):
            s.State = 2
         else:
            s.State = 0

      elif s.State == 2:
         if val == chr(65):
            val = curses.KEY_UP
            s.Logger.debug("Return a KEY_UP!")
         elif val == chr(66):
            val = curses.KEY_DOWN
            s.Logger.debug("Return a KEY_DOWN!")
         elif val == chr(67):
            val = curses.KEY_RIGHT
            s.Logger.debug("Return a KEY_RIGHT!")
         elif val == chr(68):
            val = curses.KEY_LEFT
            s.Logger.debug("Return a KEY_LEFT!")
         else:
            s.State = 0
      
      s.Logger.debug( "State: {}".format(s.State) )
      s.Logger.debug( "Final Key Value: {}".format( val ))      
      return val
      




