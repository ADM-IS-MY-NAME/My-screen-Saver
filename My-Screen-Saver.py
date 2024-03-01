# Made by Ansony Dylan Martinez ADM

print("1 is Snow")
print("2 is rain")
print("3 is SSAANNDD")
print("4 is trans")
print("5 is pan")
print("6 is Stars!!")
print("hit ENTER to start")
input()

import pygame
import random   
import sys

# Initialize Pygame
pygame.init()

LIGHT_BLUE = (91, 206, 250)
PINK = (245, 169, 184)
WHITE = (255, 255, 255)
PINK2 = (255, 0, 255)
YELLOW = (255,255,0)
CYAN = (0,255,255)

weather = "on"
snow_c = 0
rain_c = 1
sand_c = 2
transgender_c = "BLAHAJ"
PANSEXUAL_c = "PAN"
Star_c = 3

# Use the maximum available width and height for full screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Get the width and height of the full screen
width, height = screen.get_size()
stripe_height = height // 5
pansexual_height = height // 3
pygame.display.set_caption("Screensaver")
clock = pygame.time.Clock()

# Load images with transparency
blaha_image = pygame.image.load("BLAHAJ.png").convert_alpha()
blaha_image = pygame.transform.scale(blaha_image, (30, 30))

pancake_image = pygame.image.load("Pancake.png").convert_alpha()
pancake_image = pygame.transform.scale(pancake_image, (30, 30))


# Functions to generate a random position within the screen
def y_position():
    return random.randint(0, width), random.randint(-10, 10)

def random_position():
    return random.randint(0, width), random.randint(0, height)

def x_position():
    return random.randint(-10, 10), random.randint(0, height)

# Modify the rain class to include movement, size, and animation
class rain:
    def __init__(self):
        self.x, self.y = random_position()
        self.radius = random.randint(3, 4)
        self.speed = random.randint(25, 50)
        self.rotation = random.randint(-90, 90)  # Initial rotation angle
        self.rotation_speed = random.randint(-1, 1)  # Rotation speed

    def update(self):
        self.y += self.speed
        self.x += random.randint(-1, 1)
        self.rotation = (self.rotation + self.rotation_speed) % 360  # Update rotation angle
        # Reset rain position if it goes off the screen
        if self.y > height:
            self.x, self.y = y_position()
            self.radius = random.randint(2, 2)
            self.speed = random.randint(25, 50)
            self.rotation = random.randint(-90, 90)
            self.rotation_speed = random.randint(-1, 1)

    def draw(self, surface):
        # Rotate the rain  image
        rain_image = pygame.Surface((self.radius * 2.5, self.radius * 2.5), pygame.SRCALPHA)
        pygame.draw.circle(rain_image, (0, 0, 255), (self.radius, self.radius), self.radius)
        rain_image = pygame.transform.rotate(rain_image, self.rotation)
        surface.blit(rain_image, (self.x - self.radius, self.y - self.radius))
        
# Modify the sand class to include movement, size, and animation
class sand:
    def __init__(self):
        self.x, self.y = random_position()
        self.radius = random.randint(1, 2)
        self.speed = random.randint(50, 100)
        self.rotation = random.randint(0, 360)  # Initial rotation angle
        self.rotation_speed = random.randint(-3, 3)  # Rotation speed

    def update(self):
        self.y += self.speed
        self.x += self.speed
        self.rotation = (self.rotation + self.rotation_speed) % 360  # Update rotation angle
        # Reset sand position if it goes off the screen
        if self.y > height:
            self.x, self.y = y_position()
            self.radius = random.randint(1, 2)
            self.speed = random.randint(50, 100)
            self.rotation = random.randint(0, 360)
            self.rotation_speed = random.randint(-3, 3)
        
        if self.x > width:
            self.x, self.y = x_position()
            self.radius = random.randint(1, 2)
            self.speed = random.randint(50, 100)
            self.rotation = random.randint(0, 360)
            self.rotation_speed = random.randint(-3, 3)

    def draw(self, surface):
        # Rotate the sand image
        sand_image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(sand_image, (255, 255, 159), (self.radius, self.radius), self.radius)
        sand_image = pygame.transform.rotate(sand_image, self.rotation)
        surface.blit(sand_image, (self.x - self.radius, self.y - self.radius))
        
