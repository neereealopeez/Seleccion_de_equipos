import flet as ft


def main(page: ft.Page):
    page.title="Proyecto Ángela y Nerea"

    vEquipos=["Madrid","Barcelona","Atletico de Bilbao","Atletico de Madrid","Betis"]
    vEquiposSeleccionados=[]

    img = ft.Image(src=f"esto no se ve", width=100, height=100)
   
    nombreEquipo = ""


    lv = ft.ListView(expand=True, spacing=20, auto_scroll=True)

    def cambiar_imagen(e):
        if (dropdown_menu.value == "Madrid"):
            img.src = "madrid.jpg"
        elif (dropdown_menu.value == "Barcelona"):
            img.src = "barcelona.jpg"
        elif (dropdown_menu.value == "Betis"):
            img.src = "betis.jpg" 
        elif (dropdown_menu.value == "Atletico de Bilbao"):
            img.src = "atleticodebilbao.jpg"   
        else:
            img.src = "atleticodemadrid.jpg"
           
    
        page.update()
   
    def guardarEquipo(e):
        equipo=dropdown_menu.value
        if(vEquiposSeleccionados.count(equipo)==0):
            vEquiposSeleccionados.append(dropdown_menu.value)
            lv.controls.append(ft.Text(equipo))
            lv.controls.append(ft.Image(src="betis.jpg"))
        else:
            dlg= ft.AlertDialog(title=ft.Text(f"El equipo {equipo} ya está dentro de la lista"))
            page.dialog = dlg
            dlg.open = True
    
        page.update()
        

       
    dropdown_menu= ft.Dropdown(width=205, on_change=cambiar_imagen, hint_text="Selecciona un equipo")



    
    for equipo in vEquipos:
        dropdown_menu.options.append(ft.dropdown.Option (equipo))
    page.add(dropdown_menu,img)

   
    botonAñadir =ft.ElevatedButton(text="Añadir equipo", on_click=guardarEquipo)
    page.add(botonAñadir,lv)

ft.app(target=main, assets_dir="imagenesEquipos")