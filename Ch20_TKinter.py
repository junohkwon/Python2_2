from tkinter import *

width = 300
height = 300

root = Tk()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mycanvas = Canvas(root)
mycanvas.grid(column=0, row=0, sticky=(N,W,E,S))

mycanvas.create_line((10,10,10,100))
mycanvas.create_line((10,10,100,10))

mycanvas.create_rectangle(100,100,150,150)
mycanvas.create_oval(200,100,250,150)
mycanvas.create_arc(200,200,300,300)
mycanvas.create_polygon(280,150,280,100,350,150,360,100,380,250)
mycanvas.create_text(50,200,text='canvas')


root.mainloop()