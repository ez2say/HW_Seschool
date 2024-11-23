import asyncio
from datetime import datetime
from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from collections import defaultdict

token = TOKEN

bot = Bot(token=token)

dp = Dispatcher()

tasks = defaultdict(list)

notification_tasks = []

reset_time = datetime.strptime("00:00", "%H:%M").time()


def get_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Добавить задачу"))
    builder.add(types.KeyboardButton(text="Удалить задачу"))
    builder.add(types.KeyboardButton(text="Показать задачи"))
    builder.add(types.KeyboardButton(text="Отчистить список задач"))
    builder.add(types.KeyboardButton(text="Обновить время автоматического удаления задач"))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


class TaskState(StatesGroup):
    adding_task = State()
    removing_task = State()
    setting_reset_time = State()
    notifying_task = State()
    postponing_task = State()


@dp.message(Command('start'))
async def start_handler(message: types.Message):
    await message.reply("Бонжур! Я бот для составления плана дня. Вот что я могу:", reply_markup=get_keyboard())


@dp.message(lambda message: message.text == "Добавить задачу")
async def add_task_handler(message: types.Message, state: FSMContext):
    await message.reply("Введите время и описание задачи в формате: вре:мя описание")
    await state.set_state(TaskState.adding_task)


@dp.message(lambda message: message.text == "Удалить задачу")
async def remove_task_handler(message: types.Message, state: FSMContext):
    await message.reply("Введите время задачи, которую хотите удалить в формате: вре:мя")
    await state.set_state(TaskState.removing_task)


@dp.message(lambda message: message.text == "Показать задачи")
async def show_tasks_handler(message: types.Message):
    user_tasks = tasks[message.chat.id]
    if not user_tasks:
        await message.reply("У вас нет задач на сегодня.")
        return

    user_tasks.sort(key=lambda x: x[0])
    task_list = "\n".join([f"{time.strftime('%H:%M')} - {description}" for time, description in user_tasks])
    await message.reply(f"Ваши задачи на сегодня:\n{task_list}")


@dp.message(lambda message: message.text == "Отчистить список задач")
async def clear_tasks_handler(message: types.Message):
    tasks[message.chat.id] = []
    await message.reply("Весь план дня очищен.")


@dp.message(lambda message: message.text == "Обновить время автоматического удаления задач")
async def set_reset_time_handler(message: types.Message, state: FSMContext):
    await message.reply("Введите время сброса задач в формате: вре:мя")
    await state.set_state(TaskState.setting_reset_time)


@dp.message(TaskState.adding_task)
async def process_add_task(message: types.Message, state: FSMContext):
    try:
        time, description = message.text.split(' ', 1)
        time = datetime.strptime(time, '%H:%M').time()
        tasks[message.chat.id].append((time, description))
        await message.reply(f"Задача '{description}' добавлена на {time}")

        current_time = datetime.now().time()
        if time > current_time:
            notification_time = (datetime.combine(datetime.today(), time) - datetime.combine(datetime.today(), current_time)).total_seconds()
            notification_tasks.append(asyncio.create_task(send_notification(message.chat.id, description, notification_time)))

        await state.clear()
    except ValueError:
        await message.reply("Неверный формат команды. Используйте: вре:мя описание")


@dp.message(TaskState.removing_task)
async def process_remove_task(message: types.Message, state: FSMContext):
    try:
        time = datetime.strptime(message.text, '%H:%M').time()
        tasks[message.chat.id] = [(t, desc) for t, desc in tasks[message.chat.id] if t != time]
        await message.reply(f"Задача на {time} удалена.")
        await state.clear()
    except ValueError:
        await message.reply("Неверный формат команды. Используйте: вре:мя")


@dp.message(TaskState.setting_reset_time)
async def process_set_reset_time(message: types.Message, state: FSMContext):
    global reset_time
    try:
        reset_time = datetime.strptime(message.text, '%H:%M').time()
        await message.reply(f"Время сброса задач установлено на {reset_time.strftime('%H:%M')}")
        await state.clear()
    except ValueError:
        await message.reply("Неверный формат команды. Используйте: вре:мя")


async def send_notification(chat_id, description, delay):
    await asyncio.sleep(delay)
    await bot.send_message(chat_id, f"Напоминание: '{description}'", reply_markup=get_notification_keyboard())


def get_notification_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Ок", callback_data="ok"))
    builder.add(types.InlineKeyboardButton(text="Перенести", callback_data="postpone"))
    return builder.as_markup()


def get_postpone_keyboard():
    builder = InlineKeyboardBuilder()
    for minutes in [10, 20, 30, 40, 50, 60]:
        builder.add(types.InlineKeyboardButton(text=f"{minutes} минут", callback_data=f"postpone_{minutes}"))
    return builder.as_markup()


@dp.callback_query(lambda c: c.data == "ok")
async def process_ok_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Задача отмечена как выполненная.", reply_markup=None)
    await state.clear()


@dp.callback_query(lambda c: c.data == "postpone")
async def process_postpone_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выберите время для переноса:", reply_markup=get_postpone_keyboard())
    await state.set_state(TaskState.postponing_task)


@dp.callback_query(lambda c: c.data.startswith("postpone_"))
async def process_postpone_minutes_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    minutes = int(callback_query.data.split("_")[1])
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=f"Задача будет перенесена на {minutes} минут.", reply_markup=None)
    await state.clear()
    notification_tasks.append(asyncio.create_task(send_notification(callback_query.message.chat.id, callback_query.message.text, minutes * 60)))


async def reset_tasks():
    while True:
        now = datetime.now().time()
        if now >= reset_time:
            for chat_id in tasks:
                tasks[chat_id] = []
            await asyncio.sleep(86400 - (datetime.combine(datetime.today(), now) - datetime.combine(datetime.today(), reset_time)).total_seconds())
        else:
            await asyncio.sleep((datetime.combine(datetime.today(), reset_time) - datetime.combine(datetime.today(), now)).total_seconds())


async def main():
    await dp.start_polling(bot)
    asyncio.create_task(reset_tasks())

asyncio.run(main())