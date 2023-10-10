import flet as ft
from database.bancoDados import validarLogin

# Padronização do tamanho dos campos
_width_input = 350
_size_text = 20
_width_button= 350
_height_button = 50

def main(page: ft.Page):
    # Definindo orientação da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Criando coluna e sua orientação
    coluna = ft.Column()
    coluna.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    coluna_pop_pup = ft.Column()
    coluna_pop_pup.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    coluna_pop_pup.height = 150

    # criando as funções
    def realizarLogin(e):
        popUp.content = None
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
        popUp.content = None
        coluna_pop_pup.controls.clear()
        popUp.title = ft.Text('Problema teu, meu nobre')
        popUp.content = coluna_pop_pup
        email_recuperacao = ft.TextField(label='E-mail de recuperação',width=_width_input)
        botao_enviar = ft.ElevatedButton('Enviar',on_click=enviarEmailRecuperacao)
        texto_email_recuperacao = ft.Text('''Para recuperar a sua senha, informe seu endereço de email
que nós enviaremos um link para a alteração da senha.''',text_align=ft.TextAlign.CENTER)
        coluna_pop_pup.controls.append(texto_email_recuperacao)
        coluna_pop_pup.controls.append(email_recuperacao)
        coluna_pop_pup.controls.append(botao_enviar)
        page.dialog = popUp
        popUp.open = True
        page.update()
    
    def enviarEmailRecuperacao(e):
        coluna_pop_pup.controls.append(ft.Text('E-mail de recuperação enviado com sucesso!'))
        page.update()


    # Criando campos
    texto = ft.Text(value="Só um teste bóia", text_align= ft.TextAlign.CENTER, size=_size_text,selectable=True)
    login = ft.TextField(label='Insira seu login', width=_width_input,text_align=ft.TextAlign.CENTER,on_submit=realizarLogin)
    senha = ft.TextField(label='Insira sua senha',password=True, width=_width_input,text_align=ft.TextAlign.CENTER,on_submit=realizarLogin)
    botao_login = ft.ElevatedButton('Entrar',on_click=realizarLogin, width=_width_button, height=_height_button)
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