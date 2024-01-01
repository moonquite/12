# ----------------------------------------------------------------------------
#                                Импорт библиотек


import aiogram


from bot_loading import bot

from keyboard import inline as inl
from keyboard import markup as key


from datetime import datetime as dt
import datetime

import random



import os
from aiogram import types




from datetime import datetime

from etc.data_actual import date_tog
from etc.world import good_word
from etc.photos import content, photo_folder

from apscheduler.triggers.cron import CronTrigger

from apscheduler.schedulers.asyncio import AsyncIOScheduler



from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import State, StatesGroup
#----------------------------------------------------------------------------
#                                Общие переменные

compliments = [
    "Твои глаза, это как звезды в ночном небе, они такие яркие и загадочные.",
    "Твоя улыбка, словно магия, которая разгоняет тучи в моей душе.",
    "Когда ты рядом, весь мир становится красочнее, как в самых крутых фильмах.",
    "Ты - как любимый персонаж из книги, который делает каждый день интересным приключением.",
    "Твои слова, как поэзия, которую я читаю снова и снова, чтобы чувствовать тепло внутри.",
    "Твои объятия - мое самое безопасное укрытие, словно нежный покрывало в холодные ночи.",
    "Твоя уверенность - как заклинание, которое придает силы в трудные моменты.",
    "С тобой каждый момент - как веселая комедия, полная смеха и веселья.",
    "Твои мечты - как сказка, которую я хочу слышать каждый день, чтобы засыпать с улыбкой на лице.",
    "Твой смех - как мелодия, которую я бы слушал бесконечно, как любимую песню.",
    "Твоя любовь - это мое сокровище, которое я бережно храню в самом сердце.",
    "С тобой я чувствую себя как волшебник, который обнаружил свой собственный магический мир.",
    "Твои героические поступки - как из фильма, и я горжусь тем, что рядом с тобой.",
    "Твоя уникальность - мое самое ценное открытие, словно сокровище в заброшенной лавке.",
    "Твои заботливые слова - как добрые записочки в старинной книге, написанные с любовью.",
    "Ты - моя личная звезда, яркая и невероятно прекрасная.",
    "Твои мечты - маяк, направляющий меня через штормы повседневной жизни.",
    "Ты - как волшебный калейдоскоп, каждый день предлагающий новые и яркие оттенки чувств.",
    "Твои идеи - как вдохновляющие главы в самой интересной книге моей жизни.",
    "С тобой я осваиваю свой собственный танец любви, полный неукоснительного восхищения и нежности."
]


id_accept = [937704618, 1028562446]

# 937704618 - Никита
# 1028562446 - Маша

photo_amount = len(content)
photo_number = 0


EVENTS_DIR = "events"
if not os.path.exists(EVENTS_DIR):
    os.makedirs(EVENTS_DIR)

EVENTS_FILE = os.path.join(EVENTS_DIR, "events.txt")

now = dt.now()

scheduler = AsyncIOScheduler()
scheduler.start()

class EventStates(StatesGroup):
  delete_event = None
  add_event = State()

class DeleteEventStates(StatesGroup):
    delete_event = State()


async def send_reminder():
    await bot.send_message(id_accept[1], f'💌\t\t{random.choice(compliments)}')

async def send_new():
    await bot.send_message(id_accept[1],'🎄\t\tС новым 2024 годом, наполненным обещаниями и возможностями, я хочу тебе передать всю гамму моих чувств. В этот волшебный переход от старого к новому году, я осознаю, что ты — моя главная радость, и каждый момент с тобой — настоящий подарок судьбы.\n\nС любовью, силой и вдохновением ты наполняешь каждый день моей жизни. Твоя любовь — моя надежда, твои поцелуи — волшебные мгновения, а твои объятия — мое укрытие от жизненных бурь. В этот праздничный момент я хочу выразить благодарность за твою преданность и тепло, которое ты несешь в мою жизнь.\n\nС каждым годом наша любовь становится глубже, слова становятся излишними, и мы начинаем понимать друг друга даже без слов. Ты — моя невероятная половина, без которой я не могу представить свою жизнь. Ты делаешь меня лучше, и я горжусь, что могу быть твоим партнером в этом захватывающем путешествии.\n\nПусть этот новый год приносит нам еще больше смеха, волнующих приключений и моментов, которые будут теплыми воспоминаниями в будущем. Пусть каждый день будет наполнен любовью, а каждый вечер будет нежным прикосновением наших сердец.\n\nС наступившим Новым 2024 годом, моя любимая! Ты — мой самый дорогой подарок, и я готов встретить этот год с тобой рядом.❤️😘❤️😘❤️😘❤️')

