import pygame
from atom_split_simulation import AtomSplitSimulation

def main():
    pygame.init() # Initialize the pygame library
    simulation = AtomSplitSimulation(num_dots=25, screen_width=1250, screen_height=1250)
    simulation.run_simulation() # Start the dot simulation
    pygame.quit()

if __name__ == "__main__":
    main()
