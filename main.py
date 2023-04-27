import pygame
import random
from pygame.locals import *
import numpy as np
from enum import Enum

class MazeUnit(Enum):
    walkable = 0
    wall = 1
    start = 2
    end = 3

def create_maze(num_start_points, num_end_points, width, height):
    maze = np.zeros((height, width), dtype=MazeUnit)
    maze[::, ::] = MazeUnit.wall
    start_points = [(0, random.randint(0, height - 1)) for _ in range(num_start_points)]
    end_points = [(width - 1, random.randint(0, height - 1)) for _ in range(num_end_points)]
    for x, y in start_points:
        maze[y][x] = MazeUnit.start
    for x, y in end_points:
        maze[y][x] = MazeUnit.end
    return maze, start_points, end_points

def draw_maze(screen, maze, start_points, end_points):
    cell_width = screen.get_width() // len(maze[0])
    cell_height = screen.get_height() // len(maze)

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)

            if cell == MazeUnit.walkable:  # Empty space
                color = (0, 255, 0)  # Green
            elif cell == MazeUnit.wall:  # Wall
                color = (0, 0, 0)  # Black
            elif cell == MazeUnit.start:  # Starting point
                color = (255, 255, 255)  # White
                pygame.draw.circle(screen, color, rect.center, min(cell_width, cell_height) // 2)
            elif cell == MazeUnit.end:  # Ending point
                color = (255, 0, 0)  # Red
                pygame.draw.circle(screen, color, rect.center, min(cell_width, cell_height) // 2)

            if cell != MazeUnit.start and cell != MazeUnit.end:  # If not starting or ending point
                pygame.draw.rect(screen, color, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Maze Game')

    num_start_points = 2
    num_end_points = 2
    width = 30
    height = 30
    maze, start_points, end_points = create_maze(num_start_points, num_end_points, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill((0, 0, 0))
        draw_maze(screen, maze, start_points, end_points)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
