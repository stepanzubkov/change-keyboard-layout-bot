"""
VKbottle router that changes layout of reply message.
Copyright © 2023 Stepan Zubkov <stepanzubkov@florgon.com>
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

from typing import Tuple

from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import ReplyMessageRule, CommandRule

from services.layout_changer import change_keyboard_layout, guess_layout_conversion_name

bl = BotLabeler()


@bl.message(ReplyMessageRule(), CommandRule("раскладка", ["!", "/"], 0) | CommandRule("layout", ["!", "/"], 0))
async def handler_guess_and_change_keyboard_layout(message: Message):
    layout = guess_layout_conversion_name(message.reply_message.text)
    await message.reply(change_keyboard_layout(message.reply_message.text, layout))


@bl.message(ReplyMessageRule(), CommandRule("раскладка", ["!", "/"], 1) | CommandRule("layout", ["!", "/"], 1))
async def handler_change_keyboard_layout(message: Message, args: Tuple[str]):
    layout = args[0]
    if layout in ["ru", "ру", "рус", "русская", "russian"]:
        await message.reply(change_keyboard_layout(message.reply_message.text, ("en", "ru")))
    elif layout in ["en", "ен", "англ", "английская", "англиская", "english"]:
        await message.reply(change_keyboard_layout(message.reply_message.text, ("ru", "en")))
    else:
        await message.reply(f"\u2757 Раскладка '{layout}' не поддерживается! Доступные раскладки:\n"
                      f"- en (ен, англ, английская, english)\n"
                      f"- ru (ру, рус, русская, russian)")


