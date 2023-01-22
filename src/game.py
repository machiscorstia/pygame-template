import pygame as py

from .constants import COLORS, DISPLAY

class Game:

    def __init__(self):
        self.running = False
        self.screen = None
        self.clock = None
        self.panels = []
        self.panel_id = 0
    
    def init(self):
        py.init()
        self.screen = py.display.set_mode(DISPLAY.SIZE)
        self.clock = py.time.Clock()
        self.screen.fill(COLORS.BLACK)
    
    def handle_events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.stop()
            self.panels[self.panel_id].event_handler(event)
    
    def get_panel(self, name: str):
        for panel in self.panels:
            if panel.name == name:
                return panel
        return None

    def switch_panel(self, name: str):
        panel = self.get_panel(name)
        if panel:
            self.panels[self.panel_id].visible = False
            self.panel_id = self.panels.index(panel)
            self.panels[self.panel_id].visible = True

    def update(self):
        self.panels[self.panel_id].update()
        py.display.update()
    
    def draw(self):
        self.panels[self.panel_id].draw()
    
    def exit(self):
        self.stop()

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(DISPLAY.FPS)
            self.handle_events()
            self.update()
            self.draw()
        py.quit()