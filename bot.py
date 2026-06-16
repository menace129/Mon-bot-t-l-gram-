import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

CANAL = "@from_saison_04_vf"

# Chaque saison contient la liste des numéros de messages
series = {
    "saison1": [19, 22],  # numéros des épisodes
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if args and args[0] in series:
        saison = args[0]
        episodes = series[saison]
        await update.message.reply_text(f"⏳ Envoi de {saison} en cours...")
        for message_id in episodes:
            await context.bot.copy_message(
                chat_id=update.effective_chat.id,
                from_chat_id=CANAL,
                message_id=message_id
            )
        await update.message.reply_text("✅ Envoi terminé ! Bon visionnage 🎬")
    else:
        await update.message.reply_text("👋 Bienvenue ! Allez sur le canal principal pour choisir un fichier https://t.me/sqdgme_s123.")

import os
TOKEN = os.environ.get("TOKEN")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
