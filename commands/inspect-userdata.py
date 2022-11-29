def list_to_dict(ls):
    dictionary = {}
    for i in range(len(ls)):
        dictionary[i] = ls[i]
    return dictionary

def repr_dict(dictionary, indent=0):
    string = ''
    for k in dictionary:
        v = dictionary[k]
        if type(v) == dict:
            string += ' '*indent + f'{k} = \n{repr_dict(v, indent+2)}\n'
        elif type(v) == list:
            string += ' '*indent + f'{k} = \n{repr_dict(list_to_dict(v), indent+2)}\n'
        else:
            string += ' '*indent + f'{k} = {v}\n'
    return string

async def userdata(commands, bot, conf, message, rm):
    id_to_get = int(rm.group(1))
    if message.author.id == conf['admin_id']:
        data = bot.get_all_user_data(id_to_get)
        await message.channel.send('here\'s what i know about this user:\n'+repr_dict(data))
    else:
        await message.channel.send('you\'re not my owner!')

command = {
    'example': 'get <id>\'s (saved/user) data',
    'help_text': '(only for bot owner) will let you inspect the user data i\'ve saved',
    'regex': r'get +(\w+)\'s +(saved|user) +data',
    'function': userdata
}