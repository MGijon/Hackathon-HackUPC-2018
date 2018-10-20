import picamera 
from time import sleep
import tkinter as tk

camera = picamera.PiCamera
choices=['off', 'auto', 'sunlight', 'cloudy', 'shade', 'tungsten', 'fluorescent', 'incandescent', 'flash', 'horizon']
effects=['none', 'negative', 'solarize', 'sketch', 'denoise', 'emboss', 'oilpaint', 'hatch', 'gpen', 'pastel', 'watercolor', 'film', 'blur', 'saturation', 'colorswap']

def CameraOn():
    camera.preview_fullscreen=False
    camera.preview_window=(90, 100, 320, 240)
    camera.resolution(640, 480)
    camera.start_preview()
    
def CameraOff():
    camera.stop_preview()
    
def EXIT():
    root.destroy
    camera.stop_preview()
    camera.close()
    quit
    
root = tk.Tk()
root.resizable(width=False, height=False)
root.title('Night vision first version')

root.buttonframe = tk.Frame(root)
root.geometry("320x300+89+50")
root.buttonframe.grid(row=5, column=3, columnspan=2)

tk.Button(root.buttonframe, text="Start", command=CameraOn).grid(row=1, column=1)
tk.Button(root.buttonframe, text="Stop", command=CameraOff).grid(row=1, column=2)
tk.Button(root.buttonframe, text="Exit", command=EXIT).grid(row=1, column=3)

root.mainloop() 