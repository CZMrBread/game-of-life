import random as rand

from bcolors import Bcolors
from cell import Cell

HEIGHT = 20
WIDTH = 20
GENERATIONS = 1
BOARD = [[Cell(0, 0) for i in range(WIDTH)] for j in range(HEIGHT)]

OPTIONS = {
    "stopAfterEachGeneration": {"id_option": 1, "name": "Pause between generations", "value": False},
    "showGenerationNumber": {"id_option": 2, "name": "Show generation number", "value": True},
    "showBetweenStates": {"id_option": 3, "name": "Show between states", "value": True},
    "showUpdatedBoard": {"id_option": 4, "name": "Show updated board", "value": True},
    "infiniteBoard": {"id_option": 5, "name": "Infinite board", "value": True},
}


def menu():
    while True:
        print(f"{Bcolors.HEADER}Please select an option:{Bcolors.END}")
        menuOptions = ["Edit the board",
                       "Run for 10 generations",
                       "Run for X generations",
                       "Options",
                       "Random board",
                       "Clear the board",
                       "Help"]
        for i, option in enumerate(menuOptions, 1):
            print(f"{i:>4}. {option}")
        choice = input(f"{Bcolors.BOLD}Enter the number of your choice:{Bcolors.END}")
        match choice:
            case "1":
                edit()
            case "2":
                run(10)
            case "3":
                run(int(input(f"{Bcolors.BOLD}Enter the number of generations:{Bcolors.END}")))
            case "4":
                options()
            case "5":
                percent = input(f"{Bcolors.BOLD}Enter the chance of cell birth (0-100):{Bcolors.END}")
                if percent.isdigit() and 0 <= int(percent) <= 100:
                    randomBoard(int(percent))
                else:
                    print(f"{Bcolors.FAIL}Invalid input.{Bcolors.END}")
            case "6":
                for row in BOARD:
                    for cell in row:
                        cell.setDead()
                printBoard()
                print(f"{Bcolors.BOLD}Board is cleared{Bcolors.END}")
            case "7" | "help":
                helpMenu()
            case _:
                print(f"{Bcolors.FAIL}Invalid choice.{Bcolors.END}")
        print(f"{Bcolors.BOLD}{'─' * 30}{Bcolors.END}")


def helpMenu():
    print(f"{Bcolors.HEADER}Help:{Bcolors.END}")
    print(f"{Cell.liveCell()} cells are alive")
    print(f"{Cell.bornCell()} cells will be born in the next generation")
    print(f"{Cell.deadCell()} cells will die in the next generation")
    print(f"{Cell.emptyCell()} cells are empty")
    print(f"{Bcolors.BOLD}{'─' * 30}{Bcolors.END}")


def options():
    def switchOptions(option):
        OPTIONS[option]["value"] = not OPTIONS[option]["value"]

    while True:
        success = f"{Bcolors.BOLD}[{Bcolors.PASS}ON{Bcolors.END}{Bcolors.BOLD}/OFF]{Bcolors.END}"
        failure = f"{Bcolors.BOLD}[ON{Bcolors.BOLD}/{Bcolors.FAIL}OFF{Bcolors.END}{Bcolors.BOLD}]{Bcolors.END}"
        print(f"{Bcolors.HEADER}Options:{Bcolors.END}")
        i = 1
        print(f"{Bcolors.BOLD}{Bcolors.HELP}{0:>3}. Back to menu.{Bcolors.END}")
        for key, value in sorted(OPTIONS.items(), key=lambda x: x[1]["id_option"]):
            if value["value"]:
                print(f"{Bcolors.BOLD}{value['id_option']:>3}. {value['name']:<40}{success}{Bcolors.END}")
            else:
                print(f"{Bcolors.BOLD}{value['id_option']:>3}. {value['name']:<40}{failure}{Bcolors.END}")
            i += 1
        choice = input(f"{Bcolors.BOLD}Enter the number of the option you want to change:{Bcolors.END}")
        print(f"{Bcolors.BOLD}{'─' * 30}{Bcolors.END}")
        if choice == "0":
            break
        for key, value in OPTIONS.items():
            if str(value["id_option"]) == choice:
                switchOptions(key)
                break
        else:
            print(f"{Bcolors.FAIL}Invalid choice.{Bcolors.END}")


def printBoard():
    print("    ", end="")
    for i in range(1, WIDTH + 1):
        print(f"{Bcolors.UNDERLINE}{i:>3}{Bcolors.END}", end="|")
    print()
    for i, row in enumerate(BOARD, 1):
        print(f'{i:>3}|', end='')
        for j, cell in enumerate(row, 1):
            print(cell.printCell(), end="|")
        print()


