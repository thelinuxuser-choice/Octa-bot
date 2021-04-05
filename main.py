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
async def greet(ctx,content:str):
  import asyncio
  message = await ctx.send("`starting greetings `:smile:")
  await asyncio.sleep(3)
  await message.edit(content="`h`")
  await asyncio.sleep(1)
  await message.edit(content="`he`")
  await asyncio.sleep(1)
  await message.edit(content="`hel`")
  await asyncio.sleep(1)
  await message.edit(content="`hell`")
  await asyncio.sleep(1)
  await message.edit(content="`hello`")
  await asyncio.sleep(1)
  await message.edit(content="`hellow`")
  await asyncio.sleep(1)
  await message.edit(content=f"`hellow`{content} `hope you are good!`")

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
      import asyncio
      from requests import get
      track = get(f'https://ipapi.co/{ip}/json/')
      traced = (track.json())
      await ctx.send(f"```py\ntracked ip is\n{traced}```")
      message = await ctx.send("[:octopus:]`USE my github link for more tools link will be display in 10 seconds`")
      await asyncio.sleep(10)
      await message.edit(content="**https://github.com/thelinuxuser-choice/**")



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



@bot.command()
async def hack(ctx):
  import asyncio
  message = await ctx.send("[:octopus:]`hacking the NASA`")
  await asyncio.sleep(3)
  await message.edit(content="[:key:]**IP FOUND!**")
  await asyncio.sleep(3)
  await message.edit(content="[:warning:] `DDOSING the ip of NASA {127.0.0.1}`")
  await asyncio.sleep(3)
  await message.edit(content="[:sos:]**Deploying botnets and sending 'weareanonymous' in tcp packets...**")
  await asyncio.sleep(4)
  await message.edit(content="> successfully taken down the nasa website now corps will come for ya!")
  await asyncio.sleep(4)
  await message.edit(content="[:wave:]**exiting tor nodes ....**")








bot.run('ODI3MjE1NDU0MjM4MDE1NTk4.YGXybQ.fRp13Oxwr9iIolzwmevBVWBr4tg')
