# Atom-Splitter

# Dot Simulation Project

This is a simple dot simulation project using the Pygame library. The program creates a set of dots that move around the screen with bouncing behavior when they hit the screen edges. The dots can also collide with each other, creating new dots with adjusted velocities.

## Installation

1. Make sure you have Python and the Pygame library installed.
2. Clone this repository to your local machine.

## Usage

Run the `main.py` script to start the dot simulation. The dots will move around the screen, bouncing off the edges and potentially colliding with each other.

## Known Issue

Sometimes, the program might crash due to a bug where dots collide and split into multiple new dots in the same position. This can create a chain reaction of dots splitting and generating an increasing number of dots, ultimately leading to a crash of the simulation.

This issue is caused by the way dots are created when collisions occur. If two dots collide at the same position, they both create new dots with adjusted velocities, and the process repeats, leading to a potential explosion of dot creation.

## Future Improvements

- A fix for the collision bug by implementing a more robust collision detection and handling mechanism.
- Adding user controls to adjust simulation parameters.
- Implementing more sophisticated dot behaviors.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a pull request or open an issue.

