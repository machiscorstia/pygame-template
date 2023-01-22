import pygame as py

from ..constants import COLORS, GLOBAL

class Component:

    __slots__ = ['parent', 'screen', 'size', 'pos', 'color', 'rect', 'visible', 'name', 'hover', 'layer']

    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', None)
        self.screen = kwargs.get('screen', None)
        self.size = kwargs.get('size', GLOBAL.DEFAULT_SIZE)
        self.pos = kwargs.get('pos', GLOBAL.DEFAULT_POSITION)
        self.color = kwargs.get('color', COLORS.BLACK)
        self.rect = py.Rect(self.pos, self.size)
        self.name = kwargs.get('name', 'Component')
        self.visible = kwargs.get('visible', False)
        self.hover = False
        self.layer = kwargs.get('layer', 0)
    
    def draw(self):
        if not self.visible:
            return

    def update(self):
        if not self.visible:
            return

    def event_handler(self, event: py.event.Event):
        if not self.visible:
            return
    
    def is_collidepoint(self, pos: tuple):
        return self.rect.collidepoint(pos)