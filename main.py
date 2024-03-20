############### Blackjack Project #####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_over_1 = {1: "You win", 2: "You lose", 3: "DRAW"}

import random
from art import logo


def hit_me():
    return random.choice(cards)


def game_over(your_cards, computer_cards, end_number):
    print(f"Your final hand: {your_cards}, final score {sum(your_cards)}")
    print(f"Computers final hand {computer_cards}, final score {sum(computer_cards)}")
    print(f"{game_over_1[end_number]}")
    blackjack()


def blackjack():
    a = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if a == "y":
        print(logo)
        your_cards = []
        computer_cards = []

        for i in range(2):
            your_cards.append(hit_me())
            computer_cards.append(hit_me())

        if sum(your_cards) < 10:
            your_cards.append(hit_me())

        print(f"Your cards: {your_cards}, current score {sum(your_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        another = True
        while another:
            choice = input(f"Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y":
                your_cards.append(hit_me())
                if sum(your_cards) > 21:
                    if your_cards.count(11) > 0:
                        your_cards[your_cards.index(11)] = 1
                if sum(your_cards) > 21:
                    end_number = 2
                    game_over(your_cards, computer_cards, end_number)
                print(f"Your cards: {your_cards}, current score {sum(your_cards)}")
                print(f"Computer's first card: {computer_cards[0]}")
            else:
                another = False
                while sum(computer_cards) < 17:
                    computer_cards.append(hit_me())
                    if sum(computer_cards) > 21:
                        if computer_cards.count(11) > 0:
                            computer_cards[computer_cards.index(11)] = 1
                    if sum(computer_cards) > 21:
                        end_number = 1
                        game_over(your_cards, computer_cards, end_number)

        if sum(computer_cards) < sum(your_cards):
            end_number = 1
            game_over(your_cards, computer_cards, end_number)
        elif sum(computer_cards) == sum(your_cards):
            end_number = 3
            game_over(your_cards, computer_cards, end_number)
        else:
            end_number = 2
            game_over(your_cards, computer_cards, end_number)

    else:
        print("Goodbye")


blackjack()