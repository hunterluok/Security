

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pyttsx3
from multiprocessing import Process, Queue
import logging

logging.basicConfig(logging.ERROR)


def get_data():
    data = input("shuru: ")
    return data


def speak(data):
    data = float(data)
    # if not isinstance(data, (int, float)):
    # print("wrong")
    # break
    if data <= 0:
        print("data must be greater than 0, but it's {}".format(data))
        engine.say("现金必须大于0")
        engine.runAndWait()
        return
        # break
    # 控制语速
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-150)
    # 控制音量
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 0.25)

    # 声音。
    voices = engine.getProperty('voices')
    # getting details of current voice
    # engine.setProperty('voice', voices[0].id)
    # #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)

    engine.say('现金到账， {} 元'.format(data))
    engine.runAndWait()



if __name__ == "__main__":
    engine = pyttsx3.init()
    while True:
        data = get_data()
        try:
            speak(data)
        except:
            print(data, '--')
            pass
