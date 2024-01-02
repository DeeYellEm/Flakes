import pyglet
from pyglet import image
from pyglet.gl import *

from files import thing, load, resources
from collections import namedtuple

# Set up a window
myWindow = namedtuple('myWindow', ['X', 'Y'])
myWin = myWindow(800, 600)
game_window = pyglet.window.Window(myWin.X, myWin.Y, visible=True, resizable=False)

main_batch = pyglet.graphics.Batch()

# Set up the two top labels
#score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Testing - Flakes!", x=400, y=575, anchor_x='center', batch=main_batch)

# Set up the game over label offscreen
game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=400, y=-300, anchor_x='center',
                                    batch=main_batch, font_size=48)

counter = pyglet.window.FPSDisplay(window=game_window)

game_objects = []

# We need to pop off as many event stack frames as we pushed on
# every time we reset the level.
event_stack_size = 0

def init():
    global num_things, fgpic, fgpicSprite, bgpic, bgpicSprite

    num_things = 10
    fgpic = pyglet.image.load('../resources/window.png')
    fgpicSprite = pyglet.sprite.Sprite(fgpic, 0, 0)
    bgpic = pyglet.image.load('../resources/wintersky.png')
    bgpicSprite = pyglet.sprite.Sprite(bgpic, 0, 0)
    reset_level()


def reset_level():
    global game_objects, event_stack_size

    # Clear the event stack of any remaining handlers from other levels
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1

    things = load.things(num_things, myWin, main_batch)

    # Store all objects that update each frame in a list
    game_objects = things

    # Add any specified event handlers to the event handler stack
    for obj in game_objects:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)
            event_stack_size += 1


@game_window.event
def on_draw():
    game_window.clear()

    #bgpicSprite.draw()

    main_batch.draw()

    #fgpicSprite.draw()

    counter.draw()

def update(dt):
    global num_things

    # To avoid handling collisions twice, we employ nested loops of ranges.
    # This method also avoids the problem of colliding an object with itself.
    # for i in range(len(game_objects)):
        # for j in range(i + 1, len(game_objects)):
            #
            # obj_1 = game_objects[i]


            # Make sure the objects haven't already been killed
            # if not obj_1.dead and not obj_2.dead:
                # if obj_1.collides_with(obj_2):
                    # obj_1.handle_collision_with(obj_2)



    # Let's not modify the list while traversing it
    to_add = []

    for obj in game_objects:
        obj.update(dt)

        to_add.extend(obj.new_objects)
        obj.new_objects = []

if __name__ == "__main__":
    # Start it up!
    init()

    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pyglet.app.run()
