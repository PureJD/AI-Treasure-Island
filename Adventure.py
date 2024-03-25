import pygame
import sys
from functions import *
from variables import *
from GPTAPI import *

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        test_line = f'{current_line} {word}'.strip()
        # Check the width of the line with the new word added
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            # If the line is too wide, start a new line with the current word
            lines.append(current_line)
            current_line = word
    # Add the last line to the lines list
    if current_line:
        lines.append(current_line)
    return lines

pygame.init()
pygame.mixer.init()

# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure")


# Font initialization
font = pygame.font.SysFont("Courier", 18)

response = ''''''  # Initialize response variable

# Game loop
running = True
while running:
    # Clear the screen
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Handle pressing Enter key here
                if question:
                    response, context = open_ai_chat(question, context)  # Replace with actual response logic
                    question = ""  # Clear the question input
            elif event.key == pygame.K_BACKSPACE:
                question = question[:-1]  # Remove the last character
            else:
                question += event.unicode  # Append typed character to the question

    


    # Update and draw the stars
    for i, star in enumerate(stars):
        x, y, size, vx, vy = star
        x += vx  # Update x position based on velocity
        y += vy  # Update y position based on velocity
        # Wrap around if the star goes off-screen
        x %= WIDTH
        y %= HEIGHT
        # Update the star's position
        stars[i] = (x, y, size, vx, vy)
        # Draw the star
        pygame.draw.circle(screen, (255, 0, 0), (x, y), size)

    # Render and wrap text
    lines = response.split('\n')
    y_offset = 0
    for line in lines:
        response_surface = font.render(line, True, (255, 0, 0))  # Use white or another color that suits your game's theme
        response_rect = response_surface.get_rect(topleft=(10, 150 + y_offset))  # Adjust positioning as needed
        screen.blit(response_surface, response_rect)
        y_offset += font.get_linesize()

    # Render question
    question_surface = font.render(question, True, (255, 0, 0))
    question_rect = question_surface.get_rect(topleft=(50, HEIGHT - 200))
    pygame.draw.rect(screen, (0, 0, 0, 128), question_rect)
    screen.blit(question_surface, question_rect)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

