#!/usr/bin/env python

import atexit
import curses
import datetime
import logging
import menu
import os

class App():
   def __init__( s ):
      s.Running = True
      s.Logger= logging.getLogger( '' )
      s.Logger.info("App initilized")
      s.State = 'Main Menu'
      s.Scr = None


   def Run( s ):
      s.Logger.info("Run Application")
      s.Scr = curses.initscr()
      while s.Running:
         s.Main()
      s.Logger.info("Terminate Application")

   def Main( s ):
      if s.State == 'Main Menu':
         m = menu.Menu(
            (3,3,50,50),
            ( ('1',One), ('2',Two))
         )
         tmp = m.Run()
         if tmp != None:
            tmp()
         else:
            s.State = 'Exit'
      else:
         s.Logger.debug("Exit due to no valid state")
         s.Running = False


def One():
   logger = logging.getLogger( '' )
   logger.debug("One")

def Two():
   logger = logging.getLogger( '' )
   logger.debug("Two")

def OneMoreThing():
   logger = logging.getLogger( '' )
   logger.info( "Run atexit callback function" )
   curses.endwin()
   logger.info( "Exit Program" )


if __name__ == '__main__':
   
   atexit.register( OneMoreThing )

   scriptPath = os.path.dirname( os.path.realpath(__file__) ) + "/"

   # create logger with 'spam_application'
   logger = logging.getLogger('')
   logger.setLevel(logging.DEBUG)
   
   # Make sure we have a logging directory
   if not os.path.isdir( scriptPath + 'logs' ):
      os.mkdir( scriptPath + 'logs' )

   # create file handler which logs even debug messages
   fh = logging.FileHandler(scriptPath + 'logs/RogueE-{}.log' .format( datetime.date.today() ) )
   fh.setLevel(logging.DEBUG)
   
   # create console handler with a higher log level
   ch = logging.StreamHandler()
   ch.setLevel(logging.ERROR)
   
   # create formatter and add it to the handlers
   formatter = logging.Formatter('%(asctime)s - %(module)s:%(lineno)d:%(funcName)s() - %(levelname)s - %(message)s')
   fh.setFormatter(formatter)
   #ch.setFormatter(formatter)
   
   # add the handlers to the logger
   logger.addHandler(fh)
   logger.addHandler(ch)

   logger.info('')
   logger.info('')
   logger.info('')

   x = App()
   x.Run()
