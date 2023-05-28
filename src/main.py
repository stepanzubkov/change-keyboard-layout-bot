"""
    Bot that changes keyboard layout.
    Example:
    'Ghbdtn? rfr ltkf&' -> 'Привет, как дела?'
    'Руддщб роц фку нщг,' - 'Hello, how are you?'
"""
from vkbottle import Bot
from routes import labelers

import config

bot = Bot(token=config.VK_BOT_TOKEN)

for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)

bot.run_forever()
