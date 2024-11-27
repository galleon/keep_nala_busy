import pygame
import random
import time
import math

# Initialize Pygame
pygame.init()

# Set screen dimensions to be a sixth of the screen width and 90% of the height
screen_info = pygame.display.Info()
screen_width = screen_info.current_w // 6
screen_height = int(screen_info.current_h * 0.9)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set a title for the window
pygame.display.set_caption("Cat Entertainment")

# Load mouse image
mouse_image = pygame.image.load("mouse.png")  # Make sure to have a 'mouse.png' image in your directory
mouse_image = pygame.transform.scale(mouse_image, (50, 50))  # Scale to desired size

# Define colors
white = (255, 255, 255)

# Define mouse properties
mouse_x = random.randint(0, screen_width - mouse_image.get_width())
mouse_y = random.randint(0, screen_height - mouse_image.get_height())
mouse_speed_x = 5 * random.choice([-1, 1])
mouse_speed_y = 5 * random.choice([-1, 1])

# Ensure speed is always positive
min_speed = 2.0  # Minimum speed to ensure it always moves

# Main loop
running = True
while running:
    screen.fill(white)

    # Draw the mouse
    screen.blit(mouse_image, (mouse_x, mouse_y))

    # Move the mouse
    mouse_x += mouse_speed_x
    mouse_y += mouse_speed_y

    # Bounce off the edges of the screen
    if mouse_x <= 0 or mouse_x + mouse_image.get_width() >= screen_width:
        mouse_speed_x = -mouse_speed_x
        # Add a small random angle to change direction
        angle = random.uniform(-math.pi / 12, math.pi / 12)  # Random angle between -15 and 15 degrees
        speed = max(min_speed, abs(mouse_speed_x)) * random.uniform(0.5, 1.5)
        mouse_speed_x = speed * math.cos(angle) * (1 if mouse_speed_x > 0 else -1)
        mouse_speed_y = speed * math.sin(angle) * (1 if mouse_speed_y > 0 else -1)

    if mouse_y <= 0 or mouse_y + mouse_image.get_height() >= screen_height:
        mouse_speed_y = -mouse_speed_y
        # Add a small random angle to change direction
        angle = random.uniform(-math.pi / 12, math.pi / 12)  # Random angle between -15 and 15 degrees
        speed = max(min_speed, abs(mouse_speed_y)) * random.uniform(0.5, 1.5)
        mouse_speed_y = speed * math.cos(angle) * (1 if mouse_speed_y > 0 else -1)
        mouse_speed_x = speed * math.sin(angle) * (1 if mouse_speed_x > 0 else -1)

    # Ensure speed is always greater than the minimum
    if abs(mouse_speed_x) < min_speed:
        mouse_speed_x = min_speed * (1 if mouse_speed_x > 0 else -1)
    if abs(mouse_speed_y) < min_speed:
        mouse_speed_y = min_speed * (1 if mouse_speed_y > 0 else -1)

    # Update the display
    pygame.display.flip()

    # Delay for a while to make the movement visible to your cat
    time.sleep(0.02)

    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

