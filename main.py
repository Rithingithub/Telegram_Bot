from logging import Filter
import Constants as keys
from telegram.ext import Filters, Updater, CommandHandler, MessageHandler
import Responses as R
import telepot
import urllib.request, json
from telegram import MessageEntity
import datetime




print("started!!")

bot = telepot.Bot('5527692918:AAHzJ3eWIFO5jEsXv-DWIoP3ohwpx_1UZZo')


endpoint_link = "https://www.youtube.com/"

def fetchjson(url):
    resp = urllib.request.urlopen(url)
    return json.loads(resp.read().decode())


def download(update, context):
    # update.message.reply_text("Working .....")
    x = update.message.parse_entities(types = MessageEntity.URL)
    for i in x:
        msg = update.message.reply_text("working....")
        rjson = fetchjson(endpoint_link + x[i])
        if "error" in json:
            msg.edit_text("Invalid!")
        
    update.message.reply_text("I cant fetch from that url")





def start_command(update, context):
    update.message.reply_text('Type something !')


def dt_command(update, context):
    dt = datetime.datetime.today()
    update.message.reply_text(dt)


def help_command(update, context):
    #update.message.reply_text('google it  !')
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="How can i help you Mr.{yourname} ?".format(yourname=update.effective_user.full_name))


# def add_command(update, context):
#     # update.message.reply_text(a = int(input('Enter num')))
#     # update.message.reply_text(a)



def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.resp(text)  

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} coused error {context.error}")




def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    #dp.add_handler(CommandHandler("add", add_command))
    dp.add_handler(CommandHandler("date", dt_command))


    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_handler(MessageHandler(Filters.entity(MessageEntity.URL), download))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()