# Modify the snowflake class to include movement, size, and animation
class Snowflake:
    def __init__(self):
        self.x, self.y = random_position()
        self.radius = random.randint(1, 3)
        self.speed = random.randint(1, 3)
        self.rotation = random.randint(0, 360)  # Initial rotation angle
        self.rotation_speed = random.randint(-3, 3)  # Rotation speed

    def update(self):
        self.y += self.speed
        self.x += 0.1 * random.randint(-10, 10)
        self.rotation = (self.rotation + self.rotation_speed) % 360  # Update rotation angle
        # Reset snowflake position if it goes off the screen
        if self.y > height:
            self.x, self.y = y_position()
            self.radius = random.randint(1, 3)
            self.speed = random.randint(1, 3)
            self.rotation = random.randint(0, 360)
            self.rotation_speed = random.randint(-3, 3)
            
        if self.x > width:
            self.x, self.y = y_position()
            self.radius = random.randint(1, 3)
            self.speed = random.randint(1, 3)
            self.rotation = random.randint(0, 360)
            self.rotation_speed = random.randint(-3, 3)

    def draw(self, surface):
        # Rotate the snowflake image
        snowflake_image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(snowflake_image, (255, 255, 255), (self.radius, self.radius), self.radius)
        snowflake_image = pygame.transform.rotate(snowflake_image, self.rotation)
        surface.blit(snowflake_image, (self.x - self.radius, self.y - self.radius))

# Modify the BLAHAJ class to include movement, size, and animation
class BLAHAJ:
    def __init__(self):
        self.x, self.y = random_position()
        self.radius = 15  # Adjusted radius to match scaled image size
        self.speed = random.randint(1, 3)
        self.rotation = random.randint(0, 360)  # Initial rotation angle
        self.rotation_speed = random.randint(-3, 3)  # Rotation speed

    def update(self):
        self.y += self.speed
        self.rotation = (self.rotation + self.rotation_speed) % 360  # Update rotation angle
        # Reset BLAHAJ position if it goes off the screen
        if self.y > height:
            self.x, self.y = y_position()
            self.radius = 15  # Adjusted radius to match scaled image size
            self.speed = random.randint(1, 3)
            self.rotation = random.randint(0, 360)
            self.rotation_speed = random.randint(-3, 3)

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(blaha_image, self.rotation)
        surface.blit(rotated_image, (self.x - self.radius, self.y - self.radius))

# Modify the pan class to include movement, size, and animation
class PAN:
    def __init__(self):
        self.x, self.y = random_position()
        self.radius = 15  # Adjusted radius to match scaled image size
        self.speed = random.randint(1, 3)
        self.rotation = random.randint(0, 360)  # Initial rotation angle
        self.rotation_speed = random.randint(-3, 3)  # Rotation speed

    def update(self):
        self.y += self.speed
        self.rotation = (self.rotation + self.rotation_speed) % 360  # Update rotation angle
        # Reset pan position if it goes off the screen
        if self.y > height:
            self.x, self.y = y_position()
            self.radius = 15  # Adjusted radius to match scaled image size
            self.speed = random.randint(1, 3)
            self.rotation = random.randint(0, 360)
            self.rotation_speed = random.randint(-3, 3)

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(pancake_image, self.rotation)
        surface.blit(rotated_image, (self.x - self.radius, self.y - self.radius))

