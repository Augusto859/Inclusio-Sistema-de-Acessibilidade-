import enviaremail

destinatario = input("Digite seu destinatário: ")
assunto = input("Digite seu assunto: ")
mesnagem = input("Digite sua mensagem: ")
enviaremail.enviar_email(assunto, destinatario, mesnagem)