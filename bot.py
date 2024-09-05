import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

# Your bot token
BOT_TOKEN = "7542010899:AAESLyBa0VFfSeNmo2jycGDwuSzaWHF1KRw"
API_URL = "https://evobuscas.squareweb.app/leak.php"

# Function to handle the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! Send a website to search for leaked login details.')

# Function to search logins using your API and save the data to a text file
async def search_logins(update: Update, context: CallbackContext):
    website = ' '.join(context.args)
    
    if not website:
        await update.message.reply_text('Please provide a website to search.')
        return

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{API_URL}?busca={website}&token=yoda") as response:
                data = await response.text()

        if response.status == 200 and data:
            # Save the response data into a text file
            with open(f"{website}_login_data.txt", "w") as file:
                file.write(data)
            await update.message.reply_text(f"Search results for {website} saved to {website}_login_data.txt")
        else:
            await update.message.reply_text('No data found for this website.')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

# Main function to start the bot
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("search", search_logins))

    print("Bot is running...")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
    