# Modify the Stars class to include size, and animation
class Stars:
    def __init__(self):
        self.x, self.y = random_position()
        self.radius = random.randint(1, 3)
        self.rotation = random.randint(0, 360)  # Initial rotation angle
        self.rotation_speed = random.randint(-10, 10)  # Rotation speed
        self.speed = random.randint(1, 2)

    def update(self):
        self.rotation = (self.rotation + self.rotation_speed) % 360 # Update rotation angle
        self.rotation_speed = random.randint(-10, 10)  # Rotation speed
        self.x += self.speed
        
        # Reset Stars position if it goes off the screen
        if self.x > width:
            self.radius = random.randint(1, 3)
            self.rotation = random.randint(0, 360)
            self.rotation_speed = random.randint(-3, 3)
            self.x, self.y = x_position()
            
            

    def draw(self, surface):
        # Rotate the snowflake image
        snowflake_image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(snowflake_image, (255, 255, 255), (self.radius, self.radius), self.radius)
        snowflake_image = pygame.transform.rotate(snowflake_image, self.rotation)
        surface.blit(snowflake_image, (self.x - self.radius, self.y - self.radius))

# Create a list to hold objects
snowflakes = [Snowflake() for _ in range(200)]
rainfall = [rain() for _ in range(100)]
sandfall = [sand() for _ in range(100)]
transgender = [BLAHAJ() for _ in range(100)]
pansexual = [PAN() for _ in range(50)]
starlight = [Stars() for _ in range(500)]

# Function to draw the background
def draw_transgender():
    # Fill the screen with white color
    screen.fill(WHITE)
    # Draw stripes in correct order
    pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, width, stripe_height))
    pygame.draw.rect(screen, PINK, (0, stripe_height, width, stripe_height))
    pygame.draw.rect(screen, WHITE, (0, stripe_height * 2, width, stripe_height))
    pygame.draw.rect(screen, PINK, (0, stripe_height * 3, width, stripe_height))
    pygame.draw.rect(screen, LIGHT_BLUE, (0, stripe_height * 4, width, stripe_height))
    
def draw_pansexual():
    # Calculate stripe height

    # Fill the screen with white color
    screen.fill(WHITE)
    # Draw stripes in correct order
    pygame.draw.rect(screen, PINK2, (0, 0, width, pansexual_height))
    pygame.draw.rect(screen, YELLOW, (0, pansexual_height, width, pansexual_height))
    pygame.draw.rect(screen, CYAN, (0, pansexual_height * 2, width, pansexual_height))
    
    
# Initialize the running variable
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                weather = snow_c
            elif event.key == pygame.K_2:
                weather = rain_c
            elif event.key == pygame.K_3:
                weather = sand_c
            elif event.key == pygame.K_4:
                weather = transgender_c
            elif event.key == pygame.K_5:
                weather = PANSEXUAL_c
            elif event.key == pygame.K_6:
                weather = Star_c

    if weather == "BLAHAJ":
        # Draw the background
        draw_transgender()
        
        # Update and draw BLAHAJ instances
        for BLAHAJ_instance in transgender:
            BLAHAJ_instance.update()
            BLAHAJ_instance.draw(screen)  # Pass the screen surface
            
    elif weather == "PAN":
        # Draw the background
        draw_pansexual()
        
        # Update and draw BLAHAJ instances
        for PAN_instance in pansexual:
            PAN_instance.update()
            PAN_instance.draw(screen)  # Pass the screen surface

    else:
        # Fill the background with the gradient color
        color = (0, 0, 0)
        screen.fill(color)

        # Draw weather effects based on the current weather condition
        if weather == "on":
            color = (0, 0, 0)
            screen.fill(color)

        elif weather == 0:
            color = (25, 25, 40)
            screen.fill(color)
            # Update and draw snowflakes
            for snowflake in snowflakes:
                snowflake.update()
                snowflake.draw(screen)
                
        elif weather == 1:
            color = (0, 0, 0)
            screen.fill(color)
            # Update and draw rain
            for raindrop in rainfall:
                raindrop.update()
                raindrop.draw(screen)

        elif weather == 2:
            color = (40, 35, 25)
            screen.fill(color)
            # Update and draw sand
            for sand in sandfall:
                sand.update()
                sand.draw(screen)

        elif weather == 3:
            color = (0, 0, 0)
            screen.fill(color)
            # Update and draw Star
            for Star in starlight:
                Star.update()
                Star.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
