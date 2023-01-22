import pygame as py
from ..components import Panel
from ..constants import COLORS

class ExamplePanel(Panel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = COLORS.BACKGROUND
        self.childrens.extend([
            # Put your components here
        ])

    def event_handler(self, event):
        super().event_handler(event)
        
    def update(self):
        super().update()
        