import pymunk.pygame_util
import pygame as pg

pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 1200, 900
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)
ball_mas, ball_radius = 1, 60


def create_ball(space, pos):
    ball_moment = pymunk.moment_for_circle(ball_mas, 0, ball_radius)
    ball_body = pymunk.Body(ball_mas, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8
    ball_shape.friction = 0.5
    space.add(ball_body, ball_shape)


space = pymunk.Space()
space.gravity = 0, 2000

segment_shape = pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20)
segment_shape.elasticity = 0.8
segment_shape.friction = 0.5
space.add(segment_shape)

segment_shape1 = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), 20)
segment_shape1.elasticity = 0.8
segment_shape1.friction = 0.5
space.add(segment_shape1)

segment_shape2 = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), 20)
segment_shape2.elasticity = 0.8
segment_shape2.friction = 0.5
space.add(segment_shape2)

while 1:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                create_ball(space, i.pos)

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)
