from slackbot.bot import Bot, default_reply
import threading
import funcs

class Controler(threading.Thread):
    def run(self):
        bot = Bot()
        bot.run()

@default_reply()
def default_func(msg):
    funcs.pick(msg)

def main():
    c = Controler()
    c.start()
    while True:
        funcs.command()

if __name__ == "__main__":
    print("Wake up")
    main()

