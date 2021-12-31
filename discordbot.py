
import discord
from discord.ext import commands

TOKEN = open("token.txt","r").readline()

bot = commands.Bot(command_prefix='>')
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#bot.run(TOKEN)

class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'l':
            await message.channel.send('pong')

client = MyClient()
client.run(TOKEN)