async def utro():
    body = '¨¨/ \¨'
    img = open(f'{photo_folder}/{content[photo_number]}', 'rb')
    await bot.send_photo(
        chat_id=id_accept[0],
        photo=img,
        caption=
        f'Доброе утро, лучики!!!❤️⛄ \n\n\n¨/\_/\ \t\t\n\t>^,^<\t\t\t\t\t\t👩🏼‍❤️‍💋‍👨🏽\t\t\t\tМы вместе:' + '\n' + f'{body}\t\t\t\t\t' + f'\t\t\t\t{date_tog()[0]}' + '\t' + f'{date_tog()[1]}' + '\t' + f'{date_tog()[2]}'
        + '\n' + '’¨(__)__' + f'\n\\n\n💐Ты у меня такая\t{random.choice(good_word)}',
        reply_markup=inl.info)
    body = '¨¨/ \¨'
    await bot.send_photo(
        chat_id=id_accept[1],
        photo=img,
        caption=
        f'Доброе утро, лучики!!!❤️⛄ \n\n\n¨/\_/\ \t\t\n\t>^,^<\t\t\t\t\t\t👩🏼‍❤️‍💋‍👨🏽\t\t\t\tМы вместе:' + '\n' + f'{body}\t\t\t\t\t' + f'\t\t\t\t{date_tog()[0]}' + '\t' + f'{date_tog()[1]}' + '\t' + f'{date_tog()[2]}'
        + '\n' + '’¨(__)__' + f'\n\\n\n💐Ты у меня такая\t{random.choice(good_word)}',
        reply_markup=inl.info)

async def noch():
    body = '¨¨/ \¨'
    img = open(f'{photo_folder}/{content[photo_number]}', 'rb')
    await bot.send_photo(
        chat_id=id_accept[0],
        photo=img,
        caption=
        f'Добрых снов, зайки!!!❤️🕯️ \n\n\n¨/\_/\ \t\t\n\t>^,^<\t\t\t\t\t\t👩🏼‍❤️‍💋‍👨🏽\t\t\t\tМы вместе:' + '\n' + f'{body}\t\t\t\t\t' + f'\t\t\t\t{date_tog()[0]}' + '\t' + f'{date_tog()[1]}' + '\t' + f'{date_tog()[2]}'
        + '\n' + '’¨(__)__' + f'\n\\n\n💐Ты у меня такая\t{random.choice(good_word)}',
        reply_markup=inl.info)
    body = '¨¨/ \¨'
    img = open(f'{photo_folder}/{content[photo_number]}', 'rb')
    await bot.send_photo(
        chat_id=id_accept[1],
        photo=img,
        caption=
        f'Добрых снов, зайки!!!❤️🕯️ \n\n\n¨/\_/\ \t\t\n\t>^,^<\t\t\t\t\t\t👩🏼‍❤️‍💋‍👨🏽\t\t\t\tМы вместе:' + '\n' + f'{body}\t\t\t\t\t' + f'\t\t\t\t{date_tog()[0]}' + '\t' + f'{date_tog()[1]}' + '\t' + f'{date_tog()[2]}'
        + '\n' + '’¨(__)__' + f'\n\\n\n💐Ты у меня такая\t{random.choice(good_word)}',
        reply_markup=inl.info)


scheduler.add_job(utro, trigger=CronTrigger(hour=8, minute=0, second=0))
scheduler.add_job(send_reminder, trigger=CronTrigger(hour=9, minute=0, second=0))
scheduler.add_job(send_reminder, trigger=CronTrigger(hour=13, minute=0, second=0))
scheduler.add_job(send_reminder, trigger=CronTrigger(hour=15, minute=0, second=0))
scheduler.add_job(send_reminder, trigger=CronTrigger(hour=17, minute=0, second=0))
scheduler.add_job(send_reminder, trigger=CronTrigger(hour=19, minute=0, second=0))
scheduler.add_job(send_reminder, trigger=CronTrigger(hour=22, minute=0, second=0))
scheduler.add_job(noch, trigger=CronTrigger(hour=23, minute=0, second=0))


