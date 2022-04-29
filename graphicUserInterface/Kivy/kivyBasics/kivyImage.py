from kivy.app import App
from kivy.uix.image import Image, AsyncImage


class ImageApp(App):
    def build(self):
        # dolphin_image = Image(source='dolphin.png')
        # car_image = Image(source='car.jpg')
        nature = AsyncImage(source='https://image.shutterstock.com/image-photo/mountains-under-mist-morning-amazing-260nw-1725825019.jpg')
        return nature


ImageApp().run()