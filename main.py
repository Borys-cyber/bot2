from aiogram import Bot, Dispatcher, executor, types
import os
import sqlite3
import DB
import keaboard
import keaboard as kb

TOKEN = os.environ['token']
# print(TOKEN)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

users={}

@dp.message_handler(content_types=['contact', 'location'])
async def ph(message: types.Message):
    print('--')
    print(message)

# def add_db(users_id, u_name, email, phone):
#     connect = sqlite3.connect('user_inews.db')
#     cursor = connect.cursor()
#     cursor.execute('CREATE TABLE IF NOT EXISTS USERSiNEWS(users_id integer, u_name text NOT NULL, email text, phone text)')
#     cursor.execute(f'INSERT INTO USERSiNEWS (users_id, u_name, email, phone) VALUES (?, ?, ?, ?)', (users_id, u_name, email, phone))
#     connect.commit()
#     connect.close()


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    # print(message.from_user.id, ' - ', message.from_user.first_name, ' - ', message.text)
    user = {
        'id_telegram': message.from_user.id,
        'username': message.from_user.username,
        'name': message.from_user.first_name
    }
    if len(DB.get_user(message.from_user.id)) == 0:
        DB.add_user(user)
    users.update({message.from_user.id: message.from_user.first_name})
    # keyboard = kb.keyboard_menu
    if message.text == 'Инлайн клавиатура':
        keyboard = kb.inline_keyboard()
    else:
        keyboard = kb.get_kbrd()
        keyboard.add(types.KeyboardButton('Инлайн клавиатура'))

@dp.message_handler()
async def echo(message: types.Message):
    print(message.from_user.id, ' - ', message.from_user.first_name, ' - ', message.text)
    users.update({message.from_user.id: message.from_user.first_name})
    user = {
        'users_id': message.from_user.id,
        'u_name': message.from_user.username,
        'name': message.from_user.first_name
    }
    if len(DB.get_user(message.from_user.id)) == 0:
        DB.add_user(user)
    for i in users:
        await bot.send_message(chat_id=i, text=message.text)
    text = f'"Пользователь" {message.from_user.first_name} "написал" {message.text}'
    for i in users.keys():
        if i != message.from_user.id:
            await bot.send_message(chat_id=i,
                                   text=text)
    # users_id = message.from_user.id
    # u_name = message.from_user.first_name
    # email = "?"
    # phone = "?"
    # add_db(users_id=users_id, u_name=u_name, email=email, phone=phone)

@dp.callback_query_handler()
async def call_echo(callback_q: types.CallbackQuery):
    print(callback_q)
    await bot.answer_callback_query(callback_q.id)
    await bot.send_message(chat_id=callback_q.from_user.id, text=callback_q.data)


# urlkb = InlineKeyboardMarkup(row_width=2)
# btn = InlineKeyboardButton(text='Google', url="google.com.ua")
# btn1 = InlineKeyboardButton(text='youtube', url="youtube.com.ua")
# urlkb.add(InlineKeyboardMarkup().add(btn, btn1))

# @dp.message_handler(commands="ссылки")
# async def url_command(message: types.Message):
#     await message.answer("Cсылки:", reply_markup=urlkb)

if __name__ == '__main__':
    executor.start_polling(dp)























if __name__ == '__main__':
    print_hi('PyCharm')


