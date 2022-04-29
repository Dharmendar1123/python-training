from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class InputApp(App):
    def build(self):
        layout = GridLayout(cols=1, row_force_default=True, row_default_height=50, spacing=20, padding=50)
        self.first_name = TextInput(text='First Name')
        self.last_name = TextInput(text='Last Name')
        submit_btn = Button(text='Submit', on_press=self.submit)

        layout.add_widget(self.first_name)
        layout.add_widget(self.last_name)
        layout.add_widget(submit_btn)

        return layout

    def submit(self, obj):
        print("First Name :" + self.first_name.text)
        print("Last Name: " + self.last_name.text)


InputApp().run()