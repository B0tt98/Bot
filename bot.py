import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

# Your bot token
BOT_TOKEN = "7542010899:AAESLyBa0VFfSeNmo2jycGDwuSzaWHF1KRw"
API_URL = "https://evobuscas.squareweb.app/leak.php"

# Function to handle the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! Send a website to search for leaked login details using /search <website>.')

# Function to handle the /search command
async def search(update: Update, context: CallbackContext):
    website = ' '.join(context.args)
    
    if not website:
        await update.message.reply_text('Please provide a website to search.')
        return

    try:
        # Make a request to your API with the provided website
        response = requests.get(f"{API_URL}?busca={website}&token=yoda")
        data = response.text

        if response.status_code == 200 and data:
            # Send the response data back to the user
            await update.message.reply_text(f"Search results for {website}:\n{data}")
        else:
            await update.message.reply_text('No data found for this website.')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

# Main function to start the bot
async def main():
    # Create the application instance
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("search", search))

    # Print to indicate that the bot is running
    print("Bot is running...")

    # Start polling for updates
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
    
