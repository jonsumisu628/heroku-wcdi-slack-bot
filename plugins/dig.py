from slackbot.bot import respond_to
import re
import socket

def reverse_lookup(ip):
    try:
        return socket.gethostbyaddr(ip)[2]
    except:
        return False

@respond_to('dig (.*)')
def dig(message, domain):
    match = re.search(r'<.*\|(.*)>', domain)
    message.reply(str(reverse_lookup(match.group(1))))

