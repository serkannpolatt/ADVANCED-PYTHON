from insta_bot import Bot
from datetime import datetime
import time

bot=Bot()

username ="İNSTA_NİCKNAME"
password ="PASSWORD"
arkadas="RECEİVER"

bot.login(username=username,password=password)


def gunaydin():
    message="iyi akşamlar"
    friend=[arkadas]
    
    bot.send_message(message,friend)

while True:
    t=datetime.now()
    if t.hour==15 and t.minute==15:
        gunaydin()
        continue
    time.sleep(50)