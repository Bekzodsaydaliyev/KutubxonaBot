from aiogram.types import *

menustart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text="Qo'shimcha")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

menuqoshimcha = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kitoblar ro'yxati"),
            KeyboardButton(text="Yordam uchun")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

menuqoshimcharus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Список книг"),
            KeyboardButton(text="За помощью")
        ],
        [
            KeyboardButton(text="Назадд")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

menustartrus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="Дополнительный")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

Yordamuchun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱Telefon nomer", request_contact=True),
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

textdiniy1 = (f"1. Qur'oni karimga oid kitoblar (Tafsiri Hilol, Tafsiri Irfon, Qur'oni karim ma'nolarining tarjimalari).\n"
f"2. Hadis kitoblari (Oltin Silsila, Hadis va Hayot, Riyozus-solihiyn va boshqa hadis kitoblari).\n"
f"3. O‘zbek davlatchiligiga oid kitoblar (Konstitutsiya, Prezident asarlari, qonunlar va h.k.).\n"
f"4. Hazrati Alisher Navoiy va boshqa mumtoz adabiyotimizga tegishli asarlar.\n"
f"5. Al-Adab Al-Mufrad (Imom Buxoriy).\n"
f"6. Muxtasarul viqoya (Kifoya) (Shayx Muhammad Sodiq Muhammad Yusuf).\n"
f"7. Ibodati Islomiya (Ahmad Hodiy Maqsudiy).\n"
f"8. Sunniy aqidalar (Shayx Muhammad Sodiq Muhammad Yusuf).\n"
f"9. Payg‘ambarlar tarixi Islom tarixidir (Rahmatulloh Obidov).\n"
f"10. O‘tkan kunlar, Mehrobdan chayon (Abdulla Qodiriy).\n")

textdiniy2 = (f"11. Turkiston qayg‘usi (Alixonto‘ra Sog‘uniy).\n"
f"12. Qazo bo‘lgan namoz (Xurshid Do‘stmuhammmad).\n"
f"13. Boburnoma (Zahiriddin Muhammad Bobur).\n"
f"14. Iqrornoma, Urush va tinchlik (Lev Tolstoy).\n"
f"15. Yulduzli tunlar, Ajdodlar dovoni (Pirimqul Qodirov).\n"
f"16. Tarixi Muhammadiy (Alixonto‘ra Sog‘uniy).\n"
f"17. Graf Monte Kristo (Aleksandr Dyuma).\n"
f"18. Robinzon Kruzo va uning sarguzashtlari (Daniyel Defo).\n"
f"19. Usta va Margarita (Mixail Bulgakov).\n"
f"20. Shohnoma (Firdavsiy).\n")

textilmiy1 = (f"1- 1984, Jorj Oruell\n"
f"2- tubsizlikka olov, Vernor vinge\n"
f"3- o'yinchi, Iain M. Banks\n"
f"4- Enderning o'yini, Orson Scott Card\n"
f"5- qor halokati, Nil stivenson\n"
f"6- Starship Troopers, Robert A. Xaynlayn\n"
f"7- Dune, Frank Xerbert\n"
f"8- Ubik, Filipp K. Dik\n"
f"9- Anatema, Nil stivenson\n"
f"10- Avtostopchilar uchun Galaktika bo'yicha qo'llanma, Duglas Adams\n")

textilmiy2 = (f"11- Olamlar urushi, Jorj Uells\n"
f"12- cheksiz urush, Jou Xaldeman\n"
f"13- eski qorovul, Jon skalzi\n"
f"14- Portiko, Frederik pohl\n"
f"15- Solaris, Stanislav Lem\n"
f"16- yengilmas, Stanislav Lem\n"
f"17- 2001 yil: Kosmik odisseya, Artur C. Klark\n"
f"18- Triffidlar kuni, John Wyndham\n"
f"19- Mars yilnomalari, Rey Bredberi\n"
f"20- gumanoidlar, Jek Uilyamson\n")

textbadiiy1 = (f"Garri Potter – muallif: Joanna Rouling\n"
f"Uzuklar hukmdori – muallif: Jon Tolkien\n"
f"Kichkina shahzoda – muallif: Antuan de Sent-Ekzyuperi\n" 
f"Da Vinchi siri – muallif: Den Braun\n"
f"Alkimyogar – muallif: Paulo Koelo\n"
f"Yashil yo`lak – muallif: Stiven King\n"
f"Shamollarda qolgan hislarim – muallif: Margaret Mitchell\n"
f"Usta va Margarita – muallif: Mixail Bulgakov\n"
f"Uch og`ayni – muallif: Erix Mariya Remark\n")

textbadiiy2 = (f"Dorian Grey portreti – muallif: Oskar Uayld\n"
f"Anna Frankning kundaligi – muallif: Anna Frank\n"
f"Jarliklabi javdarzordagi haloskor – muallif: Jeerom Devid Selindjer\n"
f"Andisha va g`urur – muallif: Jeyn Ostin\n"
f"Buyuk Getsbi – muallif: Frensis Skott Fisjerald\n"
f"Alisa mo`jizalar mamlakatida – muallif: Lyuis Keroll\n")