import os
import random

#import os (operating system) to run code
#import random so that the cards can be shuffled

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
count = 0


# defines the variables values (cards) for blackjack
#*4 signals that there are 4 decks being used

def deal(deck):
    hand = []
    for item in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
                card = 'J'
        if card == 12:
                card = "Q"
        if card == 13:
                card = "K"
        if card == 14:
                card = "A"
        hand.append(card)
    return hand

# the function 'deal' represents the dealer shuffling the 'deck' of cards
# numbers 2 through 9 do not have an alphabetical value in the game, but 11, 12, 13, & 14 are represented as J, Q, K, A, respectfully
# the object of the game is to reach 21 or below by summing the cards drawn, anything over 21 results in busting & losing the hand

def play_again():
    again = input('Play again? (Y/N) : ').lower()
    if again == 'y':
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()
    else:
	    print('Bye!')
	    count = 0
	    exit()

# the function 'play_again' is requesting whether the player would like to play another hand

def total(hand):
    total = 0
    for card in hand:
	    if card == 'J' or card == 'Q' or card == 'K':
	        total += 10
	    elif card == 'A':
	        if total >= 11: 
                    total += 1
	        else: 
                    total += 11
	    else: 
                total += card
    return total

# the total function is giving a numerical value of the alphabetical cards that can sum with numeric cards

def hit(hand):
    global count
    card = deck.pop()
    if card == 11:
            card = 'J'
    if card == 12:
            card = 'Q'
    if card == 13:
            card = 'K'
    if card == 14:
            card = 'A'
    hand.append(card)
    #print("The count is " + str(count))
    return hand

# the function 'hit' is asking the player whether it would like another chance to sum up to 21, caution, hitting can lead to busting the hnad and losing!

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

# clear allows the code to be called in other operating systems

def hand_results(dealer_hand, player_hand):
	clear()
	print ('dealer hand = ' + str(dealer_hand) + ' dealer total = ' + str(total(dealer_hand)))
	print ('player hand = ' + str(player_hand) + ' player total = ' + str(total(player_hand)))

# hand_results prints the final outcome of the current hand for both the dealer and the player                                    

def blackjack(dealer_hand, player_hand):
	if total(player_hand) == 21:
		hand_results(dealer_hand, player_hand)
		print ('Player hits Blackjack! Player wins!')
		play_again()
	elif total(dealer_hand) == 21:
		hand_results(dealer_hand, player_hand)		
		print ('Dealer hits blackjack... You lose...')
		play_again()

# the hand is automatically over when either the dealer or the player hits a blackjack!
# results are printed for either dealer or player that are dealt a blackjack

def score(dealer_hand, player_hand):
	if total(player_hand) == 21:
		hand_results(dealer_hand, player_hand)
		print ('Player Blackjack!\n')
	elif total(dealer_hand) == 21:
		hand_results(dealer_hand, player_hand)		
		print ('Dealer Blackjack. Player loses...\n')
	elif total(player_hand) > 21:
		hand_results(dealer_hand, player_hand)
		print ('Player busted. Player loses...\n')
	elif total(dealer_hand) > 21:
		hand_results(dealer_hand, player_hand)			 
		print ('Dealer busted. Player wins!\n')
	elif total(player_hand) < total(dealer_hand):
		hand_results(dealer_hand, player_hand)
		print ('Dealer is closer to 21. You lose...\n')
	elif total(player_hand) > total(dealer_hand):
		hand_results(dealer_hand, player_hand)			
		print('Player closer to 21. You win!\n')		
	elif total(player_hand) == total(dealer_hand):
		hand_results(dealer_hand, player_hand)
		print('Dealer and Player have the same hand. Draw!')
        
# the score function displays who wins.
# there are many options in blackjack in terms of winning or losing, drawing 21 = automatic win, whichever players is closest to 21 also wins.


def Count(player_hand, dealer_hand):
    global count
    
    if 2 in dealer_hand:
        count += 1
    if 2 in player_hand:
        count += 1
    if 3 in dealer_hand:
        count += 1
    if 3 in player_hand:
        count += 1
    if 4 in dealer_hand:
        count += 1
    if 4 in player_hand:
        count += 1
      
    if 8 in dealer_hand:
        count -= 1
    if 8 in player_hand:
        count -= 1
    if 9 in dealer_hand:
        count -= 1
    if 9 in player_hand:
        count -= 1
    if 10 in dealer_hand:
        count -= 1
    if 10 in player_hand:
        count -= 1
    if 'J' in dealer_hand:
        count -= 1
    if 'J' in player_hand:
        count -= 1
    if 'Q' in dealer_hand:
        count -= 1
    if 'Q' in player_hand:
        count -= 1
    if 'K' in dealer_hand:
        count -= 1
    if 'K' in player_hand:
        count -= 1
    if 'A' in dealer_hand:
        count -= 1
    if 'A' in player_hand:
        count -= 1
    return count

# The Count function is meant to display the current count of the deck. The more positive the count is, the higher the probability of 7 or greater card coming. the more negative the count is, the more likely a 4 or lower card will come
# i could not figure out how to run the count function without using if statements:-/
   
def game():
    global count
    choice = 0
    clear()
    print ('Would you like to play Blackjack with a count on your cards? \n')
    print('The more positive the count, the larger the probability a card 7 or larger may come!')
    print('The more negative the count, the larger the probability a card 4 or smaller may come!')
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print('The dealer is showing a ' + str(dealer_hand[0]))
    print('You have ' + str(player_hand) + ' = ' + str(total(player_hand)))
    print('The count is ' + str(Count(player_hand, dealer_hand)))
    blackjack(dealer_hand, player_hand)
    quit = False
    while not quit:        
        choice = input('Do you want to [H]it, [S]tand, or [Q]uit: ').lower()
        if choice == 'h':
            count = 0
            hit(player_hand)
            print(player_hand)
            print('The count is ' + str(Count(player_hand, dealer_hand)))
            if total(player_hand) > 21:
                print('You Busted. You lose.')
                play_again()
        elif choice == "s":
            while total(dealer_hand) < 17:
              	count = 0
              	hit(dealer_hand)
              	print (dealer_hand)
              	print('The count is ' + str(Count(player_hand, dealer_hand)))
              	if total(dealer_hand) > 21:
                    print ('dealer Busted. You win!')
              	play_again()
            score(dealer_hand, player_hand)
            play_again()
        elif choice == 'q':
            print ('Bye!')
            count = 0
            quit = True
            exit()
            
# The game function allows the actual game of blackjack to be carried out
# The dealer and the player are each given a deck representing the cards they'll each be getting
# a while loop is ran since the code will execute as long as the players agrees to continue to play
# the game is over once the player quits

if __name__ == '__main__':
    game()

#__main__ allows game() to be called in order to play blackjack