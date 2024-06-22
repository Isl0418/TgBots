from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text = 'Mackbook Air 13 M1 2020',
            callback_data='apple_air_13_m1_2020'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 14 M1 Pro 2021',
            callback_data='apple_pro_14_m1_2020'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 16 2019',
            callback_data='apple_pro_16_i7_2019'
        )
    ],
    [
        InlineKeyboardButton(
            text='Link',
            url='https://kaspi.kz'
        )
    ],
    [
        InlineKeyboardButton(
            text="Profile",
            url='tg://user?id=6937917295'
        )
    ]
])
