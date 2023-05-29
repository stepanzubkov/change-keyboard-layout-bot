# Change keyboard layout bot

![](https://www.gnu.org/graphics/gplv3-127x51.png)

This vk bot changes layout of reply message.

# Commands

`<prefix>layout <layout>` or `<prefix>раскладка <layout>` - Changes layout of reply message. Prefix must be `!` or `/`.

Avaliable layouts:
1. en (ен)
2. ru (ру)


Examples:
1. `!layout ru`: "Lj,hjt enhj? rjkktub!" -> "Доброе утро, коллеги!"
2. `/раскладка ен`: "Руддщ цщкдвб руддщ кшсрфквю" -> "Hello world, hello richard."

# Screenshots

![](https://i.postimg.cc/BbvWLG1N/Screenshot-20230528-223658.png)

![](https://i.postimg.cc/WtRDpSdN/Screenshot-20230528-223421.png)

# Embed in your bot

This bot is made with vkbottle framework.

WARNING: If you want to use this bot in your own bot, you should release your bot with a GNU GPL v3-or-later license (for details, read license conditions in `COPYING` file)

1. Clone this repo:
`git clone https://github.com/stepanzubkov/change-keyboard-layout-bot.git`

2. Copy routes from `src/routes/` folder to your vkbottle routes.
3. Load routes in your bot (see `src/main.py` and vkbottle docs)

That's all! You embedded this bot into your bot!

# Contributions

This bot is licensed under GNU GPL v3 or later. Feel free to leave an issue or send a pull request.

Contacts: Stepan Zubkov <stepanzubkov@florgon.com>
