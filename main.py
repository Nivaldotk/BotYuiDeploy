import telebot

CHAVE_API = "1980584583:AAEL6-Psse_gwUZqEp3t1I_VsF_3zgG_84g"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['animes'])
def animes(mensagem):
    bot.send_message(mensagem.chat.id, "Os animes do qual eu mais gosto são Berserk, Sankarea e D-gray man e você?")

@bot.message_handler(commands=['jogos'])
def jogos(mensagem):
    bot.send_message(mensagem.chat.id, "Meu jogo favorito é Resident Evil, e adoro jogar YU GI OH, qual jogos vc gosta de jogar?")

@bot.message_handler(commands=['sobreVida'])
def sobreVida(mensagem):
    bot.send_message(mensagem.chat.id, "Ainda não tenho uma vida completa mas logo terei ;--;")

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = """Sobre o que você deseja conversar(clique em uma opção?
    /animes Animes
    /jogos Jogos
    /sobreVida SobreVida"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Desculpa ainda não tenho autonomia para interpretar uma frase sozinha, mas muito obrigada, pela gentileza ela esta salva no meu banco de dados")

@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Muito obrigado! Junior mandou um abraço de volta!")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """Olá eu sou a Yui, no que posso te ajudar?
    /opcao1 Conversar comigo
    /opcao2 Me mandar alguma frase
    /opcao3 Mandar um abraço para o Junior
 Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem,texto)

bot.polling()