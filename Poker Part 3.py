import random
random.seed()

from operator import itemgetter

def suits_changer(hands):
    if hands[0]['suits'] == 'Spades':
        return 4
    if hands[0]['suits'] == 'Hearts':
        return 3
    if hands[0]['suits'] == 'Diamonds':
        return 2
    if hands[0]['suits'] == 'Clubs':
        return 1

def ranks_changer(hands):
    if hands == '2':
        return 2
    if hands == '3':
        return 3
    if hands == '4':
        return 4
    if hands == '5':
        return 5
    if hands == '6':
        return 6
    if hands == '7':
        return 7
    if hands == '8':
        return 8
    if hands == '9':
        return 9
    if hands == '10':
        return 10
    if hands == 'Jack':
        return 11
    if hands == 'Queen':
        return 12
    if hands == 'King':
        return 13
    if hands == 'Ace':
        return 14
        
def rank_value_of_card(card):
    rank = card['ranks']
    card_rank_value = rank_value[rank]
    return card_rank_value

def is_a_flush(hands):
    values = list(suit_count.values())
    if 5 in values:
        return True

def is_a_straight(hands):
    s = []
    ranks = 0
    for i in range(5):
        if hands[i]['ranks'] == 'Jack':
            s.append('11')
            
        elif hands[i]['ranks'] == 'Queen':
            s.append('12')
            
        elif hands[i]['ranks'] == 'King':
            s.append('13')
            
        elif hands[i]['ranks'] == 'Ace':
            s.append('14')
                
        else:
            s.append(hands[i]['ranks'])

    p = 0
    for i in range(4):
        a = int(''.join(s[i]))
        b = int(''.join(s[i+1]))
        if a == b - 1:
            p += 1
            
    if int(''.join(s[0])) == 2:
        if int(''.join(s[4])) == 14:
            p += 1

    if p == 4:
        ranks = ranks_changer(s[4])
        return True, ranks
    else:
        return False, ranks
        
def is_a_royal_flush(hands):
    flush = is_a_flush(list(suit_count.values()))
    straight = is_a_straight(hands)

    if hands[0]['ranks'] == '10':
        if hands[4]['ranks'] == 'Ace':
            return True
            
def is_a_straight_flush(hands):
    flush = is_a_flush(list(suit_count.values()))
    straight = is_a_straight(hands)

    if flush == True:
        if straight == True:
            return True

def is_four_of_a_kind(hands):
    a = 0
    ranks = 0
    for i in range(4):
        if hands[i]['ranks'] == hands[i + 1]['ranks']:
            ranks = 0
            a += 1
            ranks = ranks_changer(hand[i]['ranks'])
                
            if i < 3:
                if hands[i]['ranks'] == hands[i + 2]['ranks']:
                    a += 1

    if a == 5:
        return True, ranks
    else:
        return False, ranks

def is_a_full_house(hands):
    a = 0
    ranks = 0
    for i in range(4):
        if hands[i]['ranks'] == hands[i + 1]['ranks']:
            ranks = 0
            a += 1
            ranks = ranks_changer(hand[i]['ranks'])

            if i < 3:
                if hands[i]['ranks'] == hands[i + 2]['ranks']:
                    a += 1

    if a == 4:
        return True, ranks
    else:
        return False, ranks
        
def is_three_of_a_kind(hands):
    a = 0
    ranks = 0
    for i in range(4):
        if hands[i]['ranks'] == hands[i + 1]['ranks']:
            ranks = 0
            a += 1
            ranks = ranks_changer(hand[i]['ranks'])

            if i < 3:
                if hands[i]['ranks'] == hands[i + 2]['ranks']:
                    a += 1

    if a == 3:
        return True, ranks
    else:
        return False, ranks
    
def is_two_pair(hands):
    a = 0
    ranks = 0
    for i in range(4):
        if hands[i]['ranks'] == hands[i + 1]['ranks']:
            ranks = 0
            a += 1
            ranks = ranks_changer(hand[i]['ranks'])

            if i < 3:
                if hands[i]['ranks'] == hands[i + 2]['ranks']:
                    a += 1


    if a == 2:
        return True, ranks
    else:
        return False, ranks

