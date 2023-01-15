
import random

card_deck = []
face_cards = []

for num in range(4):
    for number in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        card_deck.append(number)
    for faces in ['Ace', 'Jack', 'Queen', 'King']:
        face_cards.append(faces)
card_deck.sort()
face_cards.sort()
card_deck.extend(face_cards)

game = 'active'

class PlayerHand:
    def __init__(self):
        #self.num_of_cards = 2
        self.card_count = 0
        self.total = 0
        self.my_hand = {}
        self.aces = 0
        global card_deck

    '''def total_of_cards(self):
        for num in self.my_hand:
            card = self.my_hand[num][1]
            self.total += card
        return self.total'''

    def add_to_hand(self):  # adds cards at random from card_deck,and removes them from card_deck
        self.my_hand[self.card_count] = [card_deck[random.randint(0, (len(card_deck) - 1))], 0]
        if self.my_hand[self.card_count][0] == 'King' or self.my_hand[self.card_count][0] == 'Queen' or\
        self.my_hand[self.card_count][0] == 'Jack':
            self.my_hand[self.card_count][1] = 10
        elif self.my_hand[self.card_count][0] == 'Ace':
            self.my_hand[self.card_count][1] = 1
        else:
            self.my_hand[self.card_count][1] = self.my_hand[self.card_count][0]
        card_deck.remove(self.my_hand[self.card_count][0])  # removes card from the deck
        card = self.my_hand[self.card_count][1]
        self.total += card  # add total of cards
        self.card_count += 1


    def print_hand(self):
        print('You have the following cards:')
        for card in self.my_hand:
            print(self.my_hand[card][0])

    def contains_ace(self):
        for card in self.my_hand:
            if self.my_hand[card][0] == 'Ace':
                self.aces += 1
        if self.aces > 0:
            print(f'you have {self.aces} Aces')
        for card in self.my_hand:
            if self.my_hand[card][0] == 'Ace':
                print('Do you wish to use this Ace as 1 or 11?')
                answer = input('Enter(1/11) ')
                if answer == 11:
                    self.my_hand[card][1] = 11
                else:
                    self.my_hand[card][1] = 1







class EnemyAI:
    def __init__(self,player):
        #self.choose_hit = choose_hit
        self.player = player

    #def cycle_all_cards(self):
       #for card in self.player.my_hand:
            #return card

    def pick_one_or_eleven(self):
        total_ace_cards = 0
        for card in self.player.my_hand:
            if self.player.my_hand[card][0] == 'Ace':
                total_ace_cards += 1

        if total_ace_cards == 1 and self.player.total == 11: # Ace card is default 1, so change it to 11 makes 21
            for card in self.player.my_hand:
                if self.player.my_hand[card][0] == 'Ace':
                    self.player.my_hand[card][1] = 11
                    return 'stay'
        if total_ace_cards == 1 and self.player.total >= 8:
            for card in self.player.my_hand:
                if self.player.my_hand[card][0] == 'Ace':
                    self.player.my_hand[card][1] = 11
                    return 'stay'
        if total_ace_cards == 1 and self.player.total <= 7:
            rand_choice = random.randrange(1, 3)
            if rand_choice = 1:
                return 'stay'
            if rand_choice = 2:
                return 'hit'
        if total_ace_cards == 2:
            return 'hit'
        if total_ace_cards == 3:
            return 'hit'
        if total_ace_cards == 4:
            return 'hit'




        '''if 'Ace' in self.player.my_hand:
            if self.player.total == 21:
                return 'n'
            if self.player.total == 20:'''














def ace_one_or_eleven(player):
    if 'Ace' in player.my_hand:
        player.contains_ace()

player_one = PlayerHand()
player_two = PlayerHand()

player_one.add_to_hand()
player_two.add_to_hand()
player_one.add_to_hand()
player_two.add_to_hand()
player_two_ai = EnemyAI(player_two)
#player_one.print_hand()
player_two.print_hand()
#print(player_two.card_count)

player_two_ai.pick_one_or_eleven()
print(player_two.my_hand)



while player_one.total < 22 and game == 'active':
    player_one.contains_ace()
    hit_again = input('hit again? (Y/N)')


    if hit_again == 'Y' or hit_again == 'y':

        player_one.add_to_hand()
        print('Your total value is:')
        print(player_one.total)
        player_one.print_hand()
    else:
        game = 'not active'





player_one.print_hand()
print('You have busted\nGAME OVER')
