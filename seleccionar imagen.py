import flet as ft



def main(page: ft.Page):
    page.title="Proyecto Ángela y Nerea"
    img = ft.Image(src=f"atleticodebilbao.jpg", width=100, height=100)

    dropdown_menu=ft.Dropdown(width=200, options=[ft.dropdown.Option("Madrid"),ft.dropdown.Option("Barcelona"),ft.dropdown.Option("Atletico del Madrid"),ft.dropdown.Option("Atletido de Bilbao"),ft.dropdown.Option("Betis")])
    page.add(dropdown_menu)

    page.add(img)



ft.app(target=main, assets_dir="imagenesEquipos")