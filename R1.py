import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
import requests
import html
import json
import random
import pprint
import html
from kivy.uix.popup import Popup

url = "https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple"


class Main(Screen):
    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    btn3 = ObjectProperty(None)
    btn4 = ObjectProperty(None)
    btn5 = ObjectProperty(None)

    txt = ObjectProperty(None)
    txt2 = ObjectProperty(None)
    points = 0
    rightans = ""

    def btn6(self):
        try:
            r = requests.get(url)
            q = json.loads(r.text)
            pprint.pprint(q)
            qu1 = q['results'][0]['question']
            question = html.unescape(qu1)
            self.rightans = q['results'][0]['correct_answer']
            ans2 = q['results'][0]['incorrect_answers'][0]
            ans3 = q['results'][0]['incorrect_answers'][1]
            ans4 = q['results'][0]['incorrect_answers'][2]

            ans = [self.rightans, ans3, ans4, ans2]
            random.shuffle(ans)
            self.txt.text = question

            self.btn1.text = html.unescape(ans[0])
            self.btn2.text = html.unescape(ans[1])
            self.btn3.text = html.unescape(ans[2])
            self.btn4.text = html.unescape(ans[3])
            self.txt2.text = str(self.points)

        except:
            net()

    def bn(self):
        if self.btn1.text == self.rightans:
            self.txt.text = "BINGO!\nPRESS NEXT OR YOU CAN QUIT"
            self.points += 1
            self.txt2.text = str(self.points)
        else:
            error()
            self.points -= 1
            self.txt2.text = str(self.points)

    def bn1(self):
        if self.btn2.text == self.rightans:

            self.txt.text = "BING0!\nPRESS NEXT OR YOU CAN QUIT"
            self.points += 1
            self.txt2.text = str(self.points)
        else:
            error()
            self.points -= 1
            self.txt2.text = str(self.points)

    def bn2(self):
        if self.btn3.text == self.rightans:
            self.txt.text = "BINGO!\nPRESS NEXT OR YOU CAN QUIT"

            self.points += 1
            self.txt2.text = str(self.points)
        else:
            error()
            self.points -= 1
            self.txt2.text = str(self.points)

    def bn3(self):
        if self.btn4.text == self.rightans:
            self.txt.text = "BINGO!\nPRESS NEXT OR YOU CAN QUIT"
            self.points += 1
            self.txt2.text = str(self.points)
        else:
            error()
            self.points -= 1
            self.txt2.text = str(self.points)


class Second(Screen):
    sbtn1 = ObjectProperty(None)
    sbtn2 = ObjectProperty(None)
    sbtn3 = ObjectProperty(None)
    sbtn4 = ObjectProperty(None)
    sbtn5 = ObjectProperty(None)
    sbtn6 = ObjectProperty(None)
    stxt1 = ObjectProperty(None)
    stxt2 = ObjectProperty(None)


class Manager(ScreenManager):
    pass


kv = Builder.load_file("he.kv")
sm = Manager()
screens = [Main(name="main"), Second(name="second")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


def error():
    pop = Popup(title='TRY AGAIN',
                content=Label(text='WRONG ANSWER'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


def net():
    pop = Popup(title='NETWORK ISSUE',
                content=Label(text='YOUR ARE NOT CONNECTED TO THE INTERNET'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


class HeApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    HeApp().run()
