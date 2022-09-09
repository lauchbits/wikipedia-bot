import discord, wikipedia

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We've logged in as {bot.user}.")

testing = [744661575360577576]

@bot.slash_command(guild_ids = testing, name = "random", description = "Returns a random Wikipedia article")
async def random(ctx):
    await ctx.channel.trigger_typing()
    randomtitle = wikipedia.random()
    randomsummary = wikipedia.summary(randomtitle, chars = 1950)
    link = randomtitle.replace(' ', '_')
    try:
        await ctx.respond(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")
    except:
        await ctx.send(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")

bot.run('MTAxNzg1NzE4MTA2MTc2MzA3Mw.GbMjq_.qyjJuBX888efnWpbxKhYAOmuyJZ60UISBm9hi4')