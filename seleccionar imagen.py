import flet as ft



def main(page: ft.Page):
    page.title="Proyecto Ángela y Nerea"

    dropdown_menu=ft.Dropdown(width=200, options=[ft.dropdown.Option("Madrid"),ft.dropdown.Option("Barcelona"),ft.dropdown.Option("Atletico del Madrid"),ft.dropdown.Option("Atletido de Bilbao"),ft.dropdown.Option("Betis")])
    page.add(dropdown_menu)



ft.app(target=main)