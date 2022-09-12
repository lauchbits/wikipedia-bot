from optparse import Option
import discord, wikipedia, os
from discord import Option

bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"/random | {len(bot.guilds)} servers"))
    print(f"Logged in as {bot.user}")


@bot.slash_command(name = "search", description = "Search Wikipedia")
async def search(ctx, search: Option(str, description = "What do you want to search for)", required = True)):
    await ctx.channel.trigger_typing()
    try:
        title = wikipedia.search(search)[0]
        summary = wikipedia.summary(title, sentences = 5)
        link = wikipedia.page(title).url
        try:
            await ctx.respond(f"**{title}** \n\n{summary}\n\n{link}")
        except:
            await ctx.send(f"**{title}** \n\n{summary}\n\n{link}")
    except:
        try:
            await ctx.respond(f"Couldn't find an article called {search}")
        except:
            await ctx.send(f"Couldn't find an article called {search}")
    

@bot.slash_command(name = "random", description = "Returns a random Wikipedia article")
async def random(ctx):
    await ctx.channel.trigger_typing()
    randomtitle = wikipedia.random()
    randomsummary = wikipedia.summary(randomtitle, sentences = 5)
    link = randomtitle.replace(' ', '_')
    try:
        await ctx.respond(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")
    except:
        await ctx.send(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")

bot.run(os.environ["DISCORD_TOKEN"])
