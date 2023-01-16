import flet as ft



def main(page: ft.Page):
    page.title="Proyecto Ángela y Nerea"
    img = ft.Image(src=f"atleticodebilbao.jpg", width=100, height=100)
    img2 = ft.Image(src=f"atleticodemadrid.jpg", width=100, height=100)
    img3 = ft.Image(src=f"betis.jpg", width=100, height=100)
    img4 = ft.Image(src=f"mardrid.jpg", width=100, height=100)
    img5 = ft.Image(src=f"barcelona.jpg", width=100, height=100)


    page.add(img, img2, img3, img4, img5)



ft.app(target=main, assets_dir="imagenesEquipos")