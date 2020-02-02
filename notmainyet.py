from card import Card
from absPlayer import AbsPlayer

gameOver = False
numPlayer = 3
players = [AbsPlayer(id=0), AbsPlayer(id=1), AbsPlayer(id=2)]
story_teller = players[0]
listeners = [players[1], players[2]]
listener_play_card = [0, 0, 0]
listener_guess_card = [0, 0, 0]

while not gameOver:
    correct_image_id = story_teller.teller_choose_card()
    print('teller chose {}'.format(correct_image_id))
    for each_listener in listeners:
        # listener play card
        listener_play_card[each_listener.id] = each_listener.listener_choose_card()

    for each_listener in listeners:
        # listener guess card
        guess_result = listener_guess_card[each_listener.id] = each_listener.listener_guess_card()
        print('listener {} guess the option is {}'.format(str(each_listener.id), str(guess_result)))

        # calculate score
        if guess_result == correct_image_id:
            each_listener.score += 3
        else:
            players[guess_result].score += 1

    for each_listener in listeners:
        if each_listener.score >= 8:
            print('game over {} win'.format(each_listener.id))
            exit()

