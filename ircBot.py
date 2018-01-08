import socket


class IrcBot:

    def __init__(self, channel):
        self.channel = channel
        self.connection = socket.socket()
        self.port = 6667
        self.host = 'irc.chat.twitch.tv'

    def connect(self):
        print("Connecting to IRC server")
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.host, self.port))

    def login(self, NICK, PASS):
        self.connection.send(bytes("PASS %s\r\n" % PASS, "UTF-8"))
        self.connection.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
        print("Logging to %s" % NICK)
        print(self.connection.recv(2048).decode())

    def joinChannel(self):
        print("Joining to %s" % self.channel)
        self.connection.send(bytes("JOIN %s\r\n" % self.channel, "UTF-8"))
        print(self.connection.recv(2048))

    def send(self, msg):
        self.connection.send(bytes("PRIVMSG %s :%s\r\n" % (self.channel, msg), "UTF-8"))
        print("Message sent")

    def disconnect(self):
        self.connection.send(bytes("QUIT\r\n", "UTF-8"))
        self.connection.close()
        print("Disconnected from account")

    def run(self, nick, oauth, msg):
        self.connect()
        self.login(nick, oauth)
        self.joinChannel()
        self.send(msg)
        self.disconnect()


