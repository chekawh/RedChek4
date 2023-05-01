from tkinter import *
from PIL import Image , ImageTk
import subprocess
import os
import sys
import threading
import tkinter as tk
from tkinter import ttk
import urllib . request
if 82 - 82: Iii1i
#------------------------------------->APLICACION BASE<--------------------------------
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
OOoOoo000O00 = Tk ( )
if 55 - 55: o0Oo - ii1I1iII1I1I . i1I1IiIIiIi1 % oo0O000ooO * iIIiiIIiii1
if 11 - 11: ooo0O0oO00
urllib . request . urlretrieve ( "https://drive.google.com/uc?id=1hQHp7kmYNkKH3SwLB6xydfWXDXcKksY7" , "favicon.ico" )
if 55 - 55: I11II1Ii % iIi
ii = Image . open ( "favicon.ico" )
iiI = ImageTk . PhotoImage ( ii )
if 10 - 10: ooOOO / oo0O000ooO * ooo0O0oO00 / I11II1Ii / I11II1Ii
OOoOoo000O00 . iconphoto ( True , iiI )
if 61 - 61: ii1I1iII1I1I - I1I
iIIIII1i111i = OOoOoo000O00 . winfo_screenwidth ( )
IIiiii1IiIiII = OOoOoo000O00 . winfo_screenheight ( )
if 32 - 32: i1I1IiIIiIi1
if 71 - 71: Ii
iiIII = ( iIIIII1i111i - 1160 ) // 2
IioOOOO000 = ( IIiiii1IiIiII - 700 ) // 2
OOoOoo000O00 . geometry ( "1160x700+{0}+{1}" . format ( iiIII , IioOOOO000 ) )
OOoOoo000O00 . resizable ( False , False )
OOoOoo000O00 . title ( "RedChek4 ~ Auditoria Wifi ~" )
if 85 - 85: OooOoo - oOo0O00 / Ii / ooo0O0oO00 % i1iiIII111 . Ii
if 7 - 7: iIIiiIIiii1 - I1Ii1I1 % iIIiiIIiii1 . I1Ii1I1 . i1i1i1111I
ii1i11i1 = tk . Menu ( OOoOoo000O00 )
if 11 - 11: I11II1Ii * iIIiiIIiii1 % ooOOO + I1I
if 86 - 86: i1 + o0Oo + oOo0O00 / i1iiIII111 - Iii1i . i1I1IiIIiIi1
def ii1IiIiiII ( ) :
               I1I111i11I = tk . Toplevel ( )
               I1I111i11I . title ( "Ayuda" )
               if 85 - 85: OooOoo
               if 34 - 34: Oo
               I1I111i11I . minsize ( width = 860 , height = 450 )
               I1I111i11I . maxsize ( width = 860 , height = 450 )
               if 96 - 96: ooOOO / iIi + i1iiIII111 / ooOOO / iIIiiIIiii1
               if 63 - 63: i1i1i1111I . ii1I1iII1I1I * ooOOO
               iIIIII1i111i = I1I111i11I . winfo_screenwidth ( )
               IIiiii1IiIiII = I1I111i11I . winfo_screenheight ( )
               if 6 - 6: i1iiIII111
               if 99 - 99: ooOOO * I1Ii1I1
               iiIII = ( iIIIII1i111i - 860 ) // 2
               IioOOOO000 = ( IIiiii1IiIiII - 450 ) // 2
               I1I111i11I . geometry ( "860x450+{0}+{1}" . format ( iiIII , IioOOOO000 ) )
               Oooo0o0oO0 = tk . Text ( I1I111i11I , wrap = tk . WORD )
               Oooo0o0oO0 . pack ( expand = True , fill = tk . BOTH )
               Oooo0o0oO0 . tag_configure ( "center" , justify = 'center' )
               Oooo0o0oO0 . insert ( tk . END , "\n\nSi has llegado aquí, es por que necesitas ayuda con el funcionamiento del programa. A continuación te explico como funciona y como se combina entre los campos que necesitas en cada paso. \n\n Primer paso:\n Debes hacer uso del campo Wifi para seleccionar tu tarjeta, luego eliminar procesos y luego entrar en modo escucha. \n\n Segundo paso: \n Debes mantener el nombre de la tarjeta wifi, luego añadir el BSSID (Router), seleccionar el canal por donde escucha tu router, que aparece en el paso anterior y ponerle nombre al archivo que vas a guardar. \n\n Tercer Paso (OPCIONAL): \nEste paso es para acelerar un poco el Handshake si no queremos esperar, aqui debemos añadir la MAC de nuestro cliente que aparece cuando iniciamos el paso dos, y seleccionar el numero de paquetes a enviar, todo los demás campos debe permanecer colocado sin modificación. \n\nCuarto Paso: \n Pulsar el botón de resetear wifi para dejar la tarjeta en modo Managed nuevamente." "\n\n\n ------>Gracias por utilizar el programa.<-----\n ------>Créditos para Cheka@WH.<-----" , "center" )
               Oooo0o0oO0 . config ( state = tk . DISABLED )
               if 71 - 71: OooOoo - Ii
