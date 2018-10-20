from picamera import PiCamera 
from time import sleep
import tkinter as tk
import datetime as dt

route_images = 'screenshots/'
route_records = 'vids/'

def time_stamp():
    '''
    '''
    date = dt.timedelta(microseconds=1)
    aux = str(date.days) + '-' + str(date.seconds) + '-' + str(date.microseconds)
    return aux

camera = PiCamera() # creo un objeto de la clase PiCamera

try:
    def start():
        '''
        '''
        camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))  # nos crea un objeto de la clase preview

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
    
    ventana = tk.Tk()
    ventana.title('night_cosa')
    
    ventana.buttonframe = tk.Frame(ventana)
    ventana.buttonframe.grid(row=1, column=5, columnspan=2)
    
    tk.Button(ventana.buttonframe, text='start', command=start).grid(row=1, column=2)
    tk.Button(ventana.buttonframe, text='stop', command=exit).grid(row=1, column=1)
    tk.Button(ventana.buttonframe, text='screenshot', command=screenshot).grid(row=1, column=3)
    tk.Button(ventana.buttonframe, text='record', command=record_start).grid(row=1, column=4)
    tk.Button(ventana.buttonframe, text='stop recordind', command=record_stop).grid(row=1, column=5)
    
    ventana.mainloop()
finally:
    pass
