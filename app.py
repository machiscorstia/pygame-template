from src.game import Game
from src.panels import MainMenu

if __name__ == "__main__":
    game = Game()
    game.init()

    game.panels.extend([
        # Add your panels here
        MainMenu(screen=game.screen, parent=game, name='main_menu'),
    ])
    
    # Switch to the main menu IMPORTANT!
    game.switch_panel('main_menu')
    game.run()

