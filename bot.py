import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

CANAL =-1004466288853

# Chaque saison contient la liste des numéros de messages
series = {
    "saison1": list(range(3, 26)),# numéros des épisodes
    "saison2": list(range(26, 49)),
    "saison3": list(range(49, 68)),
    "saison4": list(range(68, 92)),
    "saison5": list(range(92, 115)),

    "saison6": list(range(115, 126)),
    "saison7": [127, 146, 147, 128, 129, 130, 131, 132, 133, 134],
    "saison8": list(range(135, 146)),
    "saison9": [148, 149, 150, 151, 152, 153, 154, 155, 156],
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if args and args[0] in series:
        saison = args[0]
        episodes = series[saison]
        await update.message.reply_text(f"⏳ Envoi en cours...")
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
