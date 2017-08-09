#!/usr/bin/python python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class Anzeige(BoxLayout):
    pass

''' 
Beschreibung :

Es gibt 3 Objekte in der Reihenfolge Label --> Knopf_Links --> Knopf_Rechts

Das Touch ereignis wird in umgekehrter Reihenfolge abgearbeitet

1 Knopf_Rechts
2 Knopf_Links
3 Label

return True  besagt, das das Touchereignis abgearbeitet wurde und nichts mehr getan werden muss

'''


class Anzeige_label(BoxLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("1 Inside Label")
            return True
        else:
            print("1 Outsside Label")
            super(Anzeige_label, self).on_touch_down(touch)
            pass

    pass
class Knopf_links(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("2 Inside Knopf links")
            """
             super wird hier eingefügt da on_touch die Ereigniskette unterbricht
             und der Knopf on_release nicht mehr ausgeführt werden kann
             super sorgt dafür das es weitergeht und auch die Funktion on release
             funzt
            """
            super(Knopf_links, self).on_touch_down(touch)
            return True
        else:
            print("2 Outsside KL")
            super(Knopf_links, self).on_touch_down(touch)

            pass
    pass
class Knopf_rechts(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("3 Inside Knopf rechts")
            """
             super wird hier eingefügt da on_touch die Ereigniskette unterbricht
             und der Knopf on_release nicht mehr ausgeführt werden kann
             super sorgt dafür das es weitergeht und auch die Funktion on release
             funzt
            """
            super(Knopf_rechts, self).on_touch_down(touch)
            return True
        else:
            print("3 Outsside KR")
            super(Knopf_rechts, self).on_touch_down(touch)
            pass
    pass


# Alle im der KV Datei verwendeten Klassen müssen vor dem Laden definiert sein
# Die Klassen werden dann beim Laden aufgerufen
Kivy_Beschreibung_laden = Builder.load_file('beispiel_touch.kv')




class programm(App):

    title = 'Beispiel für Touch Felder'

    def build(self):
        Window.clearcolor = (0.38, 0.35, 0.35, 1)
        Window.size = (800, 480)
        # Window.fullscreen = True
        return Kivy_Beschreibung_laden


if __name__ == "__main__":
    programm().run()