import random

def get_bet(balance, minimum=1):
    while True:
        try:
            bet = int(input(f"Your balance: ${balance}. Enter bet (min ${minimum}): "))
            if minimum <= bet <= balance:
                return bet
            print("Invalid bet.")
        except ValueError:
            print("Enter a valid integer bet.")

def blackjack(balance):
    bet = get_bet(balance, 1)
    def deal_card():
        return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
    def hand_value(hand):
        value = sum(hand)
        aces = hand.count(11)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    player = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]
    print("Dealer shows:", dealer[0])
    print("Your hand:", player, f"(= {hand_value(player)})")

    while hand_value(player) < 21:
        move = input("Hit or stand? (h/s): ").strip().lower()
        if move == 'h':
            player.append(deal_card())
            print("Your hand:", player, f"(= {hand_value(player)})")
        elif move == 's':
            break

    pval = hand_value(player)
    if pval > 21:
        print("Bust! Dealer wins.")
        return balance - bet
    print("Dealer's hand:", dealer)
    while hand_value(dealer) < 17:
        dealer.append(deal_card())
    dval = hand_value(dealer)
    print("Dealer's final hand:", dealer, f"(= {dval})")
    if dval > 21 or pval > dval:
        print("You win!")
        return balance + bet
    elif pval == dval:
        print("Push!")
        return balance
    else:
        print("Dealer wins.")
        return balance - bet

def baccarat(balance):
    bet = get_bet(balance, 1)
    def draw_hand():
        return [random.randint(1, 10), random.randint(1, 10)]
    def hand_value(hand):
        return sum(hand) % 10

    player = draw_hand()
    banker = draw_hand()
    print("Player:", player, f"(= {hand_value(player)})")
    print("Banker:", banker, f"(= {hand_value(banker)})")

    if hand_value(player) <= 5:
        player.append(random.randint(1, 10))
        print("Player draws:", player[-1])
    if hand_value(banker) <= 5:
        banker.append(random.randint(1, 10))
        print("Banker draws:", banker[-1])

    pv = hand_value(player)
    bv = hand_value(banker)
    print("Final Player:", player, f"(= {pv})")
    print("Final Banker:", banker, f"(= {bv})")
    if pv > bv:
        print("Player wins.")
        return balance + bet
    elif bv > pv:
        print("Banker wins.")
        return balance - bet
    else:
        print("Tie.")
        return balance

def slots(balance):
    symbols = ['7', 'BAR', '🍒', '🍋', '🔔']
    min_bet = 10 if balance >= 10 else 1
    bet = get_bet(balance, min_bet)
    balance -= bet
    result = [random.choice(symbols) for _ in range(3)]
    print(" | ".join(result))
    if result.count(result[0]) == 3:
        print("Jackpot! +$" + str(bet * 10))
        balance += bet * 10
    elif len(set(result)) == 1 or len(set(result)) == 2:
        print("Small win! +$" + str(bet * 2))
        balance += bet * 2
    else:
        print("No win.")
    print("Balance:", balance)
    return balance

if __name__ == "__main__":
    balance = 100
    while balance > 0:
        print("\nChoose a game:")
        print("1. Blackjack")
        print("2. Baccarat")
        print("3. Slots")
        print("4. Quit")
        print(f"Current balance: ${balance}")
        choice = input("> ").strip()
        if choice == '1':
            balance = blackjack(balance)
        elif choice == '2':
            balance = baccarat(balance)
        elif choice == '3':
            balance = slots(balance)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
        if balance <= 0:
            print("You're out of money! Game over.")
            break
