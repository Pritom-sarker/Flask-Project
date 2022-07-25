from telethon import TelegramClient, events, sync
import requests
 


def isItNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def findSignal(parts):
    b = 'buy'
    s = 'sell'
    for part in parts:
        if b in part:
            if isItNumber(part.split(' ')[-1]):
                return 'buy', float(part.split(' ')[-1])
        elif s in part:
            if isItNumber(part.split(' ')[-1]):
                return 'sell', float(part.split(' ')[-1])

def TP(parts):
    data = []
    for part in parts:
        if 'tp' in part:
            if isItNumber(part.split('=')[1]):
                data.append(float(part.split('=')[1]))
    return data

def SL(parts):
    for part in parts:
        if 'sl' in part:
            if isItNumber(part.split('=')[1]):
                return float(part.split('=')[1])


# Remember to use your own values from my.telegram.org!
api_id = 7245145
api_hash = '962930c707a46df8f9f6f31244c502c5'
client = TelegramClient('anon', api_id, api_hash)


def telegram_bot_sendtext(bot_message):
    
    bot_token = '5411042447:AAEsMTImzpuh3r2lc3MYlOAAROFMVUzvv-Q'
    bot_chatID = '-1001580874787'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()



@client.on(events.NewMessage(chats='GOLD KING VIP'))
async def my_event_handler(event):
    s = str(event.raw_text).lower()
    telegram_bot_sendtext(s)
    parts = s.split('\n')
    signal = (findSignal(parts))
    tp = (TP(parts))
    sl = (SL(parts))
    # print(signal, tp, sl)
    query = '''{} {} {} {} {}'''.format(signal[0], signal[1], tp[0], sl,'0.01')
    f = open('query.txt', 'w')
    f.write(query)
    f.close()


    

client.start()
client.run_until_disconnected()