import random
async def set_pronouns(commands, bot, conf, message, rm):
    success_messages = ['noted, i\'ll use them for you!', 'thank you for telling me, i\'ll remember them!']
    failure_messages = ['i\'m afraid i don\'t know these', 'oh i don\'t know this set...', 'oh i have no idea what these are, sorry']
    known_sets = {
        'they/them': [{
            'subjective': 'they',
            'objective': 'them',
            'posdet': 'their',
            'posprn': 'theirs',
            'reflexive': 'themself',
        }],
        'she/her': [{
            'subjective': 'she',
            'objective': 'her',
            'posdet': 'her',
            'posprn': 'hers',
            'reflexive': 'herself',
        }],
        'he/him': [{
            'subjective': 'he',
            'objective': 'him',
            'posdet': 'his',
            'posprn': 'his',
            'reflexive': 'himself',
        }],
        'she/they': ['she/her', 'they/them'],
        'he/they': ['he/him', 'they/them'],
        'he/she': ['he/him', 'she/her'],
        'he/she/they': ['he/him', 'she/her', 'they/them']
    }
    if rm.group(2) in known_sets:
        # replace pronoun sets for combined pronouns
        for i in range(len(known_sets[rm.group(2)])):
            if type(known_sets[rm.group(2)][i]) == str:
                known_sets[rm.group(2)][i] = known_sets[known_sets[rm.group(2)][i]]
        # set userdata
        bot.set_user_data(message.author.id, 'pronouns', known_sets[rm.group(2)])
        await message.channel.send(random.choice(success_messages))
    else:
        split_prns = rm.group(2).split('/')
        if len(split_prns) == 5:
            bot.set_user_data(message.author.id, 'pronouns', {
                'subjective': split_prns[0],
                'objective': split_prns[1],
                'posdet': split_prns[2],
                'posprn': split_prns[3],
                'reflexive': split_prns[4],
            })
            await message.channel.send(random.choice(success_messages))
        else:
            await message.channel.send(random.choice(failure_messages) + '\ntry giving me all 5 of your pronouns following this example: they/them/their/theirs/themself')

command = {
    'example': 'my pronouns are/i use <pronoun set>',
    'help_text': f'lets me know about your pronouns so i can use them for you',
    'regex': '(my +pronouns +are|i +use) +(.+)',
    'function': set_pronouns
}