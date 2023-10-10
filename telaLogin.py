import flet as ft
from bancoDados import validarLogin

# Padronização do tamanho dos campos
_with_input = 250
_size_text = 20
_with_button = 250
_height_button = 50

def main(page: ft.Page):
    # Definindo orientação da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Criando coluna e sua orientação
    coluna = ft.Column()
    coluna.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # criando as funções
    def realizarLogin(e):
        if validarLogin(usuario=login.value,senha=senha.value) == True:
            popUp.title = ft.Text(f'Bem-vindo {login.value}!')   
        else:
            popUp.title = ft.Text(f'Credenciais inválidas.')

        login.value = ''
        senha.value = ''

        page.dialog = popUp
        popUp.open = True
        page.update()
    
    def esqueciSenha(e):
        popUp.title = ft.Text('Problema teu, meu nobre')
        page.dialog = popUp
        popUp.open = True
        page.update()


    # Criando campos
    texto = ft.Text(value="Só um teste bóia", text_align= ft.TextAlign.CENTER, size=_size_text)
    login = ft.TextField(label='Insira seu login', width=_with_input,text_align=ft.TextAlign.CENTER,on_submit=realizarLogin)
    senha = ft.TextField(label='Insira sua senha',password=True, width=_with_input,text_align=ft.TextAlign.CENTER,on_submit=realizarLogin)
    botao_login = ft.ElevatedButton('Entrar',on_click=realizarLogin, width=_with_button, height=_height_button)
    esqueci_senha = ft.TextButton('Esqueci minha senha',on_click=esqueciSenha)

    # Criando popup
    popUp = ft.AlertDialog(on_dismiss='')

    # Inserindo os campos na página
    coluna.controls.append(texto)
    coluna.controls.append(login)
    coluna.controls.append(senha)
    coluna.controls.append(esqueci_senha)
    coluna.controls.append(botao_login)
    page.controls.append(coluna)
    
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)