import flet as ft



def main(page: ft.Page):
    page.title="Proyecto Ángela y Nerea"
    img = ft.Image(src=f"atleticodebilbao.jpg", width=100, height=100)


    page.add(img)



ft.app(target=main, assets_dir="imagenesEquipos")