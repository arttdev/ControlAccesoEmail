from email import message
from email.mime import base
import tkinter as tk
from tkinter import ANCHOR, Frame, ttk
import os
from tkinter import messagebox
import pymysql
import threading


from setuptools import Command

#funcion salir 
def salir():
    root.destroy()
#funcion messageBox info
def ArttdevInfo():
    messagebox.showinfo("Información", "Sistema Desarrollado por Arttdev©\n\n" + "Version 1.0" + "\n\n" + "2022")	

def prepare():
    os.system('python index.py')

def downloadInfoEmail():
    t = threading.Thread(target=prepare)
    t.start()
#put prepare to multithread

#Ventana  Impotante
class Window:
    def __init__(self, master):
        self.master = master

        self.notebook = ttk.Notebook(self.master)
        #tk tittle
        self.master.title("Xtractor")
        #default size 
        self.master.geometry("800x600")
        #icon
        #self.master.iconbitmap("icon.ico")
        #background color modern black
        #self.master.configure(background='#000000')


        #resizable
        #self.master.resizable(0,0)
        #menu
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        #file menu
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.master.destroy)
              
        
        #help menu
        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="About", menu=self.help_menu)
        self.help_menu.add_command(label="Info" , command=   ArttdevInfo )
        #when click in Info button show a message
               


        #frames
        self.frames = {}
        frame = ttk.Frame(self.notebook)
        frame1 = ttk.Frame(self.notebook)
        frame2 = ttk.Frame(self.notebook)
        frame3 = ttk.Frame(self.notebook)
        



        frame.pack(padx = 5, pady=5)
        frame1.pack(padx = 5, pady=5)
        frame2.pack(padx = 5, pady= 5)
        frame3.pack(padx = 5, pady = 5)
        
        self.notebook.add(frame, text = "Inicio")
        self.notebook.add(frame1, text = "Persona")
        self.notebook.add(frame2, text = "Herramienta")
        self.notebook.add(frame3, text = "Vehiculo")
        self.notebook.pack(padx = 5, pady = 5)
        
        
        #buttons to Inicio

        self.button1 = ttk.Button(frame, text = "Prepararar Datos", command = downloadInfoEmail)
        self.button1.pack(padx = 5, pady = 5)

        



        
        #when click en prepare button run a python file
        #self.btn_prepare.config(command = self.prepare)



        
        

        

        
        #insert a table into frame1
        
        self.tree = ttk.Treeview(frame1)
#        insert a search box into frame 1
        self.searching = ttk.Entry(frame1)
        self.searching.pack(padx = 5, pady = 5)
        self.searching.bind("<Return>", self.searchPerson)


        
