import smtplib
from email.message import EmailMessage


def enviar_email(assunto, destinatario, mensagem):
    meu_email = "pedroaugustosale@gmail.com"
    email_destinatario = destinatario
    senha = "olod iipi tgdx mtec"
    smtp = "smtp.gmail.com"
    mensagem_email = mensagem
    assunto_email = assunto
    
    msg = EmailMessage()
    msg["Subject"] = assunto
    msg["From"] = meu_email
    msg["To"] = email_destinatario
    msg.set_content(mensagem_email)
    
    
    server = smtplib.SMTP(smtp,587) # ativar servidor
    server.starttls() # iniciar servidor
    server.login(meu_email,senha)  
    server.send_message(msg)
    server.quit() # encerrar servidor