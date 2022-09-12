import discord, wikipedia
import os

bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"/random | {len(bot.guilds)} servers"))
    print(f"Bot is ready")

@bot.slash_command(name = "random", description = "Returns a random Wikipedia article")
async def random(ctx):
    await ctx.channel.trigger_typing()
    randomtitle = wikipedia.random()
    randomsummary = wikipedia.summary(randomtitle, chars = 1950)
    link = randomtitle.replace(' ', '_')
    try:
        await ctx.respond(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")
    except:
        await ctx.send(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")

bot.run(os.environ["DISCORD_TOKEN"])