#----------------------------------------------------------------------------
#                            Работа бота

# Функция для старта. С проверкой id.
# @dp.message_handler(commands=['start'])
async def start_bot(message: aiogram.types.Message):
  if message.from_user.id == id_accept[0] or message.from_user.id == id_accept[1]:
    await message.answer_sticker('CAACAgQAAxkBAAEIjNhkNeRvVi31Zpgu6JHrZAABisQFaNsAAugJAAJtBelTd_RVxHQso7gvBA')
    await message.answer('💒Приветик, солнышко!!! \n Я тебя очень сильно люблю моя зайка. \n Этот бот предназначен для нас!!!',
      reply_markup=key.Main)
  else:
     await message.answer('😡Вход запрещен.')


#------

# Функция отображающая основное меню
# @dp.message_handler()
async def info(message: aiogram.types.Message):
  if message.text == '✨О нас':
    await bot.delete_message(message.from_user.id, message.message_id)
    body = '¨¨/ \¨'
    img = open(f'{photo_folder}/{content[photo_number]}', 'rb')
    await bot.send_photo(
      chat_id=message.chat.id,
      photo=img,
      caption=
      f'¨/\_/\ \t\t\n\t>^,^<\t\t\t\t\t\t👩🏼‍❤️‍💋‍👨🏽\t\t\t\tМы вместе:' + '\n' + f'{body}\t\t\t\t\t' + f'\t\t\t\t{date_tog()[0]}' + '\t' + f'{date_tog()[1]}' + '\t' + f'{date_tog()[2]}'
      + '\n' + '’¨(__)__' + f'\n\n🎁Ты у меня такая\t{random.choice(good_word)}',
      reply_markup=inl.info)

#------

# ---->
# @dp.callback_query_handler(text='btnSled')
async def sled(query: aiogram.types.CallbackQuery):
    global photo_folder
    global content
    global photo_amount
    global photo_number

    if photo_number < 0:
        photo_number == 0

    if photo_number == photo_amount:
        photo_number = 0


    if photo_number >= 0 and photo_number <= photo_amount:
        photo_number += 1



    media_file = open(f'{photo_folder}/{content[photo_number]}', 'rb')

    # Check if the file is an image or a video
    is_video = content[photo_number].endswith('.mp4')

    if is_video:
        media = aiogram.types.InputMediaVideo(media=aiogram.types.InputFile(media_file), caption="Your video caption")
    else:
        media = aiogram.types.InputMediaPhoto(media=aiogram.types.InputFile(media_file), caption="Your photo caption")

    body = '¨¨/ \¨'
    caption_text = (
        f'¨/\_/\ \t\t\n\t>^,^<\t\t\t\t\t\t👩🏼‍❤️‍💋‍👨🏽\t\t\t\tМы вместе:' + '\n' +
        f'{body}\t\t\t\t\t' + f'\t\t\t\t{date_tog()[0]}' + '\t' + f'{date_tog()[1]}' + '\t' + f'{date_tog()[2]}' +
        '\n' + '’¨(__)__' + f'\n\n🎁Ты у меня такая\t{random.choice(good_word)}'
    )

    media.caption = caption_text

    await query.message.edit_media(media, reply_markup=inl.info)
    print(photo_number)
#------


# <----
# @dp.callback_query_handler(text='btnBack')
async def back(query: aiogram.types.CallbackQuery):
    global photo_folder
    global content
    global photo_amount
    global photo_number

    if photo_number == photo_amount:
        photo_number = 0

    if photo_number < 0:
        photo_number += 1
    else:
        photo_number -= 1



    print(photo_number)
    media_file = open(f'{photo_folder}/{content[photo_number]}', 'rb')

    # Check if the file is an image or a video
    is_video = content[photo_number].endswith('.mp4')

    if is_video:
        media = aiogram.types.InputMediaVideo(media=aiogram.types.InputFile(media_file), caption="Your video caption")
    else:
        media = aiogram.types.InputMediaPhoto(media=aiogram.types.InputFile(media_file), caption="Your photo caption")

    body = '¨¨/ \¨'
    caption_text = (
        f'¨/\_/\ \t\t\n\t>^,^<\t\t\t\t\t\t👩🏼‍❤️‍💋‍👨🏽\t\t\t\tМы вместе:' + '\n' +
        f'{body}\t\t\t\t\t' + f'\t\t\t\t{date_tog()[0]}' + '\t' + f'{date_tog()[1]}' + '\t' + f'{date_tog()[2]}' +
        '\n' + '’¨(__)__' + f'\n\n🎁Ты у меня такая\t{random.choice(good_word)}'
    )

    media.caption = caption_text

    await query.message.edit_media(media, reply_markup=inl.info)
