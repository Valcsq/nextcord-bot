import nextcord
intents = nextcord.Intents.default()
intents.message_content = True
client = nextcord.Client(intents=intents)
from nextcord.ext import commands
bot = commands.Bot(command_prefix='$', intents=intents)



@bot.command(name="vip")
async def SendMessage(ctx):
    await ctx.send('Blini: <https://www.roblox.com/games/8304191830?privateServerLinkCode=70793599947811530966944011435717>')
    await ctx.send('Rai: <https://www.roblox.com/share?code=cb177a5e8d1dbd4b88d167f361d38c84&type=Server>')

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")









if __name__ =='__main__':
    bot.run("MTE2OTQwNDU0NDU1NjQ3NDQzOA.G49PTa.sRrrn2djGlf8X5GZpzlVK2pg2qBQh8RI5DNIIc")