import pyglet,time,util,avatars,hud,random,enemies,impt

game_objects=[]

def create_hazards(dt):
    #global max_notes,notes_spawned,level,max_spd

    #if notes_spawned<max_notes:

    x,y=random.randint(100,hud.window.width-200),random.randint(100,hud.window.height-150)
    hazards=Hazards(x=x,y=y,batch=hud.main_batch)
    hazards.vel_x,hazards.vel_y=enemies.new_direction(100)
    game_objects.append(hazards)

def delete_hazards():
    for obj in game_objects:
        if isinstance(obj,Hazards):
            obj.dead=True
            

class Hazards(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        super(Hazards,self).__init__(impt.hazard_image,*args,**kwargs)
        self.scale=0.3
        self.left=0
        self.right=0
        self.top=0
        self.bottom=0
        self.dead=False
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
        min_y=self.height//2
        max_y=hud.window.height-150

        if self.x<min_x or self.x>max_x:self.vel_x*=-1
        if self.y<min_y or self.y>max_y:self.vel_y*=-1

    def collides_with(self,other):
        
        pass
        
    def handle_collision_with(self,other):
        pass
