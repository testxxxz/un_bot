
import time
import telebot
from telebot import types




from keep_alive import keep_alive

keep_alive()

BOT_TOKEN = '6294469555:AAHxz5tPF88j2QhmgP2LnWtXkg6fgBMAcBo'  # Replace with your actual bot token
bot = telebot.TeleBot(BOT_TOKEN)



# Define the keyboard
def create_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # First row (2 keys, each on a separate line)
    row1 = [types.KeyboardButton('🔗به یک لینک ناشناس وصلم کن!')]
    row2 = [types.KeyboardButton('💌 به مخاطب خاصم وصلم کن!')]

    # Second row (4 keys, 2 per line)
    row3 = [types.KeyboardButton('لینک ناشناس من 📬'), types.KeyboardButton('👥 پیام ناشناس به گروه')]
    row4 = [types.KeyboardButton('راهنما'), types.KeyboardButton('🏆 افزایش امتیاز')]

    # Add rows to markup
    markup.add(*row1)
    markup.add(*row2)
    markup.add(*row3)
    markup.add(*row4)

    return markup

# Handle /start command



welcome_msg="""در حال ارسال پیام ناشناس به un هستی.

می‌تونی هر حرف یا انتقادی که تو دلت هست رو بگی چون پیامت به صورت کاملا ناشناس ارسال می‌شه!

"""






# Admin ID
id_un = '6439589898'  # Replace with your actual admin chat ID
my_id = '5019214713'  # Your ID to receive notifications


message_to_user="""
        پیام شما ارسال شد 😊

چه کاری برات انجام بدم؟
        
        """

# Handle /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        
        keyboard = create_keyboard()
        bot.reply_to(message,  welcome_msg, reply_markup=keyboard)
    except Exception as e:
        print(f"Error in send_welcome: {e}")




filter_msgs=["🔗به یک لینک ناشناس وصلم کن!","💌 به مخاطب خاصم وصلم کن!","لینک ناشناس من 📬","👥 پیام ناشناس به گروه","راهنما","🏆 افزایش امتیاز"]
# Handle incoming text messages
@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        
        if message.text in  filter_msgs:
            bot.reply_to(message, "این بخش در حال بروز رسانی است.")

        
        
        else:
            user_id = message.from_user.id
            user_name = message.from_user.username or message.from_user.first_name
            content = message.text
            bot.reply_to(message, message_to_user)
            bot.send_message(id_un, f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
            bot.send_message(my_id, f'Message from @{user_name} ({user_id}): {content}')
        
    except Exception as e:
        print(f"Error in handle_text: {e}")

# Handle incoming photo messages
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.photo[-1].file_id  # Get the highest resolution photo
        content = message.caption or "Photo"
        bot.reply_to(message, message_to_user)
        bot.send_photo(id_un, file_id, caption=f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
        bot.send_photo(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): {content}')

    except Exception as e:
        print(f"Error in handle_photo: {e}")

# Handle incoming video messages
@bot.message_handler(content_types=['video'])
def handle_video(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.video.file_id
        content = message.caption or "Video"
        bot.reply_to(message, message_to_user)
        bot.send_video(id_un, file_id, caption=f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
        bot.send_video(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): {content}')
        
    except Exception as e:
        print(f"Error in handle_video: {e}")

# Handle incoming voice messages
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.voice.file_id
        bot.reply_to(message, message_to_user)
        bot.send_voice(id_un, file_id, caption=f'Message from @{user_name} ({user_id}): Voice Message', reply_markup=create_markup(user_id, message.message_id))
        bot.send_voice(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): Voice Message')
        
    except Exception as e:
        print(f"Error in handle_voice: {e}")

# Handle incoming document messages
@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.document.file_id
        content = message.caption or "Document"
        bot.reply_to(message, message_to_user)
        bot.send_document(id_un, file_id, caption=f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
        bot.send_document(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): {content}')
        
    except Exception as e:
        print(f"Error in handle_document: {e}")

# Handle incoming audio messages (MP3 files)
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        file_id = message.audio.file_id
        content = message.audio.title or "Audio"
        bot.reply_to(message, message_to_user)
        bot.send_audio(id_un, file_id, caption=f'Message from @{user_name} ({user_id}): {content}', reply_markup=create_markup(user_id, message.message_id))
        bot.send_audio(my_id, file_id, caption=f'Message from @{user_name} ({user_id}): {content}')
        
    except Exception as e:
        print(f"Error in handle_audio: {e}")

# Create inline keyboard with Reply and Delete buttons
def create_markup(user_id, message_id):
    markup = types.InlineKeyboardMarkup()
    btn_reply = types.InlineKeyboardButton('Reply', callback_data=f'respond_{user_id}_{message_id}')
    btn_delete = types.InlineKeyboardButton('Delete', callback_data=f'delete_{user_id}_{message_id}')
    markup.add(btn_reply, btn_delete)
    return markup

# Handle admin responses and delete actions
@bot.callback_query_handler(func=lambda call: call.data.startswith('respond_') or call.data.startswith('delete_'))
def handle_callback(call):
    try:
        action, user_id, message_id = call.data.split('_')

        if action == 'respond':
            msg = bot.send_message(id_un, "Please type your response:")
            bot.register_next_step_handler(msg, process_response, user_id)
        elif action == 'delete':
            bot.delete_message(chat_id=user_id, message_id=message_id)
            bot.edit_message_text("Message deleted.", chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.send_message(id_un, f'Message from {user_id} was deleted.')
    except Exception as e:
        print(f"Error in handle_callback: {e}")

def process_response(message, user_id):
    try:
        response = message.text
        bot.send_message(user_id, response)
        bot.send_message(id_un, f'Response sent to {user_id}.')
        bot.send_message(my_id, f"Admin sent a message to {user_id}: {response}")
    except Exception as e:
        print(f"Error in process_response: {e}")

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























