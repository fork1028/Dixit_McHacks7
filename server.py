# first of all import the socket library
import socket
from card import Card
from absPlayer import AbsPlayer
# next create a socket object


class Server(object):
    """
    arg:    @gameOver               boolean             whether game is over
            @numPlayer              int
            @players                Player objects      all players in the game
            @story_teller           int                 id of story teller
            @listeners              array of int        list of id of listeners
            @listener_play_card     list of int         list of card id the listener play (listener i plays ith element)
            @listener_guess_card    list of int         list of card id the listener guess (listener i guess ith element)
            @correct_image_id       int                 id of the story telling image
            @teller_description     string              the description given by story teller
    """


    def __init__(self):
        self.gameOver = False
        self.numPlayer = 3
        self.players = [AbsPlayer(id=0), AbsPlayer(id=1), AbsPlayer(id=2)]
        self.story_teller = 0
        self.listeners = [1, 2]
        self.listener_play_card = [0, 0, 0]
        self.listener_guess_card = [0, 0, 0]
        self.correct_image_id = 0
        self.teller_description = ''

        self.s = socket.socket()
        print("Socket successfully created")
        port = 12345
        self.s.bind(('127.0.0.1', port))
        print("socket binded to {}".format(port))
        # put the socket into listening mode
        self.s.listen(5)
        print("socket is listening")

        # wait for all clients to be ready, client message_type should be 'ready'
        self._hear_client(3)
        # deal cards to all players
        self.deal_cards(6)
        # now we are ready for the first round

    def _receive_package(self):
        # receive one package sent by the client
        return

    def deal_cards(self, num_card):
        return

    def send_instruction(self):
        return

    def _hear_client(self, num_expect):
        # receive num_expected inputs
        num_msg = 0
        while num_msg < num_expect:
            self._receive_package()

    def broadcast_description(self):
        return

    def _have_one_turn(self):
        # a turn starts by server sending message_type 'instruction'
        self.send_instruction()
        # expect one reply from the story teller, message_type should be 'choose card'
        self._hear_client(1)
        print('story teller chose {}'.format(self.correct_image_id))
        # broadcast the description from story teller
        self.broadcast_description()
        # listening will play their card
        self._hear_client(2)
        for each_listener in self.listeners:
            # listener play card
            self.listener_play_card[each_listener] = each_listener.listener_choose_card()

        for each_listener in self.listeners:
            # listener guess card
            guess_result = self.listener_guess_card[each_listener.id] = each_listener.listener_guess_card()
            print('listener {} guess the option is {}'.format(str(each_listener.id), str(guess_result)))

            # calculate score
            if guess_result == correct_image_id:
                each_listener.score += 3
            else:
                self.players[guess_result].score += 1

        for each_listener in self.listeners:
            if each_listener.score >= 8:
                print('game over {} win'.format(each_listener.id))
                exit()
# a forever loop until we interrupt it or
# an error occurs

# one turn for each loop
while True:
    numPackets = 0
    while numPackets < 3:
        recievePackets()




    # Establish connection with client.
    c, addr = s.accept()



    print('Got connection from', addr)

    # send a thank you message to the client.
    c.send(str.encode('Thank you for connecting'))

    # Close the connection with the client

