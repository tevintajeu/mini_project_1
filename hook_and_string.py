import cairo
import math

#create an image surface
WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

#draw the string
string_x = 300  # Centered at the middle of the 600px width
string_top_y = 20  # Top of the string
string_bottom_y = 80.7
ctx.move_to(300, 20)
ctx.line_to(300, 80.7)
ctx.set_source_rgb(0.85, 0.75, 0.4)
ctx.set_line_width(2)
ctx.stroke()


#draw the gold cap with rounded edges
cap_width, cap_height = 40, 20
cap_x = string_x - cap_width / 2
cap_y = string_bottom_y
radius = 20

# Define a linear gradient from the top to the bottom of the cap
gradient = cairo.LinearGradient(cap_x, cap_y, cap_x, cap_y + cap_height)
gradient.add_color_stop_rgb(0, 0.9, 0.8, 0.4)  # Light gold at the top
gradient.add_color_stop_rgb(0.5, 0.8, 0.7, 0.2)  # Slightly darker gold in the middle
gradient.add_color_stop_rgb(1, 0.6, 0.5, 0.1)  # Darker gold at the bottom
ctx.set_source(gradient)

# Draw the rounded rectangle (rounded top, flat bottom)
ctx.move_to(cap_x, cap_y + radius)  # Move to starting point of left side
ctx.arc(cap_x + radius, cap_y + radius, radius, math.pi, 2 * math.pi)  # Top-left corner arc
ctx.line_to(cap_x + cap_width - radius, cap_y)  # Top edge
ctx.arc(cap_x + cap_width - radius, cap_y + radius, radius, 2 * math.pi, 2 * math.pi)  # Top-right corner arc
ctx.line_to(cap_x + cap_width, cap_y + cap_height)  # Right side down
ctx.line_to(cap_x, cap_y + cap_height)  # Bottom edge (flat)
ctx.close_path()  # Connect back to starting point
ctx.fill()

#use  gradient to fill the cap
ctx.set_source(gradient)  # Gold color
ctx.rectangle(cap_x,cap_y,40,20)
ctx.fill()

def draw_sphere(context, center_x, center_y, radius):
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x + radius * 0.5, center_y - radius * 0.5, radius * 0.2,
                                    center_x, center_y, radius)
  
    gradient.add_color_stop_rgb(0, 0.9, 0.5, 0.6)     
    gradient.add_color_stop_rgb(0.7, 0.7, 0.1, 0.1)    
    gradient.add_color_stop_rgb(1, 0.5, 0, 0)         


    context.set_source(gradient)
    context.fill()
    context.set_source_rgb(1,1,1)
    context.set_line_width(5)
    


draw_sphere(ctx, WIDTH // 2, HEIGHT // 2, 200)

#save the image
surface.write_to_png('christmas.png')
