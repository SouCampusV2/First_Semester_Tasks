from tkinter import *
 
window = Tk()
window.title("The Ship")
area = Canvas(window, width=400, height=400, background="white")
area.grid() #this geometry manager organizes widgets into a table-like structure
 
# one line (x0, y0, x1, y1)
area.create_line(165, 160, 165, 60)
area.create_line(165, 60, 80, 140)
area.create_line(80, 140, 250, 140)
area.create_line(250, 140, 165, 60)
  
area.create_polygon(30,160,  300,160,  260,200,  60,200, outline = "black", fill="blue")
 
window.mainloop()