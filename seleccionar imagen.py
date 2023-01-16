import flet as ft



def main(page: ft.Page):
    page.title="Proyecto Ángela y Nerea"
   
   
    nombreEquipo = ""

    def dropdown_changed(e):
        if (dropdown_menu.value == "Madrid"):
            nombreEquipo= "imagenesEquipos/madrid.jpg"
        elif (dropdown_menu.value == "Barcelona"):
            nombreEquipo = "imagenesEquipos/barcelona.jpg"
        elif (dropdown_menu.value == "Betis"):
            nombreEquipo = "imagenesEquipos/betis.jpg" 
        elif (dropdown_menu.value == "Atletico de Bilbao"):
            nombreEquipo = "imagenesEquipos/atleticodebilbao.jpg"   
        else:
            nombreEquipo = "imagenesEquipos/atleticodemadrid.jpg"

           

 
   
    img.src=f"{nombreEquipo}"
    img = ft.Image(src=f"atleticodebilbao.jpg", width=100, height=100)
    img2 = ft.Image(src=f"atleticodemadrid.jpg", width=100, height=100)
    img3 = ft.Image(src=f"betis.jpg", width=100, height=100)
    img4 = ft.Image(src=f"mardrid.jpg", width=100, height=100)
    img5 = ft.Image(src=f"barcelona.jpg", width=100, height=100)

    dropdown_menu=ft.Dropdown(width=200, options=[ft.dropdown.Option("Madrid"),ft.dropdown.Option("Barcelona"),
    ft.dropdown.Option("Atletico del Madrid"),ft.dropdown.Option("Atletico de Bilbao"),
    ft.dropdown.Option("Betis")],on_change=dropdown_changed)
    
    page.add(dropdown_menu)

    page.add(img, img2, img3, img4, img5)



ft.app(target=main, assets_dir="imagenesEquipos")