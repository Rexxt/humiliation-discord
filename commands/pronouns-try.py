import random
from commands.libs import pronouns
async def try_pronouns(commands, bot, conf, message, rm):
    failure_messages = ['i\'m afraid i don\'t know these', 'oh i don\'t know this set...', 'oh i have no idea what these are, sorry']
    pronoun_set_to_try = rm.group(2)
    known_sets = {
        'they/them': [{
            'subjective': 'they',
            'objective': 'them',
            'posdet': 'their',
            'posprn': 'theirs',
            'reflexive': 'themself',
            'conjug': 'plural',
        }],
        'she/her': [{
            'subjective': 'she',
            'objective': 'her',
            'posdet': 'her',
            'posprn': 'hers',
            'reflexive': 'herself',
            'conjug': 'singular',
        }],
        'he/him': [{
            'subjective': 'he',
            'objective': 'him',
            'posdet': 'his',
            'posprn': 'his',
            'reflexive': 'himself',
            'conjug': 'singular',
        }],
        'she/they': ['she/her', 'they/them'],
        'he/they': ['he/him', 'they/them'],
        'he/she': ['he/him', 'she/her'],
        'he/she/they': ['he/him', 'she/her', 'they/them']
    }
    if pronoun_set_to_try in known_sets:
        # replace pronoun sets for combined pronouns
        for i in range(len(known_sets[rm.group(2)])):
            if type(known_sets[rm.group(2)][i]) == str:
                known_sets[rm.group(2)][i] = known_sets[known_sets[rm.group(2)][i]][0]
        print(known_sets[rm.group(2)])
        prns = pronouns.UndefPronouns(known_sets[rm.group(2)])
    elif pronoun_set_to_try == 'my':
        prns = pronouns.UserPronouns(bot, message.author.id)
    else:
        split_prns = rm.group(2).split('/')
        if len(split_prns) == 6:
            prns = pronouns.UndefPronouns([{
                'subjective': split_prns[0],
                'objective': split_prns[1],
                'posdet': split_prns[2],
                'posprn': split_prns[3],
                'reflexive': split_prns[4],
                'conjug': split_prns[5]
            }])
        else:
            await message.channel.send(random.choice(failure_messages) + '\ntry giving me all 5 of your pronouns and the conjugation of verbs following this example: they/them/their/theirs/themself/plural')
            return
    verbs = {
        'be': {
            'singular': 'is',
            'plural': 'are'
        },
        'have': {
            'singular': 'has',
            'plural': 'have'
        },
        'do': {
            'singular': 'does',
            'plural': 'do'
        }
    }
    prns.use(random.randint(0, prns.get_set_number() - 1))
    end_messages = ['how\'s that?', 'sounds good?', 'how does it sound?', 'do you like it?', 'ya like it?', '\'s it sound good?']
    await message.channel.send(f'> i just met {message.author.display_name} today! {prns.subjective} {verbs["be"][prns.conjugation]} a really cool person. that smile of {prns.possessive_pronoun} is always brightening! i really could talk with {prns.objective} all day long, even if {prns.subjective} {verbs["do"][prns.conjugation]}n\'t talk about {prns.reflexive} too much. i hope {prns.possessive_determiner} day was great!')
    await message.channel.send(random.choice(end_messages))

command = {
    'example': 'try out <pronouns> (pronouns)/my pronouns for me',
    'help_text': 'makes me say a test sentence with your specified pronouns',
    'regex': 'try +out +((.+?)( +pronouns)?|my +pronouns) for me',
    'function': try_pronouns
}