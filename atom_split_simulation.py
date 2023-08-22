import pygame
import random
import math
from dot import Dot

class AtomSplitSimulation:
    def __init__(self, num_dots, screen_width, screen_height):
        pygame.init()
        
        # Initialize the screen and clock
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Dot properties
        self.dot_radius = 2
        self.dot_color = (255, 255, 255)
        self.num_dots = num_dots
        self.font = pygame.font.Font(None, 36)
        self.dots = []

        # Create initial dots with random positions and velocities
        for _ in range(self.num_dots):
            dot_x_position, dot_y_position = self.get_random_start_position()
            dot_x_velocity = random.uniform(1, 17)
            dot_y_velocity = random.uniform(1, 17)
            self.dots.append(Dot(dot_x_position, dot_y_position, dot_x_velocity, dot_y_velocity))

    def get_random_start_position(self):
        # Generate a random start position for a dot
        x = random.randint(0, self.screen_width)
        y = random.randint(0, self.screen_height)
        return x, y

    def distance(self, point1, point2):
        # Calculate the Euclidean distance between two points
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def run_simulation(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 255))  # Set background color

            new_dots = []

            for dot in self.dots:
                dot.x += dot.x_velocity
                dot.y += dot.y_velocity

                # Dots will bounce off screen edges
                if dot.x - self.dot_radius < 0 or dot.x + self.dot_radius > self.screen_width:
                    dot.x_velocity *= -1
                if dot.y - self.dot_radius < 0 or dot.y + self.dot_radius > self.screen_height:
                    dot.y_velocity *= -1

                collided = False

                for new_dot in new_dots:
                    # Check for collision between dots
                    if self.distance((dot.x, dot.y), (new_dot.x, new_dot.y)) <= self.dot_radius * 2:
                        collided = True
                        break

                if not collided:
                    new_dots.append(dot)
                else:
                    # If the dot collided with another dot, create two new dots with adjusted velocities
                    new_x_velocity = random.uniform(1, 17)
                    new_y_velocity = random.uniform(1, 17)
                    new_dots.append(Dot(dot.x, dot.y, new_x_velocity, new_y_velocity))
                    new_dots.append(Dot(dot.x, dot.y, -new_x_velocity, -new_y_velocity))

            self.dots = new_dots

            # Draw dots on the screen
            for dot in self.dots:
                pygame.draw.circle(self.screen, self.dot_color, (dot.x, dot.y), self.dot_radius)

            dots_text = self.font.render(f"Dots: {len(self.dots)}", True, (255, 255, 255))
            self.screen.blit(dots_text, (10, 10))  # Display dot count

            if len(self.dots) >= 500:
                pygame.quit() # Game will quit after 500 dots

            pygame.display.flip()
            pygame.time.delay(1)  # Add a short delay

            self.clock.tick(120)  # Cap the frame rate

        pygame.quit()

if __name__ == "__main__":
    simulation = AtomSplitSimulation(num_dots=25, screen_width=1250, screen_height=1250)