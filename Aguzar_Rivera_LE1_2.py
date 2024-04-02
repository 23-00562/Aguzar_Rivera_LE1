
game_library = {
    "Donkey Kong" : {"quantity": 3, "cost" : 2},
    "Super Mario Bros" : {"quantity": 5, "cost" : 3},
    "Tetris" : {"quantity": 2, "cost" : 1}
}

user_accounts = {"admin": {"password": "adminpass", "balance": 0,"amount_purchased": 0,"points": 0, "inventory": {}}}


admin_username = "admin"
admin_password = "adminpass"

def register_user():
    print ("\nREGISTER")
    while True:
        try:
            username = input ("\nEnter a Valid Username (Press ENTER to go back): ")
            if not username:
                return
            else:
                password = str(input("Enter a Password (at least 8 characters): "))
                if len(password) < 8:
                    print("\nTry Again! Password must be at least 8 characters long.")
                else:
                    user_accounts[username] = {
                        "password": password,
                        "balance": 0,
                        "amount_purchased": 0,
                        "points": 0,
                        "inventory": {}
                    }
                    print("\nYou have successfully created your account!")
                    break
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def login():
    print ("\nLOG IN")
    while True:
        try:
            username = input ("\nEnter your Username (Press ENTER to go back): ")
            if not username:
                return
            elif username == admin_username:
                password = str (input("Enter your Password: "))
                if password == admin_password:
                    print (f"\nWelcome Admin {username}")
                    admin_menu(username)
                    break
                else:
                    print ("\nPlease try again! Password doesn't match.")
            elif username not in user_accounts:
                print ("\nUser not found! Please create an acoount.")
            else:
                password = str (input("Enter your Password: "))
                if user_accounts [username] ["password"] == password:
                    print (f'\nWelcome to Game Library {username}')
                    user_menu(username)
                    break
                else:
                    print ("\nPlease try again! Password doesn't match.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def available_games():
    print ("\nAVAILABLE GAMES")
    for game, details in game_library.items():
        print (f"Game: {game}, Quantity: {details ["quantity"]}, Price:{details ["cost"]}")

def rent_game(username):
    print ("\nRENT A GAME")
    while True:
        try:
            available_games()
            game = input ("\nEnter the game you want to rent (Press ENTER to go back): ")
            if not game:
                return
            elif game not in game_library:
                print ("\nGame not found! Choose a valid game.")
            else:
                if game_library [game] ["quantity"] > 0:
                    if username in user_accounts:
                        balance = user_accounts[username]["balance"]
                        cost = game_library[game]["cost"]
                        if balance > cost:
                            user_accounts[username]["balance"] -= cost
                            game_library[game]["quantity"] -= 1
                            user_accounts[username]["amount_purchased"] += cost
                            if game in user_accounts[username]["inventory"]:
                                user_accounts[username]["inventory"][game] += 1
                            else:
                                user_accounts[username]["inventory"][game] = 1
                            print (f"You have successfully rented {game} ")
                            break
                        else:
                            print ("\nInsufficient balance. Please top up your account.")
                    else:
                        print ("\nUsername not found! Please create an Account.")
                else:
                    print ("\nGame not available for rent. Choose another game")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def user_inventory(username):
    if username in user_accounts:
        if not user_accounts[username]["inventory"]:
            print("\nNo games rented yet.")
            return
        else:
            print("\nYOUR GAME INVENTORY")
        for game, quantity in user_accounts[username]["inventory"].items():
            print(f"Game: {game}, Quantity: {quantity}")
    else:
        print("\nUser not found.")

def return_game(username):
    print ("\nRETURN A GAME")
    while True:
        try:
            user_inventory(username)
            game = input ("\nEnter the Game you want to Return (Press ENTER to go Back): ")
            if not game:
                return
            elif game in user_accounts[username] ["inventory"]:
                game_library[game]["quantity"] += 1
                user_accounts[username] ["inventory"] [game] -= 1
                print (f"You have successfully returned {game}.")
                if user_accounts[username] ["inventory"] [game] == 0:
                    del user_accounts[username] ["inventory"] [game]
                    break
                else:
                    return
            else:
                print ("The game you entered is not in your inventory.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def top_up (username):
    print ("\nTOP UP")
    while True:
        try:
            amount = float(input ("\nEnter the amount you want to top up (Press ENTER to go Back): "))
            if not amount:
                return
            elif amount <= 0:
                print ("Amount should be greter than 0.")
            else:
                if username in user_accounts:
                    user_accounts [username] ["balance"] += amount
                    print(f"Successfully topped up ${amount}.")
                    print(f"\nCurrent balance for {username}: ${user_accounts[username]["balance"]}.")
                    break
                else:
                    print("\nUser not found! Please create an account.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def check_points(username):
    if username in user_accounts:
        available_points  = user_accounts[username]["amount_purchased"]//2
        user_accounts[username]["points"] = available_points
        print (f"\nHey {username}! You have {available_points} points.")
    else:
        print ("\nUsername not found! Please create an Account.")

def redeem_free_game(username):
    print ("\nREDEEM FREE GAME")
    while True:
        try:
            check_points(username)
            choice = input("\nDo you want to Redeem a Free Game (y/n): ").lower()
            if choice == "n":
                break
            elif choice == "y":
                available_games()
                game = input ("\nEnter the game you want to rent (Press ENTER to go back): ")
                if not game:
                    return
                elif game not in game_library:
                    print ("Game not found! Choose a valid game.")
                else:
                    if game_library [game] ["quantity"] > 0:
                        if username in user_accounts:
                            free_point = user_accounts[username]["points"]
                            if free_point > 3:
                                user_accounts[username]["points"] -= 3
                                game_library[game]["quantity"] -= 1
                                user_accounts[username]["amount_purchased"] -= 6
                                user_accounts[username] ["inventory"] [game] = 0
                                user_accounts[username] ["inventory"] [game] += 1
                                print (f"You have successfully rented {game} ")
                                break
                            else:
                                print ("Insufficient Points. Please purchase more.")
                        else:
                            print ("Username not found! Please create an Account.")
                    else:
                        print ("Game not available for rent. Choose another game")
            else:
                print ("Invalid choice. Please try again.")

        except ValueError as e:
            print (f"An error occured: {e}")

def add_game(username):
    print ("\nADD GAME")
    available_games()
    game = input("\nEnter the name of the game: ")
    if game in game_library:
        print("\nGame already exists in the library.")
    else:
        quantity = int(input("\nEnter the quantity of the game: "))
        cost = float(input("Enter the cost of the game: "))
        game_library[game] = {"quantity": quantity, "cost": cost}
        print(f"\n{game} added to the game library.")

def remove_game(username):
    print ("\nREMOVE GAME")
    available_games()
    game = input("\nEnter the name of the game (Press ENTER to go Back): ")
    if not game:
        return
    else:
        if game not in game_library:
            print("\nGame doesn't exists in the library.")
        else:
            del game_library [game] 
            print(f"\n{game} has been remove from the game library.")

def update_quantity(username):
    print ("\nUPDATE GAME QUANTITY")
    game = input ("\nEnter the name of the game (Press ENTER to go Back): ")
    if not game:
        return
    else: 
        if game not in game_library:
            print("\nGame doesn't exists in the library.")
        else:
            quantity = int(input("Enter the new quantity of the game: "))
            game_library[game]["quantity"] = quantity
            print(f"\nQuantity of {game} updated.")

def update_cost(username):
    print ("\nUPDATE THE GAME COST")
    game = input ("\nEnter the name of the game (Press ENTER to go Back): ")
    if not game:
        return
    else: 
        if game not in game_library:
            print("\nGame doesn't exists in the library.")
        else:
            cost = int(input("Enter the new cost of the game: "))
            game_library[game]["cost"] = cost
            print(f"Cost of {game} updated.")

def admin_options(username):
    print("\nADMIN OPTIONS")
    while True:
        print("\nPlease select an option:")
        print("1. Add Game")
        print("2. Remove Game")
        print("3. Update Game Quantity")
        print("4. Update Game Cost")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_game(username)
        elif choice == "2":
            remove_game(username)
        elif choice == "3":
            update_quantity(username)
        elif choice == "4":
            update_cost(username)
        elif choice == "5":
            break
        else:
            print("\nInvalid choice. Please try again.")

def admin_menu(username):
    print("\nADMIN MENU")

    while True:
        print("\nPlease select an option:")
        print("1. Rent a Game")
        print("2. Return a Game")
        print("3. Top Up")
        print("4. Game Inventory")
        print("5. Redeem Free Game")
        print("6. Check Points")
        print("7. Admin Options")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            rent_game(username)
        elif choice == "2":
            return_game(username)
        elif choice == "3":
            top_up(username)
        elif choice == "4":
            user_inventory(username)
        elif choice == "5":
            redeem_free_game(username)
        elif choice == "6":
            check_points(username)
        elif choice == "7":
            admin_options(username)
        elif choice == "8":
            print("\nExiting admin menu.")
            break
        else:
            print("\nInvalid choice. Please try again.")

def user_menu(username):
    print(f"\n{username}'s MENU")

    while True:
        print("\nPlease select an option:")
        print("1. Rent a Game")
        print("2. Return a Game")
        print("3. Top Up")
        print("4. Game Inventory")
        print("5. Redeem Free Game")
        print("6. Check Points")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            rent_game(username)
        elif choice == "2":
            return_game(username)
        elif choice == "3":
            top_up(username)
        elif choice == "4":
            user_inventory(username)
        elif choice == "5":
            redeem_free_game(username)
        elif choice == "6":
            check_points(username)
        elif choice == "7":
            print(f"\nExiting {username} menu.")
            break
        else:
            print("\nInvalid choice. Please try again.")


def main():
    while True:
        print("\n----------------------------------------------------")
        print("               WELCOME TO GAME LIBRARY                ")
        print("----------------------------------------------------")
        print("\nPlease select an option:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            register_user()
        elif choice == "3":
            break
        else:
            print("\nInvalid choice. Please try again.")

    print("\nExiting Game Mania")

main ()