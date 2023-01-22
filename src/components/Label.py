import pygame as py
from .Component import Component

from ..constants import COLORS, DISPLAY, FONT

class Label(Component):

    __slots__ = ['text', 'font', 'font_size', 'font_color', 'font_obj', 'text_surface', 'text_rect']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = kwargs.get('text', '')
        self.font = kwargs.get('font', FONT.DEFAULT)
        self.font_size = kwargs.get('font_size', FONT.DEFAULT_SIZE)
        self.font_color = kwargs.get('font_color', COLORS.WHITE)
        self.font_obj = py.font.Font(FONT.DEFAULT_PATH, self.font_size)
        self.text_surface = self.font_obj.render(self.text, True, self.font_color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.rect.center
    
    def draw(self):
        text = self.font_obj.render(self.text, True, self.font_color)
        self.screen.blit(text, self.text_rect)
        