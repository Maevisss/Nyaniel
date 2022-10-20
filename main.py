import discord
from discord.ext import commands

#Discord.py 2.0
#Python 3.10


bot = commands.Bot(command_prefix='<', intents=discord.Intents.all())

@bot.event
async def on_ready() :
    print('Nyaniel Jung ist online!')
    await bot.change_presence(activity=discord.Game(name='<edelgase'))

@bot.event
async def on_command_error(ctx, error) :
    if isinstance (error, commands.MissingRequiredArgument) :
        await ctx.channel.send('Schreib wenigstens URI sonst sende ich das nicht rüber.')
        return

@bot.command()
async def edelgase(ctx) :
    with open('info.txt', 'r', encoding='utf_8') as info_file :
        info = info_file.read()
    await ctx.channel.send(info)


@bot.command()
async def send(ctx, *, arg) :
    with open('gc_channel_id.txt', 'r') as GCID :
        gc_id = GCID.read()
    gc_channel = bot.get_channel(int(gc_id))

    with open('sfd_channel_id.txt', 'r') as SFDID :
        sfd_id = SFDID.read()
    sfd_channel = bot.get_channel(int(sfd_id))


    with open('sfd_guild_id.txt', 'r') as SFDGID :
        sfd_guild_id = SFDGID.read()
    guild_id = ctx.message.author.guild

    User = str(ctx.message.author)
    
    guild_id = ctx.message.guild.id

    flak = 0
    if not ctx.message.attachments :
        flak = 0
    else :
        attachment = ctx.message.attachments[0]
        flak = 1

    if (guild_id == int(sfd_guild_id)) :
        await gc_channel.send(User + " : \n" + arg)
        if flak == 1 :
            await gc_channel.send(attachment)
    else :
        await sfd_channel.send(User + " : \n" + arg)
        if flak == 1 :
            await sfd_channel.send(attachment)


with open('Token.txt', 'r') as TokenFile :
    Token = TokenFile.read() 
bot.run(Token)