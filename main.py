import discord
from discord.ext import commands
import datetime 


bot = commands.Bot(command_prefix='>', description="hi welcome :D ")

@bot.command()
async def ping(ctx,name='ping',help='this command can bot s latency'):  
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    embed = discord.Embed(title=f"Ping.. Pong ..latency is {latency}", description="👌 how fast am i?", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.set_thumbnail(url="https://i.postimg.cc/FH4pGFHR/images.png")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def sum(ctx, numOne: int, numTwo: int,name='sum',help='this command will sums numbers what you insert'):
    output = (numOne + numTwo)
    embed = discord.Embed(title=f"Sum is {output}", description="i ❤ sums", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.set_thumbnail(url="https://i.postimg.cc/XNyV8r9b/download.jpg")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.green()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)
  embed.set_footer(text=ctx.author.name , icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed) 


@bot.command()
async def helpme(ctx):
    embed = discord.Embed(title="COMMANDS LIST", description="Help list", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.add_field(name="command name", value="help")
    embed.add_field(name="Usage", value=">help")
    embed.add_field(name="explained", value="shows this")
    embed.add_field(name="Enjoy!", value="✔bot is coded by subodha prabash")
    embed.set_thumbnail(url="https://i.postimg.cc/sXx0cG8C/868681.png")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)




@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="use >help", url="http://www.twitch.tv/accountname"))
    


@bot.command()
async def iptrack(ctx, ip: str,name='iptrack',help='this command can track ips'):
      from requests import get
      track = get(f'https://ipapi.co/{ip}/json/')
      traced = (track.json())
      await ctx.send(f"```py\ntracked ip is\n{traced}```")
      embed = discord.Embed(title="Track ip easily", description="project on my github", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
      embed.set_thumbnail(url="https://i.postimg.cc/dVy6jkYg/download.png")
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed) 



@bot.command(name='clear', help='this command will clear messages ask author for permission')
async def clear(ctx, amount:int,static=1):
 if ctx.author.id == 780400901553782824 :   
  
    await ctx.channel.purge(limit=amount)
    author = ctx.author.name
    await ctx.send(f"CLEARED {amount} MESSAGES...BY {author} ")
 else:
    await ctx.send('You do not have permission to delete this messages')      
    

@bot.command()
async def print(ctx, *, content:str, name='print',help='this command will echo what you type'):
    embed = discord.Embed(title=f"{content}", timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.green())
    embed.set_footer(text=ctx.author.name , icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    embed = discord.Embed(title= ('{} just got slapped for {}'.format(slapped, reason)),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.red())
    embed.set_footer(text=ctx.author.name , icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.event
async def on_message_edit(ctx,message_before, message_after):
      
        author = message_before.author
        guild = message_before.guild.name
        channel = message_before.channel
        embed = discord.Embed(title=f"""original message was {message_before.content} new message is {message_after.content}"""  ,timestamp=datetime.datetime.utcnow(), 
        color=discord.Color.red())
        await ctx.send(embed=embed)










bot.run('ODI3MjE1NDU0MjM4MDE1NTk4.YGXybQ.fRp13Oxwr9iIolzwmevBVWBr4tg')
