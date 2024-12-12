# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:56:48 2022

Cette application a pour but de calculer l'énergie électrique nécessaire en kWh qu'un véhicule thermique
aurait besoin pour fonctionner si elle est transformer en véhicule électrique. 
Pour effectuer ce calcul on se sert du pouvoir caloriique des combustibles afin de trouver la correspon-
dance entre la consommation d'un litre de carburant et l'énergie dégagé en kWh.

Les paramètres prises en comptes sont :
    - Le type de carburant
    - La consommation de L/100 Km
    - L'identification si le véhicule tire une rémorque
    - Le nombre de Km moyen parcouru dans 1 jour
    - La saison 
    
@author: gwmazonzika
"""
# Il faut commencer par installer tkinter pour que l'interface graphique apparaisse
#pip install tk

#Importation et installation des packages
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
#from tkinter.messagebox import showerror, showwarning, showinfo
import sys, os 

#Couleurs de l'interface
co0 = "#444466" #Black
co1 = "#feffff" #White
co2 = "#6856FF" #Blue

# Deéfinition des caractéristiques de la fenêtre de l'application
window = Tk()
window.title('Calculateur de capacité véhicule')
window.geometry('480x380')
window.resizable(height=True, width=True)
window.configure(bg=co1)

#Changer l'icône de l'application
#photo1= Image.open(r"C:\Users\gwmazonzika\Documents\python\Logo_BQ.png")
#photo1 = tk.PhotoImage(file = r"C:\Users\gwmazonzika\Documents\python\Logo_BQ.png")
#window.wm_iconphoto(False, photo1)

# Ouvrir l'image
#load = Image.open(r"C:\Users\gwmazonzika\Documents\python\Logo_BQ_2.png")
# Redimensionner l'image 
#load.thumbnail((200,200))
# Création de la photo à partir de l'objet image
#photo = ImageTk.PhotoImage(load)

#Les frames (cadre ou apparence) de l'application
top_frame = Frame(window, width=480, height=50, bg=co1, pady=0, padx=0)
top_frame.grid(row=0, column=0)

down_frame = Frame(window, width=480, height=50, bg=co1, pady=0, padx=0)
down_frame.grid(row=1, column=0)

app_name = Label(top_frame, text = "Calculateur de la capacité de battérie", width=40, height=1, padx=0, anchor="center", font = ('Ivy 12 bold'), bg=co1, fg="black")
app_name.place(x=7, y=2)

app_line = Label(top_frame, text = "", width=480, height=1, padx=0, anchor="center", font = ('Arial 1'), bg='yellow', fg=co0)
app_line.place(x=0, y=35)

# Définition de la fonction de calcul de capacité 
# Rendement moteur VE entre 75 et 90 % moyenne 82.5%
# Augmentation de la consommation de carburant en hiver environ 20 %
# Si le véhicule tire une rémorque, la consommation augmente entre 40 et 50%
#---------------------------------------------------------------------------
def capacite(): 
    carb=str(carb_combobox.get())
    cons_l= float(e_cons.get())
    rem = str(rem_combobox.get())
    remor= float(e_remor.get())
    km_j=float(e_km_j.get())
    saison=str(saison_combobox.get())
    
    if carb=='Essence' or carb=='essence':
        pc=35.5
        c_kwh=(pc/3.6)*0.825
        l_result_text['text'] = ""
    elif carb=='Diesel' or carb=='diesel':
        pc=38
        c_kwh=(pc/3.6)*0.825
        l_result_text['text'] = ""
    elif carb=='Propane' or carb=='propane':
        pc=48.9
        c_kwh=(pc/3.6)*0.825
        l_result_text['text'] = ""
    else:
        l_result_text['text'] = "Erreur! Ce type de carburant n'est pas repertorié" 
    
    if cons_l<0 or km_j < 0:
        messagebox.showinfo("Attention!", "Cette valeur ne doit pas être négative!")   
    elif rem == 'oui' or rem =='Oui' :
        cons_l=cons_l*(1+(remor/15000)*0.5)
    else :
        cons_l=cons_l
    if saison=='Hiver' or saison=='hiver':
        cons_l=cons_l*(1+0.2)
    else:
        cons_l=cons_l
    cons_km = cons_l/100
    cons_l_km=km_j*cons_km 
    result=cons_l_km*c_kwh
    l_result['text'] = "{:.{}f} kWh".format(result, 0)
    
# Placer l'image dans un label
#label_image = Label(window,image=photo)
#label_image.place(x=0, y=90)


#Définition de l'emplacement et format des inputs de l'application
l_carb = tk.Label(down_frame, text= " Type de carburant", height=1, padx=0, anchor="nw", font=("Ivy 10 bold"), bg=co1, fg='black')

carb_combobox= ttk.Combobox(down_frame, values=["Essence", "Diesel", "Propane"], state="readonly", width=7, font=("Ivy 9 bold"))

l_carb.grid(row=0, column = 0, columnspan=1, pady=1, padx=1)
carb_combobox.grid(row=0, column=1, columnspan=1, pady=1, padx=1)

#e_carb = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="left", relief = SOLID)
#e_carb.grid(row=0, column = 1, columnspan = 1, pady =10, padx=0)
#carb_combobox.grid(row=2, column=2)

l_cons = Label(down_frame, text= " Consommation L/100 Km", height=1, padx=0, anchor="nw", font=("Ivy 10 bold"), bg=co1, fg='black')
l_cons.grid(row=1, column = 0, columnspan=1, pady=1, padx=1)
e_cons = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="left", relief = SOLID)
e_cons.grid(row=1, column = 1, columnspan = 1, pady =10, padx=0)

l_rem = Label(down_frame, text= " Le véhicule tire-t-il une rémorque ?", height=1, padx=0, anchor="nw", font=("Ivy 10 bold"), bg=co1, fg='black')
rem_combobox=  ttk.Combobox(down_frame, values=["Oui", "Non"], state="readonly", width=7, font=("Ivy 10 bold"))
l_rem.grid(row=2, column = 0, columnspan=1, pady=1, padx=1)
rem_combobox.grid(row=2, column=1, columnspan=1, pady=1, padx=1)

l_remor = Label(down_frame, text= " Capacité de remorquage (en lbs)", height=1, padx=0, anchor="nw", font=("Ivy 10 bold"), bg=co1, fg='black')
l_remor.grid(row=3, column = 0, columnspan=1, pady=1, padx=1)
e_remor = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="left", relief = SOLID)
e_remor.grid(row=3, column = 1, columnspan = 1, pady =10, padx=0)

#e_rem = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="left", relief = SOLID)
#e_rem.grid(row=2, column = 1, columnspan = 1, pady =10, padx=0)

l_km_j = Label(down_frame, text= " Nombre de Km/jour", height=1, padx=0, anchor="nw", font=("Ivy 10 bold"), bg=co1, fg='black')
l_km_j.grid(row=4, column = 0, columnspan=1, pady=1, padx=1) #pady 45, padx=0
e_km_j = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="left", relief = SOLID)
e_km_j.grid(row=4, column = 1, columnspan = 1, pady =10, padx=3)

l_saison = Label(down_frame, text= " Saison", height=1, padx=1, anchor="nw", font=("Ivy 10 bold"), bg=co1, fg='black')
saison_combobox = ttk.Combobox(down_frame, values=["Été", "Hiver"], state="readonly", width=7, font=("Ivy 10 bold"))
l_saison.grid(row=5, column = 0, columnspan=1, pady=1, padx=0)
saison_combobox.grid(row=5, column=1, columnspan=1, pady=1, padx=1)

#e_saison = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="left", relief = SOLID)
#e_saison.grid(row=4, column = 1, columnspan = 1, pady =10, padx=3)

#Définition de l'emplacement et format de l'espace du résultat
l_result = Label (down_frame, width=10, text= "---", height=1, padx=6, pady=1, anchor="center", font=("Ivy 14 bold"), bg='yellow', fg='black')
l_result.place(x=115, y=220)

l_result_text = Label(down_frame ,width=40, text="", height=3, padx=0, pady=1, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg='red')
l_result_text.place(x=0, y=250)

# Définition du bouton "calculer"
b_calculate = Button(down_frame, text="Calculer", width=35, height=1, bg='yellow', fg='black', font=("Ivy 12 bold"), anchor="center", command=capacite)
b_calculate.grid(row=10, column=0, pady=90, padx=5, columnspan=2)

# Ouverture ou visualisation de l'application
window.mainloop()