import telebot
from decouple import config
import time

token = config("TOKEN_BOT") 
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start','iniciar']) 
def start(message):
    bot.send_message(message.chat.id, "Olá! Somos da empresa La Lully. Tudo bem com você?", timeout=120)
    time.sleep(3)

@bot.message_handler(regexp='iniciar')
def iniciar(message):
    bot.send_message(message.chat.id, "Olá! Somos da empresa La Lully. Tudo bem com você?", timeout=120)
    time.sleep(3)

@bot.message_handler(regexp=r'tudo|td|sim|belez|claro|tranquilo|Tudo|Sim|claro|certo')
def pergunta_suporte(message):
    bot.send_message(message.chat.id, "Ótimo! Aqui tudo certo!", timeout=120)
    time.sleep(3)
    bot.send_message(message.chat.id, "Como podemos te ajudar hoje? ", timeout=120)
    bot.send_message(message.chat.id, "Por favor, digite uma das palavras: 'atendimento' ou 'financeiro' que vamos te atender da melhor forma.", timeout=120)

@bot.message_handler(regexp=r'atendimento|Atendimento')
def duvida_suporte(message):
    bot.send_message(message.chat.id, "Estamos aqui para ajudar você. 😊", timeout=120)
    time.sleep(2)
    bot.send_message(message.chat.id, "Se você deseja agendar um horário, clique aqui: [https://lalully.com/agendamento]", timeout=120)    
    time.sleep(2)
    bot.send_message(message.chat.id, "Para compras de produtos, visite nossa loja: [https://lalully.com/compras]", timeout=120)
    time.sleep(2)
    bot.send_message(message.chat.id, "Falar com uma atendente, acesse:[https://lalully.com/atendimento]", timeout=120)
    time.sleep(2)
    bot.send_message(message.chat.id, "Se não precisar de mais assistência, digite 'encerrar' para encerrar o atendimento.", timeout=120)

@bot.message_handler(regexp=r'financeiro')
def financeiros_suporte(message):
    bot.send_message(message.chat.id, "Para emitir um novo boleto acesse: [https://lalully.com/meuboleto]", timeout=120)
    time.sleep(2)
    bot.send_message(message.chat.id, "Erro na emissão do boleto, acesse:[https://lalully.com/duvidas-financeiro]", timeout=120)
    time.sleep(2)
    bot.send_message(message.chat.id, "Falar com um atendente, acesse:[https://lalulyy.com/atendimento]", timeout=120)
    time.sleep(2)
    bot.send_message(message.chat.id, "Se não precisar de mais assistência, digite 'encerrar' para encerrar o atendimento.", timeout=120)
    

@bot.message_handler(regexp=r'encerrar')
def encerrar_atendimento(message):
    bot.send_message(message.chat.id, "Obrigada por entrar em contato conosco! Se precisar estaremos por aqui.", timeout=120)
    bot.send_message(message.chat.id, "Tenha um ótimo dia!", timeout=120)
    bot.send_photo(message.chat.id, open('goodbye.jpg', 'rb'), timeout=120)

bot.polling() # fica escutando o tempo todo