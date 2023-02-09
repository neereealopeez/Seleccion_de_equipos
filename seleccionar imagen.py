import flet as ft


def main(page: ft.Page):
    page.title="Proyecto Ángela y Nerea"
    vEquiposSeleccionados=[]
    img = ft.Image(src=f"esto no se ve", width=100, height=100)
    vEquipos = []
    lv = ft.ListView(expand=False, spacing=10, auto_scroll=True)
    

    

#Funciones del programa

    def cargarEquipos():
        vEquipos=[]
        f = open("equipos.txt", "r")

        for linea in f:
            vEquipos.append(linea)

        f.close()
        return vEquipos

        #Guardar todos los equipos seleccionados en un archivo

    def guardarEquipo(e):
        f = open('seleccionados.txt', 'w')
        for equipo in vEquiposSeleccionados:
            f.write(equipo)
        f.close()


    def cambiar_imagen(e):
        if (dropdown_menu.value == "Madrid\n"):
            img.src = "madrid.jpg"
        elif (dropdown_menu.value == "Barcelona\n"):
            img.src = "barcelona.jpg"
        elif (dropdown_menu.value == "Betis\n"):
            img.src = "betis.jpg" 
        elif (dropdown_menu.value == "Atletico de Bilbao\n"):
            img.src = "atleticodebilbao.jpg"   
        elif(dropdown_menu.value == "Atletico de Madrid\n"):
            img.src = "atleticodemadrid.jpg"
        else:
            img.src = "imagenno.jpg"

           
    
        page.update()
   


    def añadirEquipo(e):
        equipo=dropdown_menu.value
        if(vEquiposSeleccionados.count(equipo)==0):
            vEquiposSeleccionados.append(dropdown_menu.value)
            row=ft.Row(controls=[ft.Image(src=img.src ,width=50,height=50),ft.Text(equipo)])
            lv.controls.append(row)
           
        else:
            dlg= ft.AlertDialog(title=ft.Text(f"El equipo {equipo} ya está dentro de la lista"))
            page.dialog = dlg
            dlg.open = True
    
        page.update()


#Fin funciones del programa


   
#Inicio programa Principal

    vEquipos=cargarEquipos()
    
    dropdown_menu= ft.Dropdown(width=205, on_change=cambiar_imagen, hint_text="Selecciona un equipo")
   

    
    for equipo in vEquipos:
        dropdown_menu.options.append(ft.dropdown.Option (equipo))
    page.add(dropdown_menu,img)

   
    botonAñadir =ft.ElevatedButton(text="Añadir equipo", on_click=añadirEquipo)
    page.add(botonAñadir,lv)

    botonGuardar =ft.ElevatedButton(text="Guardar equipo en el archivo", on_click=guardarEquipo)
    page.add(botonGuardar,lv)

ft.app(target=main, assets_dir="imagenesEquipos")