
import curses
import logging
import keypress
from time import sleep

## Create and manage menus. 
# 
# Menus are to be groups of options to be selected by the user. 
# Upon selection of the item, the call back is returned to the
# calling fucntion. 

class Menu():
   def __init__( s, screenPos, options = [('exit',None)] ):
      
      # Valid options and calls to make
      s.Options = options
      
      # Index of cursor
      s.Cursor = 0
      s.Logger = logging.getLogger('')
      s.ScreenPos = screenPos
      s.Window = curses.newwin( screenPos[2], screenPos[3], screenPos[0], screenPos[1] )
      s.Window.nodelay(1)

      # s.Window.raw()
      # We must keep a copy of this instance, as its job is to keep state of the keyboard at times
      s.KeyReader = keypress.KeyDetect() 

   # Display the menu and its selection
   def Display( s ):
      s.Logger.info("Run")
      s.Window.border()
      xOffset = 2
      for i in s.Options:
         if s.Cursor + 2 == xOffset:
            attr = curses.A_STANDOUT
         else:
            attr = curses.A_NORMAL

         s.Window.addstr( xOffset, 2, i[0], attr )
         xOffset += 1
      curses.doupdate()
      s.Logger.info("Fin")
      sleep(1)

   def Run( s ):
      s.Logger.info("Run")
      while 1:
         s.Display()
         # Get a key press
         s.Logger.info("Call CheckForKey()")
         key = s.KeyReader.CheckForKey( s.Window )
         s.Logger.info("Got back from CheckForKey()")
         s.Logger.debug( "Key was: {}".format(key))
         s.Logger.debug( "Cursor is: {}".format(s.Cursor))

         if key == curses.KEY_UP:
            s.Cursor = max( s.Cursor-1, 0 )
         elif key == curses.KEY_DOWN:
            s.Cursor = min( s.Cursor+1, len( s.Options ) )
         elif key == curses.KEY_ENTER:
            return s.Options[s.Cursor][1]

      return None
      pass

