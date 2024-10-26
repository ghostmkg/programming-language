from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. How can I assist you today?')

# Function to handle text messages
def echo(update: Update, context: CallbackContext) -> None:
    # Echo the user's message
    update.message.reply_text(update.message.text)

# Main function to set up the bot
def main():
    # Replace 'YOUR_TOKEN' with the token you received from BotFather
    token = 'YOUR_TOKEN'
    
    # Create the Updater and pass it the bot's token
    updater = Updater(token)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler('start', start))

    # Register a message handler to echo all text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
