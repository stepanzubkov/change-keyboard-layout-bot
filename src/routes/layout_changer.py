"""
    Main bot labeler.
"""
from typing import Tuple

from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import ReplyMessageRule, CommandRule

bl = BotLabeler()


@bl.message(ReplyMessageRule(), CommandRule("раскладка", ["!", "/"], 1) | CommandRule("layout", ["!", "/"], 1))
async def handler_change_heyboard_layout(message: Message, args: Tuple[str]):
    layout = args[0]
    if layout in ["ru", "ру"]:
        await message.reply(change_keyboard_layout(message.reply_message.text, "ru"))
    elif layout in ["en", "ен"]:
        await message.reply(change_keyboard_layout(message.reply_message.text, "en"))
    else:
        await message.reply(f"\u2757 Раскладка '{layout}' не поддерживается! Доступные раскладки:\n"
                      f"- en (ен)\n"
                      f"- ru (ру)")



def change_keyboard_layout(text: str, lang: str) -> str:
    """
    Changes keyboard layout of text to specified lang.
    """
    from_ = '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''
    to = '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''
    if lang == "en":
        from_, to = to, from_
    elif lang != "ru":
        raise ValueError("lang must be one of 'ru', 'en'")
    layout = dict(zip(map(ord, from_), to))
    return text.translate(layout)