#------


#Функция для добавки фоток.
# @dp.callback_query_handler(text='Add_Photo')
async def add_photos(query: aiogram.types.CallbackQuery):
  await query.message.answer_sticker(
    'CAACAgIAAxkBAAEKbbBlGY0y1Q8erCDeRdAtuI-PycWudAACJx0AAh1CoUlGLRZG9tpvFTAE')
  await query.message.answer('Кидай фоточку ваших милых мордашек 👼')

# @dp.callback_query_handler(text='Add_Video')
async def add_video(query: aiogram.types.CallbackQuery):
  await query.message.answer_sticker(
    'CAACAgIAAxkBAAELE5FlktyWKRCBJZe9Vai9gNgEaE7eFwACJyUAAlVFmEmvASFg9o1HgjQE')
  await query.message.answer('Кидай видео ваших милых мордашек ☃️')

# @dp.message_handler(content_types=['photo', 'video'])
async def handle_docs(message):
    global photo_amount
    try:
        if message.photo:
            await handle_docs_photo(message)
        elif message.video:
            await handle_docs_video(message)
        else:
            await message.answer('Извините, я пока не могу обработать этот тип документа.')
    except Exception as e:
        await message.answer(f'Произошла ошибка при обработке документа: {e}')

async def handle_docs(message):
    global photo_amount

    try:
        if message.photo:
            print(1)
            await handle_docs_photo(message)
        elif message.video:
            print(2)
            await handle_docs_video(message)
        else:
            await message.answer('Извините, я пока не могу обработать этот тип документа.')
    except Exception as e:
        await message.answer(f'Произошла ошибка при обработке документа: {e}')

async def handle_docs_photo(message):
    global photo_amount
    try:
        await message.photo[-1].download(destination_file=f'{photo_folder}/{photo_amount}.png')
        await message.answer('🎄\t\tЗагрузил фото в альбомчик!!!')
        photo_amount += 1
    except Exception as e:
        await message.answer(f'Произошла ошибка при загрузке фото: {e}')

async def handle_docs_video(message):
    global photo_amount
    try:
        video_path = f'{photo_folder}/{photo_amount}.mp4'
        video = message.video
        video_file = await video.get_file()
        await video.bot.download_file_by_id(video_file.file_id, video_path)
        await message.answer('🎄\t\tЗагрузил видео в альбомчик!!!')
        photo_amount += 1
    except Exception as e:
        await message.answer(f'Произошла ошибка при загрузке видео: {e}')
#------

# @dp.callback_query_handler(text='Add_Sob')


async def sob_add(query: aiogram.types.CallbackQuery):
  await query.message.answer("🐻‍❄️Отправь мне текст события и время напоминания в формате \n\n Событие YYYY-MM-DD HH:MM")
  await EventStates.add_event.set()


#@dp.message_handler()
async def send_reminder(bot, event_text):
  await bot.send_message(id_accept[0], f"🎉\t\tНапоминаю: {event_text}")
  await bot.send_message(id_accept[1], f"🎉\t\tНапоминаю: {event_text}")

# @dp.message_handler(state=EventStates.add_event)
async def add_event_text(message: types.Message, state: FSMContext):
    event_info = message.text.split(' ', 2)

    if len(event_info) != 3:
      await message.reply("🥶\t\tНекорректный формат. Пожалуйста, используйте формат: Событие YYYY-MM-DD HH:MM.")
      return

    date_string = event_info[1]
    time_string = event_info[2]
    event_text = event_info[0]

    try:
      event_time = datetime.strptime(f"{date_string} {time_string}", '%Y-%m-%d %H:%M')
    except ValueError:
      await message.reply("🥶\t\tНекорректный формат. Пожалуйста, используйте формат Событие YYYY-MM-DD HH:MM.")
      return

    # Сохранение события в текстовый файл
    with open(EVENTS_FILE, "a") as event_file:
      event_file.write(f"{event_time.strftime('%Y-%m-%d %H:%M')} {event_text}\n")

    # Запланировать отправку напоминания
    scheduler.add_job(
      send_reminder,
      'date',
      run_date=event_time,
      args=[bot, event_text],
      id=f"{event_time}"
    )

    await message.reply(f"☃️\t\tСобытие добавлено! Напомню вам {event_time.strftime('%Y-%m-%d %H:%M')}.")

    # Завершение состояния
    await state.finish()