def is_one_pair(hands):
    a = 0
    ranks = 0
    for i in range(4):
        if hands[i]['ranks'] == hands[i + 1]['ranks']:
            ranks = 0
            a += 1
            ranks = ranks_changer(hands[i]['ranks'])

            if i < 3:
                if hands[i]['ranks'] == hands[i + 2]['ranks']:
                    a += 1

    if a == 1:
        return True, ranks
    else:
        return False, ranks

def check_hand(hands):
    royal_flush = is_a_royal_flush(hands)
    
    straight_flush = is_a_straight_flush(hands)
        
    flush = is_a_flush(list(suit_count.values()))

    straight, rank = is_a_straight(hands)

    four_of_a_kind, rank = is_four_of_a_kind(hands)

    full_house, rank = is_a_full_house(hands)

    three_of_a_kind, rank = is_three_of_a_kind(hands)

    two_pair, rank = is_two_pair(hands)

    one_pair, rank = is_one_pair(hands)

    if royal_flush == True:
        return 'a royal flush!', 9, 0
    elif straight_flush == True:
        return 'a straight flush!', 8, 0
    elif flush == True:
        return 'a flush!', 5, 0
    elif straight == True:
        return 'a straight!', 4, rank
    elif four_of_a_kind == True:
        return 'a four of a kind!', 7, rank
    elif full_house == True:
        return 'a full house!', 6, rank
    elif three_of_a_kind == True:
        return 'a Three of a kind!', 3, rank
    elif two_pair == True:
        return 'a two pair!', 2, rank
    elif one_pair == True:
        return 'a pair!', 1, rank
    else:
        a = ('{}'.format(hands[4]['ranks']))
        rank = ranks_changer(a)
        return 'a high card!', 0, rank


def judgement(you, pc, your_ranks, pc_ranks):
    if you > pc:
        return 'YOU WIN!'
    elif you < pc:
        return 'YOU LOSE.'
    else:
        
        if you == 9 or you == 8 or you == 5:
            your_suits = suits_changer(your_hands)
            pc_suits = suits_changer(pc_hands)
            if your_suits > pc_suits:
                return 'YOU WIN!'
            elif your_suits < pc_suits:
                return 'YOU LOSE.'
            else:
                return 'DUCE'

        else:
            if int(your_ranks) > int(pc_ranks):
                return 'YOU WIN!'
            if int(your_ranks) < int(pc_ranks):
                return 'YOU LOSE.'
            else:
                return 'DUCE'

            