def OO ( ) :
               OOoOoo000O00 . destroy ( )
               if 27 - 27: Oo / ooo0O0oO00 + iIi - OooOoo * I1Ii1I1 / I1Ii1I1
               if 53 - 53: I1Ii1I1
O0oOo0oOoOoo = tk . Menu ( ii1i11i1 , tearoff = 0 )
O0oOo0oOoOoo . add_command ( label = "Ayuda" , command = ii1IiIiiII )
O0oOo0oOoOoo . add_command ( label = "Salir" , command = OO )
if 59 - 59: i1 + Iii1i / I1I
if 52 - 52: i1i1i1111I + IiIIii11Ii + iIIiiIIiii1
OOoOoo000O00 . config ( menu = ii1i11i1 )
if 52 - 52: i1iiIII111 % Oo . I1Ii1I1 + ooOOO % Oo . iIi
if 56 - 56: i1iiIII111 * iIi - iIIiiIIiii1
ii1i11i1 . add_cascade ( label = "Opciones" , menu = O0oOo0oOoOoo )
if 15 - 15: I1I % Ii + ii1I1iII1I1I * Iii1i
if 67 - 67: I1I * ii1I1iII1I1I + i1iiIII111 . i1iiIII111 % Oo
if 93 - 93: oOo0O00 % ii1I1iII1I1I * i1iiIII111
if 52 - 52: ooo0O0oO00 + I1I / o0Oo - I1Ii1I1 * I11II1Ii % oOo0O00
if 52 - 52: oOo0O00 . I1I + I11II1Ii - i1iiIII111 % i1I1IiIIiIi1
def Oo0O0o0oO000 ( ) :
               o0Ooo . insert ( END , "\n------------------>>Cheka@WH CopyRigth©️ 2023-2024<<------------------\n" )
               iioO00o00OO = o00o . get ( )
               Ii11I = "airmon-ng start " + iioO00o00OO
               iIiO000O0Oo0 = subprocess . Popen ( Ii11I , shell = True , stdout = subprocess . PIPE )
               Oo0O0O , Ii1IiIII1 = iIiO000O0Oo0 . communicate ( )
               o0Ooo . insert ( END , Oo0O0O . decode ( 'utf-8' ) )
               if 11 - 11: i1 / o0Oo
               o0Ooo . see ( END )
               if 89 - 89: I1I * i1i1i1111I
               if 54 - 54: ooo0O0oO00 + ii1I1iII1I1I - I1I . ii1I1iII1I1I
               if 50 - 50: Iii1i * o0Oo % Iii1i - oOo0O00 + o0Oo
def ooOOOoOO0 ( ) :
               o0Ooo . insert ( END , "\n------------------>>Cheka@WH CopyRigth©️ 2023-2024<<------------------\n" )
               oo00oO000 = "airmon-ng check kill"
               iIiIiiIIIiII = subprocess . Popen ( oo00oO000 , stdout = subprocess . PIPE , stderr = subprocess . PIPE , shell = True )
               Oo0O0O , Ii1IiIII1 = iIiIiiIIIiII . communicate ( )
               o0Ooo . insert ( END , Oo0O0O . decode ( 'utf-8' ) )
               o0Ooo . insert ( END , "\n¡Completado: He eliminado los procesos correctamente!\n" )
               if 44 - 44: ii1I1iII1I1I + i1i1i1111I + Iii1i - ooo0O0oO00
               o0Ooo . see ( END )
               if 7 - 7: i1i1i1111I / Ii * Iii1i
               if 32 - 32: iIi . OooOoo
               if 31 - 31: Oo - I11II1Ii
