#fantasy_worldsv6.py

import pyglet,math,random,time
from game import util
from pyglet.window import key

def center_image(image):
    image.anchor_x=image.width//2
    image.anchor_y=image.height//2


        
'''def interstitial():
    global interstitial
    pause_game()
    interstitial=Interstitial(batch=inst_batch)
    window.push_handlers(interstitial.key_handler)
    pyglet.clock.schedule_interval(interstitial.update,1/120.0)

def check_inter(dt):
    global level
    if interstitial.complete:
        pyglet.clock.unschedule(interstitial.update)
        pyglet.clock.unschedule(check_inter)
        level+=1
        set_level(level)
        start_game()'''
        

    

def update(dt):

    if boss_exist():
        if is_boss_level(points):
            
            delete_monsters()
            boss_hits_label.y=window.height-75
    

    
            
            
        

    if not avatar.dead:

        
            
        for i in xrange(len(game_objects)):
            for j in xrange(i+1,len(game_objects)):

                obj_1=game_objects[i]
                obj_2=game_objects[j]

                    #make sure objects are not dead

                if not obj_1.dead and not obj_2.dead:
                    if obj_1.__class__ is not obj_2.__class__:
                        if obj_1.collides_with(obj_2) or obj_2.collides_with(obj_1):
                            obj_1.handle_collision_with(obj_2)
                            obj_2.handle_collision_with(obj_1)


        for obj in game_objects:
                obj.update(dt)
                
        to_remove=[obj for obj in game_objects if obj.dead]

        for item in to_remove:
            item.delete()
            game_objects.remove(item)
            
            
    if lives<=0:
        avatar.dead=True
        game_over_label.y=v_ctr

    if is_boss_level(points):
        global boss1,level,boss_defeated_label
        
        if not boss_exist() and boss_hits==0:
            boss1=spawn_boss()
        if boss_hits>=10:
            
            boss_defeated_label.y=v_ctr
            
            pyglet.clock.schedule_once(set_level,5)
        
def update_boss_level(dt):
    if is_boss_level(points):
        global boss1
        if boss_exist():
            boss1.fire_at_avatar()

        
def boss_exist():
    counter=0
    for obj in game_objects:
        counter+=1
        if obj.is_boss:
            return True
        elif counter==len(game_objects):
            return False


        
        
def spawn_monster(dt):
    #global max_notes,notes_spawned,level,max_spd

    #if notes_spawned<max_notes:
    
    if not is_boss_level(points):
        x,y=random.randint(100,window.width-200),random.randint(100,window.height-150)
        monster=Monster(x=x,y=y,batch=main_batch)
        monster.vel_x,monster.vel_y=new_direction(100)
        game_objects.append(monster)
        

#pass in boss so can change boss name
def spawn_boss():
    #global max_notes,notes_spawned,level,max_spd

    #if notes_spawned<max_notes:
    
    if is_boss_level(points):
        #x,y=random.randint(0,window.width),random.randint(100,window.height)
        x,y=random.randint(100,window.width-200),random.randint(100,v_ctr)
        boss=Supervillain(x=x,y=y,batch=main_batch)
        boss.vel_x,boss.vel_y=new_direction(100)
        game_objects.append(boss)
        return boss

def create_hazards(dt):
    #global max_notes,notes_spawned,level,max_spd

    #if notes_spawned<max_notes:

    x,y=random.randint(100,window.width-200),random.randint(100,window.height-150)
    hazards=Hazards(x=x,y=y,batch=main_batch)
    hazards.vel_x,hazards.vel_y=new_direction(100)
    game_objects.append(hazards)

def delete_hazards():
    for obj in game_objects:
        if isinstance(obj,Hazards):
            obj.dead=True
def delete_monsters():
    for obj in game_objects:
        if isinstance(obj,Monster):
            obj.dead=True
    
def new_direction(max_spd):
    vel_x=random.random()*max_spd
    if random.randint(0,1):vel_x*=-1
    vel_y=random.random()*max_spd
    if random.randint(0,1):vel_y*=-1
    return vel_x,vel_y    

def change_direction(dt):
     
    for obj in game_objects:
        if isinstance(obj,Monster):
            obj.vel_x,obj.vel_y=new_direction(100)
        if is_boss_level(points):
            if isinstance(obj,Supervillain):
                obj.vel_x,obj.vel_y=new_direction(100)

            
