from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivy.lang import Builder

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

class ListApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):

        for i in range(1, 21):
            items = OneLineListItem(text="Item " + str(i))
            self.root.ids.container.add_widget(items)


ListApp().run()