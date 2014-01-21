import pyglet,util,avatars,hud,hazards,random,enemies


def center_image(image):
    image.anchor_x=image.width//2
    image.anchor_y=image.height//2

def init():
    global inst
    inst=hud.Instructions_display(batch=hud.inst_batch)
    hud.window.push_handlers(inst.key_handler)
    pyglet.clock.schedule_interval(inst.update,1/120.0)


def check_instructions(dt):
    
    if inst.complete:
        pyglet.clock.unschedule(inst.update)
        pyglet.clock.unschedule(check_instructions)
        set_level(dt)
        

def update(dt):

    if enemies.boss_exist():
        if enemies.is_boss_level(points):
            enemies.delete_monsters()
            hud.boss_hits_label.y=hud.window.height-75
            
    

    if not avatar.dead:

       
        for i in xrange(len(hazards.game_objects)):
            for j in xrange(i+1,len(hazards.game_objects)):

                obj_1=hazards.game_objects[i]
                obj_2=hazards.game_objects[j]

                    #make sure objects are not dead

                if not obj_1.dead and not obj_2.dead:
                    if obj_1.__class__ is not obj_2.__class__:
                        if obj_1.collides_with(obj_2) or obj_2.collides_with(obj_1):
                            obj_1.handle_collision_with(obj_2)
                            obj_2.handle_collision_with(obj_1)


        for obj in hazards.game_objects:
                obj.update(dt)
                
        to_remove=[obj for obj in hazards.game_objects if obj.dead]

        for item in to_remove:
            item.delete()
            hazards.game_objects.remove(item)
            
            
    if avatar.lives<=0 and boss_hits!=10:
        avatar.dead=True
        hud.game_over_label.y=hud.v_ctr
        game_over()

    if enemies.is_boss_level(points):
        global boss1,level
        
        if not enemies.boss_exist() and boss_hits==0:
            boss1=enemies.spawn_boss()
            
    
        


def set_level(dt):
    global level,avatar_image,weapon_image,iceball_image,explosion_image,henchmen_image,hazard_image
    global boss_hits,points,supervillain_image,bkgd,game_objects,avatar,boss_defeated_label,boss_hits_label,lives
    global points_label,lives_label,target_points,avatar_image_1,avatar_image_2,weapon_image_1
    global weapon_image_2,enemy_image_1,enemy_image_2
    
    if level>1:
        
        hud.boss_defeated_label.y=-200
        hud.boss_hits_label.y=-200
        for item in hazards.game_objects:
            item.dead=True
    
        
    points=0
    lives=3
    boss_hits=0
    target_points=level*10

    hud.points_label.text='Points:%i'%(points)
    hud.lives_label.text='Lives:%i'%(lives)
    
    if level==1:
        image_list=hud.level_1_images
    elif level==2:
        image_list=hud.level_2_images
    elif level==3:
        image_list=hud.level_3_images
        avatar_image_1=pyglet.resource.image('wizard.png')
        center_image(avatar_image_1)
        weapon_image_1=pyglet.resource.image('magical_blast.png')
        center_image(weapon_image_1)
        
        avatar_image_2=pyglet.resource.image('elf.png')
        center_image(avatar_image_2)
        weapon_image_2=pyglet.resource.image('arrow.png')
        center_image(weapon_image_2)

        enemy_image_1=pyglet.resource.image('z_critter.png')
        enemy_image_2=pyglet.resource.image('w_critter.png')
        

    avatar_image=pyglet.resource.image(image_list[0])
    center_image(avatar_image)
    weapon_image=pyglet.resource.image(image_list[1])
    center_image(weapon_image)
    iceball_image=pyglet.resource.image(image_list[2])
    center_image(iceball_image)
    explosion_image=pyglet.resource.image(image_list[3])
    center_image(explosion_image)
    henchmen_image=pyglet.resource.image(image_list[4])
    center_image(henchmen_image)
    hazard_image=pyglet.resource.image(image_list[5])
    center_image(hazard_image)
    supervillain_image=pyglet.resource.image(image_list[6])
    center_image(supervillain_image)
    
    bkgd=pyglet.resource.image(image_list[7])
    bkgd.x=0
    bkgd.y=0
    
    avatar=avatars.Avatar(batch=hud.main_batch)
    hazards.game_objects.append(avatar)
    hud.window.push_handlers(avatar.key_handler)

    
    if level==1:
        
        pyglet.clock.schedule_interval(update,1.0/120.0)
        pyglet.clock.schedule_interval(enemies.update_boss_level,2)

        pyglet.clock.schedule_interval(enemies.change_direction,3)
        pyglet.clock.schedule_interval(hazards.create_hazards,5)

        pyglet.clock.schedule_interval(enemies.spawn_monster,2)

def victory(dt):
    global bkgd
    pyglet.clock.unschedule(enemies.spawn_monster)
    pyglet.clock.unschedule(hazards.create_hazards)
    

    bkgd=pyglet.resource.image('end_screen.png')
    bkgd.x=0
    bkgd.y=0

def game_over():
    pyglet.clock.unschedule(enemies.spawn_monster)
    pyglet.clock.unschedule(hazards.create_hazards)
    
hazards.game_objects=[]
level=1

