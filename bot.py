import os
import time
import threading
from datetime import datetime
import telebot
from flask import Flask

print("=" * 60)
print("🤖 TRADER BOT PRO - VERSION SIMPLIFIÉE")
print("🇲🇬 Madagascar | 🕒 24/7")
print("=" * 60)

# Configuration
TELEGRAM_TOKEN = "8239945370:AAHgBmLRMj2_t3Vq1Cwi-iMqvSxMSaKiGhk"
PORT = int(os.getenv('PORT', 10000))

print(f"✅ Token: {TELEGRAM_TOKEN[:10]}...")
print(f"✅ Port: {PORT}")
print(f"✅ Heure: {datetime.now().strftime('%H:%M:%S')}")
print()

# Initialisation Flask
app = Flask(__name__)

# Initialisation Telegram Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Route web principale
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🤖 Trader Bot Pro</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; }
            h1 { color: #4CAF50; }
            .status { background: green; color: white; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>🤖 TRADER BOT PRO</h1>
        <div class="status">🟢 EN LIGNE ET ACTIF</div>
        <p>🇲🇬 Madagascar | Version 1.0</p>
        <p>📍 <a href="/health">Vérifier l'état</a></p>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "active", "bot": "Trader Bot Pro", "region": "Madagascar"}

# Commandes Telegram SIMPLES
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🤖 Trader Bot Pro activé ! 🇲🇬")

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, f"✅ Actif | {datetime.now().strftime('%H:%M:%S')}")

# Fonction pour démarrer Telegram bot
def start_telegram_bot():
    print("📱 Démarrage du bot Telegram...")
    bot.polling(non_stop=True)

# Démarrer tout
if __name__ == "__main__":
    print("🚀 Démarrage des services...")
    
    # Démarrer Telegram dans un thread
    telegram_thread = threading.Thread(target=start_telegram_bot, daemon=True)
    telegram_thread.start()
    
    print(f"🌐 Serveur web sur le port {PORT}")
    print("⚡ Tout est prêt !")
    
    # Démarrer Flask
    app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)
