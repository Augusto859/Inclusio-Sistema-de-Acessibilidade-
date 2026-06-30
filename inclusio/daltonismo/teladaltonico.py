import tkinter as tk
from PIL import Image, ImageTk
import enviaremail
from tkinter import messagebox

def selecionar(radio_var, janela_principal, teladaltonico):
    selecionado = radio_var.get()
    
    setores = {
        1: "secretário",
        2: "secretário",  
        3: "Recepcionista",
        4: "Cantina",
        5: "Coordenação",
        6: "Coordenador"
    }
    
    if selecionado in setores:
        destinatario = "pedroaugustosale@gmail.com"
        assunto = "Suporte ao daltônico"
        mensagem = f"Atenção {setores[selecionado]}, você receberá uma pessoa daltônica, preste o suporte necessário."
        
        # Envia o e-mail
        enviaremail.enviar_email(assunto, destinatario, mensagem)
        
        # MODIFICAÇÃO AQUI: Em vez de fechar a tela, apenas avisamos que deu certo
        messagebox.showinfo("Sucesso", "Aguarde a chegada do auxiliar.")
        
    else:
        messagebox.showwarning("Aviso", "Selecione uma opção válida")

def visivel(janela_principal):
    tela_daltonico = tk.Toplevel()
    tela_daltonico.title("Auxílio ao Daltônico")
    tela_daltonico.geometry("1920x1080")

    # Carregando a imagem de fundo
    imagem2_bg = Image.open(r"D:\Users\Aluno\Documents\uc3\inclusio\daltonismo\tela-daltonico.png")
    imagem2_bg = imagem2_bg.resize((1920, 1080))
    imagem2_tk = ImageTk.PhotoImage(imagem2_bg)
    
    label2_imagem = tk.Label(tela_daltonico, image=imagem2_tk)
    label2_imagem.place(x=0, y=0)
    # Linha crucial: guarda a referência da imagem para o Tkinter não apagá-la da memória
    label2_imagem.image = imagem2_tk 

    radio_var = tk.IntVar()
    radio_var.set(1)

    # Criação dos Radiobuttons
    radio1 = tk.Radiobutton(tela_daltonico, text="Secretaria", variable=radio_var, value=1, font=("Arial", 30))
    radio1.place(x=100, y=250)
    radio2 = tk.Radiobutton(tela_daltonico, text="Biblioteca", variable=radio_var, value=2, font=("Arial", 30))
    radio2.place(x=100, y=350)
    radio3 = tk.Radiobutton(tela_daltonico, text="Auditório", variable=radio_var, value=3, font=("Arial", 30))
    radio3.place(x=100, y=450)
    radio4 = tk.Radiobutton(tela_daltonico, text="Cantina", variable=radio_var, value=4, font=("Arial", 30))
    radio4.place(x=100, y=550)
    radio5 = tk.Radiobutton(tela_daltonico, text="Coordenação", variable=radio_var, value=5, font=("Arial", 30))
    radio5.place(x=100, y=650)
    radio6 = tk.Radiobutton(tela_daltonico, text="Curso", variable=radio_var, value=6, font=("Arial", 30))
    radio6.place(x=100, y=750)

    # CORREÇÃO: Uso do lambda e ajuste na ordem dos argumentos (radio_var, janela_principal, tela_daltonico)
    botao_enviar = tk.Button(
        tela_daltonico, 
        text="Enviar", 
        font=("Arial", 25, "bold"), 
        command=lambda: selecionar(radio_var, janela_principal, tela_daltonico)
    )
    botao_enviar.place(x=100, y=850)
    
    def voltar():
        janela_principal.deiconify()      
        tela_daltonico.destroy()
        
    # CORREÇÃO: Mudança no x de 100 para 300 para não sobrepor o botão de enviar
    botao_voltar = tk.Button(tela_daltonico, text="Voltar", font=("Arial", 30, "bold"), bg="white", fg="darkred", command=voltar)
    botao_voltar.place(x=300, y=850)
    
    tela_daltonico.mainloop()
    