def is_boss_level(points):
    if points>=10:
        return True
    else:
        return False

window=pyglet.window.Window(1100,700)

main_batch=pyglet.graphics.Batch()
inst_batch=pyglet.graphics.Batch()
label_batch=pyglet.graphics.Batch()


h_ctr=window.width//2
v_ctr=window.height//2

font_color1=(255,191,54,225)
font_color2=(255,0,0,255)

points_label=pyglet.text.Label(text='Points:0',
                              anchor_x='right',
                              anchor_y='top',
                              x=window.width,
                              y=window.height-20,
                              font_name='Narnfont',
                              batch=label_batch,
                              font_size=24,
                              color=font_color1)

game_over_label=pyglet.text.Label(text='Game Over',
                                  anchor_x='center',
                                  anchor_y='center',
                                  x=window.width//2,
                                  y=-300,
                                  batch=label_batch,
                                  font_size=40,
                                  color=font_color2,
                                  font_name='Narnfont')

lives_label=pyglet.text.Label(text='Lives:3',
                              anchor_x='right',
                              anchor_y='top',
                              x=window.width,
                              y=window.height-50,
                              batch=label_batch,
                              font_size=20,
                              font_name='Narnfont',
                              color=font_color1)

boss_hits_label=pyglet.text.Label(text='Boss Hits:0/10',
                                       anchor_x='right',
                                       anchor_y='top',
                                       x=window.width,
                                       y=-200,
                                       batch=label_batch,
                                       font_size=14,
                                       font_name='Narnfont',
                                       color=font_color1)

boss_defeated_label=pyglet.text.Label(text='SUPERVILLAIN DEFEATED',
                                       anchor_x='center',
                                       anchor_y='center',
                                       x=h_ctr,
                                       y=-200,
                                       batch=label_batch,
                                       font_size=60,
                                       font_name='Narnfont',
                                       color=font_color2)
                                  
pyglet.resource.path.append('./images')
pyglet.resource.reindex()

#avatar_image=pyglet.resource.image('Susan3.png')
#center_image(avatar_image)
#weapon_image=pyglet.resource.image('arrow.png')
#center_image(weapon_image)
#iceball_image=pyglet.resource.image('iceball.png')
#center_image(iceball_image)

#explosion_image=pyglet.resource.image('explosion.png')
#center_image(explosion_image)

#henchmen_image=pyglet.resource.image('henchmen3.png')
#center_image(henchmen_image)
#hazard_image=pyglet.resource.image('wardrobe.png')
#center_image(hazard_image)
#supervillain_image=pyglet.resource.image('witch.png')
#center_image(supervillain_image)

inst_1_img=pyglet.resource.image('screen1.png')
inst_2_img=pyglet.resource.image('screen2.png')
inst_3_img=pyglet.resource.image('screen3.png')

#int_img1=pyglet.resource.image('screen1.png')


#world1_bkgd=pyglet.resource.image('world1_back.png')
#world1_bkgd.x=0
#world1_bkgd.y=0

world2_bkgd=pyglet.resource.image('hp_bkgd.png')
world2_bkgd.x=0
world2_bkgd.y=0


    





