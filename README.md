# This is an easy Bot Setup

I will upload much Bot Commands as tar.gz for Python Discord Bots.
Setup the main.py with your own Prefix and import my Pakages

main.py

```python
from discord.ext import commands
from {pakage}.setup_commands import setup_commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

setup_commands(bot)  

//customise your commands here

bot.run('token')
```
