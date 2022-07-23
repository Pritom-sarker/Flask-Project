from telethon import TelegramClient, events, sync


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



@client.on(events.NewMessage(chats='test'))
async def my_event_handler(event):
    s = str(event.raw_text).lower()
    parts = s.split('\n')
    signal = (findSignal(parts))
    tp = (TP(parts))
    sl = (SL(parts))
    # print(signal, tp, sl)
    query = '''{} {} {} {} {}'''.format(signal[0], signal[1], tp[0], sl,'0.01')
    print(query)
    

client.start()
client.run_until_disconnected()