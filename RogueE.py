#!/usr/bin/env python

import curses
import os
import logging
import datetime

class App():
   def __init__( s ):
      s.Running = True
      s.Logging = logging.getLogger( '' )
      s.Logging.info("App initilized")

   def Run( s ):
      while s.Running:
         s.Main()
      s.Logging.info("Terminate Application")

   def Main( s ):
      s.Running = False

if __name__ == '__main__':
   
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