def updateBoard():
    flag = False
    for row in BOARD:
        for cell in row:
            if cell.status == 1:
                flag = True
            cell.next_status = cell.status
    if not flag:
        return

    for i in range(HEIGHT):
        for j in range(WIDTH):
            count = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if OPTIONS["infiniteBoard"]["value"]:
                        count += BOARD[(i + x) % HEIGHT][(j + y) % WIDTH].status
                    else:
                        if 0 <= i + x < HEIGHT and 0 <= j + y < WIDTH:
                            count += BOARD[i + x][j + y].status
            if BOARD[i][j].status == 1:
                if count < 2 or count > 3:
                    BOARD[i][j].die()
            else:
                if count == 3:
                    BOARD[i][j].born()
    if OPTIONS["showGenerationNumber"]["value"]:
        print(f"{Bcolors.HEADER}Generation {GENERATIONS}:{Bcolors.END}")
    if OPTIONS["showBetweenStates"]["value"]:
        printBoard()
    for row in BOARD:
        for cell in row:
            cell.status = cell.next_status
    return flag


def run(gen):
    printBoard()
    global GENERATIONS
    for generation in range(gen):
        flag = updateBoard()
        if not flag:
            print(f"{Bcolors.FAIL}All cells are dead.{Bcolors.END}")
            print(f"{Bcolors.BOLD}{GENERATIONS} generations were run.{Bcolors.END}")
            print(f"{Bcolors.BOLD}{'─' * 30}{Bcolors.END}")
            break
        GENERATIONS += 1
        if OPTIONS["showUpdatedBoard"]["value"]:
            print(f"{Bcolors.HEADER}Board updated.{Bcolors.END}")
            printBoard()
        if OPTIONS["stopAfterEachGeneration"]["value"]:
            input(f"{Bcolors.BOLD}Press Enter to continue.{Bcolors.END}")
        print(f"{Bcolors.BOLD}{'─' * 90}{Bcolors.END}")


def edit():
    print(f"{Bcolors.HEADER}Editing the board.{Bcolors.END}")
    while True:
        printBoard()
        print(f"{Bcolors.BOLD}Enter the coordinates of the cell you want to change.{Bcolors.END}")
        print(f"{Bcolors.HELP}{Bcolors.BOLD}Enter 0 to exit.{Bcolors.END}")
        print(f"{Bcolors.BOLD}{'─' * 30}{Bcolors.END}")
        coordinates = input(f"{Bcolors.BOLD}Enter the row and column:{Bcolors.END}").strip()
        if coordinates == "0":
            break
        try:
            row, col = map(int, coordinates.split())
        except ValueError:
            print(f"{Bcolors.FAIL}Invalid input.{Bcolors.END}")
            continue
        if row < 1 or row > HEIGHT or col < 1 or col > WIDTH:
            print(f"{Bcolors.FAIL}Invalid coordinates.{Bcolors.END}")
            continue
        cell: Cell = BOARD[row - 1][col - 1]
        if cell.status == 0:
            cell.setAlive()
        else:
            cell.setDead()

def randomBoard(percent=50):
    for row in BOARD:
        for cell in row:
            chance = rand.randint(1, 100)
            if chance <= percent:
                cell.setAlive()
            else:
                cell.setDead()


if __name__ == "__main__":
    print(f"""{Bcolors.BLUE}
    ▓█▓█▓█▀▀▓█▓▓▓█▀▀▓█▀█▓█▄█▓█▀▀▓▓▓▀█▀▓█▀█▓▓▓▀█▀▓█▓█▓█▀▀
    ▓█▄█▓█▀▀▓█▓▓▓█▓▓▓█▓█▓█▓█▓█▀▀▓▓▓▓█▓▓█▓█▓▓▓▓█▓▓█▀█▓█▀▀
    ▓▀▓▀▓▀▀▀▓▀▀▀▓▀▀▀▓▀▀▀▓▀▓▀▓▀▀▀▓▓▓▓▀▓▓▀▀▀▓▓▓▓▀▓▓▀▓▀▓▀▀▀
    ▓█▀▀▓█▀█▓█▄█▓█▀▀▓▓▓█▀█▓█▀▀▓▓▓█▓▓▓▀█▀▓█▀▀▓█▀▀▓█      
    ▓█▓█▓█▀█▓█▓█▓█▀▀▓▓▓█▓█▓█▀▀▓▓▓█▓▓▓▓█▓▓█▀▀▓█▀▀▓▀      
    ▓▀▀▀▓▀▓▀▓▀▓▀▓▀▀▀▓▓▓▀▀▀▓▀▓▓▓▓▓▀▀▀▓▀▀▀▓▀▓▓▓▀▀▀▓▀      
    {Bcolors.END}""")
    welcomeText = f"{Bcolors.HEADER}Press Enter to continue.{Bcolors.END}"
    welcome = input(f"{welcomeText:─^70}")
    helpMenu()
    menu()
