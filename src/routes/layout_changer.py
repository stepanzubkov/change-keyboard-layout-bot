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

from transliterate import get_available_language_codes, translit
from transliterate.base import TranslitLanguagePack, registry

bl = BotLabeler()


@bl.message(ReplyMessageRule(), CommandRule("раскладка", ["!", "/"], 1) | CommandRule("layout", ["!", "/"], 1))
async def handler_change_keyboard_layout(message: Message, args: Tuple[str]):
    layout = args[0]
    if args in ["ru", "en", "ру", "ен"]:
        try:
            await message.reply(change_keyboard_layout(message.reply_message.text, layout))
        except ValueError:
            await message.reply(f"\u2757 Раскладка '{layout}' не поддерживается! Доступные раскладки:\n"
                                f"- en (ен)\n"
                                f"- ru (ру)")


def change_keyboard_layout(text: str, lang: str) -> str:
    """
    Changes keyboard layout of text to specified lang.
    """
    if lang not in get_available_language_codes():
        raise ValueError("lang must be one of 'ru', 'en'")

    return translit(text, lang)


class KBDLanguagePack(TranslitLanguagePack):
    language_code = "en-ru"
    language_name = "English-Russian"
    mapping = (
       'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?qwertyuiop[]asdfghjkl;\'zxcvbnm,./',
       'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,йцукенгшщзхъфывапролджэячсмитьбю.',
    )


registry.register(KBDLanguagePack)

