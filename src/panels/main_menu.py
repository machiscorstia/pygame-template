import pygame as py
from ..components import Panel, Label, Button, Image
from ..constants import DISPLAY, COLORS, GLOBAL

class MainMenu(Panel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = COLORS.BACKGROUND
        self.childrens.extend([
            Button(
                screen=self.screen,
                parent=self,
                size=(150, 50),
                pos= (DISPLAY.WIDTH / 2 - 75, DISPLAY.HEIGHT / 2 - 25),
                rect=(150, 50),
                text='Start',
                color=COLORS.BLACK,
                font_color=COLORS.WHITE,
                name='start_btn'
            ),
            Button(
                screen=self.screen,
                parent=self,
                size=(150, 50),
                pos=(DISPLAY.WIDTH / 2 - 75, DISPLAY.HEIGHT / 2 + 50),
                rect=(150, 50),
                text='Settings',
                color=COLORS.BLACK,
                font_color=COLORS.WHITE,
                name='settings_btn'
            ),
            Button(
                screen=self.screen,
                parent=self,
                size=(150, 50),
                pos=(DISPLAY.WIDTH / 2 - 75, DISPLAY.HEIGHT / 2 + 125),
                rect=(150, 50),
                text='Exit',
                color=COLORS.RED,
                font_color=COLORS.WHITE,
                name='exit_btn'
            ),
        ])

    def event_handler(self, event):
        super().event_handler(event)
        if event.type == py.MOUSEBUTTONDOWN:
            children = self.active_child
            if not children:
                return
            if children.name == 'start_btn':
                self.parent.switch_panel('multiplayer_menu')
            elif children.name == 'settings_btn':
                self.parent.switch_panel('settings_menu')
            elif children.name == 'exit_btn':
                self.parent.exit()

    def update(self):
        super().update()
        