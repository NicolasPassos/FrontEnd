import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    coluna = ft.Column()
    coluna.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    texto = ft.Text(value="Só um teste bóia", text_align= ft.TextAlign.CENTER)
    login = ft.TextField(label='Insira seu login', width=200,text_align=ft.TextAlign.CENTER)
    senha = ft.TextField(label='Insira sua senha',password=True, width=200,text_align=ft.TextAlign.CENTER)

    resposta = ft.AlertDialog(title=ft.Text('Login realizado com sucesso!'),content=texto,on_dismiss='')
    
    def fecharPopUp(e):
        resposta.open = False
        page.update()

    def botaoLogin(e):
        page.dialog = resposta
        resposta.open = True
        page.update()
    botao = ft.ElevatedButton('Clique aqui',on_click=botaoLogin)
    
    

    coluna.controls.append(texto)
    coluna.controls.append(login)
    coluna.controls.append(senha)
    coluna.controls.append(botao)
    page.controls.append(coluna)
    
    page.update()

    

    

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)