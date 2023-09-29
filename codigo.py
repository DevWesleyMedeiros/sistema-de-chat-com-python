import flet as ft


def main(pagina):
    
    nome_usuario = ft.TextField(label="Escreva o seu nome")
    campo_mensagem = ft.TextField(label="Digite uma mensagem")
    botao_enviar_mensagem = ft.ElevatedButton("Enviar")
    
    def entrar_popup(evento):
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.add(campo_mensagem)
        pagina.add(botao_enviar_mensagem)
        pagina.update()
        
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao HashZap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)]
    )
    
    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    texto = ft.Text("HasZap")
    botao_iniciar = ft.ElevatedButton("Começar Chat", on_click=entrar_chat)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main)
