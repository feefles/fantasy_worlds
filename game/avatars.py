import pyglet,time,util,hazards,hud,random,enemies,impt,math
from pyglet.window import key


class Avatar(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        super(Avatar,self).__init__(impt.avatar_image,*args,**kwargs)
        self.x=hud.window.width//2
        self.y=hud.window.height-30
        self.scale=1
        self.spd=250
        self.key_handler=key.KeyStateHandler()
        self.batch=hud.main_batch
        self.dead=False
        self.left=0
        self.right=0
        self.top=0
        self.bottom=0
        self.is_boss=False
        self.lives=3
        
    def dead(self):
        if self.dead==True:
            return True
        else:
            return False
        
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
        max_x=hud.window.width-(self.width*2)
        min_y=self.height//2
        max_y=hud.window.height-(self.height//2)

        if self.x<min_x:self.x=min_x
        if self.x>max_x:self.x=max_x
        if self.y<min_y:self.y=min_y
        if self.y>max_y:self.y=max_y

    #changed fire_at_target

    def fire_at_target(self):
        
        fireball=Fireball(x=self.x,y=self.y)
        hazards.game_objects.append(fireball)

    def collides_with(self,other):
         pass
    def handle_collision_with(self,other):
        pass


class Missile(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        super(Missile,self).__init__(*args,**kwargs)
        
        self.spd=400
        self.batch=hud.main_batch
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
        if self.top<0 or self.bottom>hud.window.height:
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
        super(Fireball,self).__init__(impt.weapon_image,*args,**kwargs)
        self.scale=0.5
        self.target_x=self.x
        self.target_y=0
        self.spd=-400

    def handle_collision_with(self,other):
        if isinstance(other,enemies.Monster):
            if impt.level!=3:
                other.dead=True
                self.dead=True
                impt.points+=1
                hud.points_label.text='''Points: %i'''%(impt.points)

            elif impt.level==3:
                if (self.image==impt.weapon_image_1 and other.image==impt.enemy_image_1) or (self.image==impt.weapon_image_2 and other.image==impt.enemy_image_2):
                    other.dead=True
                    self.dead=True
                    impt.points+=1
                    hud.points_label.text='Points:%i'%(impt.points)


            
        elif isinstance(other,hazards.Hazards):
            other.dead=True
            self.dead=True
            impt.avatar.lives-=1
            hud.lives_label.text='Lives:%i'%(impt.avatar.lives)
            hazards.delete_hazards()
        elif isinstance(other,enemies.Supervillain):
            self.dead=True
            other.lives-=1
            impt.boss_hits+=1
            hud.boss_hits_label.text=\
            '''Boss Hits:%i/10'''%(impt.boss_hits)

class Iceball(Missile):

    def __init__(self,*args,**kwargs):
        super(Iceball,self).__init__(impt.iceball_image,*args,**kwargs)
        self.scale=0.3
        self.target_x=self.x
        self.target_y=hud.window.height
    
    def handle_collision_with(self,other):
        if isinstance(other,Avatar):
            impt.avatar.lives-=1 
            hud.lives_label.text='Lives:%i'%(impt.avatar.lives)
            self.dead=True

    

