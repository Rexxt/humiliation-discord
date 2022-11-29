async def bot_help(commands, bot, conf, message, rm):
    help_strings = ['here\'s what i can do:\n']
    for command in commands:
        cmd_string = f'● `{command["example"]}`: {command["help_text"]}'
        if len(help_strings[-1] + cmd_string + '\n') > 2000:
            help_strings.append('')
        help_strings[-1] += cmd_string + '\n'
    for hs in help_strings:
        await message.channel.send(hs)

command = {
    'example': 'help (me)',
    'help_text': 'helps around the bot commands',
    'regex': 'help( +me)?',
    'function': bot_help
}