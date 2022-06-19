from classes.deck import Deck

class textFunc:
    green = '\u001b[32m'
    magenta = '\u001b[35m'
    cyan = '\033[96m'
    white = '\u001b[37m'
    red = '\u001b[31m'
    dashout = "\n\n-----------------------------------------------------------\n"

class Game:
    def __init__(self,):
        self.player1 = Player()
        self.player2 = Player()
        self.pile = []

    def run_game(self):
        while len(self.player1.deck.cards) > 0:
            self.pile_add()
            self.compare()
        if len(self.player1.hoard) > len(self.player2.hoard):
            print("YOU WIN")
        elif len(self.player1.hoard) < len(self.player2.hoard):
            print("GET REKT SCRUB")
        else:
            print("ITS A TIE")

    def pile_add(self):
        # Display Cards Against Eachother
        self.pile.append(self.player1.get_hand())
        self.pile.append(self.player2.get_hand())
    
    def compare(self):
        input("\nPress Enter to Begin Next Round\n")
        self.pile[len(self.pile) - 2].card_info()
        self.pile[len(self.pile) - 1].card_info()
        # Compares 2 Card Values to determine weight, rewards accordingly
        if self.pile[len(self.pile) - 2].point_val > self.pile[len(self.pile) - 1].point_val:
            for card in self.pile:
                self.player1.hoard.append(card)
            print("Human Wins this Round")
            self.pile.clear()
        elif self.pile[len(self.pile) - 2].point_val < self.pile[len(self.pile) - 1].point_val:
            for card in self.pile:
                self.player2.hoard.append(card)
            print("NPC Wins this Round")
            self.pile.clear()
        else:
            if len(self.player1.deck.cards) >= 1:
                self.pile_add()
                print("Draw Again")
                self.compare()
            else:
                self.pile.clear()
                print("No More Cards, Cards Discarded")

def menu():
    playVal = get_play_val()
    if playVal == "2":
        return
    elif playVal == "1":
        game = Game()
        game.run_game()
        menu()
    else:
        restart_menu()

def restart_menu():
    print(f"{textFunc.red}Invalid input, try again!")
    menu()

def get_play_val():
    return input(f"{textFunc.cyan}WAR. LETS PLAY? \n{textFunc.green}1) YEA!\n{textFunc.red}2) nah.{textFunc.white}\n")


class Player:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hoard = []
    
    def get_hand(self):
        return self.deck.cards.pop(0)

menu()