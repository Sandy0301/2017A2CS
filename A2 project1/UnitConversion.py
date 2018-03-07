#Hanna and Sandy's winter holiday homework

import tkinter as tk

def volumeconversion():
    a=float(key.get())
    screen.config(text='%.4fgal = %.4fl'%(a,a*3.7854))

def volume():
    screen.config(text='Convert from gal to l')
    Cal = tk.Button(top, text = "Calculate", command = volumeconversion)
    Cal.pack()

def tempconversion():
    a=float(key.get())
    screen.config(text='%.2f°C = %.2f°F'%(a,a*1.8+32))

def temp():
    screen.config(text='Convert from °C to °F')
    Cal = tk.Button(top, text = "Calculate", command = tempconversion)
    Cal.pack()

def distanceconversion():
    a=float(key.get())
    screen.config(text='%.4fmi = %.4fkm'%(a,a*1.6093))

def distance():
    screen.config(text='Convert from mi to km')
    Cal = tk.Button(top, text = "Calculate", command = distanceconversion)
    Cal.pack()

def areaconversion():
    a=float(key.get())
    screen.config(text='%.3f㎡ = %.3fsq.ft'%(a,a*10.764))

def area():
    screen.config(text='Convert from ㎡ to sq.ft')
    Cal = tk.Button(top, text = "Calculate", command = areaconversion)
    Cal.pack()

def massconversion():
    a=float(key.get())
    screen.config(text='%.3flb = %.3fkg'%(a,a*0.454))

def mass():
    screen.config(text='Convert from lb to kg')
    Cal = tk.Button(top, text = "Calculate", command = massconversion)
    Cal.pack()

def densityconversion():
    a=float(key.get())
    screen.config(text='%.2flb/cu.ft = %.2fkg/m³'%(a,a*2767.9))

def density():
    screen.config(text='Convert from lb/cu.ft to kg/m³')
    Cal = tk.Button(top, text = "Calculate", command = densityconversion)
    Cal.pack()
    
top = tk.Tk()
top.title("CONVERSION")


screen = tk.Label(top, text = "Choose a type", height = 3, font=("Arial", 12))
screen.pack()

key=tk.Entry(top,text='0')
key.pack()

top.quit=tk.Button(top, text="QUIT",font=('Arial',10), width=10,command=top.destroy)
top.quit.pack(side="bottom")


tk.Radiobutton(top, text = "Volume",command =volume).pack(side = tk.LEFT)
tk.Radiobutton(top, text = "Temperature", command = temp).pack(side = tk.LEFT)
tk.Radiobutton(top, text = "Distance",  command = distance).pack(side = tk.LEFT)
tk.Radiobutton(top, text = "Area",  command = area).pack(side = tk.LEFT)
tk.Radiobutton(top, text = "Mass",  command = mass).pack(side = tk.LEFT)
tk.Radiobutton(top, text = "Density", command = density).pack(side = tk.LEFT)


top.mainloop()

