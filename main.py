import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram import F
from aiogram import html
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.formatting import Text, Bold
from datetime import datetime
from aiogram.types import FSInputFile, BufferedInputFile, URLInputFile
from aiogram.utils.media_group import MediaGroupBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6770510552:AAFQ0Wht_VW1LxI_hd_kSwm18_iy-lOatuQ")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# @dp.message(F.text)
# async def echo_with_time(message: Message):
#     time_now = datetime.now().strftime('%H:%M')
#     added_text = html.bold(f"Создано в {time_now}")
#     await message.answer(f"{message.text}\n\n{added_text}", parse_mode="HTML")

@dp.message(F.text == 'Hello')
async def name(message: types.message):
    await message.answer(message.from_user.username)

@dp.message(Command("images"))
async def cmd_image(message: types.message):
    file_ids = []

    with open("bmw-x7.jpg", "rb") as file:
        result = await message.answer_photo(
            BufferedInputFile(
                file.read(),
                filename="image from buffer.jpg"
            ),
            caption="Изображение из буфера")
        file_ids.append(result.photo[-1].file_id)

    image_from_pc = FSInputFile("lexus_gx460_1039136.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )
    file_ids.append(result.photo[-1].file_id)

    image_from_url = URLInputFile("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPHJkHDOuLIip1dqKaD10ePfqo4XL6nk3VCg&usqp=CAU")
    result = await message.answer_photo(
        image_from_url,
        caption="Изображение по ссылке"
    )
    file_ids.append("Отправленные файлы:\n"+"\n".join(file_ids))

@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    await bot.download(
        message.photo[-1],
        destination=f"C://Users//amiha//Desktop//Adilet//{message.photo[-1].file_id}.jpg"
    )
    
    await message.answer("Фото сохранено в desktop")

# @dp.message(F.text == 'Hello')
# async def echo(message: Message):
#     await message.answer(message.text)

# @dp.message(Command("help"))
# async def cmd_help(message: types.Message):
#     await message.answer("Help!")

# @dp.message(Command("wait"))
# async def cmd_help(message: types.Message):
#     await message.answer("Waiting...")

# @dp.message(Command("about"))
# async def cmd_about(message: types.Message):
#     await message.reply("About!")

# @dp.message(Command("dice"))
# async def cmd_dice(message: types.Message):
#     await message.answer(DiceEmoji.DICE)

# @dp.message(Command("dart"))
# async def cmd_dice(message: types.Message):
#     await message.answer(DiceEmoji.DART)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