def IIIi1111iiIi1 ( ) :
               o0Ooo . insert ( END , "\n------------------>>Cheka@WH CopyRigth©️ 2023-2024<<------------------\n" )
               o0Ooo . insert ( END , "\n¡Revisa la terminal que he abierto, estoy en modo escucha!\n" )
               iioO00o00OO = o00o . get ( )
               if 4 - 4: o0Oo % I1I - i1i1i1111I
               def iI11i1iI1I1Ii ( ) :
                              if 65 - 65: Iii1i + oo0O000ooO - ii1I1iII1I1I . i1I1IiIIiIi1 + OooOoo * ii1I1iII1I1I
                              I1III11IIii = "gnome-terminal --command 'airodump-ng {0}'" . format ( iioO00o00OO )
                              subprocess . run ( I1III11IIii , shell = True )
                              if 36 - 36: i1I1IiIIiIi1 / iIi % o0Oo * i1iiIII111
               threading . Thread ( target = iI11i1iI1I1Ii ) . start ( )
               if 4 - 4: I1Ii1I1 + I1I - ooOOO + i1iiIII111
               if 36 - 36: ooOOO * Iii1i % I1I % i1 . ii1I1iII1I1I
               o0Ooo . see ( END )
               if 63 - 63: oo0O000ooO / oo0O000ooO * Iii1i - oOo0O00 . i1
               if 52 - 52: oOo0O00 / I11II1Ii * oo0O000ooO + iIIiiIIiii1 % ii1I1iII1I1I + ooo0O0oO00
def OOOOOoo0oOo00 ( ) :
               o0Ooo . insert ( END , "\n------------------>>Cheka@WH CopyRigth©️ 2023-2024<<------------------\n" )
               i1II1 = "sudo systemctl restart NetworkManager.service"
               oOoOo = subprocess . Popen ( i1II1 , stdout = subprocess . PIPE , stderr = subprocess . PIPE , shell = True )
               Oo0O0O , Ii1IiIII1 = oOoOo . communicate ( )
               o0Ooo . insert ( END , Oo0O0O . decode ( 'utf-8' ) )
               o0Ooo . insert ( END , "\n¡Se ha reiniciado la tarjeta de red correctamente!\n" )
               if 39 - 39: ooo0O0oO00
               o0Ooo . see ( END )
               if 17 - 17: Ii . oOo0O00 % OooOoo
               if 82 - 82: Iii1i . oOo0O00 % oo0O000ooO - i1I1IiIIiIi1
def oO ( ) :
               o0Ooo . delete ( 1.0 , END )
               if 62 - 62: i1i1i1111I
               if 52 - 52: I11II1Ii . Ii * OooOoo / I11II1Ii
def oo0O0 ( ) :
               III1II11i = iiI1iiii1iii . get ( )
               iioO00o00OO = o00o . get ( )
               O0OOooO0O0Oo0 = I11iIi1i1iIi . get ( )
               iI11 = OO0 . get ( )
               O00OOo = "airodump-ng -c {0} --bssid {1} -w {2} {3}" . format ( III1II11i , O0OOooO0O0Oo0 , iI11 , iioO00o00OO )
               subprocess . Popen ( [ 'gnome-terminal' , '--command' , O00OOo ] , stdout = subprocess . PIPE , stderr = subprocess . PIPE )
               o0Ooo . insert ( END , "\n------------------>>Cheka@WH CopyRigth©️ 2023-2024<<------------------\n" )
               o0Ooo . insert ( END , "\nLa auditoría ha comenzado. ¡Buena suerte!\n" )
               o0Ooo . see ( END )
               if 77 - 77: ii1I1iII1I1I
               if 95 - 95: ooOOO % i1i1i1111I . i1
