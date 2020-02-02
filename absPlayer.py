from card import Card


class AbsPlayer(object):
    '''
      fields:   @id:        int             unique identifier of a player
                @score:     int
                @cards:     array of cards  the hand card of a player
                @identity:  'L' or 'S'      means the player is listener or is story-teller
                @session:   Class           receives commands from human
    '''
    def __init__(self, id=0, score=0, cards=[], identity=0, session=0):
        self.id = id
        self.score = score
        self.cards = cards
        self.identity = identity
        self.session = session

    # the listeners plays a card
    def listener_choose_card(self):
        card_no = 1
        print(card_no)
        return card_no

    # the story teller plays a card
    def teller_choose_card(self):
        return 2

    # the player_listener guess which card is from the story-teller
    def listener_guess_card(self):
        return 1



