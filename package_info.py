class ClientReply(object):
    def __init__(self, msg_type='', player_id=0, content=''):
        self.message_type = msg_type
        self.player_id = player_id
        self.content = content
