from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton





info = InlineKeyboardMarkup(row_width=2)
btnInfo = InlineKeyboardButton(text='--->', callback_data='btnSled')

info_back = InlineKeyboardMarkup(row_width=2)
btnInfo_back = InlineKeyboardButton(text='<---', callback_data='btnBack')






love_btn = InlineKeyboardMarkup(row_width=2)
btn_love = InlineKeyboardButton(text=' 🥂  Отправить поцелуйчик ', callback_data='kiss')






zap = InlineKeyboardMarkup(row_width=2)
sob = InlineKeyboardMarkup(row_width=2)
btnSob = InlineKeyboardButton(text='🌲  Планы',
                              callback_data='btnSob')

sob_add = InlineKeyboardMarkup(row_width=2)
btnSob_add = InlineKeyboardButton(text='Добавить событие',
                                  callback_data="Add_Sob")
btnSob_delete = InlineKeyboardButton(text='Удалить все события',
                                     callback_data='Delete_all_Sob')
sob_back_menu = InlineKeyboardMarkup(row_width=2)
btn_sob_back_menu = InlineKeyboardButton(text='Вернуться обратно',
                                         callback_data="Back_menu")




photo_add = InlineKeyboardMarkup(row_width=2)
btnPhoto_Add = InlineKeyboardButton(text='👼  Добавить мордашки в альбомчик',
                                    callback_data='Add_Photo')

video_add = InlineKeyboardMarkup(row_width=2)
btnVideo_Add = InlineKeyboardButton(text='⛄  Добавить видео мордашки в альбомчик',
                                    callback_data='Add_Video')

pismo = InlineKeyboardMarkup(row_width=2)
btnpismo = InlineKeyboardButton(text='💌',
                                    callback_data='pismo')

info.add(btnInfo_back, btnInfo).row(btnpismo).row(btnPhoto_Add).row(btnVideo_Add).row(btnSob).row(btn_love)

zap.add(btnSob)

sob.add(btnSob_add).add(btnSob_delete)
