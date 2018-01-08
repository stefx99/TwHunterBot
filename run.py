from flask import Flask
from flask import render_template
from flask import request
from pprint import pprint
from os import getcwd
from botParser import BotParser
import ircBot
import time
import random
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/', methods=["POST"])
def send():
    if request.method == 'POST':
        data = request.form
        path = getcwd()
        path = path.__add__('\\bots.txt')
        # Parsing login data from bots.txt file
        parser = BotParser(path)
        parsed = parser.getToArray()
        keyword = data['keyword']
        channel = data['channel']

        # Creating bot instance
        bot = ircBot.IrcBot(channel)
        keys = list(parsed.keys())
        random.shuffle(keys)
        for key in keys:
            print('%s sending keyword' % key)
            bot.run(key, parsed[key], keyword)
            print('Waiting for next account')
            time.sleep(4)

        return render_template('home.html')
    else:
        return render_template('home.html')


@app.route('/winner')
def winner():
    return render_template('winnerTemplate.html')


@app.route('/winner', methods=['POST'])
def winnerChannel():
    if request.method == 'POST':
        data = request.form
        path = getcwd()
        path = path.__add__('\\bots.txt')
        parser = BotParser(path)
        parsed = parser.getToArray()
        winner_name = data['winner_name']

        if winner_name in parsed.keys():
            bot = ircBot.IrcBot(data['channel'])
            bot.connect()
            bot.login(winner_name, parsed[winner_name])
            bot.joinChannel()
            msg = 'Heyy'
            while msg:
                print("If you want to exit send blank message or just press enter")
                msg = input('Message: ')
                bot.send(msg)

            bot.disconnect()
        else:
            error = "Nick doesn't exists in bots.txt file!"
        return render_template('winnerTemplate.html', da=error)

    else:
        return render_template('winnerTemplate.html')


if __name__ == '__main__':
    app.run(debug=True)