#@dp.callback_query_handler(text = 'btnSob')
async def view_events_command(query: aiogram.types.CallbackQuery):
  try:
    with open(EVENTS_FILE, "r") as event_file:
      events = event_file.readlines()

    if events:
      formatted_events = "\n".join(events)
      await query.message.answer(f"🎅\t\ttВсе запланированные события:\n\n{formatted_events}", reply_markup=inl.sob)
    else:
      await query.message.answer("🎅\t\tНет запланированных событий.", reply_markup=inl.sob)
  except FileNotFoundError:
    await query.message.answer("🎅\t\tНет запланированных событий.", reply_markup=inl.sob)

#@dp.callback_query_handler(text = 'Delete_all_Sob')
async def delete_all_events_command(query: aiogram.types.CallbackQuery):
    try:
        os.remove(EVENTS_FILE)
        await query.message.answer("\t\t🌬️Все события удалены.")
        await info('✨О нас')
    except FileNotFoundError:
        await query.message.answer("\t\t🎅Нет запланированных событий.")



# Функция для отправки поцелуев
#@dp.callback_query_handler(text='kiss')
async def kiss(query: aiogram.types.CallbackQuery):
    if query.from_user.id == id_accept[0]:
        await bot.send_message(id_accept[1], '💋')
        await bot.send_message(id_accept[1], '❄️\t\tВам пришел поцелуйчик!')
    if query.from_user.id == id_accept[1]:
        await bot.send_message(id_accept[0], '💋')
        await bot.send_message(id_accept[0], '❄️\t\tВам пришел поцелуйчик!')

async def pismo(query: aiogram.types.CallbackQuery):
    await query.message.answer('🎄\t\tС новым 2024 годом, наполненным обещаниями и возможностями, я хочу тебе передать всю гамму моих чувств. В этот волшебный переход от старого к новому году, я осознаю, что ты — моя главная радость, и каждый момент с тобой — настоящий подарок судьбы.\n\nС любовью, силой и вдохновением ты наполняешь каждый день моей жизни. Твоя любовь — моя надежда, твои поцелуи — волшебные мгновения, а твои объятия — мое укрытие от жизненных бурь. В этот праздничный момент я хочу выразить благодарность за твою преданность и тепло, которое ты несешь в мою жизнь.\n\nС каждым годом наша любовь становится глубже, слова становятся излишними, и мы начинаем понимать друг друга даже без слов. Ты — моя невероятная половина, без которой я не могу представить свою жизнь. Ты делаешь меня лучше, и я горжусь, что могу быть твоим партнером в этом захватывающем путешествии.\n\nПусть этот новый год приносит нам еще больше смеха, волнующих приключений и моментов, которые будут теплыми воспоминаниями в будущем. Пусть каждый день будет наполнен любовью, а каждый вечер будет нежным прикосновением наших сердец.\n\nС наступившим Новым 2024 годом, моя любимая! Ты — мой самый дорогой подарок, и я готов встретить этот год с тобой рядом.❤️😘❤️😘❤️😘❤️')



#----------------------------------------------------------------------------
#                            Регестрация функций
def register_handlers_client(dp: aiogram.Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'])
    dp.register_message_handler(info)
    dp.register_message_handler(send_reminder)
    dp.register_callback_query_handler(sled, text='btnSled')
    dp.register_callback_query_handler(back, text='btnBack')
    dp.register_callback_query_handler(add_photos, text='Add_Photo')
    dp.register_message_handler(handle_docs, content_types=['photo', 'video'])
    dp.register_callback_query_handler(sob_add, text = 'Add_Sob')
    dp.register_message_handler(add_event_text, state=EventStates.add_event)
    dp.register_callback_query_handler(view_events_command, text = 'btnSob')
    dp.register_callback_query_handler(delete_all_events_command, text ='Delete_all_Sob' )
    dp.register_callback_query_handler(kiss, text = 'kiss')
    dp.register_callback_query_handler(add_video, text='Add_Video')
    dp.register_callback_query_handler(pismo, text = 'pismo')