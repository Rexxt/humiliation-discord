import random
async def get_pronouns(commands, bot, conf, message, rm):
    thanks = ["thank you for asking!", "thanks for asking!", "thank you very much for asking!"]
    await message.channel.send(random.choice(['they\'re', 'my pronouns are']) + ' ' + conf['bot_pronouns'] + ', ' + random.choice(thanks))
    await message.channel.send('you\'ll be able to teach me your pronouns in the future and i\'ll use them for you!')

command = {
    'example': '(what\'s/what are) your pronouns/what pronouns do you use',
    'help_text': f'reminds you of my pronouns',
    'regex': '((what\'(s|re)|what are) your pronouns|what pronouns do you use)',
    'function': get_pronouns
}