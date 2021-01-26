from tkinter import *



class Main:
    def __init__ (self):
        self.tk=Tk()
        self.tk.title('')
        self.tk['background']='black'
        self.tk.resizable(0,0)
        self.tk.minsize(width=100,height=100)
        self.tk.geometry('1910x1030+-5+-25')
        self.make()
    def make(self):
        self.x50AIR=PhotoImage(file='img/x50/blocks/bg/air.gif')
        self.x50VOID=PhotoImage(file='img/x50/blocks/bg/void.gif')
        self.x50RAMP_0=PhotoImage(file='img/x50/blocks/ramp/ramp0@.gif')
        self.x50RAMP_90=PhotoImage(file='img/x50/blocks/ramp/ramp90@.gif')
        self.x50RAMP_180=PhotoImage(file='img/x50/blocks/ramp/ramp180@.gif')
        self.x50RAMP_270=PhotoImage(file='img/x50/blocks/ramp/ramp270@.gif')
        self.x50TRIANGLE_0=PhotoImage(file='img/x50/blocks/triangle/triangle0@.gif')
        self.x50TRIANGLE_90=PhotoImage(file='img/x50/blocks/triangle/triangle90@.gif')
        self.x50TRIANGLE_180=PhotoImage(file='img/x50/blocks/triangle/triangle180@.gif')
        self.x50TRIANGLE_270=PhotoImage(file='img/x50/blocks/triangle/triangle270@.gif')
        self.x50SPIKE_0=PhotoImage(file='img/x50/blocks/spike/spike0@.gif')
        self.x50SPIKE_90=PhotoImage(file='img/x50/blocks/spike/spike90@.gif')
        self.x50SPIKE_180=PhotoImage(file='img/x50/blocks/spike/spike180@.gif')
        self.x50SPIKE_270=PhotoImage(file='img/x50/blocks/spike/spike270@.gif')
        self.x50BLOCK=PhotoImage(file='img/x50/blocks/block.gif')
        self.x50SELECTED_TILE_FF=PhotoImage(file='img/x50/blocks/select/select_ff.gif')
        self.x50SELECTED_TILE_F=PhotoImage(file='img/x50/blocks/select/select_f.gif')
        self.x50SELECTED_TILE_R=PhotoImage(file='img/x50/blocks/select/select_r.gif')
        self.x50SELECTED_TILE_L=PhotoImage(file='img/x50/blocks/select/select_l.gif')
        self.x30AIR=PhotoImage(file='img/x30/blocks/bg/air.gif')
        self.x30VOID=PhotoImage(file='img/x30/blocks/bg/void.gif')
        self.x30RAMP_0=PhotoImage(file='img/x30/blocks/ramp/ramp0@.gif')
        self.x30RAMP_90=PhotoImage(file='img/x30/blocks/ramp/ramp90@.gif')
        self.x30RAMP_180=PhotoImage(file='img/x30/blocks/ramp/ramp180@.gif')
        self.x30RAMP_270=PhotoImage(file='img/x30/blocks/ramp/ramp270@.gif')
        self.x30TRIANGLE_0=PhotoImage(file='img/x30/blocks/triangle/triangle0@.gif')
        self.x30TRIANGLE_90=PhotoImage(file='img/x30/blocks/triangle/triangle90@.gif')
        self.x30TRIANGLE_180=PhotoImage(file='img/x30/blocks/triangle/triangle180@.gif')
        self.x30TRIANGLE_270=PhotoImage(file='img/x30/blocks/triangle/triangle270@.gif')
        self.x30SPIKE_0=PhotoImage(file='img/x30/blocks/spike/spike0@.gif')
        self.x30SPIKE_90=PhotoImage(file='img/x30/blocks/spike/spike90@.gif')
        self.x30SPIKE_180=PhotoImage(file='img/x30/blocks/spike/spike180@.gif')
        self.x30SPIKE_270=PhotoImage(file='img/x30/blocks/spike/spike270@.gif')
        self.x30BLOCK=PhotoImage(file='img/x30/blocks/block.gif')
        self.x30SELECTED_TILE_FF=PhotoImage(file='img/x30/blocks/select/select_ff.gif')
        self.x30SELECTED_TILE_F=PhotoImage(file='img/x30/blocks/select/select_f.gif')
        self.x30SELECTED_TILE_R=PhotoImage(file='img/x30/blocks/select/select_r.gif')
        self.x30SELECTED_TILE_L=PhotoImage(file='img/x30/blocks/select/select_l.gif')
        self.RAMP_ICON=PhotoImage(file='img/icons/ramp.gif')
        self.TRIANGLE_ICON=PhotoImage(file='img/icons/triangle.gif')
        self.BLOCK_ICON=PhotoImage(file='img/icons/block.gif')
        self.DELETE=PhotoImage(file='img/icons/delete.gif')
        self.SPIKE_ICON=PhotoImage(file='img/icons/spike.gif')
        self.SELECTED_RAMP_ICON=PhotoImage(file='img/selected_icons/ramp.gif')
        self.SELECTED_TRIANGLE_ICON=PhotoImage(file='img/selected_icons/triangle.gif')
        self.SELECTED_BLOCK_ICON=PhotoImage(file='img/selected_icons/block.gif')
        self.SELECTED_DELETE=PhotoImage(file='img/selected_icons/delete.gif')
        self.SELECTED_SPIKE_ICON=PhotoImage(file='img/selected_icons/spike.gif')
        self.c_w,self.c_h=50,50
        self.see_w,self.see_h=38,17
        self.able=0
        self.size=50
        self.x_pos=0
        self.y_pos=0
        self.grid=True
        self.toolbar=True
        self.select_index=0
        self.current_tile,self.map_='air',{}
        self.arr_fill=[[],[]]
        self.f_arr_fill=[[],[]]
        self.r_arr_fill=[[],[]]
        self.l_arr_fill=[[],[]]
        self.dict={50:{'air':self.x50AIR,'void':self.x50VOID,\
                   'ramp0':self.x50RAMP_0,'ramp90':self.x50RAMP_90,'ramp180':self.x50RAMP_180,'ramp270':self.x50RAMP_270,\
                   'triangle0':self.x50TRIANGLE_0,'triangle90':self.x50TRIANGLE_90,'triangle180':self.x50TRIANGLE_180,'triangle270':self.x50TRIANGLE_270,\
                   'block':self.x50BLOCK,\
                   'spike0':self.x50SPIKE_0,'spike90':self.x50SPIKE_90,'spike180':self.x50SPIKE_180,'spike270':self.x50SPIKE_270},\
                   30:{'air':self.x30AIR,'void':self.x30VOID,\
                   'ramp0':self.x30RAMP_0,'ramp90':self.x30RAMP_90,'ramp180':self.x30RAMP_180,'ramp270':self.x30RAMP_270,\
                   'triangle0':self.x30TRIANGLE_0,'triangle90':self.x30TRIANGLE_90,'triangle180':self.x30TRIANGLE_180,'triangle270':self.x30TRIANGLE_270,\
                   'block':self.x30BLOCK,\
                   'spike0':self.x30SPIKE_0,'spike90':self.x30SPIKE_90,'spike180':self.x30SPIKE_180,'spike270':self.x30SPIKE_270}}
        self.states={'air':[self.dict[self.size]['air']],'void':[self.dict[self.size]['void']],\
                     'ramp':[self.dict[self.size]['ramp0'],self.dict[self.size]['ramp90'],self.dict[self.size]['ramp180'],self.dict[self.size]['ramp270']],\
                     'triangle':[self.dict[self.size]['triangle0'],self.dict[self.size]['triangle90'],self.dict[self.size]['triangle180'],self.dict[self.size]['triangle270']],\
                     'block':[self.dict[self.size]['block']],\
                     'spike':[self.dict[self.size]['spike0'],self.dict[self.size]['spike90'],self.dict[self.size]['spike180'],self.dict[self.size]['spike270']]}
        self.icons={'ramp':self.RAMP_ICON,'triangle':self.TRIANGLE_ICON,'block':self.BLOCK_ICON,'delete':self.DELETE,'spike':self.SPIKE_ICON}
        self.selected_icons={'ramp':self.SELECTED_RAMP_ICON,'triangle':self.SELECTED_TRIANGLE_ICON,'block':self.SELECTED_BLOCK_ICON,'delete':self.SELECTED_DELETE,'spike':self.SELECTED_SPIKE_ICON}
        self.select_tiles={30:[self.x30SELECTED_TILE_FF,self.x30SELECTED_TILE_F,self.x30SELECTED_TILE_R,self.x30SELECTED_TILE_L],50:[self.x50SELECTED_TILE_FF,self.x50SELECTED_TILE_F,self.x50SELECTED_TILE_R,self.x50SELECTED_TILE_L]}
        self.ics={}
        self.tiles={}
        self.all_blocks=['block','ramp','triangle','spike']
        self.cv_fr=Frame(self.tk,bg='black')
        self.tl_fr=Frame(self.tk,bg='black')
        self.del_btn=Button(self.tl_fr,image=self.selected_icons['delete'],command=self.del_,borderwidth=0,highlightbackgroun='black',highlightthickness=0,highlightcolor='black',activebackground='black')
        self.ics['delete']=self.del_btn
        self.create_toolbar()
        self.canvas=Canvas(self.cv_fr,bg='black',width=10,height=10,borderwidth=0,highlightbackgroun='black',highlightthickness=0,highlightcolor='black')
        self.canvas.bind_all('<f>',func=self.flip)
        self.canvas.bind_all('<r>',func=self.r_right)
        self.canvas.bind_all('<l>',func=self.r_left)
        self.canvas.bind_all('<g>',func=self.switch_grid)
        self.canvas.bind_all('<c>',func=self.clear)
        self.canvas.bind_all('<MouseWheel>',func=self.resize)
        self.canvas.bind_all('<Escape>',func=self.kill)
        self.canvas.bind_all('<Shift-KeyPress-Left>',func=self.inventory_left)
        self.canvas.bind_all('<Shift-KeyPress-Right>',func=self.inventory_right)
        self.canvas.bind_all('<KeyPress-Up>',func=self.m_up)
        self.canvas.bind_all('<KeyPress-Down>',func=self.m_down)
        self.canvas.bind_all('<KeyPress-Left>',func=self.m_left)
        self.canvas.bind_all('<KeyPress-Right>',func=self.m_right)
        self.canvas.bind_all('<Button-3>',func=self.place_tile)
        self.canvas.bind_all('<Button-2>',func=self.fill)
        self.canvas.bind_all('<Shift-F>',func=self.fill_flip)
        self.canvas.bind_all('<Shift-R>',func=self.fill_right)
        self.canvas.bind_all('<Shift-L>',func=self.fill_left)
        self.canvas.bind_all('<F1>',func=self.toggle_toolbar)
        self.cv_fr.grid(row=0,column=0,columnspan=100)
        self.tl_fr.grid(row=1,column=0,pady=30)
        self.del_btn.grid(row=0,column=0)
        self.canvas.pack(padx=0,pady=0)
        if self.size==30:
            self.canvas['height']=840
            self.canvas['width']=1500
        elif self.size==50:
            self.canvas['height']=850
            self.canvas['width']=1900
        for y in range(self.c_h):
            for x in range(self.c_w):
                self.tiles[(x,y)]=self.canvas.create_image((x*self.size)+(self.size//2),(y*self.size)+(self.size//2),image=self.dict[self.size]['air'])
                self.map_[(x,y)]='air'
    def kill(self,arg):
        self.tk.destroy()
        quit()
    def resize(self,arg):
        if arg.delta//120>0 and self.size==30:self.size=50
        elif arg.delta//120<0 and self.size==50:self.size=30
        if self.size==30:
            self.canvas['height']=840
            self.canvas['width']=1500
            self.see_h,self.see_w=28,50
            while self.x_pos>0:
                for itm in self.tiles.values():self.canvas.move(itm,-30,0)
                self.x_pos-=1
        elif self.size==50:
            self.canvas['height']=850
            self.canvas['width']=1900
            self.see_h,self.see_w=17,38
        self.update_display()
    def del_(self):
        if self.grid:self.current_tile='air'
        else:self.current_tile='void'
        self.update_icons()
    def inventory_left(self,arg):
        if self.able==0:
            self.select_index-=1
            if self.select_index<0:self.select_index=len(self.all_blocks)
            if self.select_index==0 and self.grid:self.current_tile='air'
            elif self.select_index==0 and not self.grid:self.current_tile='void'
            else:
                end=''
                if len(self.states[self.all_blocks[self.select_index-1]])>1:end='0'
                self.current_tile=str(self.all_blocks[self.select_index-1])+end
            self.update_icons()
    def inventory_right(self,arg):
        if self.able==0:
            self.select_index+=1
            if self.select_index>len(self.all_blocks):self.select_index=0
            if self.select_index==0 and self.grid:self.current_tile='air'
            elif self.select_index==0 and not self.grid:self.current_tile='void'
            else:
                end=''
                if len(self.states[self.all_blocks[self.select_index-1]])>1:end='0'
                self.current_tile=str(self.all_blocks[self.select_index-1])+end
            self.update_icons()
    def clear(self,arg):
        for y in range(self.c_h):
            for x in range(self.c_w):
                if self.grid:block='air'
                else:block='void'
                self.canvas.delete(self.tiles[(x,y)])
                self.tiles[(x,y)]=self.canvas.create_image((x*self.size)+(self.size//2),(y*self.size)+(self.size//2),image=self.dict[self.size][block])
                self.map_[(x,y)]=block
    def switch_grid(self,arg):
        self.grid=not self.grid
        if self.current_tile=='air' and not self.grid:self.current_tile='void'
        elif self.current_tile=='void' and self.grid:self.current_tile='air'
        for y in range(self.c_h):
            for x in range(self.c_w):
                if self.map_[(x,y)]=='air' and not self.grid:self.map_[(x,y)]='void'
                elif self.map_[(x,y)]=='void' and self.grid:self.map_[(x,y)]='air'
                self.canvas.delete(self.tiles[(x,y)])
                self.tiles[(x,y)]=self.canvas.create_image((x*self.size)+(self.size//2),(y*self.size)+(self.size//2),image=self.dict[self.size][self.map_[(x,y)]])
        self.x_pos,self.y_pos=0,0
        self.update_display()
    def toggle_toolbar(self,arg):
        self.toolbar=not self.toolbar
        if self.toolbar:
            self.tl_fr.grid()
            self.able=0
        else:
            self.tl_fr.grid_remove()
            self.able=1
    def create_toolbar(self):
        for i in range(0,len(self.all_blocks)):
            obj=self.all_blocks[i]
            def select(obj=obj):
                if len(self.states[obj])==1:self.current_tile=str(obj)
                else:
                    self.current_tile=str(obj)+'0'
                    self.select_index=self.all_blocks.index(str(obj))+1
                self.update_icons()
            while i>12:i-=12
            i+=1
            self.ics[obj]=Button(self.tl_fr,image=self.icons[obj],command=select,borderwidth=0,highlightbackgroun='black',highlightthickness=0,highlightcolor='black',activebackground='black')
            self.ics[obj].grid(row=0,column=int(i))
    def m_down(self,arg):
        if self.y_pos>0:
            self.y_pos-=1
            for y in range(self.c_h):
                for x in range(self.c_w):
                    self.canvas.move(self.tiles[(x,y)],0,self.size)
    def m_up(self,arg):
        if 50-self.see_h>self.y_pos:
            self.y_pos+=1
            for y in range(self.c_h):
                for x in range(self.c_w):
                    self.canvas.move(self.tiles[(x,y)],0,-1*self.size)
    def m_left(self,arg):
        if self.x_pos>0:
            self.x_pos-=1
            for y in range(self.c_h):
                for x in range(self.c_w):
                    self.canvas.move(self.tiles[(x,y)],self.size,0)
    def m_right(self,arg):
        if 50-self.see_w>self.x_pos:
            self.x_pos+=1
            for y in range(self.c_h):
                for x in range(self.c_w):
                    self.canvas.move(self.tiles[(x,y)],-1*self.size,0)
    def place_tile(self,arg):
        if not self.coords(arg)==None:
            x_,y_=self.coords(arg)
            self.canvas.delete(self.tiles[(x_,y_)])
            self.map_[(x_,y_)]=self.current_tile
            self.tiles[(x_,y_)]=self.canvas.create_image((x_*self.size)+(self.size//2),(y_*self.size)+(self.size//2),image=self.dict[self.size][self.current_tile])
    def fill(self,arg):
        if not self.coords(arg)==None:
            x_,y_=self.coords(arg)
            if self.arr_fill[0]==[]:self.arr_fill[0]=[x_,y_]
            else:
                self.arr_fill[1]=[x_,y_]
                if self.arr_fill[0][0]>self.arr_fill[1][0]:
                    self.arr_fill[0][0]=self.arr_fill[0][0]^self.arr_fill[1][0]
                    self.arr_fill[1][0]=self.arr_fill[0][0]^self.arr_fill[1][0]
                    self.arr_fill[0][0]=self.arr_fill[0][0]^self.arr_fill[1][0]
                if self.arr_fill[0][1]>self.arr_fill[1][1]:
                    self.arr_fill[0][1]=self.arr_fill[0][1]^self.arr_fill[1][1]
                    self.arr_fill[1][1]=self.arr_fill[0][1]^self.arr_fill[1][1]
                    self.arr_fill[0][1]=self.arr_fill[0][1]^self.arr_fill[1][1]
                for _x in range(self.arr_fill[0][0],self.arr_fill[1][0]+1):
                    for _y in range(self.arr_fill[0][1],self.arr_fill[1][1]+1):
                        self.canvas.delete(self.tiles[(_x,_y)])
                        self.tiles[(_x,_y)]=self.canvas.create_image((_x*self.size)+(self.size//2),(_y*self.size)+(self.size//2),image=self.dict[self.size][self.current_tile])
                        self.map_[(_x,_y)]=self.current_tile
                self.arr_fill=[[],[]]
            self.update_display()
    def fill_flip(self,arg):
        if not self.coords(arg)==None:
            x_,y_=self.coords(arg)
            if self.f_arr_fill[0]==[]:self.f_arr_fill[0]=[x_,y_]
            else:
                self.f_arr_fill[1]=[x_,y_]
                if self.f_arr_fill[0][0]>self.f_arr_fill[1][0]:
                    self.f_arr_fill[0][0]=self.f_arr_fill[0][0]^self.f_arr_fill[1][0]
                    self.f_arr_fill[1][0]=self.f_arr_fill[0][0]^self.f_arr_fill[1][0]
                    self.f_arr_fill[0][0]=self.f_arr_fill[0][0]^self.f_arr_fill[1][0]
                if self.f_arr_fill[0][1]>self.f_arr_fill[1][1]:
                    self.f_arr_fill[0][1]=self.f_arr_fill[0][1]^self.f_arr_fill[1][1]
                    self.f_arr_fill[1][1]=self.f_arr_fill[0][1]^self.f_arr_fill[1][1]
                    self.f_arr_fill[0][1]=self.f_arr_fill[0][1]^self.f_arr_fill[1][1]
                for _x in range(self.f_arr_fill[0][0],self.f_arr_fill[1][0]+1):
                    for _y in range(self.f_arr_fill[0][1],self.f_arr_fill[1][1]+1):
                        ID,state=self.get_block((_x,_y))
                        if state is not None:
                            x=(len(self.states[ID])//2)+state
                            if x>(len(self.states[ID])-1):x-=len(self.states[ID])
                            x*=(360//int(len(self.states[ID])))
                            self.map_[(_x,_y)]=ID+str(x)
                            self.canvas.delete(self.tiles[(_x,_y)])
                            self.tiles[(_x,_y)]=self.canvas.create_image((_x*self.size)+(self.size//2),(_y*self.size)+(self.size//2),image=self.dict[self.size][self.map_[(_x,_y)]])
                self.f_arr_fill=[[],[]]
            self.update_display()
    def fill_right(self,arg):
        if not self.coords(arg)==None:
            x_,y_=self.coords(arg)
            if self.r_arr_fill[0]==[]:self.r_arr_fill[0]=[x_,y_]
            else:
                self.r_arr_fill[1]=[x_,y_]
                if self.r_arr_fill[0][0]>self.r_arr_fill[1][0]:
                    self.r_arr_fill[0][0]=self.r_arr_fill[0][0]^self.r_arr_fill[1][0]
                    self.r_arr_fill[1][0]=self.r_arr_fill[0][0]^self.r_arr_fill[1][0]
                    self.r_arr_fill[0][0]=self.r_arr_fill[0][0]^self.r_arr_fill[1][0]
                if self.r_arr_fill[0][1]>self.r_arr_fill[1][1]:
                    self.r_arr_fill[0][1]=self.r_arr_fill[0][1]^self.r_arr_fill[1][1]
                    self.r_arr_fill[1][1]=self.r_arr_fill[0][1]^self.r_arr_fill[1][1]
                    self.r_arr_fill[0][1]=self.r_arr_fill[0][1]^self.r_arr_fill[1][1]
                for _x in range(self.r_arr_fill[0][0],self.r_arr_fill[1][0]+1):
                    for _y in range(self.r_arr_fill[0][1],self.r_arr_fill[1][1]+1):
                        ID,state=self.get_block((_x,_y))
                        if state is not None:
                            x=state+1
                            if x>len(self.states[ID])-1:x=0
                            x*=(360//int(len(self.states[ID])))
                            self.map_[(_x,_y)]=ID+str(x)
                            self.canvas.delete(self.tiles[(_x,_y)])
                            self.tiles[(_x,_y)]=self.canvas.create_image((_x*self.size)+(self.size//2),(_y*self.size)+(self.size//2),image=self.dict[self.size][self.map_[(_x,_y)]])
                self.r_arr_fill=[[],[]]
            self.update_display()
    def fill_left(self,arg):
        if not self.coords(arg)==None:
            x_,y_=self.coords(arg)
            if self.l_arr_fill[0]==[]:self.l_arr_fill[0]=[x_,y_]
            else:
                self.l_arr_fill[1]=[x_,y_]
                if self.l_arr_fill[0][0]>self.l_arr_fill[1][0]:
                    self.l_arr_fill[0][0]=self.l_arr_fill[0][0]^self.l_arr_fill[1][0]
                    self.l_arr_fill[1][0]=self.l_arr_fill[0][0]^self.l_arr_fill[1][0]
                    self.l_arr_fill[0][0]=self.l_arr_fill[0][0]^self.l_arr_fill[1][0]
                if self.l_arr_fill[0][1]>self.l_arr_fill[1][1]:
                    self.l_arr_fill[0][1]=self.l_arr_fill[0][1]^self.l_arr_fill[1][1]
                    self.l_arr_fill[1][1]=self.l_arr_fill[0][1]^self.l_arr_fill[1][1]
                    self.l_arr_fill[0][1]=self.l_arr_fill[0][1]^self.l_arr_fill[1][1]
                for _x in range(self.l_arr_fill[0][0],self.l_arr_fill[1][0]+1):
                    for _y in range(self.l_arr_fill[0][1],self.l_arr_fill[1][1]+1):
                        ID,state=self.get_block((_x,_y))
                        if state is not None:
                            x=state-1
                            if x<0:x=len(self.states[ID])-1
                            x*=(360//int(len(self.states[ID])))
                            self.map_[(_x,_y)]=ID+str(x)
                            self.canvas.delete(self.tiles[(_x,_y)])
                            self.tiles[(_x,_y)]=self.canvas.create_image((_x*self.size)+(self.size//2),(_y*self.size)+(self.size//2),image=self.dict[self.size][self.map_[(_x,_y)]])
                self.l_arr_fill=[[],[]]
            self.update_display()
    def coords(self,arg):
        x,y,x_,y_=0,0,-1,-1
        for xp in range(self.c_w):
            if xp<(arg.x/self.size)+self.x_pos<(xp+1):
                x_=xp
        for yp in range(self.c_h):
            if yp<(arg.y/self.size)+self.y_pos<(yp+1):
                y_=yp
        if x_>-1 and y_>-1 and self.able==0:return x_,y_
        else:return None
    def get_block(self,pos):
        ID=self.map_[pos]
        state=str(ID)
        while not ID.isalpha():ID=ID[:len(ID)-1]
        if len(self.states[ID])>1:
            while not state.isnumeric():state=state[1:]
            state=int(state)
            state//=(360//int(len(self.states[ID])))
        else:state=None
        return ID,state
    def flip(self,arg):
        pos=tuple(self.coords(arg))
        ID,state=self.get_block(pos)
        x=(len(self.states[ID])//2)+state
        if x>(len(self.states[ID])-1):x-=len(self.states[ID])
        x*=(360//int(len(self.states[ID])))
        self.map_[pos]=ID+str(x)
        self.update_display()
    def r_right(self,arg):
        pos=tuple(self.coords(arg))
        ID,state=self.get_block(pos)
        x=state+1
        if x>len(self.states[ID])-1:x=0
        x*=(360//int(len(self.states[ID])))
        self.map_[pos]=ID+str(x)
        self.update_display()
    def r_left(self,arg):
        pos=tuple(self.coords(arg))
        ID,state=self.get_block(pos)
        x=state-1
        if x<0:x=len(self.states[ID])-1
        x*=(360//int(len(self.states[ID])))
        self.map_[pos]=ID+str(x)
        self.update_display()
    def update_display(self):
        for y in range(self.c_h):
            for x in range(self.c_w):
                self.canvas.delete(self.tiles[(x,y)])
                self.tiles[(x,y)]=self.canvas.create_image((x*self.size)+(self.size//2),(y*self.size)+(self.size//2),image=self.dict[self.size][self.map_[(x,y)]])
        l=[]
        l.append(self.arr_fill[0])
        l.append(self.r_arr_fill[0])
        l.append(self.l_arr_fill[0])
        l.append(self.f_arr_fill[0])
        for plc in l:
            if plc!=[]:
                x,y=plc[0],plc[1]
                self.canvas.create_image((x*self.size)+(self.size//2),(y*self.size)+(self.size//2),image=self.select_tiles[self.size][l.index(plc)])
    def update_icons(self):
        tile=str(self.current_tile)
        while not tile.isalpha():tile=tile[:len(tile)-1]
        if tile=='air' or tile=='void':tile='delete'
        l=['delete']
        l.extend(self.all_blocks)
        for blk in l:
            if blk!=tile:self.ics[blk]['image']=self.icons[blk]
            else:self.ics[blk]['image']=self.selected_icons[blk]
Main()
