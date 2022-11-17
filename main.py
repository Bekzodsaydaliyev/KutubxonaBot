from aiogram import executor
import logging
from config import *
from inline import *
from reply import *





logging.basicConfig(level=logging.INFO)

#Kirish
@dp.message_handler(commands="start")
async def start(msg: Message):
    await msg.answer(f"<b>Tilni tanlang...</b>\n"
                     f"<b>Выберите язык...</b>\n", parse_mode='html', reply_markup=Inkirish)
    await msg.delete()

@dp.callback_query_handler(text="uzb")
async def uzb(call: CallbackQuery):
    await call.message.answer_photo(open("image/photo_2022-08-23_15-48-15.jpg", "rb"))
    await call.message.answer(f"<i><b>Assalomu alekum Kitoblar botiga Xush kelibsiz</b></i>\n"
                              f"<i><b>Ham diniy, ham dunyoviy ilm olavering. Yaxshi emasmi, dinni yaxshi tushunadiganlar bir binoni boshlig'i bo'lsa?Yaxshi emasmi, diniy ilmi kuchlilar 'katta lavozimda' o'tirsa? Din yuksalmaydimi axir, din kengroq yoyilmaydimi shunda?</b></i>\n"
                              f"<i><b>Bu yerda siz turli xildagi kitoblarni yuklab olishingiz mumkin</b></i>\n", parse_mode='html', reply_markup=menustart)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text_contains="rus")
async def rus(call: CallbackQuery):
    await call.message.answer_photo(open("image/photo_2022-08-23_15-48-15.jpg", "rb"))
    await call.message.answer(f"<i><b>Привет и добро пожаловать в книжный бот</b></i>\n", parse_mode='html', reply_markup=menustartrus)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.message_handler(text="Orqaga")
async def orqaga(msg: Message):
    await msg.answer(f"<b>Orqaga.........................</b>", parse_mode='html', reply_markup=menustart)
    await msg.delete()

@dp.callback_query_handler(text="orqaga_qaytish_start")
async def orqaga_qaytish_start(call: CallbackQuery):
    await call.message.answer(f"<i><b>Back....📝...</b></i>", parse_mode='html', reply_markup=menustart)

@dp.callback_query_handler(text="orqaga_qaytish_start_rus")
async def orqaga_qaytish_start_rus(call: CallbackQuery):
    await call.message.answer(f"<i><b>Back....📝...</b></i>", parse_mode='html', reply_markup=menustartrus)

@dp.message_handler(text="Ortga")
async def ortga(msg: Message):
    await msg.answer(f"<b>Ortga...................</b>", parse_mode='html', reply_markup=Inkirish)
    await msg.delete()

@dp.message_handler(text="Menu")
async def menu(msg: Message):
    await msg.answer(f"<b>Menyu...</b> Tanlang📌....", parse_mode='html', reply_markup=Instart)
    await msg.delete()

@dp.message_handler(text="Qo'shimcha")
async def qoshimcha(msg: Message):
    await msg.answer(f"<b>Yordam...</b>\n"
                     f"<b>Sizga yordam kerak bo'lsa yoki qo'shimcha takliflar bo'lsa ushbu {+998770001732} nomerga murojaat qilishingiz mumkin</b>", parse_mode='html', reply_markup=menuqoshimcha)
    await msg.delete()

@dp.message_handler(text="Меню")
async def menurus(msg: Message):
    await msg.answer(f"<b>Меню......</b>", parse_mode='html', reply_markup=Instartrus)
    await msg.delete()

@dp.message_handler(text="Назад")
async def orqagarus(msg: Message):
    await msg.answer(f"<b>Назад.....</b>", parse_mode='html', reply_markup=Inkirish)
    await msg.delete()

@dp.message_handler(text="Дополнительный")
async def qoshimcharus(msg: Message):
    await msg.answer(f"<b>Помощь...</b>"
                     f"<b>Свяжитесь с этим номером +998770001732, если вам нужна помощь или есть дополнительные предложения</b>", parse_mode='html', reply_markup=menuqoshimcharus)
    await msg.delete()

