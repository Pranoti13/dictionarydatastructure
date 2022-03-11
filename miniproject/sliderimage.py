from tkinter import*

from PIL import Image
import time
class Slider:
    def init (self,root):
        self.root=root
        self.root.title("Slider")
        self.root.geometry("1350*700+0+0")
         #pass
        #=====images==========
        self.image1=ImageTk.photoImage(file="image1.jpeg")
        self.image2=ImageTk.photoImage(file="image2.jpeg")
        #==========
        Frame_slider=Frame(self.root)
        Frame_slider.place(x=150,y=50,width=500,height=500)
        self.lbl1=Label(Frame_slider,image=self.image1,bd=0)
        self.lbl1.place(x=0,y=0)
        self.lbl2 =Label(Frame_slider,image=self.image2, bd=0)
        self.lbl2.place(x=500, y=0)
        self.x=500
        self.slider_func()

    def slider_func(self):
        #print(self.x)
        self.x-=1
        if self.x==0:
            self.x=500
            time.sleep(1)
            #=============swap======
            self.new_im=self.image1
            self.image1=self.image2
            self.image2=self.new_im
            self.lbl1.config(image=self.image1)
            self.lbl2.config(image=self.image2)
        self.lbl2.place(x=self.x,y=0)
       # print(self.x)
        self.lble2.after(1,self.slider_func)

root=Tk()

obj=Slider()
root.mainloop()