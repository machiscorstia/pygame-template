import pygame as py
from .Component import Component
from ..constants import FONT, COLORS

class Image(Component):
    
    __slots__ = ['image', 'image_rect']
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = py.image.load(kwargs['image_path'])
        self.image = py.transform.scale(self.image, self.size)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.rect.center
    
    def draw(self):
        self.screen.blit(self.image, self.image_rect)
    
    def update(self):
        pass
    
    def event_handler(self, event: py.event.Event):
        pass
    