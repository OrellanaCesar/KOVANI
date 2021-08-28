from  tkinter import * 
from tkinter.ttk import *
from pyhomebroker import HomeBroker

class Login (object):
    def __init__(self):
        self.__root = Tk()
        self.__dni = StringVar()
        self.__usuario = StringVar()
        self.__contrasenia = StringVar()
        self.__broker = 81
        self.__conectado = False

    def get_dni(self):
        return self.__dni
    
    def get_usuario(self):
        return self.__usuario

    def get_contrasenia(self):
        return self.__contrasenia

    def get_conectado(self):
        return self.__conectado

    def get_root(self):
        return self.__root

    def get_broker(self):
        return self.__broker

    def set_dni(self,dni):
        self.__dni = dni

    def set_usuario(self,usuario):
        self.__usuario = usuario

    def set_contrasenia(self,contrasenia):
        self.__contrasenia = contrasenia

    def set_conectado(self,conectado):
        self.__conectado = conectado

    def create_Login(self):
        ventana = self.get_root()     
        ventana.title("Login")
        ventana.geometry("320x200")
        ventana.resizable(width=False,height=False)
        s = Style()
        s.configure('My.TFrame', background='#0095ff')
        mainFrame = Frame(ventana)
        mainFrame.pack()
        mainFrame.config(width=480,height=320)


        Titulo = Label(mainFrame, text= "Acceso" ,font=("Century Gothic",24))
        Titulo.grid(column=0 , row= 0 ,padx=10 , pady=10 , columnspan=2)

        label_dni = Label(mainFrame , text = "DNI :")
        # label_dni.pack()
        label_dni.grid(column=0 , row=1)

        edni = Entry(mainFrame, width=30,textvariable= self.get_dni())
        edni.grid(column=1 , row=1)

        
        label_usuario = Label(mainFrame , text="Usuario :")
        label_usuario.grid(column=0 , row=2 , pady=5)

        eusuario = Entry(mainFrame, width=30,textvariable = self.get_usuario())
        eusuario.grid(column=1,row=2,pady=5)

        label_pass = Label(mainFrame , text="Contrsaeña :")
        label_pass.grid(column=0 ,row=3)

        epass = Entry(mainFrame, width=30 , show='*',textvariable=self.get_contrasenia())
        epass.grid(column=1,row=3)

        boton_acceso = Button(mainFrame, text="Conectar" ,command=self.conectar)
        boton_acceso.grid(column=0, row=8 ,columnspan=2, pady=10)

        self.set_dni(self.get_dni().get())
        self.set_usuario(self.get_usuario().get())
        self.set_contrasenia(self.get_contrasenia().get())
        ventana.mainloop()

    def conectar(self):
        return 'Terminar home Bronk'
