#Sacar dia, mes y año de hoy
from datetime import datetime
from tkinter import dialog
Hoy= datetime.now()
#De hoy
dia_actual=Hoy.day
mes_actual=Hoy.month
año_actual=Hoy.year
#Entradas
fecha_nacimiento=input("Poner en formato dd/mm/aaaa: ")
(dia, mes, año)= fecha_nacimiento.split("/")
dia_nacimiento=int(dia)
mes_nacimiento=int(mes)
año_nacimiento=int(año)
#Caja negra
edad=0
if(mes_actual>mes_nacimiento):
    if(dia_nacimiento>=dia_actual):
        edad=año_actual-año_nacimiento
elif(mes_actual<mes_nacimiento):
    edad=(año_actual-año_nacimiento)-1
elif(mes_actual==mes_nacimiento):
    if(dia_actual<dia_nacimiento):
        edad=(año_actual-año_nacimiento)-1
    elif(dia_actual>dia_nacimiento):
        edad=(año_actual-año_nacimiento)
    elif(dia_actual==dia_nacimiento):
        edad=(año_actual-año_nacimiento)
#Salidas
print("La edad es:", edad)
#__________Signo Zodiacal
Signo= ""
if(dia_nacimiento>=21 and mes_nacimiento==1) or (dia_nacimiento<=19 and mes_nacimiento==2):
    Signo= "Acuario"
if(dia_nacimiento>=20 and mes_nacimiento==2) or (dia_nacimiento<=19 and mes_nacimiento==3):
    Signo= "Piscis"
if(dia_nacimiento>=21 and mes_nacimiento==3) or (dia_nacimiento<=20 and mes_nacimiento==4):
    Signo="Aries"
if(dia_nacimiento>=21 and mes_nacimiento==4) or (dia_nacimiento<=21 and mes_nacimiento==5):
    Signo="Tauro"
if(dia_nacimiento>=22 and mes_nacimiento==5) or (dia_nacimiento<=21 and mes_nacimiento==6):
    Signo="Géminis"
if(dia_nacimiento>=22 and mes_nacimiento==6) or (dia_nacimiento<=22 and mes_nacimiento==7):
    Signo="Cáncer"
if(dia_nacimiento>=23 and mes_nacimiento==7) or (dia_nacimiento<=23 and mes_nacimiento==8):
    Signo="Leo"
if(dia_nacimiento>=24 and mes_nacimiento==8) or (dia_nacimiento<=22 and mes_nacimiento==9):
    Signo="Virgo"
if(dia_nacimiento>=23 and mes_nacimiento==9) or (dia_nacimiento<=22 and mes_nacimiento==10):
    Signo="Libra"
if(dia_nacimiento>=23 and mes_nacimiento==10) or (dia_nacimiento<=21 and mes_nacimiento==11):
    Signo="Escorpio"
if(dia_nacimiento>=22 and mes_nacimiento==11) or (dia_nacimiento<=21 and mes_nacimiento==12):
    Signo="Sagitario"
if(dia_nacimiento>=22 and mes_nacimiento==12) or (dia_nacimiento<=20 and mes_nacimiento==1):
    Signo="Capricornio"
#Salidas
print("El signo es:", Signo)
