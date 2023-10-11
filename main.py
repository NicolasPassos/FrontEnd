import flet as ft
from webMenu import *
from portalMenu import *

def main(page: ft.Page):
    # Definindo orientação da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(webMenu)
    
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, port=8000, assets_dir='assets')