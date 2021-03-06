from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable


class DataTableApp(MDApp):

    def build(self):
        screen = Screen()
        table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            size_hint=(0.9, 0.6),
                            check=True,
                            rows_num=10,
                            column_data=[
                                ("No.", dp(18)),
                                ("Food", dp(20)),
                                ("Calories", dp(20))
                            ],
                            row_data=[
                                ("1", "Burger", "300"),
                                ("2", "Pizza", "330"),
                                ("3", "Dosa", "200"),
                                ("4", "Pizza", "330"),
                                ("5", "Pizza", "330"),
                                ("6", "Pizza", "330"),
                                ("7", "Pizza", "330"),
                                ("8", "Pizza", "330"),
                                ("9", "Pizza", "330"),
                                ("10", "Pizza", "330"),
                                ("11", "Pizza", "330"),
                            ])

        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)
        screen.add_widget(table)
        return screen

    def check_press(self, instance_table, current_row):
        print(instance_table)
        print(current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table)
        print(instance_row)


DataTableApp().run()
