from bcolors import Bcolors
from cell import Cell

HEIGHT = 20
WIDTH = 20
GENERATIONS = 1
BOARD = [[Cell(0, 0) for i in range(WIDTH)] for j in range(HEIGHT)]

OPTIONS = {
    "stopAfterEachGeneration": {"name": "Pause between generations", "value": False},
    "showGenerationNumber": {"name": "Show generation number", "value": True},
    "showBetweenStates": {"name": "Show between states", "value": True},
    "showUpdatedBoard": {"name": "Show updated board", "value": True},
    "infiniteBoard": {"name": "Infinite board", "value": True},
}


def menu():
    while True:
        print(f"{Bcolors.HEADER}Please select an option:{Bcolors.END}")
        menuOptions = ["Edit the board",
                       "Run for 10 generations",
                       "Run for X generations",
                       "Options",
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
                for row in BOARD:
                    for cell in row:
                        cell.setDead()
                printBoard()
                print(f"{Bcolors.BOLD}Board is cleared{Bcolors.END}")
            case "6" | "help":
                helpMenu()
            case _:
                print(f"{Bcolors.FAIL}Invalid choice.{Bcolors.END}")
        print(f"{Bcolors.BOLD}{'─' * 30}{Bcolors.END}")


def helpMenu():
    print(f"{Bcolors.HEADER}Help:{Bcolors.END}")
    print(f"{Bcolors.BLUE}   ███{Bcolors.END} cells are alive")
    print(f"{Bcolors.OK}   ▓▓▓{Bcolors.END} cells will be born in the next generation")
    print(f"{Bcolors.FAIL}   ▓▓▓{Bcolors.END} cells will die in the next generation")
    print(f"   ▓▓▓ cells are empty")


def options():
    while True:
        success = f"{Bcolors.BOLD}[{Bcolors.PASS}ON{Bcolors.END}{Bcolors.BOLD}/OFF]{Bcolors.END}"
        failure = f"{Bcolors.BOLD}[ON{Bcolors.BOLD}/{Bcolors.FAIL}OFF{Bcolors.END}{Bcolors.BOLD}]{Bcolors.END}"
        print(f"{Bcolors.HEADER}Options:{Bcolors.END}")
        i = 1
        print(f"{Bcolors.BOLD}{Bcolors.HELP}{0:>3}. Back to menu.{Bcolors.END}")
        for key, value in OPTIONS.items():
            if value["value"]:
                print(f"{Bcolors.BOLD}{i:>3}. {value['name']:<40}{success}{Bcolors.END}")
            else:
                print(f"{Bcolors.BOLD}{i:>3}. {value['name']:<40}{failure}{Bcolors.END}")
            i += 1
        choice = input(f"{Bcolors.BOLD}Enter the number of the option you want to change:{Bcolors.END}")
        print(f"{Bcolors.BOLD}{'─' * 30}{Bcolors.END}")
        match choice:
            case "0":
                break
            case "1":
                OPTIONS["stopAfterEachGeneration"]["value"] = not OPTIONS["stopAfterEachGeneration"]["value"]
            case "2":
                OPTIONS["showGenerationNumber"]["value"] = not OPTIONS["showGenerationNumber"]["value"]
            case "3":
                OPTIONS["showBetweenStates"]["value"] = not OPTIONS["showBetweenStates"]["value"]
            case "4":
                OPTIONS["showUpdatedBoard"]["value"] = not OPTIONS["showUpdatedBoard"]["value"]
            case "5":
                OPTIONS["infiniteBoard"]["value"] = not OPTIONS["infiniteBoard"]["value"]
            case _:
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
            if OPTIONS["infiniteBoard"]['value']:
                topLeft = BOARD[(i - 1) % HEIGHT][(j - 1) % WIDTH].status
                top = BOARD[(i - 1) % HEIGHT][j].status
                topRight = BOARD[(i - 1) % HEIGHT][(j + 1) % WIDTH].status
                left = BOARD[i][(j - 1) % WIDTH].status
                right = BOARD[i][(j + 1) % WIDTH].status
                bottomLeft = BOARD[(i + 1) % HEIGHT][(j - 1) % WIDTH].status
                bottom = BOARD[(i + 1) % HEIGHT][j].status
                bottomRight = BOARD[(i + 1) % HEIGHT][(j + 1) % WIDTH].status
            else:
                topLeft = BOARD[i - 1][j - 1].status if 0 < i - 1 < HEIGHT and 0 < j - 1 < WIDTH else 0
                top = BOARD[i - 1][j].status if 0 < i - 1 < HEIGHT else 0
                topRight = BOARD[i - 1][j + 1].status if 0 < i - 1 < HEIGHT and 0 < j + 1 < WIDTH else 0
                left = BOARD[i][j - 1].status if 0 < j - 1 < WIDTH else 0
                right = BOARD[i][j + 1].status if 0 < j + 1 < WIDTH else 0
                bottomLeft = BOARD[i + 1][j - 1].status if 0 < i + 1 < HEIGHT and 0 < j - 1 < WIDTH else 0
                bottom = BOARD[i + 1][j].status if 0 < i + 1 < HEIGHT else 0
                bottomRight = BOARD[i + 1][j + 1].status if (0 < i + 1 < HEIGHT and 0 < j + 1
                                                             < WIDTH) else 0

            count = topLeft + top + topRight + left + right + bottomLeft + bottom + bottomRight

            if BOARD[i][j].status == 1:
                if count < 2 or count > 3:
                    BOARD[i][j].next_status = 0
            else:
                if count == 3:
                    BOARD[i][j].next_status = 1
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
