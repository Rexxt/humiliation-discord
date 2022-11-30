import random
async def get_pronouns(commands, bot, conf, message, rm):
    thanks = ["thank you for asking!", "thanks for asking!", "thank you very much for asking!"]
    await message.channel.send(random.choice(['they\'re', 'my pronouns are']) + ' ' + conf['bot_pronouns'] + ', ' + random.choice(thanks))
    if not 'pronouns' in bot.get_all_user_data(message.author.id):
        await message.channel.send(f'you can also teach me your pronouns! ({random.choice(conf["example_prefixes"])} i use <your pronouns>)')

command = {
    'example': '(what\'s/what are) your pronouns/what pronouns do you use',
    'help_text': f'reminds you of my pronouns',
    'regex': '((what\'(s|re)|what are) +your +pronouns|what +pronouns +do +you +use)',
    'function': get_pronouns
}