class player(object):

    def __init__(self, control, score, gamewincount, setwincount, advantage,  setcount, gamecount, iteration, gamer):
        self.control = control
        self.__score = 0
        self.__gamewincount = 0
        self.__setwincount = 0
        self.__advantage = 0
        self.setcount = 0
        self.gamecount = 0
        self.iteration = 0
        self.gamer = 0

    def getscore(self):
        return self.__score
    def setscore(self,score):
        self.__score = score
    def getgamewincount(self):
        return self.__gamewincount
    def setgamewincount(self,gamewincount):
        self.__gamewincount = gamewincount
    def getsetwincount(self):
        return self.__setwincount
    def setsetwincount(self,setwincount):
        self.__setwincount = setwincount
    def getadvantage(self):
        return self.__advantage
    def setadvantage(self,advantage):
        self.__advantage = advantage
