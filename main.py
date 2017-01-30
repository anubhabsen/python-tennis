from tennis import tennis
from player import player
import sys
import csv
t = tennis()

with open(str(sys.argv[1])) as f:
    reader = csv.reader(f, delimiter = ' ')
    for row in reader:
        c = 0
        d = 0
        t.p1.iteration += 1
        print 'Iteration :' ,t.p1.iteration
        if row[1] == 'Serve':
            t.serve()
        elif row[1] == 'Ace':
            t.ace()
        elif row[1] == 'Fault':
            t.fault()
        elif row[1] == 'Nets':
            t.nets()
        elif row[1] == 'PointLost-Out':
            t.lostout()
        elif row[1] == 'PointLost-SameSide':
            t.lostsameside()
        elif row[1] == 'PointLost-CouldNotReach':
            t.lostcouldnotreach()
        elif row[1] == 'Backhand':
            t.backhand()
        elif row[1] == 'Forehand':
            t.forehand()
        if t.p1.getscore() == 1000:
            var1 = t.p1.getgamewincount()
            t.p1.setgamewincount(var1 + 1)
            t.p1.gamecount = t.p1.gamecount + 1
            t.p1.setscore(0)
            t.p2.setscore(0)
            t.p1.gamer = 1
        elif t.p2.getscore() == 1000:
            var1= t.p2.getgamewincount()
            t.p2.setgamewincount(var1 + 1)
            t.p1.gamecount = t.p1.gamecount + 1
            t.p1.setscore(0)
            t.p2.setscore(0)
            t.p2.gamer = 1
        if t.p1.getgamewincount() == 6 and t.p2.getgamewincount() < 5:
            t.p1.setsetwincount(t.p1.getsetwincount() + 1)
            t.p1.setgamewincount(0)
            t.p2.setgamewincount(0)
            t.p1.setcount = t.p1.setcount + 1
            t.p1.gamecount = 0
        elif t.p2.getgamewincount() == 6 and t.p1.getgamewincount() < 5:
            t.p2.setsetwincount(t.p2.getsetwincount() + 1)
            t.p1.setgamewincount(0)
            t.p2.setgamewincount(0)
            t.p1.setcount = t.p1.setcount + 1
            t.p1.gamecount = 0
        elif t.p1.getgamewincount() - t.p2.getgamewincount() >= 2 and t.p1.getgamewincount() > 6:
            t.p1.setsetwincount(t.p1.getsetwincount() + 1)
            t.p1.setgamewincount(0)
            t.p2.setgamewincount(0)
            t.p1.setcount = t.p1.setcount + 1
            t.p1.gamecount = 0
        elif t.p2.getgamewincount() - t.p1.getgamewincount() >= 2 and t.p2.getgamewincount() > 7:
            t.p2.setsetwincount(t.p2.setsetwincount() + 1)
            t.p1.setgamewincount(0)
            t.p2.setgamewincount(0)
            t.p1.setcount = t.p1.setcount + 1
            t.p1.gamecount = 0
        if t.p1.control == 1 and row[1] == 'PointLost-CouldNotReach':
            print 'Player2 :' ,row[1]
        elif t.p2.control == 1 and row[1] == 'PointLost-CouldNotReach':
            print 'Player1 :' ,row[1]
        elif t.p1.control == 1:
            print 'Player1 :' ,row[1]
        elif t.p2.control == 1:
            print 'Player2 :' ,row[1]
        if t.p1.gamer == 1:
            print 'P1 Score : Game'
            print 'P2 Score : '
        elif t.p2.gamer == 1:
            print 'P1 Score : '
            print 'P2 Score : Game'
        elif t.p1.getscore() == 40 and t.p2.getscore() == 40 and t.p1.getadvantage() == 0 and t.p2.getadvantage() == 0:
            print 'P1 Score : Deuce'
            print 'P2 Score : Deuce'
        elif t.p1.getadvantage() == 1:
            print 'P1 Score : Advantage'
            print 'P2 Score :  '
        elif t.p2.getadvantage() == 1:
            print 'P1 Score :  '
            print 'P2 Score : Advantage'
        elif t.p1.getscore() == 0 and t.p2.getscore() != 0:
            print 'P1 Score : Love'
            print 'P2 Score :' ,t.p2.getscore()
        elif t.p2.getscore() == 0 and t.p1.getscore() != 0:
            print 'P1 Score :' ,t.p1.getscore()
            print 'P2 Score : Love'
        elif t.p1.getscore() == 0 and t.p2.getscore() == 0:
            print 'P1 Score : Love'
            print 'P2 Score : Love'
        else:
            print 'P1 Score :' ,t.p1.getscore()
            print 'P2 Score :' ,t.p2.getscore()
        print 'P1 Game Win Count :' ,t.p1.getgamewincount()
        print 'P2 Game Win Count :' ,t.p2.getgamewincount()
        print 'P1 Set Win Count :' ,t.p1.getsetwincount()
        print 'P2 Set Win Count :' ,t.p2.getsetwincount()
        print
        t.p1.gamer = 0
        t.p2.gamer = 0
