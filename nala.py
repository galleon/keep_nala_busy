import pygame
import random
import math
import yaml

pygame.init()

# Load configuration from YAML
with open("config.yaml", 'r') as yaml_file:
    config = yaml.safe_load(yaml_file)

# Set screen dimensions from YAML configuration
screen_width = config['window']['width']
screen_height = config['window']['height']

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

pygame.display.set_caption("Nala Playground")

mouse_image_path = config['resources']['mouse_image']
original_mouse_image = pygame.image.load(mouse_image_path)  # Load the original mouse image from the specified path

# Scale mouse image dynamically based on screen size
scale_factor = min(screen_width, screen_height) // 20
mouse_image = pygame.transform.scale(original_mouse_image, (scale_factor, scale_factor))

white = (255, 255, 255)

mouse_x = random.randint(0, screen_width - mouse_image.get_width())
mouse_y = random.randint(0, screen_height - mouse_image.get_height())

# Use speed and angle to determine movement
speed = config['movement']['speed']  # Load speed from YAML configuration
angle = random.uniform(0, 2 * math.pi)  # Random initial angle in radians

min_speed = 2.0  # Minimum speed to ensure it always moves

# Set up frame rate control
clock = pygame.time.Clock()
frame_rate = config['performance']['frame_rate']  # Load frame rate from YAML configuration

# Optional: Load a collision sound effect (ensure 'collision.wav' is in your directory)
# collision_sound = pygame.mixer.Sound("collision.wav")

running = True
while running:
    screen.fill(white)

    screen.blit(mouse_image, (mouse_x, mouse_y))

    # Move the mouse based on speed and angle
    mouse_x += speed * math.cos(angle)
    mouse_y += speed * math.sin(angle)

    # Bounce off the edges of the screen and change angle accordingly
    if mouse_x < 0:
        angle = math.pi - angle  # Reflect angle horizontally
        mouse_x = 0  # Prevent overlap beyond the left boundary
        # Optional: Play collision sound
        # collision_sound.play()
        # Flip mouse image horizontally if direction changes
        mouse_image = pygame.transform.flip(mouse_image, True, False)
    elif mouse_x + mouse_image.get_width() > screen_width:
        angle = math.pi - angle  # Reflect angle horizontally
        mouse_x = screen_width - mouse_image.get_width()  # Prevent overlap beyond the right boundary
        # Optional: Play collision sound
        # collision_sound.play()
        # Flip mouse image horizontally if direction changes
        mouse_image = pygame.transform.flip(mouse_image, True, False)

    if mouse_y < 0:
        angle = -angle  # Reflect angle vertically
        mouse_y = 0  # Prevent overlap beyond the top boundary
        # Optional: Play collision sound
        # collision_sound.play()
    elif mouse_y + mouse_image.get_height() > screen_height:
        angle = -angle  # Reflect angle vertically
        mouse_y = screen_height - mouse_image.get_height()  # Prevent overlap beyond the bottom boundary
        # Optional: Play collision sound
        # collision_sound.play()

    speed = max(min_speed, speed)

    pygame.display.flip()

    clock.tick(frame_rate)

    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update screen size when the window is resized
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            # Recalculate scale factor and rescale mouse image using the original cached image
            scale_factor = min(screen_width, screen_height) // 20
            mouse_image = pygame.transform.scale(original_mouse_image, (scale_factor, scale_factor))

pygame.quit()