class Avatar(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        super(Avatar,self).__init__(avatar_image,*args,**kwargs)
        self.x=window.width//2
        self.y=window.height-10
        self.scale=1
        self.spd=250
        self.key_handler=key.KeyStateHandler()
        self.batch=main_batch
        self.dead=False
        self.left=0
        self.right=0
        self.top=0
        self.bottom=0
        self.is_boss=False
        

    def update(self,dt):
        if self.key_handler[key.RIGHT]:
            self.x+=self.spd*dt
        if self.key_handler[key.LEFT]:
            self.x-=self.spd*dt

        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)





        self.check_bounds()
        

    def check_bounds(self):
        #define boundaries...min_x, max_x, etc

        min_x=self.width//2
        max_x=window.width-(self.width*2)
        min_y=self.height//2
        max_y=window.height-(self.height//2)

        if self.x<min_x:self.x=min_x
        if self.x>max_x:self.x=max_x
        if self.y<min_y:self.y=min_y
        if self.y>max_y:self.y=max_y

    #changed fire_at_target

    def fire_at_target(self):
        
        fireball=Fireball(x=self.x,y=self.y)
        game_objects.append(fireball)
       

    def collides_with(self,other):
         pass
    def handle_collision_with(self,other):
        pass


class Missile(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        super(Missile,self).__init__(*args,**kwargs)
        
        self.spd=400
        self.batch=main_batch
        self.destruct_timer=2
        self.dead=False

        self.left=0
        self.right=0
        self.top=0
        self.bottom=0
        self.is_boss=False

    def update(self,dt):

        self.y+=self.spd*dt
        if self.at_target():
         #  self.explode()
           self.destruct_timer-=dt
           if self.destruct_timer<0: self.dead=True
        
        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)

        if self.off_screen():
            self.dead=True

    
    def off_screen(self):
        if self.top<0 or self.bottom>window.height:
            return True
        else:
            return False
        
    def at_target(self):
        t=10
        if (self.target_x-t<self.x<self.target_x+t) and \
           (self.target_y-t<self.y<self.target_y+t):
            return True
        else:
            return False
    

    def collides_with(self,other):
        actual_dist=util.distance((self.x,self.y),(other.x,other.y))
        min_dist=((self.image.height/2)*math.sqrt(2))+((other.image.height/2)*math.sqrt(2))

        #if collision detected, check edges of each for overlap

        if actual_dist<min_dist:
            if self.bottom<=other.top and self.top>=other.bottom and self.left<=other.right and self.right>=other.left:
                return True
            else:
                return False
        else:
            return False


    
    
class Fireball(Missile):

    def __init__(self,*args,**kwargs):
        super(Fireball,self).__init__(weapon_image,*args,**kwargs)
        self.scale=.5
        self.target_x=self.x
        self.target_y=0
        self.spd=-400

    def handle_collision_with(self,other):
        global points,lives,boss_hits
        if isinstance(other,Monster):
            #if level!=3:
             #   other.dead=True
              #  self.dead=True
               # points+=1
                #points_label.text='''Points: %i'''%(points)
            if level==1:
                if (self.image==weapon_image_1 and other.image==enemy_image_1) or (self.image==weapon_image_2 and other.image==enemy_image_2):
                    other.dead=True
                    self.dead=True
                    points+=1
                    points+=1
                    points_label.text='Points:%i'%(points)
        elif isinstance(other,Hazards):
            other.dead=True
            self.dead=True
            lives-=1
            lives_label.text='Lives:%i'%(lives)
            delete_hazards()
        elif isinstance(other,Supervillain):
            self.dead=True
            other.lives-=1
            boss_hits+=1
            boss_hits_label.text=\
            '''Boss Hits:%i/10'''%(boss_hits)


    #def explode(self):
     #   self.vel_x=0.0
      #  self.vel_y=0.0
       # self.image=explosion_image
        #self.scale=0.35
        #explosion_sound.play()
    
class Iceball(Missile):

    def __init__(self,*args,**kwargs):
        super(Iceball,self).__init__(iceball_image,*args,**kwargs)
        self.scale=0.3
        self.target_x=self.x
        self.target_y=window.height
        
        

        
    def handle_collision_with(self,other):
        global lives
        if isinstance(other,Avatar):

            lives-=1
            lives_label.text='Lives:%i'%(lives)
            self.dead=True

class Hazards(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        super(Hazards,self).__init__(hazard_image,*args,**kwargs)
        self.scale=0.3
        self.left=0
        self.right=0
        self.top=0
        self.bottom=0
        self.dead=False
        self.is_boss=False

    def update(self,dt):
        global points
        self.x+=self.vel_x*dt
        self.y+=self.vel_y*dt

        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)
        
        self.check_bounds()

        

    def check_bounds(self):
        #define boundaries...min_x, max_x, etc

        min_x=self.width//2
        max_x=window.width-200
        min_y=self.height//2
        max_y=window.height-150

        if self.x<min_x or self.x>max_x:self.vel_x*=-1
        if self.y<min_y or self.y>max_y:self.vel_y*=-1

    def collides_with(self,other):
        
        pass
        
    def handle_collision_with(self,other):
        pass
            
            


class Monster(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        
        henchmen_image=random.choice((enemy_image_1,enemy_image_2))
        super(Monster,self).__init__(henchmen_image,*args,**kwargs)
        self.scale=0.4
        self.dead=False
        self.left=0
        self.right=0
        self.top=0
        self.bottom=0
        self.is_boss=False

    def update(self,dt):
        self.x+=self.vel_x*dt
        self.y+=self.vel_y*dt

        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)
        
        self.check_bounds()

    def check_bounds(self):
        #define boundaries...min_x, max_x, etc

        min_x=self.width//2
        max_x=window.width-200
        min_y=self.height
        max_y=window.height-150

        if self.x<min_x or self.x>max_x:self.vel_x*=-1
        if self.y<min_y or self.y>max_y:self.vel_y*=-1

    def collides_with(self,other):

        pass
     

    def handle_collision_with(self,other):
        pass

class Supervillain(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        super(Supervillain,self).__init__(supervillain_image,*args,**kwargs)
        self.scale=0.75
        self.spd=500
        self.batch=main_batch
        self.dead=False
        self.left=0
        self.right=0
        self.top=0
        self.bottom=0
        self.lives=10
        self.is_boss=True
        self.key_handler=key.KeyStateHandler()


    

    def update(self,dt):
        global boss_hits,level

        self.x+=self.vel_x*dt
        self.y+=self.vel_y*dt
        
        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)

        if boss_hits>=10:
            level+=1
            self.dead=True
            
            
            
            
            
            

        self.check_bounds()

    

    def check_bounds(self):

        min_x=self.width//2
        max_x=window.width-200
        min_y=self.height//2
        #max_y=window.height-(self.height//2)
        max_y=v_ctr

        if self.x<min_x or self.x>max_x:self.vel_x*=-1
        if self.y<min_y or self.y>max_y:self.vel_y*=-1
        
    def fire_at_avatar(self):
        iceball=Iceball(x=self.x,y=self.y)
        game_objects.append(iceball)

    def collides_with(self,other):

        pass

    def handle_collision_with(self,other):
        pass
            
           



    

level_1_images=('Susan4.png','arrow.png','iceball.png','explosion.png',
                'henchmen3.png','wardrobe.png','witch.png','world1_back.png')

level_2_images=('harry.png','magical_blast.png','iceball.png','explosion.png',
                'henchmen3.png','wardrobe.png','witch.png','hp_bkgd.png')

level_3_images=('wizard.png','magical_blast.png','iceball.png','explosion.png',
                'z_critter.png','Frodo.png','sauron.png','screen3.png')



def set_level(level):
    global avatar_image,weapon_image,iceball_image,explosion_image,henchmen_image,hazard_image,supervillain_image,points,lives,boss_hits,bkgd

    global game_objects,avatar,boss_defeated_label,boss_hits_label,avatar_image_2,weapon_image_2,weapon_image_1
    global avatar_image_1,enemy_image_1,enemy_image_2
    
    if level>1:
        for item in game_objects:
            item.dead=True
        boss_defeated_label.y=-200
        boss_hits_label.y=-200



    points=0
    lives=3
    boss_hits=0

    image_list=level_3_images

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
    
    game_objects=[]
    avatar=Avatar(batch=main_batch)
    game_objects.append(avatar)
    window.push_handlers(avatar.key_handler)


    
    if level==1:
        
        pyglet.clock.schedule_interval(update,1.0/120.0)
        pyglet.clock.schedule_interval(update_boss_level,2)

        pyglet.clock.schedule_interval(change_direction,3)
        pyglet.clock.schedule_interval(create_hazards,5)

        pyglet.clock.schedule_interval(spawn_monster,2)
    #if level==3:

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
        

    

bkgd=pyglet.resource.image('world1_back.png')

game_objects=[]
level=1
#points=0
#lives=3
#boss_hits=0

@window.event
def on_draw():
    window.clear()
    
    bkgd.blit(0,0)
    label_batch.draw()
    main_batch.draw()
    
@window.event
def on_key_press(symbol,modifiers):

    global avatar,weapon_image
    
    if symbol==key.SPACE:
        avatar.fire_at_target()
    if symbol==key.Z:
        if avatar.image==avatar_image_2:
            avatar.image=avatar_image_1
            weapon_image=weapon_image_1
    if symbol==key.X:
        if avatar.image==avatar_image:
            avatar.image=avatar_image_2
            weapon_image=weapon_image_2






set_level(level)

pyglet.app.run()

