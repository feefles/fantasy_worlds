import pyglet,time,util,avatars,hazards,random,enemies,impt
from pyglet.window import key

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

inst_1_img=pyglet.resource.image('screen1.png')
inst_2_img=pyglet.resource.image('screen2.png')
inst_3_img=pyglet.resource.image('screen3.png')




class Instructions_display(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        super(Instructions_display,self).__init__(inst_1_img,*args,**kwargs)
        self.key_handler=key.KeyStateHandler()
        self.counter=1
        self.keypress_delay=1
        self.complete=False

    def update(self,dt):

        self.keypress_delay-=dt

        if self.keypress_delay<=0:

            if self.key_handler[key.RIGHT]:
                self.counter+=1
                if self.counter==2:
                    self.image=inst_2_img
                elif self.counter==3:
                    self.image=inst_3_img
                else:
                    self.complete=True
                self.keypress_delay=1

level_1_images=('Susan4.png','arrow.png','iceball.png','explosion.png',
                'henchmen3.png','wardrobe.png','witch.png','world1_back.png')

level_2_images=('harry.png','magical_blast.png','iceball.png','explosion.png',
                'bellatrix.png','ron.png','voldemort.png','hp_bkgd.png')

level_3_images=('wizard.png','magical_blast.png','iceball.png','explosion.png',
                'z_critter.png','Frodo.png','sauron.png','world_3_bkgd.png')


