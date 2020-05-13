from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import logging
import json
import requests

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

with open('config.json') as config_file:
    config = json.load(config_file)


def message_handler(bot, update):
    message = update.message.text
    if message[0] == '/':
        return
    print('User {} type in: {}'.format(update.message.from_user.first_name, message))
    update.message.reply_markdown(result)


def get_count(bot, update):
    url = "https://swimpool.nctu.edu.tw/NCTUGym/index.php/crowd/GetGymCrowd"
    r = requests.get(url)
    data = json.loads(r.text)
    result = "游泳館健身房人數: {},\n最後更新時間: {}".format(data['crowd'], data['time'])
    if int(data['crowd']) >= 45:
        url = 'https://swimpool.nctu.edu.tw/NCTUGym/index.php/crowd/GetGymLineCrowd'
        r = requests.get(url)
        data = json.loads(r.text)
        result += "\n  排隊人數： {},\n  最後更新時間: {}".format(data['crowd'], data['time'])
    print(result)
    update.message.reply_markdown(result)


updater = Updater(config['bot_token'])
updater.dispatcher.add_handler(CommandHandler('howmuch', get_count))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

updater.start_polling()
print('bot started')
updater.idle()
