import time
import telebot
from telebot import types



from keep_alive import keep_alive

keep_alive()


BOT_TOKEN = '6294469555:AAHxz5tPF88j2QhmgP2LnWtXkg6fgBMAcBo'  # Replace with your actual bot token
bot = telebot.TeleBot(BOT_TOKEN)

# In-memory storage for user messages
user_messages = []

# Admin ID
id_fati = '6439589898'  # Replace with your actual admin chat ID
my_id = '5019214713'  # Your ID to receive notifications

# Handle /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        bot.reply_to(message, "سلام به ربات ناشناس خوش اومدی،هر پیامی که دوست داری بفرست تا ارسال کنم ")
    except Exception as e:
        print(f"Error in send_welcome: {e}")

# Command for admin to view messages
@bot.message_handler(commands=['view_messages'])
def view_messages(message):
    try:
        if str(message.chat.id) == id_fati:
            if user_messages:
                for idx, (user_id, user_name, text) in enumerate(user_messages):
                    markup = types.InlineKeyboardMarkup()
                    btn = types.InlineKeyboardButton('Respond', callback_data=f'respond_{idx}')
                    markup.add(btn)
                    bot.send_message(id_fati, f'Message from @{user_name} ({user_id}): {text}', reply_markup=markup)
            else:
                bot.send_message(id_fati, "No messages to display.")
        else:
            bot.reply_to(message, "This command is for admin only.")
    except Exception as e:
        print(f"Error in view_messages: {e}")

# Handle incoming messages from users
@bot.message_handler(func=lambda message: message.chat.id != int(id_fati))
def receive_message(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        text = message.text
        user_messages.append((user_id, user_name, text))
        bot.reply_to(message, "پیام شما ارسال شد.")
        bot.send_message(my_id, f'Message from @{user_name} ({user_id}), message: {text}')
    except Exception as e:
        print(f"Error in receive_message: {e}")

# Handle admin response
@bot.callback_query_handler(func=lambda call: call.data.startswith('respond_'))
def handle_response(call):
    try:
        if str(call.message.chat.id) == id_fati:
            idx = int(call.data.split('_')[1])
            user_id, user_name, text = user_messages[idx]
            msg = bot.send_message(id_fati, "Please type your response:")
            bot.register_next_step_handler(msg, process_response, user_id, user_name, idx)
    except Exception as e:
        print(f"Error in handle_response: {e}")

def process_response(message, user_id, user_name, idx):
    try:
        response = message.text
        bot.send_message(user_id, response)
        bot.send_message(id_fati, f'Response sent to @{user_name} ({user_id}).')
        bot.send_message(my_id, f"admin sent message to @{user_name} ({user_id}) and message: {response}")
        user_messages.pop(idx)
    except Exception as e:
        print(f"Error in process_response: {e}")

@bot.message_handler(commands=['clear_messages'])
def clear_messages(message):
    try:
        if str(message.chat.id) == id_fati:
            user_messages.clear()
            bot.send_message(id_fati, "All messages have been cleared.")
        else:
            bot.reply_to(message, "This command is for admin only.")
    except Exception as e:
        print(f"Error in clear_messages: {e}")

def polling_with_retry():
    retry_delay = 1
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Polling error: {e}")
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)  # Exponential backoff up to 60 seconds

if __name__ == '__main__':
    polling_with_retry()
