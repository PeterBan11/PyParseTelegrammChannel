from telethon import TelegramClient
import asyncio
import re

api_id = 29802755
api_hash = '34378fb1ee29d072a1e0c731f0310d73'
phone = '+79777058927'

# Название или ссылка на группу
group_username = 'https://t.me/nurstream'  # например, 'mygroup' или 'https://t.me/mygroup'

# Создаем клиента
client = TelegramClient('session_name', api_id, api_hash)

# Файл для сохранения
output_file = 'parsed_messages.txt'

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone=phone)

    # Получаем объект группы
    entity = await client.get_entity(group_username)

    # Открываем файл для записи
    with open(output_file, 'w', encoding='utf-8') as f:
        # Получаем все сообщения (или ограничение по количеству)
        async for message in client.iter_messages(entity):
            if message.text:
                text = message.text

                # Проверяем наличие ключевых элементов или шаблонов
                # Например, ищем "#литейка" или другие признаки
                if '#литейка' in text.lower() or re.search(r'\d+\.', text):
                    # Можно добавить дополнительные условия фильтрации по шаблонам
                    f.write(f"{message.date} - {message.sender_id}:\n{text}\n\n")
                    f.write(f"----------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Записано сообщение от {message.date}")



# Запуск асинхронной функции
asyncio.run(main())