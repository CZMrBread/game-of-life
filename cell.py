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

    def printCell(self):
        if self.status == 1 and self.next_status == 1:
            return f"{Bcolors.BLUE}███{Bcolors.END}"
        elif self.status == 0 and self.next_status == 1:
            return f"{Bcolors.OK}▓▓▓{Bcolors.END}"
        elif self.status == 1 and self.next_status == 0:
            return f"{Bcolors.FAIL}▓▓▓{Bcolors.END}"
        elif self.status == 0 and self.next_status == 0:
            return "▓▓▓"
