from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import requests

openai.api_key = "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"
here_api_key = "blD1GxYTnHOe8DV6IhaSopTnDn0ayqJ4QbyDw3n9XtM"


def generate_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": message},
            ]
    )
    return response['choices'][0]['message']['content']
    
def handle_message(update, context):
    message = update.message.text
    print(update.message.location)
    if message.lower() == "/start":
        update.message.reply_text("Welcome! Please send in your address to know your location for booking.")
    else:
        # use the OpenAI API to generate a response based on the message
        response = generate_response(message)
        update.message.reply_text(response)
        # get the location details from the address sent by the user
        location = get_location_details(message)
        if location:
            # send the location details back to the user
            update.message.reply_text(f"Your location is: {location['lat']}, {location['lng']}. Is this correct?")
            location = None
        else:
            update.message.reply_text("Sorry, I could not find your location. Please try again with a different address.")

        
def get_location_details(address):
    url = f"https://geocode.search.hereapi.com/v1/geocode?q={address}&apiKey={here_api_key}"
    response = requests.get(url).json()
    if response["items"]:
        location = response["items"][0]["position"]
        return {"lat": location["lat"], "lng": location["lng"]}
    else:
        return None

# create an updater object and attach the message handler
updater = Updater(token="6082192846:AAH5KONXyPhcGRgu0MMQwEdYHu-nShDgaNY", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# start the bot
updater.start_polling()
