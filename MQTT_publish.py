import paho.mqtt.client as mqtt
import random
import json
import datetime
import time


ISOTIMEFORMAT = '%m/%d %H:%M:%S'

# 連線設定

# 初始化地端程式
client = mqtt.Client()

# 設定登入帳號密碼
#client.username_pw_set("try","xxxx")

# 設定連線資訊(IP, Port, 連線時間)
client.connect("192.168.0.107", 5288, 60)
while True:
    t0 = random.randint(0, 30)
    t = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    payload = {'Temperature': t0, 'Time': t}
    print(json.dumps(payload))
    #要發布的主題和內容
    client.publish("Try/MQTT", json.dumps(payload))
    time.sleep(5)
