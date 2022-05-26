#
# Write a warships game with field 5x5
import random


def create_random_ship():
    return random.randint(0, 5), random.randint(0, 5)


def play_again():
    try_again = input("Play again? <Y>es or <N>o? >: ").lower()
    if try_again == "y":
        play_game()
    else:
        print("Goodbye!")
        return

print("Welcome to the Warships game!")
def play_game():
    game_board = [["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"]]

    for i in game_board:
        print(*i)

    ship1 = create_random_ship()
    ship2 = create_random_ship()
    ship3 = create_random_ship()
    ships_left = 3
    bullet = 10

    while bullet:
        try:
            row = int(input("Enter a row number between 1-5 >: "))
            column = int(input("Enter a column number between 1-5 >: "))
        except ValueError:
            print("Only enter number!")
            continue

        if row not in range(1, 6) or column not in range(1, 6):
            print("\nThe numbers must be between 1-5!")
            continue

        row = row - 1
        column = column - 1

        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print("\nYou have already shot that place!\n")
            continue
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3:
            print("\nYou hit!\n")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("You won!")
                play_again()
        else:
            print("\nYou missed!\n")
            game_board[row][column] = "-"
            bullet -= 1

        for i in game_board:
            print(*i)

        print(f"Bullet left: {bullet} | Ships left: {ships_left}")

    play_again()


if __name__ == "__main__":
    play_game()