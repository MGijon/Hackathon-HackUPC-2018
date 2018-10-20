from picamera import PiCamera 
from time import sleep
import tkinter as tk
import datetime as dt


camera = PiCamera() # creo un objeto de la clase PiCamera
try:
    def start():
        camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))  # nos crea un objeto de la clase preview
        #camera.preview.alpha = 128
        sleep(10)
        camera.stop_preview() # lo eliminare luego
    def exit():
        # debemos de cerrar la cámara manualmente
        pass
    ventana = tk.Tk()
    ventana.title('night_cosa')
    
    ventana.buttonframe = tk.Frame(ventana)
    ventana.buttonframe.grid(row=1, column=2, columnspan=2)
    
    tk.Button(ventana.buttonframe, text='start', command=start).grid(row=1, column=2)
    tk.Button(ventana.buttonframe, text='stop', command=exit).grid(row=1, column=1)
    
    ventana.mainloop()
finally:
    pass
