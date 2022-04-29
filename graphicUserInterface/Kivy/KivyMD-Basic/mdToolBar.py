from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)
toolbar_helper = """
Screen:
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Demo"
            left_action_items: [["menu", lambda x : app.navigation_menu()]]
            right_action_items: [["clock", lambda x : app.navigation_menu()]]
            elevation: 8
            
        MDLabel:
            text: "Hello World"
            halign: "center"
            
        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["coffee", lambda x : app.navigation_menu()]]
                mode: 'end'
                type: 'bottom'
                icon: 'mailbox'
                on_action_button: app.navigation_menu()

"""


class ToolBarApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_string(toolbar_helper)
        return screen

    def navigation_menu(self):
        print("Navigation Menu")


ToolBarApp().run()