@dp.callback_query_handler(text="ochirish")
async def ochirish(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.message_handler(text="Назадд")
async def orqagaaa(msg: Message):
    await msg.answer(f"<b>Назадд....</b>", parse_mode='html', reply_markup=menustartrus)

@dp.message_handler(text="Список книг")
async def royxat(msg: Message):
    await msg.answer(textdiniy1)
    await msg.answer(textdiniy2)
    await msg.answer(textilmiy1)
    await msg.answer(textilmiy2)
    await msg.answer(textbadiiy1)
    await msg.answer(textbadiiy2, reply_markup=menuqoshimcharus)

@dp.message_handler(text="Kitoblar ro'yxati")
async def royxatuzb(msg: Message):
    await msg.answer(textdiniy1)
    await msg.answer(textdiniy2)
    await msg.answer(textilmiy1)
    await msg.answer(textilmiy2)
    await msg.answer(textbadiiy1)
    await msg.answer(textbadiiy2, reply_markup=menuqoshimcha)

@dp.message_handler(text="Yordam uchun")
async def yordam_uchun(msg: Message):
    await msg.answer(f"<b>Yordam uchun....</b>\n"
                     f"Siz bilan tezda aloqaga chiqamiz!!!", parse_mode='html', reply_markup=Yordamuchun)
    await msg.delete()

@dp.message_handler(text="Back")
async def back(msg: Message):
    await msg.answer(f"<b>Ortga.......</b>", parse_mode='html', reply_markup=menustart)
#--------------------------------------------------------------------------------------------
#diniy
@dp.callback_query_handler(text="diniy")
async def diniyy(call: CallbackQuery):
    await call.message.answer(textdiniy1, reply_markup=InDiniy1)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="diniy1ga")
async def diniyy1(call: CallbackQuery):
    await call.message.answer(textdiniy2, reply_markup=InDiniy2)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="1diniy")
