from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
class ButtonApp(MDApp):
    def build(self):
        screen = Screen()
        flat_btn = MDFlatButton(text='Flat Button',
                                pos_hint={'center_x': 0.5, 'center_y': 0.8})
        rectangle_btn = MDRectangleFlatButton(text='Rectangle',
                                              pos_hint={'center_x': 0.5, 'center_y': 0.7})
        icon_btn = MDIconButton(icon='alpha-c-box-outline',
                                pos_hint={'center_x': 0.5, 'center_y': 0.6})
        icon_flat = MDFloatingActionButton(icon='android-messages',
                                              pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(flat_btn)
        screen.add_widget(rectangle_btn)
        screen.add_widget(icon_btn)
        screen.add_widget(icon_flat)
        return screen


ButtonApp().run()