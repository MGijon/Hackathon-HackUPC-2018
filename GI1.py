from picamera import PiCamera 
from time import sleep
import tkinter as tk
import datetime as dt

route_images = 'screenshots/' # debo creaer la carpeta
route_records = 'vids/'  # debo crear la carpeta

camera = PiCamera() # creo un objeto de la clase PiCamera

ventana = tk.Tk()
ventana.title('night_cosa')
    
ventana.buttonframe = tk.Frame(ventana)
ventana.buttonframe.grid(row=1, column=5, columnspan=2)

def time_stamp():
    '''
    Generate a string based on data time to name the files we are saving
    '''
    date = dt.datetime.now()
    aux = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + '-' + str(date.minute) + '-' + str(date.second) + '-' + str(date.microsecond)
    return aux

try:
    def start():
        '''
        '''
        camera.start_preview(fullscreen=False, window = (0, 0, 480*0.8, 320*0,8)) # coordenada donde empieza la x, primera coor de la y, tamaño en el eje x, tamaño en el eje y
        
    def exit():
        '''
        '''
        camera.stop_preview()
    
    def screenshot():
        '''
        '''
        #camera.capture(route_images + time_stamp() + '.jpg')
        camera.capture(time_stamp() + '.jpg')
    
    def record_start():
        '''
        '''
        #camera.start_recording(route_records + time_stamp() + '.h264')
        camera.start_recording(time_stamp() + '.h264')
    
    def record_stop():
        '''
        '''
        camera.stop_recording()
        pass
    '''
    ventana = tk.Tk()
    ventana.title('night_cosa')
    
    ventana.buttonframe = tk.Frame(ventana)
    ventana.buttonframe.grid(row=1, column=5, columnspan=2)
    '''
    tk.Button(ventana.buttonframe, text='start', command=start).grid(row=1, column=2)
    tk.Button(ventana.buttonframe, text='stop', command=exit).grid(row=1, column=1)
    tk.Button(ventana.buttonframe, text='screenshot', command=screenshot).grid(row=1, column=3)
    tk.Button(ventana.buttonframe, text='record', command=record_start).grid(row=1, column=4)
    tk.Button(ventana.buttonframe, text='stop recordind', command=record_stop).grid(row=1, column=5)
    
    ventana.mainloop()
finally:
    pass