def IiiI11IIi1I ( ) :
               iioO00o00OO = o00o . get ( )
               O0OOooO0O0Oo0 = I11iIi1i1iIi . get ( )
               oOOOO0ooO = O0O0oO . get ( )
               IIiI1i = OoOOooO0oOO0Oo . get ( )
               o0Ooo . insert ( END , "\n------------------>>Cheka@WH CopyRigth©️ 2023-2024<<------------------\n" )
               o0Ooo . insert ( END , "\nDesautenticando dispositivo...\n\n" )
               if 4 - 4: i1 % I1Ii1I1 * ooo0O0oO00 + ooo0O0oO00 . i1i1i1111I - i1
               def I1i ( ) :
                              O0OOOOoO0o = "aireplay-ng -0 {0} -a {1} -c {2} {3}" . format ( IIiI1i , O0OOooO0O0Oo0 , oOOOO0ooO , iioO00o00OO )
                              o00ooOOO0Oo = subprocess . Popen ( O0OOOOoO0o , shell = True , stdout = subprocess . PIPE , stderr = subprocess . PIPE , universal_newlines = True )
                              O00OoO0OOO0 = [ ]
                              while len ( O00OoO0OOO0 ) < int ( IIiI1i ) :
                                             Oo0o0Oo = o00ooOOO0Oo . stdout . readline ( )
                                             if not Oo0o0Oo :
                                                            break
                                             O00OoO0OOO0 . append ( Oo0o0Oo )
                                             o0Ooo . insert ( END , Oo0o0Oo )
                                             o0Ooo . see ( 'end' )
                                             o0Ooo . update_idletasks ( )
                              o00ooOOO0Oo . kill ( )
                              return O00OoO0OOO0 [ - 2 : - 1 ]
                              if 100 - 100: i1iiIII111 . oo0O000ooO * o0Oo * o0Oo
               O00OoO0OOO0 = I1i ( )
               o0Ooo . insert ( END , "\n" . join ( O00OoO0OOO0 ) )
               o0Ooo . see ( 'end' )
               o0Ooo . update_idletasks ( )
               o0Ooo . insert ( END , "\n\n---------------->> ¡Proceso completado! Dispositivo desautenticado de la red wifi. <<----------------\n\n" )
               if 85 - 85: oo0O000ooO / OooOoo . I11II1Ii % Oo + Oo - iIIiiIIiii1
               if 59 - 59: OooOoo
               if 53 - 53: i1i1i1111I / ooOOO - iIi + o0Oo * i1i1i1111I * i1iiIII111
               if 87 - 87: i1iiIII111 - oo0O000ooO * Ii % i1i1i1111I % i1
