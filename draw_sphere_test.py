
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
    context.move_to(165,150)
    context.curve_to(230,200,400,200,435,150)
    context.stroke()

    context.move_to(130,200)
    context.curve_to(190,250,410,250,475,200)
    context.stroke()

    context.move_to(165,150)
    context.line_to(172,222)
    context.line_to(222,175)
    context.line_to(243,232)
    context.line_to(292,188)
    context.line_to(327,238)
    context.line_to(360,183)
    context.line_to(400,230)
    context.line_to(414,168)
    context.line_to(457,213)
    context.line_to(445,164)
    context.set_line_join(cairo.LINE_JOIN_BEVEL)
    context.stroke()

    context.arc(148,192,10,0,2*math.pi)
    context.fill()
    context.arc(185,182,10,0,2*math.pi)
    context.fill()
    context.arc(215,210,10,0,2*math.pi)
    context.fill()
    context.arc(252,200,10,0,2*math.pi)
    context.fill()
    context.arc(290,219,10,0,2*math.pi)
    context.fill()
    context.arc(327,205,10,0,2*math.pi)
    context.fill()
    context.arc(365,217,10,0,2*math.pi)
    context.fill()
    context.arc(393,194,10,0,2*math.pi)
    context.fill()
    context.arc(424,205,10,0,2*math.pi)
    context.fill()
    # context.arc(440,171,10,0,2*math.pi)
    context.fill()
    
    
       # middle pattern
    context.move_to(center_x - radius + 2,center_y - 30)
    context.curve_to(center_x - 150,center_y + 25,center_x + 150,center_y + 25,center_x + radius  ,center_y - 30)
    context.stroke()

    context.move_to(center_x - radius + 2 ,center_y + 20)
    context.curve_to(center_x - 150,center_y+75,center_x + 150,center_y + 75,center_x + radius - 2,center_y + 20)
    context.stroke()
    
    
    #  the triangles
    context.move_to(center_x-radius + 3,center_y-25)#
    context.line_to(center_x-radius + 20,center_y + 35) #
    context.line_to(center_x-radius + 57 ,center_y + 2) #
    context.line_to(center_x-radius + 90,center_y + 52) #
    context.line_to(center_x-radius + 120,center_y + 8) #
    context.line_to(center_x-radius + 165,center_y + 60) #
    context.line_to(center_x-radius + 200,center_y + 11 ) #
    context.line_to(center_x-radius + 240,center_y + 60) #
    context.line_to(center_x-radius + 273,center_y + 11) #
    context.line_to(center_x-radius + 310,center_y + 55)
    context.line_to(center_x-radius + 340,center_y ) #
    context.line_to(center_x-radius + 377 ,center_y + 36)
    context.line_to(center_x - radius + 397  ,center_y - 25)
    context.set_line_join(cairo.LINE_JOIN_BEVEL)
    context.stroke()
    
    # the circles
    context.arc(center_x - radius + 28,center_y + 7,10,0,2*math.pi)#
    context.fill()
    context.arc(center_x - radius + 53,center_y + 31,10,0,2*math.pi)#
    context.fill()
    context.arc(center_x - radius + 90,center_y + 22,10,0,2*math.pi)#
    context.fill()
    context.arc(center_x - radius + 122,center_y + 39,10,0,2*math.pi) #
    context.fill()
    context.arc(center_x - radius + 165,center_y + 30,10,0,2*math.pi) #
    context.fill()
    context.arc(center_x - radius + 202,center_y + 43,10,0,2*math.pi) #
    context.fill()
    context.arc(center_x - radius + 239,center_y + 30,10,0,2*math.pi) #
    context.fill()
    context.arc(center_x - radius + 275,center_y + 43,10,0,2*math.pi) #
    context.fill()
    context.arc(center_x - radius + 307,center_y  + 26 ,10,0,2*math.pi) #
    context.fill()
    context.arc(center_x - radius + 345,center_y + 32,10,0,2*math.pi)#
    context.fill()
    context.arc(center_x - radius + 370,center_y + 12,10,0,2*math.pi)#
    context.fill()

    #Bottom Pattern
    context.move_to(121,392)
    context.curve_to(200,450,400,450,478,392)
    context.stroke()

    context.move_to(160,443)
    context.curve_to(190,490,410,490,441,443)
    context.stroke()

    context.move_to(153,442)
    context.line_to(190,422)
    context.line_to(240,470)
    context.line_to(300,436)
    context.line_to(360,472)
    context.line_to(410,422)
    context.line_to(454,430)
    context.set_line_join(cairo.LINE_JOIN_BEVEL)
    context.stroke()

    context.arc(190,446,10,0,2*math.pi)
    context.fill()
    context.arc(242,450,10,0,2*math.pi)
    context.fill()
    context.arc(300,460,10,0,2*math.pi)
    context.fill()
    context.arc(358,450,10,0,2*math.pi)
    context.fill()
    context.arc(415,440,10,0,2*math.pi)
    context.fill()
    
    print("done")

context.set_source_rgb(0.2, 0.2, 0.2)
context.paint()
draw_sphere(context, WIDTH // 2, HEIGHT // 2, 200)
surface.write_to_png("3d_sphere_test.png")

print("3D sphere image created!")
