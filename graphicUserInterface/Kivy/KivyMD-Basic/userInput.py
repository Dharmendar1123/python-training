from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog

username_helper = """
MDTextField:
    hint_text: "Enter UserName"
    helper_text: "Enter Username or Email"
    helper_text_mode: "on_focus"
    icon_right: "login-variant"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5,'center_y': 0.5}
    size_hint_x: None
    width: 300 
"""


class InputApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        self.username = Builder.load_string(username_helper)
        button = MDRectangleFlatButton(text='Submit',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_text = "Please Enter UserName"
        else:
            check_text = self.username.text + " doesn't Exist"

        close_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_btn = MDFlatButton(text='More')
        self.dialog_box = MDDialog(title="User Check", text=check_text,
                                   size_hint=(0.5, 0.7),
                                   buttons=[close_btn, more_btn])
        self.dialog_box.open()

    def close_dialog(self, obj):
        self.dialog_box.dismiss()


InputApp().run()
