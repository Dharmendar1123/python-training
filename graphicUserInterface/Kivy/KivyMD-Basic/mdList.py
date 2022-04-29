from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import Screen


class ListApp(MDApp):

    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()

        item1 = OneLineListItem(text='John Wick')
        item2 = TwoLineListItem(text='John Wick', secondary_text='Continental')
        item3 = ThreeLineListItem(text='John Wick', secondary_text='Continental', tertiary_text='Love Dog')

        list_view.add_widget(item1)
        list_view.add_widget(item2)
        list_view.add_widget(item3)

        # for i in range(1,20):
        #     items = ThreeLineListItem(text="Item " + str(i), secondary_text='Secondary Text',
        #                               tertiary_text='Tertiary Text')
        #     list_view.add_widget(items)

        for i in range(1, 20):
            icon = IconLeftWidget(icon='android')
            items = ThreeLineIconListItem(text="Item " + str(i), secondary_text='Secondary Text',
                                          tertiary_text='Tertiary Text')
            items.add_widget(icon)
            list_view.add_widget(items)

        scroll.add_widget(list_view)
        screen.add_widget(scroll)

        return screen


ListApp().run()
