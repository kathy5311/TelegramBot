import telepot  # Bring telepot module
import requests
import json
import time

token = '6508802269:AAFbzheT2SZfJiCwvPRnBBD2knJswT8cRAM'  # my own bot's token
mc = '6607672124'  # user id (@userinfobot show me my telegram id)
bot = telepot.Bot(token)  # Create bot object

def handle(msg):
    global start_key #Command key: Program start/end
    if msg['text']=="/start":
        start_key=1
        bot.sendMessage(msg['from']['id'],"Start")
    if msg['text']=="/stop":
        start_key=0
        bot.sendMessage(msg['from']['id'],"Stop")            
bot.message_loop(handle)

# Hold start_key
start_key=0
while True:
    if start_key==1:
        break
    
val_change=0
val_change_1=0
while True:
    r=requests.get("https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=X5NGFQ256QTUSWQZVR6X9PG7GZ48UUP41A ")
    text=r.text
    jsondata=json.loads(text)
    
    if int(val_change_1)==int(val_change)==0:
        bot.sendMessage(mc,"LastBlock: "+str(jsondata['result']['LastBlock'])+" SafeGasPrice: "+str(jsondata['result']['SafeGasPrice'])+" FastGasPrice: "+str(jsondata['result']['FastGasPrice'])+" Change: 0")
        val_change_1=jsondata['result']['SafeGasPrice']
        time.sleep(10) #Decide running time
    
    else:
        val_change=val_change_1
        val_change_1=jsondata['result']['SafeGasPrice']
        val_change_2=int(val_change_1)-int(val_change) #Get Change value
        bot.sendMessage(mc,"LastBlock: "+str(jsondata['result']['LastBlock'])+" SafeGasPrice: "+str(jsondata['result']['SafeGasPrice'])+" FastGasPrice: "+str(jsondata['result']['FastGasPrice'])+" Change: "+ str(val_change_2))
        time.sleep(10)

    # Program End
    if start_key==0:
        break

    
    