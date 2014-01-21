import pyglet,time,util,avatars,hud,hazards,random,impt
from pyglet.window import key

def update_boss_level(dt):
    if is_boss_level(impt.points):
        global boss1
        if boss_exist():
            impt.boss1.fire_at_avatar()

        
def boss_exist():
    counter=0
    for obj in hazards.game_objects:
        counter+=1
        if obj.is_boss:
            return True
        elif counter==len(hazards.game_objects):
            return False
        
        
def spawn_monster(dt):
    #global max_notes,notes_spawned,level,max_spd

    #if notes_spawned<max_notes:
    
    if not is_boss_level(impt.points):
        x,y=random.randint(100,hud.window.width-200),random.randint(100,hud.window.height-150)
        monster=Monster(x=x,y=y,batch=hud.main_batch)
        monster.vel_x,monster.vel_y=new_direction(100)
        hazards.game_objects.append(monster)
        

#pass in boss so can change boss name
def spawn_boss():
    global boss
    #global max_notes,notes_spawned,level,max_spd
    #if notes_spawned<max_notes:
    
    if is_boss_level(impt.points):
        #x,y=random.randint(0,window.width),random.randint(100,window.height)
        x,y=random.randint(100,hud.window.width-200),random.randint(100,hud.v_ctr)
        boss=Supervillain(x=x,y=y,batch=hud.main_batch)
        boss.vel_x,boss.vel_y=new_direction(100)
        hazards.game_objects.append(boss)
        return boss

def delete_monsters():
    for obj in hazards.game_objects:
        if isinstance(obj,Monster):
            obj.dead=True
    
def new_direction(max_spd):
    vel_x=random.random()*max_spd
    if random.randint(0,1):vel_x*=-1
    vel_y=random.random()*max_spd
    if random.randint(0,1):vel_y*=-1
    return vel_x,vel_y    

def change_direction(dt):
     
    for obj in hazards.game_objects:
        if isinstance(obj,Monster):
            obj.vel_x,obj.vel_y=new_direction(100)
        if is_boss_level(impt.points):
            if isinstance(obj,Supervillain):
                obj.vel_x,obj.vel_y=new_direction(100)

            
def is_boss_level(points):
    if points>=impt.target_points:
        return True
    else:
        return False


class Monster(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        if impt.level==3:
            henchmen_image=random.choice((impt.enemy_image_1,impt.enemy_image_2))
            super(Monster,self).__init__(henchmen_image,*args,**kwargs)

        else:  
            super(Monster,self).__init__(impt.henchmen_image,*args,**kwargs)
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
        max_x=hud.window.width-200
        min_y=self.height
        max_y=hud.window.height-150

        if self.x<min_x or self.x>max_x:self.vel_x*=-1
        if self.y<min_y or self.y>max_y:self.vel_y*=-1

    def collides_with(self,other):

        pass
     

    def handle_collision_with(self,other):
        pass

class Supervillain(pyglet.sprite.Sprite):
    def __init__(self,*args,**kwargs):
        super(Supervillain,self).__init__(impt.supervillain_image,*args,**kwargs)
        self.scale=0.75
        self.spd=500
        self.batch=hud.main_batch
        self.dead=False
        self.left=0
        self.right=0
        self.top=0
        self.bottom=0
        self.lives=10
        self.is_boss=True
        self.key_handler=key.KeyStateHandler()


    

    def update(self,dt):
        global level

        self.x+=self.vel_x*dt
        self.y+=self.vel_y*dt
        
        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)

        if impt.boss_hits>=10:
            self.dead=True
            if impt.level==3:
                for item in hazards.game_objects:
                    item.dead=True
                pyglet.clock.schedule_once(impt.victory,1)
            else:
              
                impt.level+=1
                hud.boss_defeated_label.y=hud.v_ctr
                pyglet.clock.schedule_once(impt.set_level,5)
                


            
        self.check_bounds()
    

    def check_bounds(self):

        min_x=self.width//2
        max_x=hud.window.width-200
        min_y=self.height//2
        max_y=hud.window.height-(self.height//2)
        max_y=hud.v_ctr

        if self.x<min_x or self.x>max_x:self.vel_x*=-1
        if self.y<min_y or self.y>max_y:self.vel_y*=-1
        
    def fire_at_avatar(self):
        iceball=avatars.Iceball(x=self.x,y=self.y)
        hazards.game_objects.append(iceball)

    def collides_with(self,other):

        pass

    def handle_collision_with(self,other):
        pass
            
           