while True:
    suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
    ranks = ['Ace', '2', '3', '4', '5','6','7', '8','9','10', 'Jack', 'Queen', 'King']

    cards = []

    for suit in suits:
        for rank in ranks:
            cards.append({'ranks':rank, 'suits':suit})

    hand = []
    computer = []

    for i in range(5):
        card = random.choice(cards)
        cards.remove(card)
        hand.append(card)

        card = random.choice(cards)
        cards.remove(card)
        computer.append(card)

    '''
    computer = [{'ranks': 'King', 'suits': 'Clubs'},
                {'ranks': '9', 'suits': 'Hearts'},
                {'ranks': 'Jack', 'suits': 'Diamonds'},
                {'ranks': '2', 'suits': 'Hearts'},
                {'ranks': '9', 'suits': 'Spades'}]
    '''
    
    for i in range(len(hand)):
        print('({}) {} of {}' .format(i+1, hand[i]['ranks'],hand[i]['suits']))




    card_number = input('What cards would you like to discard?　').split()


    while True:
        l = len(card_number)

        # check the number of discards
        if l <= 5:
            a = 0
            b = 0
            c = 0
        
            for i in range(l):

                # check for numbers
                if card_number[i].isdigit() == True:
                    a += 1
                
                    # check if it is less than 5
                    if int(card_number[i]) <= 5:
                        c += 1
                    
            
                # check same number
                for j in range(l):
                    if card_number[i] == card_number[j]:
                        b += 1



            # no error      
            if a == l:
                if b == l:
                    if c == l:

                        for i in range(l):
                        
                            card_number.sort()
                            s = int(card_number[i]) - (1 + i)
                        
                            # print('({}) : {}'.format(card_number[i], ' of '.join(hand[s])))
                            hand.remove(hand[s])   

                        # after discarded hand
                        hand_show = []
                        for i in range(len(hand)):
                            hand_show.append('{}'.format(' of '.join(hand[i])))

                        break
        
            # error those are not numbers
            if a != l:
                print('Error! thase are not numbers.')
                print('Can you put again?')
                card_number = input('What card would you like to discard? ').split()

            # error there is same number
            if b != l:
                print('Error! there is same number.')
                print('Can you put again?')
                card_number = input('What card would you like to discard? ').split()

            # error there is a number that is more than 5
            if c != l:
                print('Error! there is same number.')
                print('Can you put again?')
                card_number = input('What card would you like to discard? ').split()

        # number of hands
        if l > 5:
            print('Error! The number of discards has exceeded the hand.')
            print('Can you put again?')
            card_number = input('What card would you like to discard? ').split()



    draw = 5 - (len(hand))
    for i in range(draw):
        card = random.choice(cards)
        cards.remove(card)
        hand.append(card)


    '''
    hand = [{'ranks': '7', 'suits': 'Spades'},
            {'ranks': '7', 'suits': 'Hearts'},
            {'ranks': '8', 'suits': 'Spades'},
            {'ranks': 'Queen', 'suits': 'Spades'},
            {'ranks': '10', 'suits': 'Spades'}]
    '''

    print('')
    print('You:')        


    for i in range(len(hand)):
        print('({}) {} of {}' .format(i+1, hand[i]['ranks'],hand[i]['suits']))



    suit_count = {'Spades': 0, 'Hearts': 0,
                  'Clubs': 0, 'Diamonds':0,}

    rank_count = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0,
                  '8': 0, '9': 0, '10': 0, 'Jack': 0, 'Queen': 0,
                  'King': 0, 'Ace': 0}

    rank_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12,
                  'King': 13, 'Ace': 14}

    # Count cards
    for i in range(len(hand)):
        if hand[i]['ranks'] == '2':
            rank_count['2'] += 1
        elif hand[i]['ranks'] == '3':
            rank_count['3'] += 1
        elif hand[i]['ranks'] == '4':
            rank_count['4'] += 1
        elif hand[i]['ranks'] == '5':
            rank_count['5'] += 1
        elif hand[i]['ranks'] == '6':
            rank_count['6'] += 1
        elif hand[i]['ranks'] == '7':
            rank_count['7'] += 1
        elif hand[i]['ranks'] == '8':
            rank_count['8'] += 1
        elif hand[i]['ranks'] == '9':
            rank_count['9'] += 1
        elif hand[i]['ranks'] == '10':
            rank_count['10'] += 1
        elif hand[i]['ranks'] == 'Jack':
            rank_count['Jack'] += 1
        elif hand[i]['ranks'] == 'Queen':
            rank_count['Queen'] += 1
        elif hand[i]['ranks'] == 'King':
            rank_count['King'] += 1
        elif hand[i]['ranks'] == 'Ace':
            rank_count['Ace'] += 1

    
        if hand[i]['suits'] == 'Spades':
            suit_count['Spades'] += 1
        elif hand[i]['suits'] == 'Hearts':
            suit_count['Hearts'] += 1
        elif hand[i]['suits'] == 'Clubs':
            suit_count['Clubs'] += 1
        elif hand[i]['suits'] == 'Diamonds':
            suit_count['Diamonds'] += 11


    hand.sort(key = rank_value_of_card)

    final_hand, your_point, your_ranks= check_hand(hand)
    print('')
    print('Your hand is {}'.format(final_hand))


    print('')
    print('Computer:')
    for i in range(len(computer)):
        print('({}) {} of {}' .format(i+1, computer[i]['ranks'], computer[i]['suits']))

    computer.sort(key = rank_value_of_card)
    final_computer_hand, computer_point, computer_ranks= check_hand(computer)
    
    print('')
    print('Computer hand is {}' .format(final_computer_hand))
    
    judge = judgement(your_point, computer_point, your_ranks, computer_ranks)
    print('')
    print(judge)



    play_again = input('Play again?  Y/N  ')
    while True:
        if play_again == 'Y':
            print('OK.')
            print('')
            break
        elif play_again == 'N':
            print('')
            break
        else:
            print('Error')
            play_again = input('Play again?  Y/N  ')

    if play_again == 'N':
            break


