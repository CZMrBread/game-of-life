from bcolors import Bcolors


class Cell:
    def __init__(self, status, next_status):
        self.status = status
        self.next_status = next_status

    def setAlive(self):
        self.status = 1
        self.next_status = 1

    def setDead(self):
        self.status = 0
        self.next_status = 0
    def born(self):
        self.next_status = 1
    def die(self):
        self.next_status = 0
    def printCell(self):
        if self.status == 1 and self.next_status == 1:
            return self.liveCell()
        elif self.status == 0 and self.next_status == 1:
            return self.bornCell()
        elif self.status == 1 and self.next_status == 0:
            return self.deadCell()
        elif self.status == 0 and self.next_status == 0:
            return self.emptyCell()

    @staticmethod
    def liveCell():
        return f"{Bcolors.BLUE}███{Bcolors.END}"

    @staticmethod
    def deadCell():
        return f"{Bcolors.FAIL}▓▓▓{Bcolors.END}"

    @staticmethod
    def bornCell():
        return f"{Bcolors.OK}▓▓▓{Bcolors.END}"

    @staticmethod
    def emptyCell():
        return "▓▓▓"
