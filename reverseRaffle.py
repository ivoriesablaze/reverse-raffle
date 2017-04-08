"""
Title: Reverse Raffle

Developer: Joel Solomon

Version 1.0

This program is used for an event known as a "Reverse Raffle". The idea is that there is a set
list of numbers. If a number is picked, it does not win the prize and is put into a list of other
non-winners. This list is to be displayed at all times in a window that also has the button to
draw the next loser.
"""

from random import randint
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

loserList = [] #The list of losers

def drawLoser(): #Picks random number, displays it, then adds it to the loser list
    loser = randint(1,100)
    if not loserList or loser not in loserList:
        tkMessageBox.showinfo(loser)
        loserList.append(loser)
    else:
        drawLoser()

B = Tkinter.Button(top, text = "Draw", command = drawLoser())

B.pack()
top.mainloop()
#key = raw_input()

#while key is not "q":
 #   key = raw_input('Press key: ')
  #  if key is "q":
   #     break
    #elif key is "l":
    #    print loserList
    #else:
     #   drawLoser()

