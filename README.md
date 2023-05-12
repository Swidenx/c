import numpy as np
numero=int(input("Cantidad de elementos del vector")
vector=np.array ([])
vector=np.random.randint(1,num,num)
mayor=vector.max()
menor=vector.min()        
print (vector)
print (mayor)
print (menor)
           
# pip3 install.numpy




#upgrade np






#Ejemplo de numpy de calificaciones
import numpy as
vector=np.array ([])
vector=np.random.randint(10,100,10)
aprobados=vector[vector>59]
reprobados=vector[vector<59]
cantidaddeaprobados=vector[vector>59].size
cantidaddereprobados=vector[vector<59].size
print(vector)
print(aprobados)
print(reprobados)
print(cantidaddeaprobados)
print(cantidaddereprobados)











#otro ejercicio

import customtkinter as ctk
 import tkinter.messagebox
def FuncionPage1():
    pagina1.grid()
    pagina2.grid_forget()
    pagina3.grid_forget()
    pagina4.grid_forget()
    
def FuncionPage2:
    pagina2.grid()
    pagina1.grid_forget()
    pagina3.grid_forget()
    pagina4.grid_forget()
    
def FuncionPage3:
    pagina3.grid()
    pagina4.grid_forget()
    pagina2.grid_forget()
    pagina1.grid_forget()
    
def FuncionPage4:
    pagina4.grid()
    pagina3.grid_forget()
    pagina2.grid_forget()
    pagina1.grid_forget()
    
ventana = ctk.CTk()
ventana.geometry("1350x610")
ventana.title("App")
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

ventana.rowconfigure(0, minsize=20)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, minsize=20)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, minsize=20)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, minsize=20)
fuente = ("Arial", 12)

boton_verificar = ctk.CTkButton(ventana, text="Verificar tu problema", font=fuente)
boton_consejos = ctk.CTkButton(ventana, text="Consejos generales", font=fuente)
boton_consulta = ctk.CTkButton(ventana, text="Consulta", font=fuente)
descripcion_verificar = tk.Label(ventana, text="Haz clic en el botón para verificar si tu problema de obesidad se debe a ansiedad o depresión.", font=fuente)
descripcion_consejos = tk.Label(ventana, text="Haz clic en el botón para obtener consejos generales sobre cómo tratar la obesidad.", font=fuente)
descripcion_consulta = tk.Label(ventana, text="Haz clic en el botón para consultar con un profesional sobre tu problema de obesidad.", font=fuente)

boton_verificar.grid(row=1, column=1, pady=10)
descripcion_verificar.grid(row=2, column=1)
boton_consejos.grid(row=3, column=1, pady=10)
descripcion_consejos.grid(row=4, column=1)
boton_consulta.grid(row=5, column=1, pady=10)
descripcion_consulta.grid(row=6, column=1)
ventana.mainloop()


pagina1=CTk.Frame(ventana)
pagina2=CTk.Frame(ventana)
boton_verificar = ctk.CTkButton(ventana, text="Verificar tu problema", font=fuente)
boton_consejos = ctk.CTkButton(ventana, text="Consejos generales", font=fuente)
boton_consulta = ctk.CTkButton(ventana, text="Consulta", font=fuente)
pagina2Result1=ctk.CTkFrame(ventana)
pagina2Result2=ctk.CTkFrame(ventana)
pagina2Result3=ctk.CTkFrame(ventana)
pagina3=tk.Frame(ventana)
paginaResult1= tk.Button(ventana)
pagina4=tk.Frame(ventana)

#color
#7878EB









