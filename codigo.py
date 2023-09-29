import flet as ft


def main(pagina):
    
    chat = ft.Column()
    
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["Texto"]
            usuario_mensagem = mensagem["Usuário"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} : {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["Usuário"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no site", size=20, italic=True, color=ft.colors.ORANGE_600))
        pagina.update()
        
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"Texto": campo_mensagem.value, "Usuário": nome_usuario.value, "tipo":"mensagem"})
        campo_mensagem.value = ""
        pagina.update()
    
    nome_usuario = ft.TextField(label="Escreva o seu nome")
    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    def entrar_popup(evento):
        pagina.pubsub.send_all({"Usuário": nome_usuario.value, "tipo":"entrada"})
        popup.open = False
        pagina.add(chat)
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
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
    
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
