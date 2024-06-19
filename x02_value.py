#!python3

def value(hand):
    values = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 10, "K": 10,
              "Q": 10}
    if len(hand) == 2:
        letter1 = list(hand[0])[0]
        letter2 = list(hand[1])[0]
        if letter1 == "A":
            return [values[letter2], values[letter2] + 10]
        else:
            return values[letter1] + values[letter2]
    elif len(hand) == 3:
        cardValue1 = values[list(hand[0])[0]]
        cardValue2 = values[list(hand[1])[0]]
        cardValue3 = values[list(hand[2])[0]]
        return cardValue1 + cardValue2 + cardValue3


'''
input:
list hand: hand is a list of strings that contains the cards in the hand
eg: ['AH','3D','4S']

return:
int the total value of the hand
may return a list if the hand contains an Ace
eg:
'''


def main():
    assert value(['AH', '3D', '4S']) == [8, 18]
    assert value(['KH', 'TD']) == 20
    assert value(['3D', '8H']) == 11
    assert value(['KC', '6S', 'QD']) == 26


if __name__ == "__name__":
    main()
