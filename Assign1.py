#Get GasData
import requests
import json
import time
from apscheduler.schedulers.blocking import BlockingScheduler

sched= BlockingScheduler()
@sched.scheduled_job('cron', second=59, id='test_1')
def job1():
    r=requests.get("https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=X5NGFQ256QTUSWQZVR6X9PG7GZ48UUP41A ")
    
    text=r.text
    jsondata=json.loads(text)

    print("LastBlock:", jsondata['result']['LastBlock'])
    print("SafeGasPrice:",jsondata['result']['SafeGasPrice'])
    print("FastGasPrice:",jsondata['result']['FastGasPrice'])
    print("Execution Time:",time.strftime("%H:%M:%S"))

sched.start()

