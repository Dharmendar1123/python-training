from kivy.app import App
from kivy.uix.button import Button


class ButtonApp(App):
    def build(self):
        press_button = Button(text="Press Me", size_hint=(0.2, 0.2), font_size='24sp',
                              pos_hint={'center_x': 0.5, 'center_y': 0.5},
                              on_press=self.buttonPressed,
                              on_release=self.buttonReleased)
        return press_button

    def buttonPressed(self, obj):
        print("Button Pressed")

    def buttonReleased(self, obj):
        print("Button Released")


ButtonApp().run()
