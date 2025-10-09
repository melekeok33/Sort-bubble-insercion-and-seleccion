#------------------Documentacion interna-------------------
#       Autor: Manuel Roca (e11.manuelvicente.rocal@suizoamericano.edu.gt)
#       fecha de creacion: 04/08/2025
#       procesos pendientes: N/A
#       Lenguaje de programacion: Python
#       Recursos necesarios: Computadora
#       Aprendizajes: Tomar tiempo, sort burbuja, otra manera de hacer swap, funcion copy, sort inserción, uso de swap por medio de tuplas.
#       Historial de modificaciones: 
#           Primera: sort de burbuja
#           Segunda: sort de inserción
#----------------------------------------------------------


from tkinter import messagebox as ms
from tkinter import *
from random import randint
import time

class sorts_github(Tk):
    def __init__ (self):
        super().__init__()

        self.config(bg="RoyalBlue"); self.title("Ordenamientos por selección, burbuja e inserción")

        Label(self, text="Enter vector size").pack()
        self.vector_size=Entry(self); self.vector_size.pack()
        Button(self, text="Create vector", command=self.creacion_v).pack()
        self.created_vector=Label(self, text=""); self.created_vector.pack()

        Label(self, text="Sort by seleccion").pack()
        Button(self, text="Seleccion sort", command=self.seleccion_sort).pack()
        self.ams_seleccion=Label(self, text=""); self.ams_seleccion.pack()
        self.tseleccion=Label(self, text=""); self.tseleccion.pack()

        Label(self, text="Ordenamiento burbuja").pack()
        Button(self, text="Burbujear", command=self.burbuja).pack()
        self.respuestaburbuja=Label(self, text=""); self.respuestaburbuja.pack()
        self.tburbuja=Label(self, text=""); self.tburbuja.pack()

        Label(self, text="Ordenamiento por inserción").pack()
        Button(self, text="Inserción", command=self.insercion).pack()
        self.respuestainsercion=Label(self, text=""); self.respuestainsercion.pack()
        self.tinsercion=Label(self, text=""); self.tinsercion.pack()

        self.grapic_bar=Canvas(width="50", height="50"); self



    def creacion_v (self): #crear el vector
        try: #int numbers validacion
            size_int=int(self.vector_size.get())
        except:
            ms.showerror("ERROR", "Only int numbers")
        
        size=size_int
        self.posicion=0

        self.vector=[0]*size #create a list, but I treat like a vector. fixed size

        while self.posicion < size: #put random numbers in the vector
            self.vector[self.posicion]=randint(1, 1001)
            self.posicion+=1
        self.created_vector['text']=f"{self.vector}"


    def seleccion_sort(self):
        v=self.vector.copy() #copy the vector to reutilice in other sorts
        ulti=self.posicion-1 
        biger=0
        temp=0
        start=time.time()
        while ulti >0: #the vector sorts while ulti > 0
            biger=0 #the posicion of biger is very i,portant, needs to starts in 0
            for i in range(1, ulti+1):
                if v[i]>v[biger]: #compare the vector in diferent positions
                    biger=i
                    #swap variables
            temp=v[biger]
            v[biger]=v[ulti]
            v[ulti]=temp
            #Python dont need a temporal variable to swap the variables, we use a packaging lambda like this: v[biger]v[ulti]=v[ulti]v[biger]
            ulti-=1
        end=time.time()
        total=end-start
        self.ams_seleccion['text']=f"{v}"
        if total>0:
            self.tseleccion['text']=f"{total: .6f} miliseconds"
        else:
            self.tseleccion['text']=f"{total: .6f} seconds"

    def burbuja (self):
        v=self.vector.copy() #de nuevo, copia el vector
        inicio=time.time() #inicia el contador para tomar el tiempo 
        for i in range (len(v)-1, 0, -1): #conteo regresivo de la longitud del vector
            for j in range(i): #recorre el vector completo
                if v[j]>v[j+1]: #compara el vector en dos posiciones consecutivas
                    v[j], v[j+1] = v[j+1], v[j] #hace swap a las variables
        fin=time.time() #termina el contador
        total=fin-inicio #nos da el total de tiempo en hacer el sort
        self.respuestaburbuja['text']=f"{v}"
        if total>0:
            self.tburbuja['text']=f"{total: .6f} milisegundos"
        else:
            self.tburbuja['text']=f"{total: .6f} segundos"

    def insercion (self):
        v=self.vector.copy()
        i=1
        inicio=time.time() #inicia el contador de tiempo
        for i in range (len(v)-1): #las veces que el sort se repite
            j=i #j toma el valor de i 
            while j>0 and v[j]<v[j-1]: #realiza el ordenamiento
                v[j], v[j-1]=v[j-1], v[j] #hace swap a las variables (funciona con una tupla, por lo tanto no necesita una variable temporal)
               # v[j] cambia con v[j-1], para verlo de otra forma, el primero a la izquierda cambia con el primero a la derecha... de igual manera con el segundo
                j-=1
        fin=time.time() #termina el contador
        total=fin-inicio #saca el total de tiempo
        self.respuestainsercion['text']=f"{v}"
        if total>0:
            self.tinsercion['text']=f"{total: .6f} milisegundos"
        else:
            self.tinsercion['text']=f"{total: .6f} segundos"


    def graficar (self):
    
sorts_github().mainloop()