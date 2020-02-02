# first of all import the socket library
import socket
import pdb
from package_info import ClientReply
import time
# next create a socket object


class Server(object):
    """
    arg:    @client_lst              list of Clients     connected clients
            @gameOver               boolean             whether game is over
            @numPlayer              int
            @scores                 int                 the score of the players
            @story_teller           int                 id of story teller
            @listeners              array of int        list of id of listeners
            @listener_play_card     list of int         list of card id the listener play (listener i plays ith element)
            @listener_guess_card    list of int         list of card id the listener guess (listener i guess ith element)
            @correct_image_id       int                 id of the story telling image
            @teller_description     string              the description given by story teller
            @s                      class socket        the server's life
    """


    msg_all_type = ['ready_send_client', 'ready_confirm_server', 'tellstory_send_server', 'tellstory_confirm_clent',
                    'tellstory_send_client', 'tellstory_confirm_server']

    def __init__(self):
        self.client_lst = []
        self.gameOver = False
        self.numPlayer = 3
        self.scores = [0, 0, 0]
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

        # connect to all clients
        for i in range(0, 3):
            c, addr = self.s.accept()
            self.client_lst.append(c)
            print('Got connection from', addr)
          #  c.send(str.encode('welcome'))
            output = str(c.recv(1024))
            print('{}'.format(output))

        # deal cards to all players
        self.deal_cards(6)
        # now we are ready for the first round

    def process_output(self, output):
        # output is string
        output = output.split()
        print(len(output), 'length of output')
        if  'tellstory_response' in output[0]:
            self.correct_image_id = int(output[1])
            self.teller_description = output[2]
        if 'choosecard_response' in output[0]:
            self.listener_play_card[int(output[1])] = int(output[2][0:-1])

    def deal_cards(self, num_card):
        return

    def send_instruction(self, message_type, message_content,notify_who):
        # notify who is an integer
        for person in notify_who:
            self.client_lst[person].send(str.encode('{} {}'.format(message_type, message_content)))
        return

    def one_roundtrip(self, request_type, request_content, receiver_lst):
        #   @server             the server
        #   @request_type       enum
        #   @request_content    string
        #   @receiver_lst       list of numbers
        # client reply with story
        for i in receiver_lst:
            self.client_lst[i].send(str.encode('{} {}'.format(request_type, request_content)))
            output = str(self.client_lst[i].recv(1024))
            # right now just print output, but suppose to check output
            print(output)
            self.process_output(output)


new_server = Server()
new_server.one_roundtrip('tellstory_request', 'empty', [0])
new_server.one_roundtrip('choosecard_request', 'broadcast_description', [0,1,2])

new_server.s.close()


# while True:
#     new_server._have_one_turn()
