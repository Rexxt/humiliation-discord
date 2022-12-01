# humiliation-discord
HUMILIATION (HUman MachIne Language-based InterAcTION) is a Discord bot engine that parses commands written in human language.

## Why?
HUMILIATION was created to experiment with human-bot interaction using human language instead of traditional commands, making talking to a bot much more natural.

## Origins
A few years ago, [a friend of mine, Oshisaure](https://github.com/Oshisaure), created a bot called `<WEETAD>` (now `<SKWEEK>`), that could respond to diverse commands written in plain English using **Reg**ular **Ex**pressions, all with a comical intent (which, if you know Oshi, is a common occurence). Fast forward to the present day, in 2022: I, Mizu, as the bored nerd I am, decided out of complete boredom but also deep thinking about human-bot interaction to create a general bot engine inspired by `<SKWEEK>`'s functionings, with extreme modularity (in true Mizu fashion). I'll then use this engine to develop my bot, [Hachi](https://github.com/Rexxt/hachi-discord), a generalist/Splatoon bot with a developed original character.

## How to use
### Prerequisites
You will need:
* `discord.py` >= 2.1.0
* a `bot.json` file (generated by `setup.py`)
* a `userdata.pickle` file (generated by `main.py` when first starting the bot)
### Starting off
1. Run `setup.py` and follow the instructions. This will create your entire bot.json file, with your token, responses, statuses, your bot's pronouns and most importantly your bot's prefix's regex.
2. Start the bot using `main.py`. You should have a really basic command pallette to demonstrate the bot's functionality (tip: call `<prefix> help` to see the sentences the bot knows.)
3. If you want to add commands to your bot (which you will), refer to the below details.
### Modularity
#### How are modules detected?
The bot will scan over the `commands/` directory and import every Python file of it. Modules are loaded using the `command` variable that defines a help example, a help message, the full regex and the function to use. In the future there might be a possibility to have multiple commands in 1 single file.
#### Creating a module
1. Create a file in `commands/`. Its name doesn't matter.
2. Create your **async** function. It will accept 5 arguments:
   1. The registered command list.
   2. The bot instance itself.
   3. The bot configuration.
   4. The message object.
   5. The regex match object.

For example here's what the included ping command looks like:
```py
import datetime, time
async def ping(commands, bot, conf, message, rm):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-bot.start_time))))
    await message.channel.send(f'''my latency is {round(bot.latency*1000)}ms
i've been up for {uptime} (<t:{round(bot.start_time)}>)''')
```
3. Create your `command` variable. It's a dictionary consisting of 4 keys:
   * `example`: an example of how to call the command. Shown in the included help command.
   * `help_text`: the description of your command. Shown in the included help command.
   * `regex`: the regex the bot should respond to.
   * `function`: the function the command should call.

Here's what the ping command's definition looks like:
```py
command = {
    'example': 'ping/how are you doing',
    'help_text': 'shows information about my status',
    'regex': '(ping|how are you doing)',
    'function': ping
}
```
