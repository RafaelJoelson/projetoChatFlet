import flet as ft

def main(pagina):  # Recebe a página principal da aplicação
    # Título da aplicação
    titulo = ft.Text("Hashzap")  # Tipo de componente: texto

    # Campo de texto para inserir o nome do usuário
    nome_usuario = ft.TextField(label="Escreva seu nome")  # Tipo de componente: campo de texto

    # Coluna para exibir o chat
    chat = ft.Column()

    # Função para receber mensagens do "túnel"
    def receber_mensagem_tunel(informacoes):
        print(informacoes, "recebido no túnel")
        # Adiciona a mensagem ao chat
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    # Subscreve a função ao "túnel" para receber mensagens
    pagina.pubsub.subscribe(receber_mensagem_tunel)

    # Função para enviar uma mensagem quando o campo de mensagem é submetido
    def enviar_mensagem(evento):
        # Formata a mensagem com o nome do usuário
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"

        # Envia a mensagem para o "túnel"
        pagina.pubsub.send_all(texto_campo_mensagem)     
        
        # Limpa o campo de mensagem
        campo_mensagem.value = ""
        
        # Atualiza a página para refletir as mudanças
        pagina.update()

    # Campo de texto para escrever mensagens
    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    
    # Botão para enviar mensagens
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # Função para entrar no chat
    def entrar_chat(evento):
        # Fecha o popup de boas-vindas
        popup.open = False
        
        # Remove o botão "Iniciar chat" da tela
        pagina.remove(botao_iniciar)
        
        # Adiciona o componente de chat à página
        pagina.add(chat)
        
        # Adiciona a linha com o campo de mensagem e o botão de enviar
        linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
        pagina.add(linha_mensagem)
        
        # Mensagem indicando que o usuário entrou no chat
        aviso_entrou_no_chat = f"{nome_usuario.value} entrou no chat."
        pagina.pubsub.send_all(aviso_entrou_no_chat)
        # Atualiza a página
        pagina.update()

    # Diálogo de boas-vindas com o botão "Entrar" que chama a função entrar_chat
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem-vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]  # Botão "Entrar"
    )

    # Função para iniciar o chat
    def iniciar_chat(evento):
        # Exibe o diálogo de boas-vindas quando o botão "Iniciar chat" é clicado
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # Botão para iniciar o chat
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)  # Botão "Iniciar chat"

    # Adiciona os componentes à página principal
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# Inicia a aplicação usando a função 'main'
ft.app(main, view=ft.WEB_BROWSER)
#ft.app(main)