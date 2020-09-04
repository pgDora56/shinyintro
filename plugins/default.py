from slackbot.bot import default_reply

cnt = 0

@default_reply()
def default_func(msg):
    global cnt
    cnt += 1
    msg.reply(f"HELLO! This is reply no.{cnt}.")
