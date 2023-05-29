"""
Services for changing layout.
Copyright © 2023 Stepan Zubkov <stepanzubkov@florgon.com>
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

from typing import Dict, Tuple

UNICODE_EN_LETTERS_RANGE = range(65, 123)
UNICODE_RU_LETTERS_RANGE = range(1040, 1104)


def change_keyboard_layout(text: str, lang_pair: Tuple[str, str]) -> str:
    """
    Changes keyboard layout of text to specified lang.
    :param str text: text
    :param str lang_pair: languages pair to change
    :rtype: str
    :return: text with changed layout
    """
    conversions = get_available_layout_conversions()
    try:
        conversion = conversions[lang_pair]
    except KeyError:
        raise ValueError(f"{lang_pair[0]}-{lang_pair[1]} conversion is not available! It can be one of: {conversions.keys()}")
    else:
        return text.translate(conversion)


def guess_layout_conversion_name(text: str) -> Tuple[str, str]:
    """
    Guesses keyboard layout name, using ord() on every char.
    :param str text: text
    :rtype: str
    :return: Keyboard layout name (en, ru)
    """
    chars_count = {
        "en": 0, "ru": 0,
    }
    for char in text:
        if ord(char) in UNICODE_EN_LETTERS_RANGE:
            chars_count["en"] += 1
        elif ord(char) in UNICODE_RU_LETTERS_RANGE:
            chars_count["ru"] += 1

    from_layout = max(chars_count.items(), key=lambda pair: pair[1])[0]
    if from_layout != "en":
        return (from_layout, "en")
    return ("en", "ru")


def get_available_layout_conversions() -> Dict[Tuple[str, str], Dict[int, str]]:
    en_symbols = "qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?~"
    ru_symbols = "йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё"
    return {
        ("ru", "en"): _construct_translate_dict(ru_symbols, en_symbols),
        ("en", "ru"): _construct_translate_dict(en_symbols, ru_symbols),
    }

def _construct_translate_dict(from_: str, to: str) -> Dict[int, str]:
    return dict(zip(map(ord, from_), to))


