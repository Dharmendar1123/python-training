from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)


class BoxLayoutApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=100, padding=80)
        car = Image(source='car.jpg')
        btn = Button(text='Login', size_hint=(None, None), width=100, height=50,
                     pos_hint={'center_x': 0.5})
        layout.add_widget(car)
        layout.add_widget(btn)
        return layout


BoxLayoutApp().run()
