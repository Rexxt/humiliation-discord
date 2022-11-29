# script to create the bot.json file for the engine to handle
import json
bot_conf = {}

print('HUMILIATION engine setup')

print('1/11 - What is the bot\'s token?')
uin = ''
while uin == '':
    uin = input('> ')
bot_conf['bot_token'] = uin

print('2/11 - What is the Discord ID of the bot\'s admin?')
uin = ''
while uin == '' or not uin.isdigit():
    uin = input('> ')
bot_conf['admin_id'] = int(uin)

print('3/11 - What are the statuses the bot should pick out at random?\nGive an empty message to stop.')
motds = []
while True:
    uin = input(f'{len(motds)}> ')
    if uin == '':
        break
    motds.append(uin)
bot_conf['motd'] = motds

print('4/11 - What are some example prefixes to show in the status?\nGive an empty line to stop.')
ex = []
while True:
    uin = input(f'{len(ex)}> ')
    if uin == '':
        break
    ex.append(uin)
bot_conf['example_prefixes'] = ex

print('5/11 - What is the actual prefix regex the bot should match against?')
uin = ''
while uin == '' or uin.count('(') != uin.count(')'):
    uin = input('> ')
bot_conf['prefix_regex'] = uin
bot_conf['command_regex_group_number'] = (uin.count('(') + uin.count(')')) // 2 + 1

print('6/11 - What should the bot answer when it is called without a command?\nGive an empty line to stop.')
resp = []
while True:
    uin = input(f'{len(resp)}> ')
    if uin == '':
        break
    resp.append(uin)
bot_conf['empty_call_responses'] = resp

print('7/11 - What should the bot answer when it is called *repetitively* without a command, and is now in an annoyed state?\nGive an empty line to stop.')
resp = []
while True:
    uin = input(f'{len(resp)}> ')
    if uin == '':
        break
    resp.append(uin)
bot_conf['empty_call_responses_annoyed'] = resp

print('8/11 - What should the bot answer when it is called with a command that it doesn\'t know how to handle?\nGive an empty line to stop.')
resp = []
while True:
    uin = input(f'{len(resp)}> ')
    if uin == '':
        break
    resp.append(uin)
bot_conf['unknown_command_responses'] = resp

print('9/11 - What should the bot answer when it is called *repetitively* with a command that it doesn\'t know how to handle, and is now in an annoyed state?\nGive an empty line to stop.')
resp = []
while True:
    uin = input(f'{len(resp)}> ')
    if uin == '':
        break
    resp.append(uin)
bot_conf['unknown_command_responses_annoyed'] = resp

print('10/11 - What are the bot\'s pronouns?')
uin = ''
while uin == '':
    uin = input('> ')
bot_conf['bot_pronouns'] = uin

print('11/11 - What is the bot\'s usage name?')
uin = ''
while uin == '':
    uin = input('> ')
bot_conf['bot_usage_name'] = uin

print('All set! Do you want to write to "bot.json" (w) or output the json config (o)?')
uin = ''
while not uin in ('w', 'o'):
    uin = input('w/o> ')
if uin == 'w':
    with open('bot.json', 'w') as f:
        json.dump(bot_conf, f)
else:
    print(json.dumps(bot_conf))