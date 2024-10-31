import cairo
import math
import random
from PIL import Image

# Set up image dimensions and animation parameters
WIDTH, HEIGHT = 600, 600
NUM_FRAMES = 50  # Number of frames in the GIF
NUM_SNOWFLAKES = 1000  # Number of snowflakes

# Snowflake class to create snow particles
class Snowflake:
    def __init__(self, width, height, depth):
        self.x = random.uniform(0, width)
        self.y = random.uniform(0, height)
        self.speed = random.uniform(1, 3) * depth  # Slower for background
        self.size = random.uniform(1, 3) * depth  # Smaller for background
        self.brightness = random.uniform(0.5, 1) if depth == 1 else random.uniform(0.2, 0.5)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:  # Reset snowflake to top after falling off screen
            self.y = 0
            self.x = random.uniform(0, WIDTH)

# Draw hook, string, and sphere with patterns
def draw_sphere(context, center_x, center_y, radius):
    # Draw the string
    string_x = center_x
    string_top_y = 20
    string_bottom_y = 80.7
    context.move_to(string_x, string_top_y)
    context.line_to(string_x, string_bottom_y)
    context.set_source_rgb(0.85, 0.75, 0.4)
    context.set_line_width(2)
    context.stroke()

    # Draw the cap with gradient
    cap_width, cap_height = 40, 20
    cap_x = string_x - cap_width / 2
    cap_y = string_bottom_y
    radius_cap = 20
    gradient = cairo.LinearGradient(cap_x, cap_y, cap_x, cap_y + cap_height)
    gradient.add_color_stop_rgb(0, 0.9, 0.8, 0.4)
    gradient.add_color_stop_rgb(0.5, 0.8, 0.7, 0.2)
    gradient.add_color_stop_rgb(1, 0.6, 0.5, 0.1)
    context.set_source(gradient)
    context.rectangle(cap_x, cap_y, cap_width, cap_height)
    context.fill()

    # Draw the spherical ornament with radial gradient
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x + radius * 0.5, center_y - radius * 0.5, radius * 0.2,
                                    center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 0.9, 0.5, 0.6)
    gradient.add_color_stop_rgb(0.7, 0.7, 0.1, 0.1)
    gradient.add_color_stop_rgb(1, 0.5, 0, 0)
    context.set_source(gradient)
    context.fill()


# Draw snowflakes and update their positions
def draw_snowflakes(context, snowflakes):
    for snowflake in snowflakes:
        context.arc(snowflake.x, snowflake.y, snowflake.size, 0, 2 * math.pi)
        context.set_source_rgba(1, 1, 1, snowflake.brightness)
        context.fill()
        snowflake.fall()

# Create and save the snowfall GIF
def create_snowfall_gif(width, height, num_snowflakes, num_frames, output_file):
    snowflakes = [Snowflake(width, height, depth=1) for _ in range(num_snowflakes // 2)] + \
                 [Snowflake(width, height, depth=0.5) for _ in range(num_snowflakes // 2)]
    frames = []

    for frame_num in range(num_frames):
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        context = cairo.Context(surface)

        # Background color
        context.set_source_rgb(0.1, 0.1, 0.1)
        context.paint()

        # Draw background snowflakes (dimmer, smaller)
        draw_snowflakes(context, [s for s in snowflakes if s.brightness < 0.5])

        # Draw the sphere with patterns, hook, and string
        draw_sphere(context, width // 2, height // 2, 200)

        # Draw foreground snowflakes (brighter, larger)
        draw_snowflakes(context, [s for s in snowflakes if s.brightness >= 0.5])

        # Convert cairo surface to PIL image for GIF frames
        cairo_image = Image.frombuffer("RGBA", (width, height), surface.get_data(), "raw", "BGRA", 0, 1)
        frames.append(cairo_image.convert("RGB"))

    # Save frames as animated GIF
    frames[0].save(output_file, save_all=True, append_images=frames[1:], duration=100, loop=0)
    print("GIF saved as", output_file)

# Run the GIF creation
create_snowfall_gif(WIDTH, HEIGHT, NUM_SNOWFLAKES, NUM_FRAMES, "snow.gif")
