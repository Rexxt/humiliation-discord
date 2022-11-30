async def say(commands, bot, conf, message, rm):
    what_to_say = rm.group(1)
    say_stealthily = True if rm.group(2) else False

    await message.channel.send(what_to_say)
    if say_stealthily:
        await message.delete()

command = {
    'example': 'say <something> [stealthily/anonymously]',
    'help_text': 'repeats what you tell me to',
    'regex': 'say +(.+)( +stealthily|anonymously)?',
    'function': say
}