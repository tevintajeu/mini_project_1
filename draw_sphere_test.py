import math
import cairo
import pygame

# Constants for the window size and sphere properties
WIDTH, HEIGHT = 600, 600
RADIUS = 200  # Radius of the sphere
SWING_AMPLITUDE = 50  # Maximum distance from center to swing

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Swinging Ornament")

# Set up a clock for controlling the frame rate
clock = pygame.time.Clock()

# Swing parameters
angle = 0  # Starting angle for swinging
angle_speed = 0.05  # Speed of swinging


def draw_sphere(context, center_x, center_y, radius):
    # Draw the sphere with a radial gradient for 3D effect
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x, center_y, radius * 0.2, center_x, center_y, radius)

    # Dark blue at the edges, lighter blue in the center
    gradient.add_color_stop_rgb(0, 0.1, 0.1, 0.5)  # Darker blue at the edges
    gradient.add_color_stop_rgb(0.7, 0.1, 0.5, 0.8)  # Lighter blue
    gradient.add_color_stop_rgb(1, 0.5, 0.8, 1)  # Even lighter blue towards the center

    context.set_source(gradient)
    context.fill()

    context.set_source_rgb(0, 0, 0)
    context.set_line_width(5)

    # Middle Pattern
    context.move_to(center_x - radius + 2, center_y - 30)
    context.curve_to(center_x - 150, center_y + 25, center_x + 150, center_y + 25, center_x + radius, center_y - 30)
    context.stroke()

    context.move_to(center_x - radius + 2, center_y + 20)
    context.curve_to(center_x - 150, center_y + 75, center_x + 150, center_y + 75, center_x + radius - 2, center_y + 20)
    context.stroke()

    # Draw triangles for the middle pattern
    context.move_to(center_x - radius + 3, center_y - 25)
    context.line_to(center_x - radius + 20, center_y + 35)
    context.line_to(center_x - radius + 57, center_y + 2)
    context.line_to(center_x - radius + 90, center_y + 52)
    context.line_to(center_x - radius + 120, center_y + 8)
    context.line_to(center_x - radius + 165, center_y + 60)
    context.line_to(center_x - radius + 200, center_y + 11)
    context.line_to(center_x - radius + 240, center_y + 60)
    context.line_to(center_x - radius + 273, center_y + 11)
    context.line_to(center_x - radius + 310, center_y + 55)
    context.line_to(center_x - radius + 340, center_y)
    context.line_to(center_x - radius + 377, center_y + 36)
    context.set_line_join(cairo.LINE_JOIN_BEVEL)
    context.stroke()

    # Draw small circles in the triangle pattern
    for x, y in [(28, 7), (53, 31), (90, 22), (122, 39), (165, 30), (202, 43), (239, 30), (275, 43), (307, 26),
                 (345, 32), (370, 12)]:
        context.arc(center_x - radius + x, center_y + y, 10, 0, 2 * math.pi)
        context.fill()


def main():
    global angle  # Make angle accessible within the function
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((255, 255, 255))  # White background

        # Calculate the new position for swinging
        center_x = WIDTH // 2
        center_y = HEIGHT // 2
        swing_x = center_x + SWING_AMPLITUDE * math.sin(angle)  # Swing left and right
        swing_y = center_y  # Keep the y-coordinate constant

        # Create a new Cairo surface to draw the sphere
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        context = cairo.Context(surface)

        # Draw the sphere at the new position
        draw_sphere(context, swing_x, swing_y, RADIUS)

        # Copy Cairo surface to Pygame surface
        data = surface.get_data()
        image = pygame.image.fromstring(bytes(data), (WIDTH, HEIGHT), "ARGB")
        screen.blit(image, (0, 0))

        # Update the angle for the next frame
        angle += angle_speed
        if angle > 2 * math.pi:  # Reset angle if it exceeds 360 degrees
            angle -= 2 * math.pi

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        clock.tick(60)

    pygame.quit()
    print("Pygame exited cleanly.")  # Confirm exit
c

if __name__ == "__main__":
    main()
