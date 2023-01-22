import pygame as py
from ..constants import COLORS, GLOBAL, DISPLAY

class Panel:
    __slots__ = ['parent', 'screen', 'size', 'pos', 'color', 'rect', 'childrens', 'visible', 'name', 'active_child']
    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', None)
        self.screen = kwargs.get('screen', None)
        self.size = kwargs.get('size', DISPLAY.SIZE)
        self.pos = kwargs.get('pos', GLOBAL.DEFAULT_POSITION)
        self.color = kwargs.get('color', COLORS.BLACK)
        self.rect = py.Rect(self.pos, self.size)
        self.visible = kwargs.get('visible', False)
        self.childrens = kwargs.get('childrens', [])
        self.name = kwargs.get('name', 'Panel')
        self.active_child = None
    
    def draw(self):
        if not self.visible:
            return
        py.draw.rect(self.screen, self.color, self.rect)
        for child in self.childrens:
            child.draw()
    
    def update(self):
        if not self.visible:
            return
        mouse_pos = py.mouse.get_pos()
        children = self.get_children_at(mouse_pos)
        if children != self.active_child:
            if self.active_child:
                self.active_child.hover = False
            if children:
                children.hover = True
            self.active_child = children
            print(self.active_child)
        if self.active_child:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
        
    def event_handler(self, event: py.event.Event):
        if not self.visible:
            return
        
    def get_children_at(self, pos: tuple):
        for child in self.childrens:
            if child.is_collidepoint(pos):
                return child
        return None
    
    def get_children_by_name(self, name: str):
        for child in self.childrens:
            if child.name == name:
                return child
        return None