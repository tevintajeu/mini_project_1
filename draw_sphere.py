import math

import cairo

WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)


def draw_sphere(context, center_x, center_y, radius):
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.2,
                                    center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 1, 1, 1)
    gradient.add_color_stop_rgb(0.7, 0.5, 0.5, 0.5)
    gradient.add_color_stop_rgb(1, 0.1, 0.1, 0.1)
    context.set_source(gradient)
    context.fill()

    context.set_source_rgb(0,0,0)
    context.set_line_width(5)
    #Top Pattern
    context.move_to(170,145)
    context.curve_to(200,190,400,190,430,145)
    context.stroke()

    context.move_to(150,170)
    context.curve_to(190,260,410,260,450,170)
    context.stroke()

    context.move_to(170,145)
    context.line_to(190,210)
    context.line_to(260,177)
    context.line_to(300,236)
    context.line_to(340,177)
    context.line_to(410,210)
    context.line_to(430,145)
    context.stroke()

    context.arc(200,185,10,0,2*math.pi)
    context.fill()
    context.arc(255,200,10,0,2*math.pi)
    context.fill()
    context.arc(300,195,10,0,2*math.pi)
    context.fill()
    context.arc(345,200,10,0,2*math.pi)
    context.fill()
    context.arc(400,185,10,0,2*math.pi)
    context.fill()

    #Bottom Pattern
    context.move_to(120,385)
    context.curve_to(200,450,400,450,480,385)
    context.stroke()

    context.move_to(150,430)
    context.curve_to(190,490,410,490,450,430)
    context.stroke()

    context.move_to(150,430)
    context.line_to(190,420)
    context.line_to(240,470)
    context.line_to(300,436)
    context.line_to(360,470)
    context.line_to(410,420)
    context.line_to(450,430)
    context.stroke()

    context.arc(185,440,10,0,2*math.pi)
    context.fill()
    context.arc(242,450,10,0,2*math.pi)
    context.fill()
    context.arc(300,460,10,0,2*math.pi)
    context.fill()
    context.arc(358,450,10,0,2*math.pi)
    context.fill()
    context.arc(415,440,10,0,2*math.pi)
    context.fill()




context.set_source_rgb(0.2, 0.2, 0.2)
context.paint()
draw_sphere(context, WIDTH // 2, HEIGHT // 2, 200)
surface.write_to_png("3d_sphere.png")

print("3D sphere image created!")
