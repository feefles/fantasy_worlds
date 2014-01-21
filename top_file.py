#top_file.py

import pyglet,math,random,time
from game import util,avatars,enemies,hazards,hud,impt
from pyglet.window import key

impt.bkgd=pyglet.resource.image('world1_back.png')


@hud.window.event
def on_draw():
    hud.window.clear()
    if not impt.inst.complete:
        hud.inst_batch.draw()
    else:
        impt.bkgd.blit(0,0)
        hud.label_batch.draw()
    hud.main_batch.draw()
    
@hud.window.event
def on_key_press(symbol,modifiers):

    if impt.inst.complete:
        if symbol==key.SPACE:
            impt.avatar.fire_at_target()

        if symbol==key.Z:
            if impt.avatar.image==impt.avatar_image_2:
                impt.avatar.image=impt.avatar_image_1
                impt.weapon_image=impt.weapon_image_1
        if symbol==key.X:
            if impt.avatar.image==impt.avatar_image:
                impt.avatar.image=impt.avatar_image_2
                impt.weapon_image=impt.weapon_image_2

impt.init()
pyglet.clock.schedule_interval(impt.check_instructions,1.0/120.0)

pyglet.app.run()
