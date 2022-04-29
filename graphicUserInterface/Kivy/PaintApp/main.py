from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
from random import randint
from kivy.uix.button import Button

Window.clearcolor = (1, 1, 1, 1)


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        randomRed = randint(0, 255)
        randomGreen = randint(0, 255)
        randomBlue = randint(0, 255)
        self.canvas.add(Color(rgb=(randomRed/255.0, randomGreen/255.0, randomBlue/255.0)))
        d = 30
        self.canvas.add(Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d)))
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class PaintApp(App):

    def build(self):
        rootWindow = Widget()
        self.painter = PaintWindow()
        clear_btn = Button(text="Clear")
        clear_btn.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clear_btn)

        return rootWindow

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


PaintApp().run()
