import random
from art import logo
from replit import clear

print(logo)

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



end_of_game = True
while end_of_game:
    playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if playGame == "y":
        user_guess1 = random.choices(cards, k=2)
        print(f"Your cards: {user_guess1}, current score: {sum(user_guess1)}")

        com_guess1 = random.choices(cards, k=2)
        print(f"computer's first card: {com_guess1[0]}")

        if 11 in user_guess1:
          print("You win! 😁")

        elif 11 in com_guess1:
          print("You Lose")
        
        elif sum(user_guess1) == 21 and sum(com_guess1) == 21:
            print("Match draw")

        elif sum(user_guess1) == 21 and sum(com_guess1) < 21:
            print("You win! 😁")

        elif sum(user_guess1) < 21 and sum(com_guess1) == 21:
            print("You lose! ")

        else:

            rounds = input(f"Type 'y' to get another card, type 'n' to pass: ")
            if rounds == "y":
                user_guess2 = random.choice(cards)
                user_guess1.append(user_guess2)
                print(f"Your cards: {user_guess1}, current score: {sum(user_guess1)}")

                com_guess2 = random.choice(cards)
                com_guess1.append(com_guess2)

                if sum(user_guess1) > 21:
                    print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                    print(f"You went over. You lose!")
                
                elif sum(com_guess1) > 21:
                    print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                    print(f"Computer went over. You win! 😁")
                  
                elif sum(user_guess1) == 21 and sum(com_guess1) == 21:
                    print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                    print("Match draw")

                elif sum(user_guess1) < 21 and sum(com_guess1) == 21:
                    print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                    print("You lose! ")

                elif sum(user_guess1) == 21 and sum(com_guess1) < 21:
                    print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                    print("You win! 😁")

                else:
                    print(f"computer's first card: {com_guess1[0]}")
                    while True:
                        
                        rounds = input(f"Type 'y' to get another card, type 'n' to pass: ")
                        if rounds == "y":
                            user_guess2 = random.choice(cards)
                            user_guess1.append(user_guess2)
                            print(f"Your cards: {user_guess1}, current score: {sum(user_guess1)}")

                            com_guess2 = random.choice(cards)
                            com_guess1.append(com_guess2)

                            if sum(user_guess1) > 21:
                                print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                                print(f"You went over. You lose!")

                            elif sum(com_guess1) > 21:
                                print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                                print(f"Computer went over. You win! 😁")

                            elif sum(user_guess1) < 21 and sum(com_guess1) == 21:
                                print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                                print("You lose! ")

                            elif sum(user_guess1) == 21 and sum(com_guess1) < 21:
                                print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                                print("You win! 😁")

                            elif sum(user_guess1) == 21 and sum(com_guess1) == 21:
                                print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                                print("Match draw")
                            else:
                              print("Game over")
                        

                        else:
                            while sum(com_guess1) <= 17:
                                com_guess2 = random.choice(cards)
                                com_guess1.append(com_guess2)
                                print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                            pass
            
            else:
                print(f"Your final hand: {user_guess1}, current score: {sum(user_guess1)}")
                while sum(com_guess1) <= 17:
                    com_guess2 = random.choice(cards)
                    com_guess1.append(com_guess2)
                print(f"Computer's final hand: {com_guess1}, current score: {sum(com_guess1)}")
                if sum(com_guess1) > 21:
                  print(f"Computer went over. You win! 😁")
                
                elif sum(user_guess1) == sum(com_guess1):
                  print("Match draw")

                elif sum(user_guess1) > sum(com_guess1):
                  print("You win! 😁")

                else:
                  print("You lose! ")
                  

    else:
        end_of_game = False
        

