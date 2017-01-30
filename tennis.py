from player import player

class tennis(object):
    def __init__(self):
        self.p1 = player(1, 0, 0, 0, 0, 0, 0, 0, 0)
        self.p2 = player(1, 0, 0, 0, 0, 0, 0, 0, 0)
    def serve(self):
            if self.p1.gamecount % 2 == 0:
                self.p2.control = 0
                self.p1.control = 1
            else:
                self.p2.control = 1
                self.p1.control = 0
    def ace(self):
        if self.p1.getscore() == 40 and self.p2.getscore() == 40:
            if self.p1.control == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p1.setscore(1000)
            elif self.p2.control == 1 and self.p2.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p2.setscore(1000)
            elif self.p1.control == 1 and self.p2.getadvantage() == 0:
                self.p1.setadvantage(1)
            elif self.p2.control == 1 and self.p1.getadvantage() == 0:
                self.p2.setadvantage(1)
            else:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
            if self.p2.getadvantage() == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
        elif self.p1.control == 1:
            var1= self.p1.getscore()
            if var1== 0:
                self.p1.setscore(15)
            elif var1== 15:
                self.p1.setscore(30)
            elif var1== 30:
                self.p1.setscore(40)
            elif var1== 40:
                self.p1.setscore(1000)
        elif self.p2.control == 1:
            var2= self.p2.getscore()
            if var2== 0:
                self.p2.setscore(15)
            elif var2== 15:
                self.p2.setscore(30)
            elif var2== 30:
                self.p2.setscore(40)
            elif var2== 40:
                self.p2.setscore(1000)
    def fault(self):
        if self.p1.getscore() == 40 and self.p2.getscore() == 40:
            if self.p1.control == 1 and self.p1.getadvantage() == 0:
                self.p1.setadvantage(1)
            elif self.p2.control == 1 and self.p2.getadvantage() == 0:
                self.p2.setadvantage(1)
            elif self.p1.control == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p2.setscore(1000)
            elif self.p2.control == 1 and self.p2.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p1.setscore(1000)
            if self.p2.getadvantage() == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
        elif self.p1.control == 1:
            var1= self.p2.getscore()
            if var1== 0:
                self.p2.setscore(15)
            elif var1== 15:
                self.p2.setscore(30)
            elif var1== 30:
                self.p2.setscore(40)
            elif var1== 40:
                self.p2.setscore(1000)
        elif self.p2.control == 1:
            var2= self.p1.getscore()
            if var2== 0:
                self.p1.setscore(15)
            elif var2== 15:
                self.p1.setscore(30)
            elif var2== 30:
                self.p1.setscore(40)
            elif var2== 40:
                self.p1.setscore(1000)
    def nets(self):
        if self.p1.getscore() == 40 and self.p2.getscore() == 40:
            if self.p1.control == 1 and self.p1.getadvantage() == 0:
                self.p1.setadvantage(1)
            elif self.p2.control == 1 and self.p2.getadvantage() == 0:
                self.p2.setadvantage(1)
            elif self.p1.control == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p2.setscore(1000)
            elif self.p2.control == 1 and self.p2.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p1.setscore(1000)
            if self.p2.getadvantage() == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
        elif self.p1.control == 1:
            var1= self.p2.getscore()
            if var1== 0:
                self.p2.setscore(15)
            elif var1== 15:
                self.p2.setscore(30)
            elif var1== 30:
                self.p2.setscore(40)
            elif var1== 40:
                self.p2.setscore(1000)
        elif self.p2.control == 1:
            var2= self.p1.getscore()
            if var2== 0:
                self.p1.setscore(15)
            elif var2== 15:
                self.p1.setscore(30)
            elif var2== 30:
                self.p1.setscore(40)
            elif var2== 40:
                self.p1.setscore(1000)
    def lostout(self):
        if self.p1.getscore() == 40 and self.p2.getscore() == 40:
            if self.p1.control == 1 and self.p1.getadvantage() == 0:
                self.p1.setadvantage(1)
            elif self.p2.control == 1 and self.p2.getadvantage() == 0:
                self.p2.setadvantage(1)
            elif self.p1.control == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p2.setscore(1000)
            elif self.p2.control == 1 and self.p2.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p1.setscore(1000)
            if self.p2.getadvantage() == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
        elif self.p1.control == 1:
            var1= self.p2.getscore()
            if var1== 0:
                self.p2.setscore(15)
            elif var1== 15:
                self.p2.setscore(30)
            elif var1== 30:
                self.p2.setscore(40)
            elif var1== 40:
                self.p2.setscore(1000)
        elif self.p2.control == 1:
            var2= self.p1.getscore()
            if var2== 0:
                self.p1.setscore(15)
            elif var2== 15:
                self.p1.setscore(30)
            elif var2== 30:
                self.p1.setscore(40)
            elif var2== 40:
                self.p1.setscore(1000)
    def lostsameside(self):
        if self.p1.getscore() == 40 and self.p2.getscore() == 40:
            if self.p1.control == 1 and self.p1.getadvantage() == 0:
                self.p1.setadvantage(1)
            elif self.p2.control == 1 and self.p2.getadvantage() == 0:
                self.p2.setadvantage(1)
            elif self.p1.control == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p2.setscore(1000)
            elif self.p2.control == 1 and self.p2.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p1.setscore(1000)
            if self.p2.getadvantage() == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
        elif self.p1.control == 1:
            var1= self.p2.getscore()
            if var1== 0:
                self.p2.setscore(15)
            elif var1== 15:
                self.p2.setscore(30)
            elif var1== 30:
                self.p2.setscore(40)
            elif var1== 40:
                self.p2.setscore(1000)
        elif self.p2.control == 1:
            var2= self.p1.getscore()
            if var2== 0:
                self.p1.setscore(15)
            elif var2== 15:
                self.p1.setscore(30)
            elif var2== 30:
                self.p1.setscore(40)
            elif var2== 40:
                self.p1.setscore(1000)
    def lostcouldnotreach(self):
        if self.p1.getscore() == 40 and self.p2.getscore() == 40:
            if self.p1.control == 1 and self.p2.getadvantage() == 0:
                self.p2.setadvantage(1)
            elif self.p2.control == 1 and self.p1.getadvantage() == 0:
                self.p1.setadvantage(1)
            elif self.p1.control == 1 and self.p2.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p1.setscore(1000)
            elif self.p2.control == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
                self.p2.setscore(1000)
            if self.p2.getadvantage() == 1 and self.p1.getadvantage() == 1:
                self.p1.setadvantage(0)
                self.p2.setadvantage(0)
        elif self.p1.control == 1:
            var1= self.p1.getscore()
            if var1== 0:
                self.p1.setscore(15)
            elif var1== 15:
                self.p1.setscore(30)
            elif var1== 30:
                self.p1.setscore(40)
            elif var1== 40:
                self.p1.setscore(1000)
        elif self.p2.control == 1:
            var2= self.p2.getscore()
            if var2== 0:
                self.p2.setscore(15)
            elif var2== 15:
                self.p2.setscore(30)
            elif var2== 30:
                self.p2.setscore(40)
            elif var2== 40:
                self.p2.setscore(1000)
    def forehand(self):
        if self.p1.control == 1:
            self.p1.control = 0
            self.p2.control = 1
        elif self.p2.control == 1:
            self.p2.control = 0
            self.p1.control = 1
    def backhand(self):
        if self.p1.control == 1:
            self.p1.control = 0
            self.p2.control = 1
        elif self.p2.control == 1:
            self.p2.control = 0
            self.p1.control = 1
