import datetime, time
async def ping(commands, bot, conf, message, rm):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-bot.start_time))))
    await message.channel.send(f'''my latency is {round(bot.latency*1000)}ms
i've been up for {uptime} (<t:{round(bot.start_time)}>)''')

command = {
    'example': 'ping/how are you doing',
    'help_text': 'shows information about my status',
    'regex': '(ping|how +are +you +doing)',
    'function': ping
}