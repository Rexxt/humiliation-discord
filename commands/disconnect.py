async def disconnect(commands, bot, conf, message, rm):
    if message.author.id == conf['admin_id']:
        await message.channel.send('ok, bai!')
        await bot.close()
    else:
        await message.channel.send('you\'re not my owner!')

command = {
    'example': 'disconnect/log off/log out',
    'help_text': '(only for bot owner) shuts down the bot',
    'regex': '(disconnect|log +(off|out))',
    'function': disconnect
}