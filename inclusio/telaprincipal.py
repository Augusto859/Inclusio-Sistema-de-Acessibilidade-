import tkinter as tk
from PIL import Image, ImageTk
from deficientefisico import deffisico
from tkinter import messagebox
from email.message import EmailMessage
from daltonismo import teladaltonico
import enviaremail


def ir_para_tela_deffisico():
    tela_principal.withdraw() # Oculta a tela principal
    
    # Chama a função 'visivel' que está dentro do arquivo 'deffisico'
    # Passando 'tela_principal' para que a segunda tela saiba quem a chamou
    deffisico.visivel(tela_principal)
    
def ir_para_tela_daltonico():
    tela_principal.withdraw()
    teladaltonico.visivel(tela_principal) 

def def_auditivo():
    destinatario = "pedroaugustosale@gmail.com"
    assunto = "Suporte ao deficiente auditivo!"
    mensagem = "Atenção! Acaba de chegar um deficiente auditivo."
    enviaremail.enviar_email(assunto, destinatario, mensagem)
    messagebox.showinfo("Aviso", "Aguarde estaremos enviando um intérprete para auxílio.")
    
def def_visual():
    destinatario = "pedroaugustosale@gmail.com"
    assunto = "Suporte ao deficiente visual!"
    mensagem = "Atenção! Acaba de chegar um deficiente visual."
    enviaremail.enviar_email(assunto, destinatario, mensagem)
    messagebox.showinfo("Aviso", "Aguarde, estaremos enviando um aconpanhante para auxílio.")
 
    
tela_principal = tk.Tk()
tela_principal.title("Inclusio - Sistema de Acessibilidade")
tela_principal.geometry("1920x1080")

# Imagem de fundo
imagem3_bg = Image.open(r"D:\Users\Aluno\Documents\uc3\inclusio\bg-inclusio.png")
#imagem3_bg_redimensionado = imagem3_bg.resize((1920, 1080))
#imagem3_bg_tk = ImageTk.PhotoImage(imagem3_bg_redimensionado)

#label3_bg = tk.Label(tela_principal, image=imagem3_bg_tk)
#label3_bg.place(x=0, y=0)
imagem3_bg = imagem3_bg.resize((1920,1080))
imagem3_tk = ImageTk.PhotoImage(imagem3_bg)
label3_imagem = tk.Label(tela_principal, image=imagem3_tk)
label3_imagem.place(x=0,y=0)
# --- Botões ---


img_botao1 = Image.open("D:/Users/Aluno/Documents/uc3/inclusio/Button-Primary1.png")
img_botao1_redimensionado = img_botao1.resize((416, 84))
img_botao1 = ImageTk.PhotoImage(img_botao1_redimensionado)
img_def1 = tk.Button(tela_principal, image=img_botao1, borderwidth=0, highlightthickness=0, bg="#030727", command=ir_para_tela_deffisico)
img_def1.place(x=751, y=338)


img_botao2 = Image.open("D:/Users/Aluno/Documents/uc3/inclusio/Button-Primary2.png")
img_botao2_redimensionado = img_botao2.resize((416, 84))
img_botao2 = ImageTk.PhotoImage(img_botao2_redimensionado)
img_def2 = tk.Button(tela_principal, image=img_botao2, borderwidth=0, highlightthickness=0, bg="#030727", command=def_visual)
img_def2.place(x=751, y=493)


img_botao3 = Image.open("D:/Users/Aluno/Documents/uc3/inclusio/Button-Primary3.png")
img_botao3_redimensionado = img_botao3.resize((416, 84))
img_botao3 = ImageTk.PhotoImage(img_botao3_redimensionado)
img_def3 = tk.Button(tela_principal, image=img_botao3, borderwidth=0, highlightthickness=0, bg="#030727",command=def_auditivo)
img_def3.place(x=753, y=648)


img_botao4 = Image.open("D:/Users/Aluno/Documents/uc3/inclusio/Button-Primary4.png")
img_botao4_redimensionado = img_botao4.resize((416, 84))
img_botao4 = ImageTk.PhotoImage(img_botao4_redimensionado)
img_def4 = tk.Button(tela_principal, image=img_botao4, borderwidth=0, highlightthickness=0, bg="#030727", command=ir_para_tela_daltonico)
img_def4.place(x=753, y=803)

tela_principal.mainloop()