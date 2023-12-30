import pyglet
import random
from . import thing, resources, util

DLMTest = 0

def things(num_things, myWin, batch=None):
    """Generate thing objects with random positions and velocities, not close to the player"""
    things = []
    for i in range(num_things):
        print('DLM: num_things: '+str(num_things))
#DLM1        thing_x, thing_y, _ = player_position
#DLM1        while util.distance((thing_x, thing_y), player_position) < 100:
#DLM1            thing_x = random.randint(0, 800)
#DLM1            thing_y = random.randint(0, 600)
        new_thing = thing.Thing(x=0, y=0, batch=batch)
        new_thing.rotation = random.randint(0, 360)

        new_thing.vx, new_thing.vy = random.uniform(0.3, 1.0) * 100, random.uniform(0.3, 1.0) * 100
        if (random.random() < 0.5):
            new_thing.vx = -1*new_thing.vx
        if (random.random() < 0.5):
            new_thing.vy = -1*new_thing.vy
        print('DLM: new_thing.vx: '+str(new_thing.vx)+' new_thing.vy: '+str(new_thing.vy))

        #print('DLM: thing.width: '+str(new_thing.width)+' thing.height: '+str(new_thing.height))

        thing_x = random.randint((0+int(new_thing.width/2)), (myWin.X-int(new_thing.width/2)))
        thing_y = random.randint((0+int(new_thing.height/2)), (myWin.Y-int(new_thing.height/2)))

        new_thing.x = thing_x
        new_thing.y = thing_y
        new_thing.n = num_things

        if DLMTest == 1:
            # Set some stuff for test purposes
            if (i == 0):
                new_thing.x = 200
                new_thing.y = 300
                new_thing.vx = 50
                new_thing.vy = 0

            if (i == 1):
                new_thing.x = 400
                new_thing.y = 100
                new_thing.vx = 0
                new_thing.vy = 50

        things.append(new_thing)
    return things
