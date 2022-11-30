# This example requires the 'message_content' intent.

import discord, json, random, re, imp, os, time, pickle
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True

if not os.path.exists('bot.json'):
    print('Missing bot config file, use setup.py before starting the bot again.')
    exit(1)

if not os.path.exists('userdata.pickle'):
    with open("userdata.pickle", "wb") as outfile:
 	    # "wb" argument opens the file in binary mode
	    pickle.dump({}, outfile)

with open("userdata.pickle", "rb") as infile:
 	user_data = pickle.load(infile)

bot_conf = json.loads(open('bot.json').read())

bot = discord.Client(intents=intents)

empty_call_cooldowns = {}
unknown_command_cooldowns = {}

def set_user_data(user: int, key: str, value: any) -> dict:
    if not user in user_data:
        user_data[user] = {}
    user_data[user][key] = value
    with open("userdata.pickle", "wb") as outfile:
        pickle.dump(user_data, outfile)
    return user_data[user]

def get_user_data(user: int, key: str) -> any:
    return user_data[user][key]

def get_all_user_data(user: int) -> any:
    return user_data[user]

bot.set_user_data = set_user_data
bot.get_user_data = get_user_data
bot.get_all_user_data = get_all_user_data

@tasks.loop(seconds=60)
async def motd_update():
    motd_string = random.choice(bot_conf['example_prefixes']) + ' help - ' + random.choice(bot_conf['motd'])
    await bot.change_presence(activity=discord.Game(motd_string))
    print('New motd:', motd_string)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # Waiting until the bot is ready
    await bot.wait_until_ready()
    bot.start_time = time.time()
    # Starting the loop
    motd_update.start()


async def bot_help(message, rm):
    help_strings = ['here\'s what i can do:\n']
    for command in commands:
        cmd_string = f'● `{command["example"]}`: {command["help_text"]}'
        if len(help_strings[-1] + cmd_string + '\n') > 2000:
            help_strings.append('')
        help_strings[-1] += cmd_string + '\n'
    for hs in help_strings:
        await message.channel.send(hs)

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    test = re.match(r'^' + bot_conf['prefix_regex'] + r' +(.*)?', message.content.lower())
    if test:
        for command_key in commands:
            command = commands[command_key]
            if re.match(command['regex'], test.group(bot_conf['command_regex_group_number'])):
                await command['function'](commands, bot, bot_conf, message, re.match(command['regex'], test.group(bot_conf['command_regex_group_number'])))
                print(f'{message.author.id} ({message.author.name}#{message.author.discriminator}): triggered command {command_key}')
                unknown_command_cooldowns[message.author.id] = {
                    'calls': 0,
                    'last_call_time': time.time()
                }
                empty_call_cooldowns[message.author.id] = {
                    'calls': 0,
                    'last_call_time': time.time()
                }
                break
        else:
            # didn't understand the command
            if not message.author.id in unknown_command_cooldowns:
                unknown_command_cooldowns[message.author.id] = {
                    'calls': 0,
                    'last_call_time': time.time()
                }
            if unknown_command_cooldowns[message.author.id]['calls'] >= 10:
                if time.time() - unknown_command_cooldowns[message.author.id]['calls'] < 300:
                    pass
                else:
                    unknown_command_cooldowns[message.author.id] = {
                        'calls': 0,
                        'last_call_time': time.time()
                    }
            else:
                if unknown_command_cooldowns[message.author.id]['calls'] >= 5:
                    await message.channel.send(random.choice(bot_conf["unknown_command_responses_annoyed"]))
                else:
                    await message.channel.send(random.choice(bot_conf["unknown_command_responses"]))
                unknown_command_cooldowns[message.author.id] = {
                    'calls': unknown_command_cooldowns[message.author.id]['calls'] + 1,
                    'last_call_time': time.time()
                }
            print(f'{message.author.id} ({message.author.name}#{message.author.discriminator}): unknown command: "{message.content}"')
    else:
        # check if the message *just* contains the prefix
        test = re.match(r'^' + bot_conf['prefix_regex'], message.content.lower())
        if test:
            if not message.author.id in empty_call_cooldowns:
                empty_call_cooldowns[message.author.id] = {
                    'calls': 0,
                    'last_call_time': time.time()
                }
            if empty_call_cooldowns[message.author.id]['calls'] >= 10:
                if time.time() - empty_call_cooldowns[message.author.id]['calls'] < 300:
                    pass
                else:
                    empty_call_cooldowns[message.author.id] = {
                        'calls': 0,
                        'last_call_time': time.time()
                    }
            else:
                if empty_call_cooldowns[message.author.id]['calls'] >= 5:
                    await message.channel.send(random.choice(bot_conf["empty_call_responses_annoyed"]))
                else:
                    await message.channel.send(random.choice(bot_conf["empty_call_responses"]))
                empty_call_cooldowns[message.author.id] = {
                    'calls': empty_call_cooldowns[message.author.id]['calls'] + 1,
                    'last_call_time': time.time()
                }
            print(f'{message.author.id} ({message.author.name}#{message.author.discriminator}): empty call')

commands = {}

# import module commands
for modfile in os.listdir("commands"):
    proper_path = f'commands/{modfile}'
    if os.path.isdir(proper_path) or modfile.startswith('_'):
        continue
    else:
        mod_name, file_ext = os.path.splitext(os.path.split(proper_path)[-1])

        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, proper_path)
        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, proper_path)
        else:
            continue

        if hasattr(py_mod, 'command'):
            commands[mod_name] = py_mod.command
            print('Imported module', mod_name + '.')
        else:
            print('Module', mod_name, 'has no defined command dict.')

print(len(commands), 'total command(s) loaded.')

bot.run(bot_conf['token'])