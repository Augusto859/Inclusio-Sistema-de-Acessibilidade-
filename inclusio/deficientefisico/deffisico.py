
from PIL import Image, ImageTk
import enviaremail
from tkinter import messagebox
import tkinter as tk

# Seleção de opções - Adicionado o parâmetro janela_principal para não dar erro
def selecionar(validar_checkbox1, validar_checkbox2, validar_checkbox3, validar_checkbox4, janela_principal):
    selecionar_opcoes = []
    
    if validar_checkbox1.get():
        selecionar_opcoes.append("Cadeira de rodas")
    if validar_checkbox2.get():
        selecionar_opcoes.append("Andador")
    if validar_checkbox3.get():
        selecionar_opcoes.append("Muleta")
    if validar_checkbox4.get():
        selecionar_opcoes.append("Assistente")
        
    # Transforma a lista em texto legível separado por vírgula
    itens_pedidos = ", ".join(selecionar_opcoes) if selecionar_opcoes else "Nenhum item selecionado"

    destinatario = "pedroaugustosale@gmail.com"
    assunto = "Suporte ao deficiente físico"
    # Corrigido aqui: mudou de {selecionar} para {itens_pedidos}
    mensagem = f"Estamos precisando dos seguintes itens para o deficiente físico: {itens_pedidos}" 
    
    enviaremail.enviar_email(assunto, destinatario, mensagem)
    
    # Corrigido: messagebox.showinfo precisa de Título e Mensagem
    messagebox.showinfo("Sucesso", "Aguarde! Em breve um auxiliar virá com os itens necessários.")
    
    # Se quiser fechar a tela atual e voltar para a principal após solicitar:
    # tela_def_fisico.destroy()
    # janela_principal.deiconify()
    
    
def visivel(janela_principal):
    global imagem_bg, imagem_tk, label_imagem, botao_solicitar, img_botao_solicitar, img_botao_solicitar_redimensionado
    
    tela_def_fisico = tk.Toplevel()
    tela_def_fisico.title("Auxílio ao deficiente físico")
    tela_def_fisico.geometry("1920x1080")

    # Plano de fundo
    imagem_bg = Image.open(r"D:\Users\Aluno\Documents\uc3\inclusio\deficientefisico\deficientefisico-acessorios.png")
    imagem_bg = imagem_bg.resize((1920, 1080))
    imagem_tk = ImageTk.PhotoImage(imagem_bg)
    label_imagem = tk.Label(tela_def_fisico, image=imagem_tk)
    label_imagem.place(x=0, y=0)

    # Checkboxes
    validar_checkbox1 = tk.BooleanVar()
    validar_checkbox2 = tk.BooleanVar()
    validar_checkbox3 = tk.BooleanVar()
    validar_checkbox4 = tk.BooleanVar()

    checkbox1 = tk.Checkbutton(tela_def_fisico, text="Cadeira de rodas", font=("Arial", 30, "bold"), fg="black", variable=validar_checkbox1, bg="#DEDA11")
    checkbox1.place(x=100, y=250)
    checkbox2 = tk.Checkbutton(tela_def_fisico, text="Andador", font=("Arial", 30, "bold"), fg="black", variable=validar_checkbox2, bg="#DEDA11")
    checkbox2.place(x=100, y=350)
    checkbox3 = tk.Checkbutton(tela_def_fisico, text="Muleta", font=("Arial", 30, "bold"), fg="black", variable=validar_checkbox3, bg="#DEDA11")
    checkbox3.place(x=100, y=450)
    checkbox4 = tk.Checkbutton(tela_def_fisico, text="Assistente", font=("Arial", 30, "bold"), fg="black", variable=validar_checkbox4, bg="#DEDA11")
    checkbox4.place(x=100, y=550)

    # Carrega e redimensiona a imagem do botão (ajuste os valores 416, 84 se necessário)
    img_carregada = Image.open(r"D:\Users\Aluno\Documents\uc3\inclusio\deficientefisico\botao-solicitar.png")
    img_botao_solicitar_redimensionado = img_carregada.resize((416, 84)) 
    img_botao_solicitar = ImageTk.PhotoImage(img_botao_solicitar_redimensionado)
    
    # Criando o botão já com a imagem aplicada e comandos certos
    botao_solicitar = tk.Button(
        tela_def_fisico, 
        image=img_botao_solicitar, 
        borderwidth=0, 
        highlightthickness=0, 
        bg="#030727", # Altere para a cor de fundo do seu design se não for esse azul escuro
        command=lambda: selecionar(validar_checkbox1, validar_checkbox2, validar_checkbox3, validar_checkbox4, janela_principal)
    )
    
    # Garante que o Python não limpe a imagem da memória
    botao_solicitar.image = img_botao_solicitar
    botao_solicitar.place(x=100, y=750)
    
    def voltar():
        janela_principal.deiconify()       
        tela_def_fisico.destroy()
        
    
            
    botao_voltar = tk.Button(tela_def_fisico, text="Voltar", font=("Arial", 30, "bold"), bg="white", fg="darkred", command=voltar)
    botao_voltar.place(x = 100, y = 850)
    
    

