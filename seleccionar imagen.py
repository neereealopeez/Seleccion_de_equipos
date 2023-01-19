import flet as ft


def main(page: ft.Page):
    page.title="Proyecto Ángela y Nerea"

    vEquipos=["Madrid","Barcelona","Atletico de Bilbao","Atletico de Madrid","Betis"]
    vEquiposSeleccionados=[]


    img = ft.Image(src=f"esto no se ve", width=100, height=100)
   
    nombreEquipo = ""

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
   
    

    dropdown_menu=ft.Dropdown(width=200, options=[ft.dropdown.Option("Madrid"),ft.dropdown.Option("Barcelona"),
    ft.dropdown.Option("Atletico del Madrid"),ft.dropdown.Option("Atletico de Bilbao"),
    ft.dropdown.Option("Betis")],on_change=cambiar_imagen)
    
    #dropdown_menu= ft.Dropdown(width=100)

    # for equipo in vEquipos:
        #menu.options.append(ft.dropdown,Option (equipo)
    # )
    page.add(dropdown_menu,img)

   



ft.app(target=main, assets_dir="imagenesEquipos")