ooOo00oOo0Ooo = list ( range ( 1 , 15 ) )
if 42 - 42: oOo0O00
if 46 - 46: OooOoo - iIIiiIIiii1 / ii1I1iII1I1I
ii1I = list ( range ( 10 , 51 ) )
if 80 - 80: oo0O000ooO / OooOoo % i1I1IiIIiIi1 / ooOOO * ooOOO - Iii1i
O0ooOO0O0O0O = Frame ( OOoOoo000O00 )
O0ooOO0O0O0O . grid ( row = 0 , column = 0 , padx = 5 , pady = 5 )
if 59 - 59: o0Oo / Oo - i1
OO0Oo0OOo00 = Frame ( OOoOoo000O00 )
OO0Oo0OOo00 . grid ( row = 0 , column = 5 , padx = 5 , pady = 5 )
if 100 - 100: iIi . oo0O000ooO * i1 + IiIIii11Ii % I1I / iIi
oo00oOOo0O0o = Frame ( OOoOoo000O00 )
oo00oOOo0O0o . grid ( row = 0 , column = 7 , padx = 5 , pady = 5 )
if 12 - 12: ii1I1iII1I1I + I1I / OooOoo
if 70 - 70: iIIiiIIiii1 % I1Ii1I1 + ooOOO
if 62 - 62: i1iiIII111 * i1I1IiIIiIi1 . i1i1i1111I
i11I1IiIiI1i = Label ( O0ooOO0O0O0O , text = "Preparar Tarjeta Wifi" )
i11I1IiIiI1i . grid ( row = 0 , column = 0 , padx = 5 , pady = 5 )
if 59 - 59: ooOOO * o0Oo % IiIIii11Ii
if 14 - 14: oo0O000ooO / iIi . i1iiIII111 % i1 % i1i1i1111I * i1I1IiIIiIi1
Ooo = StringVar ( )
o00o = Entry ( O0ooOO0O0O0O , width = 12 , textvariable = Ooo , justify = 'center' )
o00o . grid ( row = 0 , column = 1 , ipadx = 20 , ipady = 5 )
if 5 - 5: Oo - i1 . ooo0O0oO00
if 18 - 18: IiIIii11Ii - ooo0O0oO00 * I11II1Ii - OooOoo
o0OOo0OoO = Button ( O0ooOO0O0O0O , text = "Seleccionar" , command = Oo0O0o0oO000 )
o0OOo0OoO . grid ( row = 0 , column = 2 , padx = 5 , pady = 5 )
if 57 - 57: Oo + IiIIii11Ii
if 70 - 70: Ii + ooOOO - Oo / i1i1i1111I - I1I * iIi
if 3 - 3: i1iiIII111
if 32 - 32: I1I % i1i1i1111I
i11I1IiIiI1i = Label ( O0ooOO0O0O0O , text = "Eliminar Procesos: " )
i11I1IiIiI1i . grid ( row = 1 , column = 0 , padx = 5 , pady = 5 )
if 98 - 98: I11II1Ii / i1 / OooOoo + Iii1i % ooOOO
if 19 - 19: ooOOO % I1Ii1I1
o0OOo0OoO = Button ( O0ooOO0O0O0O , text = "Eliminar" , command = ooOOOoOO0 )
o0OOo0OoO . grid ( row = 1 , column = 1 , padx = 5 , pady = 5 )
if 15 - 15: OooOoo . IiIIii11Ii . I11II1Ii / Iii1i + ooOOO / Ii
if 17 - 17: iIIiiIIiii1 - i1i1i1111I . i1I1IiIIiIi1 - iIIiiIIiii1 + Oo % i1I1IiIIiIi1
if 65 - 65: Ii % iIIiiIIiii1
i11I1IiIiI1i = Label ( O0ooOO0O0O0O , text = "Iniciar escucha: " )
i11I1IiIiI1i . grid ( row = 2 , column = 0 , padx = 5 , pady = 5 )
if 39 - 39: Iii1i * oo0O000ooO . ii1I1iII1I1I - Oo
if 63 - 63: i1i1i1111I - i1iiIII111 . OooOoo % OooOoo . iIi + I11II1Ii
o0OOo0OoO = Button ( O0ooOO0O0O0O , text = "Escuchar" , command = IIIi1111iiIi1 )
o0OOo0OoO . grid ( row = 2 , column = 1 , padx = 5 , pady = 5 )
if 71 - 71: o0Oo + iIIiiIIiii1 % i1I1IiIIiIi1 + iIi % Oo - Oo
if 84 - 84: I1I % i1I1IiIIiIi1 - ii1I1iII1I1I / i1I1IiIIiIi1 + ii1I1iII1I1I - Oo
if 41 - 41: ooOOO + OooOoo + oo0O000ooO * i1i1i1111I
if 12 - 12: i1i1i1111I
i11I1IiIiI1i = Label ( OO0Oo0OOo00 , text = "Elige tu canal: " )
i11I1IiIiI1i . grid ( row = 0 , column = 0 , padx = 5 , pady = ( 40 , 5 ) )
if 56 - 56: IiIIii11Ii
if 17 - 17: I11II1Ii . ooo0O0oO00 % Oo + IiIIii11Ii - ii1I1iII1I1I
iiI1iiii1iii = ttk . Combobox ( OO0Oo0OOo00 , values = ooOo00oOo0Ooo )
iiI1iiii1iii . current ( 0 )
iiI1iiii1iii . grid ( row = 0 , column = 1 , padx = 5 , pady = ( 40 , 5 ) )
if 93 - 93: oOo0O00
if 77 - 77: Oo + iIIiiIIiii1 % I1I
if 20 - 20: i1 - IiIIii11Ii . IiIIii11Ii % ooOOO . i1 % ii1I1iII1I1I
if 72 - 72: ooo0O0oO00 % iIi . ooOOO * I1Ii1I1 . ooOOO
Oooo00O = Button ( OO0Oo0OOo00 , text = "Auditar" , command = oo0O0 )
Oooo00O . grid ( row = 4 , column = 1 )
if 9 - 9: Iii1i * i1i1i1111I
if 96 - 96: o0Oo / i1I1IiIIiIi1 - I1Ii1I1 + oOo0O00 + i1iiIII111
ii1i = Label ( OO0Oo0OOo00 , text = "BSSID (Router):" )
ii1i . grid ( row = 1 , column = 0 )
if 87 - 87: ooOOO
if 57 - 57: oo0O000ooO - i1I1IiIIiIi1 % ooOOO - iIIiiIIiii1 / IiIIii11Ii . ii1I1iII1I1I
I11I11IiiI1i = StringVar ( )
I11iIi1i1iIi = Entry ( OO0Oo0OOo00 , width = 12 , textvariable = I11I11IiiI1i , justify = 'center' )
I11iIi1i1iIi . grid ( row = 1 , column = 1 , ipadx = 20 , ipady = 5 )
if 1 - 1: I1I + OooOoo
if 98 - 98: i1iiIII111 + Iii1i . oo0O000ooO
if 96 - 96: OooOoo / ooo0O0oO00 - i1 * iIIiiIIiii1
if 72 - 72: i1i1i1111I + Ii - Iii1i - i1i1i1111I - I11II1Ii + ii1I1iII1I1I
OoOoOo = Label ( OO0Oo0OOo00 , text = "Cliente:" )
OoOoOo . grid ( row = 2 , column = 0 )
if 80 - 80: IiIIii11Ii * ii1I1iII1I1I . i1 . ii1I1iII1I1I
if 76 - 76: i1i1i1111I % oOo0O00 - i1iiIII111 * i1
o00 = StringVar ( )
O0O0oO = Entry ( OO0Oo0OOo00 , width = 12 , textvariable = o00 , justify = 'center' )
O0O0oO . grid ( row = 2 , column = 1 , ipadx = 20 , ipady = 5 )
if 15 - 15: I1I % IiIIii11Ii + OooOoo * Oo / OooOoo
if 33 - 33: iIi / OooOoo
if 98 - 98: I1Ii1I1 . oo0O000ooO * I11II1Ii - i1I1IiIIiIi1 % I11II1Ii * iIi
if 42 - 42: OooOoo + i1i1i1111I - i1I1IiIIiIi1 - oOo0O00 * I11II1Ii + Ii
oOOooO = Label ( OO0Oo0OOo00 , text = "Archivo:" )
oOOooO . grid ( row = 3 , column = 0 )
if 37 - 37: i1i1i1111I
if 79 - 79: o0Oo % I11II1Ii - Ii % I11II1Ii - I1I
OooOoO0o00 = StringVar ( )
OO0 = Entry ( OO0Oo0OOo00 , width = 12 , textvariable = OooOoO0o00 , justify = 'center' )
OO0 . grid ( row = 3 , column = 1 , ipadx = 20 , ipady = 5 )
if 23 - 23: i1
if 91 - 91: iIIiiIIiii1 - iIi % IiIIii11Ii / IiIIii11Ii
if 37 - 37: i1iiIII111 - iIi * i1iiIII111 . i1i1i1111I
i11I1IiIiI1i = Label ( oo00oOOo0O0o , text = "Elige cantidad de paquetes: " )
i11I1IiIiI1i . grid ( row = 0 , column = 6 , padx = 5 , pady = ( 33 , 5 ) )
if 43 - 43: ooo0O0oO00
if 87 - 87: ooOOO + iIi * i1iiIII111 / i1i1i1111I
OoOOooO0oOO0Oo = ttk . Combobox ( oo00oOOo0O0o , values = ii1I )
OoOOooO0oOO0Oo . current ( 0 )
OoOOooO0oOO0Oo . grid ( row = 0 , column = 7 , padx = 5 , pady = ( 33 , 5 ) )
if 75 - 75: IiIIii11Ii / o0Oo + iIi / i1i1i1111I * ooo0O0oO00 + o0Oo
if 83 - 83: iIIiiIIiii1 / ii1I1iII1I1I . iIIiiIIiii1
if 47 - 47: IiIIii11Ii
if 40 - 40: i1iiIII111 / oo0O000ooO
iiiI = Label ( oo00oOOo0O0o , text = "Desautenticar Cliente: " )
iiiI . grid ( row = 1 , column = 6 , padx = 5 , pady = 5 )
if 13 - 13: iIIiiIIiii1 % i1iiIII111 . OooOoo % o0Oo % OooOoo
if 21 - 21: iIi * I1Ii1I1
oO00oO0O = Button ( oo00oOOo0O0o , text = "Desautenticar" , command = IiiI11IIi1I )
oO00oO0O . grid ( row = 1 , column = 7 , padx = 5 , pady = 5 )
if 97 - 97: i1 - i1 % oo0O000ooO + IiIIii11Ii / I11II1Ii * i1I1IiIIiIi1
if 60 - 60: iIIiiIIiii1 - ii1I1iII1I1I % I1Ii1I1
if 26 - 26: ooOOO / oo0O000ooO . ooo0O0oO00 + iIIiiIIiii1 . Oo
if 37 - 37: I1Ii1I1
i11I1IiIiI1i = Label ( oo00oOOo0O0o , text = "Limpiar terminal: " )
i11I1IiIiI1i . grid ( row = 2 , column = 6 , padx = 5 , pady = 5 )
if 35 - 35: OooOoo % i1i1i1111I - i1I1IiIIiIi1 / IiIIii11Ii
if 4 - 4: o0Oo . IiIIii11Ii % o0Oo / i1i1i1111I
o0OOo0OoO = Button ( oo00oOOo0O0o , text = "Limpiar" , command = oO )
o0OOo0OoO . grid ( row = 2 , column = 7 , padx = 5 , pady = 5 )
if 48 - 48: i1iiIII111 . Oo
if 92 - 92: OooOoo + Ii / oo0O000ooO + OooOoo * oo0O000ooO * i1I1IiIIiIi1
if 79 - 79: i1i1i1111I
i11I1IiIiI1i = Label ( oo00oOOo0O0o , text = "Resetear Tarjeta Wifi: " )
i11I1IiIiI1i . grid ( row = 3 , column = 6 , padx = 5 , pady = 5 )
if 3 - 3: OooOoo / iIi % iIIiiIIiii1
if 55 - 55: oOo0O00
o0OOo0OoO = Button ( oo00oOOo0O0o , text = "Resetear" , command = OOOOOoo0oOo00 )
o0OOo0OoO . grid ( row = 3 , column = 7 , padx = 5 , pady = 5 )
if 31 - 31: Ii . ii1I1iII1I1I / iIi
if 59 - 59: Oo
o00o0oOOo0Oo = Frame ( OOoOoo000O00 )
o0Ooo = Text ( o00o0oOOo0Oo , height = 15 , width = 100 )
o0Ooo . pack ( )
if 74 - 74: i1i1i1111I / IiIIii11Ii % iIIiiIIiii1 . ooo0O0oO00
o00o0oOOo0Oo . place ( relx = 0.5 , rely = 0.6 , anchor = 'center' )
if 65 - 65: Iii1i % oo0O000ooO - o0Oo . ooOOO + Iii1i
if 46 - 46: IiIIii11Ii
if 31 - 31: Oo * i1iiIII111 % Ii / ooo0O0oO00 + I1Ii1I1 + i1I1IiIIiIi1
if 90 - 90: I1Ii1I1 * i1i1i1111I / i1I1IiIIiIi1 * Ii
oo = tk . Label ( OOoOoo000O00 , text = "Versión 1.0 (Free)" )
oo . place ( relx = 0.92 , rely = 0.96 , anchor = 'center' )
if 6 - 6: iIIiiIIiii1 + ooo0O0oO00 - oo0O000ooO
if 33 - 33: I1I
O0 = tk . Label ( OOoOoo000O00 , text = "Cheka@WH CopyRigth©️ 2023-2024" )
O0 . place ( relx = 0.120 , rely = 0.96 , anchor = 'center' )
if 43 - 43: IiIIii11Ii . o0Oo - i1I1IiIIiIi1
OOoOoo000O00 . mainloop ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
