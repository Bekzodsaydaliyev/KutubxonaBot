from aiogram.types import *

#kirish
Inkirish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbekcha🇺🇿", callback_data="uzb"),
            InlineKeyboardButton(text="Русский🇷🇺", callback_data="rus")
        ]
    ],
)

Instart = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Diniy", callback_data="diniy")
        ],
        [
            InlineKeyboardButton(text="Badiiy", callback_data="badiiy"),
            InlineKeyboardButton(text="Ilmiy", callback_data="ilmiy"),
        ],
        [
            InlineKeyboardButton(text="Orqaga", callback_data="orqaga_qaytish_start")
        ]
    ],
)

Instartrus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Религиозный", callback_data="diniy")
        ],
        [
            InlineKeyboardButton(text="Художественный", callback_data="badiiy"),
            InlineKeyboardButton(text="Научный", callback_data="ilmiy"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="orqaga_qaytish_start_rus")
        ]
    ],
)

InDiniy1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1diniy"),
            InlineKeyboardButton(text="2", callback_data="2diniy"),
            InlineKeyboardButton(text="3", callback_data="3diniy"),
            InlineKeyboardButton(text="4", callback_data="4diniy"),
            InlineKeyboardButton(text="5", callback_data="5diniy")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6diniy"),
            InlineKeyboardButton(text="7", callback_data="7diniy"),
            InlineKeyboardButton(text="8", callback_data="8diniy"),
            InlineKeyboardButton(text="9", callback_data="9diniy"),
            InlineKeyboardButton(text="10", callback_data="10diniy")
        ],
        [
            InlineKeyboardButton(text="❌", callback_data="ochirish"),
            InlineKeyboardButton(text="⏩", callback_data="diniy1ga")
        ]
    ],
)

InDiniy2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="11", callback_data="11diniy"),
            InlineKeyboardButton(text="12", callback_data="12diniy"),
            InlineKeyboardButton(text="13", callback_data="13diniy"),
            InlineKeyboardButton(text="14", callback_data="14diniy"),
            InlineKeyboardButton(text="15", callback_data="15diniy")
        ],
        [
            InlineKeyboardButton(text="16", callback_data="16diniy"),
            InlineKeyboardButton(text="17", callback_data="17diniy"),
            InlineKeyboardButton(text="18", callback_data="18diniy"),
            InlineKeyboardButton(text="19", callback_data="19diniy"),
            InlineKeyboardButton(text="20", callback_data="20diniy")
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="diniy"),
            InlineKeyboardButton(text="❌", callback_data="ochirish")
        ]
    ],
)

InBadiiy1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1badiiy"),
            InlineKeyboardButton(text="2", callback_data="2badiiy"),
            InlineKeyboardButton(text="3", callback_data="3badiiy"),
            InlineKeyboardButton(text="4", callback_data="4badiiy"),
            InlineKeyboardButton(text="5", callback_data="5badiiy")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6badiiy"),
            InlineKeyboardButton(text="7", callback_data="7badiiy"),
            InlineKeyboardButton(text="8", callback_data="8badiiy"),
            InlineKeyboardButton(text="9", callback_data="9badiiy"),
            InlineKeyboardButton(text="10", callback_data="10badiiy")
        ],
        [
            InlineKeyboardButton(text="❌", callback_data="ochirish"),
            InlineKeyboardButton(text="⏩", callback_data="badiiy2ga")
        ]
    ],
)

InBadiiy2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="11", callback_data="11badiiy"),
            InlineKeyboardButton(text="12", callback_data="12badiiy"),
            InlineKeyboardButton(text="13", callback_data="13badiiy"),
            InlineKeyboardButton(text="14", callback_data="14badiiy"),
            InlineKeyboardButton(text="15", callback_data="15badiiy")
        ],
        [
            InlineKeyboardButton(text="16", callback_data="16badiiy"),
            InlineKeyboardButton(text="17", callback_data="17badiiy"),
            InlineKeyboardButton(text="18", callback_data="18badiiy"),
            InlineKeyboardButton(text="19", callback_data="19badiiy"),
            InlineKeyboardButton(text="20", callback_data="20badiiy")
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="badiiy"),
            InlineKeyboardButton(text="❌", callback_data="ochirish")
        ]
    ],
)

InIlmiy1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1ilmiy"),
            InlineKeyboardButton(text="2", callback_data="2ilmiy"),
            InlineKeyboardButton(text="3", callback_data="3ilmiy"),
            InlineKeyboardButton(text="4", callback_data="4ilmiy"),
            InlineKeyboardButton(text="5", callback_data="5ilmiy")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6ilmiy"),
            InlineKeyboardButton(text="7", callback_data="7ilmiy"),
            InlineKeyboardButton(text="8", callback_data="8ilmiy"),
            InlineKeyboardButton(text="9", callback_data="9ilmiy"),
            InlineKeyboardButton(text="10", callback_data="10ilmiy")
        ],
        [
            InlineKeyboardButton(text="❌", callback_data="ochirish"),
            InlineKeyboardButton(text="⏩", callback_data="ilmiy2ga")
        ]
    ],
)

InIlmiy2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="11", callback_data="11ilmiy"),
            InlineKeyboardButton(text="12", callback_data="12ilmiy"),
            InlineKeyboardButton(text="13", callback_data="13ilmiy"),
            InlineKeyboardButton(text="14", callback_data="14ilmiy"),
            InlineKeyboardButton(text="15", callback_data="15ilmiy")
        ],
        [
            InlineKeyboardButton(text="16", callback_data="16ilmiy"),
            InlineKeyboardButton(text="17", callback_data="17ilmiy"),
            InlineKeyboardButton(text="18", callback_data="18ilmiy"),
            InlineKeyboardButton(text="19", callback_data="19ilmiy"),
            InlineKeyboardButton(text="20", callback_data="20ilmiy")
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="ilmiy"),
            InlineKeyboardButton(text="❌", callback_data="ochirish")
        ]
    ],
)