#         #self.search_box.bind("<Return>", self.search)	
        #self.tree.pack(side = tk.TOP, padx = 5, pady = 5)
        self.search_button = ttk.Button(frame1, text = "Search", command = self.searchPerson)
        self.search_button.pack(side = tk.TOP, padx = 5, pady = 5)
        #funcion de busqueda
      


        self.tree["columns"] = ("one", "two", "three", "four", "five")
        self.tree.column("#0", width=100)
        self.tree.column("one", width=100)
        self.tree.column("two", width=100)
        self.tree.heading("#0", text="Name")
        self.tree.heading("one", text="Cedula")
        self.tree.heading("two", text="Fecha Ingreso")
        self.tree.heading("three", text="Fecha Salida")
        self.tree.heading("four", text="Ver Pdf")
        #button to insert values get_persons() and put into the table
        self.button2 = ttk.Button(frame1, text = "Insert", command = self.getPersons)
        self.button2.pack(padx = 5, pady = 5)

       

        self.tree.pack(padx = 5, pady = 5)

        #Insert a table into frame2 as Herrramienta 
        self.tree1 = ttk.Treeview(frame2)
        self.searchingTool = ttk.Entry(frame2)
        self.searchingTool.pack(side = tk.TOP, padx = 5, pady = 5)
        self.search_button = ttk.Button(frame2, text = "Search", command=self.searchTool)
        self.search_button.pack(side = tk.TOP, padx = 5, pady = 5)
        self.button2 = ttk.Button(frame2, text = "Insert", command = self.getTool)
        self.button2.pack(padx = 5, pady = 5)
        self.tree1["columns"] = ("one", "two", "three", "four", "five")
        self.tree1.column("#0", width=100)
        self.tree1.column("one", width=100)
        self.tree1.column("two", width=100)
        self.tree1.heading("#0", text="Name")
        self.tree1.heading("one", text="Cedula")
        self.tree1.heading("two", text="Fecha Ingreso")
        self.tree1.heading("three", text="Fecha Salida")
        self.tree1.heading("four", text="Ver Pdf")
        self.tree1.pack(padx = 5, pady = 5)
        #Insert a table into frame3

        #insert a tabhle into frame3 as Vehicule
        self.tree2 = ttk.Treeview(frame3)
        self.searchingVeh = ttk.Entry(frame3)
        self.searchingVeh.pack(side = tk.TOP, padx = 5, pady = 5)
        self.search_button = ttk.Button(frame3, text = "Search", command=self.searchVehicule)
        self.search_button.pack(side = tk.TOP, padx = 5, pady = 5)
        self.button3 = ttk.Button(frame3, text = "Insert", command = self.getVehicule)
        self.button3.pack(padx = 5, pady = 5)
        self.search_button.pack(side = tk.TOP, padx = 5, pady = 5)
        self.tree2["columns"] = ("one", "two", "three", "four", "five")
        self.tree2.column("#0", width=100)
        self.tree2.column("one", width=100)
        self.tree2.column("two", width=100)
        self.tree2.heading("#0", text="Name")
        self.tree2.heading("one", text="Cedula")
        self.tree2.heading("two", text="Placa")
        self.tree2.heading("three", text="Fecha Ingreso")
        self.tree2.heading("four", text="Fecha Salida")
        self.tree2.heading("five", text="Ver Pdf")
        self.tree2.pack(padx = 5, pady = 5)
        #a button 'insert' side top
        


        #self.button3 = ttk.Button(frame3, text = "Insert", command= self.getVehicule)
        #self.button3.pack(side= tk.TOP, padx = 5, pady = 5)

    

       
    def runQuery(self, query):
        host = "localhost"
        user = "root"
        password = ""
        database = "porteria"
        
        #with pymysql.connect(host=host, user=user, password=password, db=database) as conn:
        #    cursor = conn.cursor()
        #    result = cursor.execute(query)
          #  conn.commit()
        #return result
        try: 
            conn = pymysql.connect(host=host, user=user, password=password, db=database)
        except pymysql.Error as e:
            print("Error al conectarse a la base de datos", e)
        cur = conn.cursor()
        cur.execute(query)
        return cur


    def getPersons(self):
        cur = self.runQuery("SELECT * FROM personas")
        for row in cur:
            print(row)
            self.tree.insert("", index='0',text=row[1], values=(row[2],row[3],row[4],row[5]))
                    #with mariadb.connect(host=host, user=user, password=password, database=database, port=port) as conn: 

    def getTool(self):
        cur = self.runQuery("SELECT * FROM herramientas")
        for row in cur:
            print(row)
            self.tree1.insert("", index='0',text=row[1], values=(row[2],row[3]))

    def getVehicule(self):
        cur = self.runQuery("SELECT * FROM vehiculos")
        for row in cur:
            print(row)
            self.tree2.insert("", index='0',text=row[1], values=(row[2],row[3]))
            
   #funcion de busquedad aplicado a todas las tablas
# ccn number for test 1245251245

    def clearTable(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        records = self.tree1.get_children()
        for element in records:
            self.tree1.delete(element)
        records = self.tree2.get_children()
        for element in records:
            self.tree2.delete(element)


    def searchPerson(self):
        try:
            
            #cur = self.runQuery("SELECT * FROM personas WHERE cedula LIKE '%{}%'".format(self.search_box.get()))
            if self.searching.get() == "":
                messagebox.showwarning("Warning", "Por favor ingresa un valor")
            else:
                self.clearTable()
                cur = self.runQuery("SELECT * FROM personas WHERE idcard LIKE '%{}%'".format(self.searching.get()))
                for row in cur:
                    self.tree.insert("", index='0',text=row[1], values=(row[2],row[3],row[4],row[5]))

        except:
            messagebox.showerror("Error", "No se encontro el registro")
            print("Error")
        
    def searchTool(self):
            try:
                if self.searchingTool.get() == "":
                    messagebox.showwarning("Warning", "Por favor ingresa un valor")
                else:
                    self.clearTable()
                    cur = self.runQuery("SELECT * FROM herramientas WHERE serial= '{}'".format(self.searchingTool.get()))
                    for row in cur:
                        self.tree1.insert("", index='0',text=row[1], values=(row[2],row[3]))
            except:
                messagebox.showerror("Error", "No se encontro el registro")
                print("Error")

    def searchVehicule(self):
            try:
                if self.searchingVeh.get() == "":
                    messagebox.showwarning("Warning", "Por favor ingresa la placa del vehiculo")
                else:
                    self.clearTable()
                    cur = self.runQuery("SELECT * FROM vehiculos WHERE plate= '{}'".format(self.searchingVeh.get()))
                    for row in cur:
                        self.tree2.insert("", index='0',text=row[1], values=(row[2],row[3]))
            except:
                messagebox.showerror("Error", "No se encontro el registro")
                print("Error")

root = tk.Tk()
window = Window(root)
#window.getPersons()
root.mainloop()
#development By: Arttdev Team