from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1, 0, 0, 1)


class MainApp(App):
    def build(self):
        name_label = Label(text="Iron Man greets you", font_size="24sp", bold=True,
                           color=(1, 1, 0, 1), italic=True)
        return name_label


MainApp().run()
