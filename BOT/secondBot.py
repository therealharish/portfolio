import logging 

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update 
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__) 

PHOTO, LOCATION, BIO = range(3)

def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("name of user is %s", user.first_name) 
    update.message.reply_text(
        'send me a photo of yourself, ' 
        'so that we can register you, or send /skip if you don\'t want to.',
        reply_markup = ReplyKeyboardRemove(),
    )

    return PHOTO

def photo(update: Update, context: CallbackContext):
    user = update.message.from_user 
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text(
        'perfect. almost complete, Now send me your location, ' 'or send /skip if you don\'t want to.'
    )

    return LOCATION 

def skip_photo(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name) 
    update.message.reply_text(
        'ok no problem! Now, send me your location please, ' 'or send /skip.'
    )

    return LOCATION 

def location(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    ) 
    update.message.reply_text(
        'ok we will take this into consideration'
    )

    return BIO 

def skip_location(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name) 
    update.message.reply_text(
        'ok no problem! ' 'At last tell us if you have any remarks.'
    )

    return BIO 

def bio(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("review by %s: %s", user.first_name, update.message.text) 
    update.message.reply_text(
        'Thank you! we will cal you soon.'
    )

    return ConversationHandler.END 

def cancel(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("User %s canceled the conversation", user.first_name) 
    update.message.reply_text(
        'reach us back if you have any query', reply_markup=ReplyKeyboardRemove
    )

    return ConversationHandler.END 


def main():

    updater = Updater(token="6082192846:AAH5KONXyPhcGRgu0MMQwEdYHu-nShDgaNY")
    dispatcher = updater.dispatcher 

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states = {
            PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            LOCATION: [
                MessageHandler(Filters.location, location),
                CommandHandler('skip', skip_location),
            ],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        fallbacks = [CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    updater.start_polling() 

    updater.idle() 

main()