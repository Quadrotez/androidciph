from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        label = Label(text='Привет, мир!')
        return label

MyApp().run()
