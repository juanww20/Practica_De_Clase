from flet import *
import flet as ft
from random import *
import numpy as np
from Validacion import *
from Ven2 import *

def main (page:Page):

    page.title = 'Evaluacion 1'
    page.window_center()
    page.window_maximizable = False
    page.window_resizable = False
    page.update()
    def change(e):
        index = e.control.selected_index
        t1.visible = True if index == 0 else False
        t2.visible = True if index == 1 else False
        page.update()

    page.navigation_bar = NavigationBar(
        bgcolor = "blue",
        selected_index= 0,
        on_change= change,
        destinations= [
            NavigationDestination(icon = "TRANSFORM"),
            NavigationDestination(icon = "CALCULATE")
    ]
    )

    #Ventana 1
    #FUNCIONES DE PRINCIPAL
    #Decir error por el ingreso
    def error():
        result.value="Por favor ingresar caracteres correctos"
        page.update()
    
    #Operación
    def cav (e):
        estado = opcion.value
        band = ident(ent)
        if estado == "1 Decimal a Binario":
            if band == True:
                num = int(ent.value)
                rr = bin(num)[2::]
                result.value = rr
                result.update()
            else:
                error()
        elif estado == "2 Binario a decimal":
            if band == True:
                num = ent.value
                num2 = int(num)
                b = True
                b = identbn(num2,b,ent,tfr2)
                if b == True:
                    rr = int(num,2)
                    result.value = str(rr)
                    result.update()
                else:
                    error()
            else:
                error()
        elif estado == "3 Decimal a Octal":
            if band == True:
                num = int(ent.value)
                rr = oct(num)[2::]
                result.value = str(rr)
                result.update()
            else:
                error()
        elif estado == "4 Octal a decimal":
            if band == True:
                num = ent.value
                num2 = int(num)
                b = True
                b = identbc(num2,b,ent,tfr2)
                if b == True:
                    rr = int(num,8)
                    result.value = str(rr)
                    result.update()
                else:
                    error()
            else:
                error()
        elif estado == "5 Decimal a Hexadecimal":
            if band == True:
                num = int(ent.value)
                rr = hex(num)[2::]
                result.value = rr
                result.update()
            else:
                error()
        elif estado == "6 Hexadecimal a Decimal":
                num = ent.value
                b = True
                b = identbd(b,ent,tfr2)
                if b == True:
                    rr = int(num,16)
                    result.value = str(rr)
                    result.update()
                else:
                    error()
        elif estado == "7 Decimal a Cuaternario":
            if band == True:
                num = int(ent.value)
                i = tras = 0
                while num > 0:
                    digito = num%4
                    num = int(num//4)
                    tras += digito*(10**i)
                    i = i +1
                result.value = tras
                result.update()
            else:
                error()
        elif estado == "8 Cuaternario a Decimal":
            if band == True:
                num = int(ent.value)
                i = tras = 0
                b = True
                b = identcuaternario(b,ent,tfr2)
                if b == True:
                    while num > 0:
                        digito = num%10
                        num = int(num//10)
                        tras += digito*(4**i)
                        i = i +1
                    result.value = tras
                    result.update()
                else:
                    error()
            else:
                error()
        elif estado == "9 Decimal a Terciario":
            if band == True:
                num = int(ent.value)
                i = tras = 0
                while num > 0:
                    digito = num%3
                    num = int(num//3)
                    tras += digito*(10**i)
                    i = i +1
                result.value = tras
                result.update()
            else:
                error()
        elif estado == "10 Terciario a Decimal":
            if band == True:
                num = int(ent.value)
                i = tras = 0
                b = True
                b = identerciaro(b,ent,tfr2)
                if b == True:
                    while num > 0:
                        digito = num%10
                        num = int(num//10)
                        tras += digito*(3**i)
                        i = i +1
                    result.value = tras
                    result.update()
                else:
                    error()
            else:
                error()
        
    def limpiar(e):
        opcion.value = ""
        ent.value = ""
        result.value = ""
        page.update()

    #Componentes
    cont1 = ft.Container(ft.Row([
        ft.Text("Conversión", weight = "bold", size = 42),
        ft.Icon(ft.icons.CALCULATE, color = "blue", size = 52)
    ],alignment=ft.MainAxisAlignment.CENTER))

    opcion = ft.Dropdown(label="Seleccion (Si no elige, no hace nada)",options=[
        ft.dropdown.Option("1 Decimal a Binario"),
        ft.dropdown.Option("2 Binario a decimal"),
        ft.dropdown.Option("3 Decimal a Octal"),
        ft.dropdown.Option("4 Octal a decimal"),
        ft.dropdown.Option("5 Decimal a Hexadecimal"),
        ft.dropdown.Option("6 Hexadecimal a Decimal"),
        ft.dropdown.Option("7 Decimal a Cuaternario"),
        ft.dropdown.Option("8 Cuaternario a Decimal"),
        ft.dropdown.Option("9 Decimal a Terciario"),
        ft.dropdown.Option("10 Terciario a Decimal")
        ],width=page.width * 0.95)

    cont2 = ft.Container(ft.Row([opcion]))

    ent = ft.TextField(label="Ingresar numero",hint_text="Ingresar correctos caracteres",width=page.width * 0.95)
    result = ft.TextField(label = "Resultado",disabled= True,width=page.width * 0.95)
    
    cont3 = ft.Container(
        ft.Column([ent,result])
        )
    
    cont4 = ft.Container(ft.Row([
        ft.ElevatedButton("Convertir",ft.icons.TRANSFORM,on_click=cav),
        ft.ElevatedButton("Borrar",ft.icons.DELETE_ROUNDED,on_click=limpiar,color="pink")
    ],alignment=ft.MainAxisAlignment.CENTER,
    spacing=250)
    )

    t1 = Container(ft.Column([cont1,cont2,cont3,cont4],spacing=25),visible=True)

    #Ventana2
    #Funciones
    def aleatorio_matriz (e):
        verificar = tfi.value
        if verificar.isdigit():
            c = int(tfi.value)
            mx = np.zeros((c,c+1))
            mr = np.zeros(c)
            tfr1.value = ""
            num(mx)
            
            aux = len(mx[0]) -1
            aux2 = len(mx[0])
            for i in range (len(mx)):
                for j in range(aux):
                    if j == (aux-1):
                        tfr1.value += str(mx[i][j]) + "x" + "(" + str(j+1) + ")"
                    else:
                        tfr1.value += str(mx[i][j]) + "x" + "(" + str(j+1) + ")" + " + "
                tfr1.value += "= "+ str(mx[i][aux2-1])
                tfr1.value += "\n"
            Gauss_Jordan(mx,mr)
            page.update()
        else:
            tfr2.value = ""
            tfr1.value = ""
            tfr2.value = "Invalido de ingreso"
            page.update()
        
    def borrar (e):
        tfr1.value = ""
        tfr2.value = ""
        tfi.value = ""
        page.update()

    #Componentes
    #Titulo de proyecto
    ti1 = ft.Text("Gauss-Jordan",font_family="New Times Roman",weight=ft.FontWeight.BOLD,size=56)
    contpr = ft.Container(ft.Row([ti1,ft.Icon(ft.icons.CALCULATE, color = "blue", size = 52)],alignment=ft.MainAxisAlignment.CENTER))

    #El Ingreso de digitos y mostrar la matriz, y con su primer contenedor
    tfi = ft.TextField(label = "Ingresar tamaño de matriz",hint_text="Por ejemplo 2, será: '2x2'",bgcolor="white",width=page.width*0.45)
    btnal = ft.ElevatedButton("Aleatorio",on_click=aleatorio_matriz)
    #btnmn = ft.ElevatedButton("Manual",on_click=aleatorio_matriz)
    btnb = ft.IconButton(icon=ft.icons.DELETE_FOREVER_ROUNDED,icon_color="pink600",icon_size=40,tooltip="Borrar",on_click= borrar)
    tfr1 = ft.TextField(multiline=True,min_lines=4,bgcolor="white",disabled=True,width=page.width*0.85)
    
    cont1 = ft.Container(ft.Row([tfi,btnal,btnb],alignment=ft.MainAxisAlignment.CENTER))
    cont11 = ft.Container(ft.Column([tfr1],alignment=ft.MainAxisAlignment.CENTER))
    cont1v = ft.Container(ft.Column([cont1,cont11],spacing=30))

    #Demostrar el resultado y con su segundo contenedor
    subt1 = ft.Text("Resultado",font_family="New Times Roman",weight=ft.FontWeight.BOLD,size=24)
    tfr2 = ft.TextField(multiline=True,min_lines=4,width=page.width*0.85,bgcolor="white",disabled=True)
    cont2 = ft.Container(ft.Column([
        subt1,tfr2
    ],spacing=30))

    t2 = Container(ft.Column([contpr,cont1v,cont2]),visible=False)

    page.add(
        Container(
            margin= margin.only(
                left=20
            ),content=Column([
                t1,
                t2
            ])
        )
    )
    
ft.app(target = main)