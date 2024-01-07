import pygame
import random

# Define vocabulary words and their corresponding meanings
vocabulary = dict(apple='fruit', car='vehicle', dog='animal')

# Initialize Pygame
pygame.init()

# Set up the game window


# Set up game fonts
font = pygame.font.Font(None, 36)

# Game loop
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))  # Fill the window with white color

    # Choose a random vocabulary word from the dictionary
    word = random.choice(list(vocabulary.keys()))
    meaning = vocabulary[word]

    # Render the word and meaning on the screen
    word_text = font.render(word, True, (0, 0, 0))
    meaning_text = font.render(meaning, True, (0, 0, 0))

    # Position the word and meaning in the center of the screen
    word_x = (window_width - word_text.get_width()) // 2
    word_y = (window_height - word_text.get_height()) // 2 - 50
    meaning_x = (window_width - meaning_text.get_width()) // 2
    meaning_y = (window_height - meaning_text.get_height()) // 2 + 50

    window.blit(word_text, (word_x, word_y))
    window.blit(meaning_text, (meaning_x, meaning_y))

    pygame.display.update()

# Quit the game
pygame.quit()
