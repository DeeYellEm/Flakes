import pyglet
import random
from . import thing, resources, util

DLMTest = 0

def things(num_things, myWin, batch=None):
    """Generate thing objects with random positions and velocities, not close to the player"""
    things = []
    for i in range(num_things):
        #print('DLM: num_things: '+str(num_things))
#DLM1        thing_x, thing_y, _ = player_position
#DLM1        while util.distance((thing_x, thing_y), player_position) < 100:
#DLM1            thing_x = random.randint(0, 800)
#DLM1            thing_y = random.randint(0, 600)
        new_thing = thing.Thing(x=0, y=0, batch=batch)
        new_thing.rotation = random.randint(0, 360)

        new_thing.vx, new_thing.vy = 0, -1*(random.uniform(0.3, 1.0) * 100)
        if (random.random() < 0.5):
            new_thing.vx = -1*new_thing.vx

        # Scale the new thing
        new_thing.scale = random.uniform(0.4, 1.0)

        #if (random.random() < 0.5):
        #    new_thing.vy = -1*new_thing.vy
        #print('DLM: new_thing.vx: '+str(new_thing.vx)+' new_thing.vy: '+str(new_thing.vy))

        #print('DLM: thing.width: '+str(new_thing.width)+' thing.height: '+str(new_thing.height))

        thing_x = random.randint((0+int(new_thing.width/2)), (myWin.X-int(new_thing.width/2)))
        #print('DLM:new_thing.height'+str(new_thing.height))
        thing_y = 600 + int(new_thing.height) + random.randint(0, 2*(new_thing.height))

        new_thing.x = thing_x
        new_thing.y = thing_y
        new_thing.n = num_things

        things.append(new_thing)
    return things