async def diniy1(call: CallbackQuery):
    await call.message.answer_document(open("diniy/40 hadis. (Topishmoqli).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="2diniy")
async def diniy2(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Anbiyolar qissasi.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="3diniy")
async def diniy3(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Ichingdagi ichingdadir.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="4diniy")
async def diniy4(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Imom G'azzoliy. Ey farzand.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="5diniy")
async def diniy5(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Imom Zarnujiy. Ilm olish sirlari.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="6diniy")
async def diniy6(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Millioner singari fikrlashni o‘rganing [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="7diniy")
async def diniy7(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Muhammad alayhissalomning bolaligi [@e_kutubxona].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="8diniy")
async def diniy8(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Mukoshafat-ul qulub [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="9diniy")
async def diniy9(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Sahih Buxoriy -1 (uzbekcha).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="10diniy")
async def diniy10(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Sahih Buxoriy -2 (uzbekcha).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="11diniy")
async def diniy11(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Sahih Buxoriy -3 (uzbekcha).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="12diniy")
async def diniy12(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Sahih Buxoriy -4 (uzbekcha).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="13diniy")
async def diniy13(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Tarixi Muhammadiy [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="14diniy")
async def diniy14(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Зеҳн_ва_хотирани_кучайтирувчи_омиллар1.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="15diniy")
async def diniy15(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Зиёвуддин_Раҳим_Бола_одоби_билан_азиз.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="16diniy")
async def diniy16(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Оилада бахтга эришиш йўллари.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="17diniy")
async def diniy17(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Онага яхшилик қилишнинг 150 усули.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="18diniy")
async def diniy18(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Muhammad alayhissalomning bolaligi [@e_kutubxona].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="19diniy")
async def diniy19(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Imom G'azzoliy. Ey farzand.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="20diniy")
async def diniy20(call: CallbackQuery):
    await call.message.answer_document(open("diniy/Millioner singari fikrlashni o‘rganing [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)
#--------------------------------------------------------------------------------------------
#ilmiy

@dp.callback_query_handler(text="ilmiy")
async def ilmiyy(call: CallbackQuery):
    await call.message.answer(textilmiy1, reply_markup=InIlmiy1)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="ilmiy2ga")
async def ilmiyy1(call: CallbackQuery):
    await call.message.answer(textilmiy2, reply_markup=InIlmiy2)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="1ilmiy")
async def ilmiy1(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Anna Karenina [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="2ilmiy")
async def ilmiy2(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Bozor dunyo (roman).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="3ilmiy")
async def ilmiy3(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Hukmdor Makiavelli(Kutubxona).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="4ilmiy")
async def ilmiy4(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Ikki eshik orasi (O`tkir Hoshimov) @worldof_books.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="5ilmiy")
async def ilmiy5(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Ilk qadam Davlat dasturi  o‘zbek 24.08.18.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="6ilmiy")
async def ilmiy6(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Kitobxonlik tanloviga.doc", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="7ilmiy")
async def ilmiy7(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/lidirlar kitobi @bookshelf_pdf.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="8ilmiy")
async def ilmiy8(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Maqsad sari tezlikni 1000 ga oshiramiz!.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="9ilmiy")
async def ilmiy9(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Martin Iden [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="10ilmiy")
async def ilmiy10(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Matematika master. J.S.Toshpo'latov. Toshkent-2020.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="11ilmiy")
async def ilmiy11(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Matematika tarixi (A.Normatov).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="12ilmiy")
async def ilmiy12(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/O'zingni angla.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="13ilmiy")
async def ilmiy13(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/O'zingni angla.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="14ilmiy")
async def ilmiy14(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Ikki eshik orasi (O`tkir Hoshimov) @worldof_books.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="15ilmiy")
async def ilmiy15(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Kitobxonlik tanloviga.doc", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="16ilmiy")
async def ilmiy16(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Hukmdor Makiavelli(Kutubxona).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="17ilmiy")
async def ilmiy17(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Matematika master. J.S.Toshpo'latov. Toshkent-2020.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="18ilmiy")
async def ilmiy18(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Ilk qadam Davlat dasturi  o‘zbek 24.08.18.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="19ilmiy")
async def ilmiy19(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Ilk qadam Davlat dasturi  o‘zbek 24.08.18.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="20ilmiy")
async def ilmiy20(call: CallbackQuery):
    await call.message.answer_document(open("ilmiy/Matematika master. J.S.Toshpo'latov. Toshkent-2020.pdf", "rb"))
    await call.answer(cache_time=30)
#--------------------------------------------------------------------------------------------
#badiiy
@dp.callback_query_handler(text="badiiy")
async def badiiyy(call: CallbackQuery):
    await call.message.answer(textbadiiy1, reply_markup=InBadiiy1)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="badiiy2ga")
async def badiiyy1(call: CallbackQuery):
    await call.message.answer(textbadiiy1, reply_markup=InBadiiy1)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="1badiiy")
async def badiiy1(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/1.O'tkir Hoshimov- Dunyoning ishlari.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="2badiiy")
async def badiiy2(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Abadiyat qonuni [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="3badiiy")
async def badiiy3(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Ahmad Lutfiy Qozonchi. Saodat asri qissalari. 1-kitob.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="4badiiy")
async def badiiy4(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Ahmad Lutfiy Qozonchi. Saodat asri qissalari. 2-kitob.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="5badiiy")
async def badiiy5(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Ahmad Lutfiy Qozonchi. Saodat asri qissalari. 3-kitob.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="6badiiy")
async def badiiy6(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Ahmad Lutfiy Qozonchi. Saodat asri qissalari. 4-kitob.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="7badiiy")
async def badiiy7(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Amina Shanliko'g'li. Vijdon azobi (qissa).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="8badiiy")
async def badiiy8(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Chol va dengiz [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="9badiiy")
async def badiiy9(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Dorian Greyning portreti [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="10badiiy")
async def badiiy10(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Faqat ahmoqlargina sakkiz soat uxlaydi.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="11badiiy")
async def badiiy11(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Kecha va kunduz (Cho'lpon) @worldof_books.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="12badiiy")
async def badiiy12(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Telba [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="13badiiy")
async def badiiy13(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Tog'ay Murod. Ot kishnagan oqshom (qissalar, 1994).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="14badiiy")
async def badiiy14(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Yolg‘izlikning yuz yili [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="15badiiy")
async def badiiy15(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Zamonamiz qahramoni [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="16badiiy")
async def badiiy16(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Марио Пьюзо.Энг сара асарлари..pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="17badiiy")
async def badiiy17(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Kecha va kunduz (Cho'lpon) @worldof_books.pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="18badiiy")
async def badiiy18(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Tog'ay Murod. Ot kishnagan oqshom (qissalar, 1994).pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="19badiiy")
async def badiiy19(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Telba [@kitoblar_pdf].pdf", "rb"))
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="20badiiy")
async def badiiy20(call: CallbackQuery):
    await call.message.answer_document(open("badiiy/Amina Shanliko'g'li. Vijdon azobi (qissa).pdf", "rb"))
    await call.answer(cache_time=30)
#--------------------------------------------------------------------------------------------

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
