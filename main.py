import discord
from discord.ext import commands
import datetime 
import asyncio
from pretty_help import PrettyHelp, Navigation


bot = commands.Bot(command_prefix='>', description="BOT IS CODED BY THELINUX-USERCHOICE",help_command=PrettyHelp())

index_title = "welcome Octa-bot help"
no_category = "react emojis to go up down"

# custom ending note using the command context and help command formatters
ending_note = "coded by subodha prabash -{ctx.bot.user.name}\nFor command {help.clean_prefix}{help.invoked_with}"

# ":discord:743511195197374563" is a custom discord emoji format. Adjust to match your own custom emoji.
nav = Navigation("✔")
color = discord.Color.gold()

bot.help_command = PrettyHelp(index_title=index_title,no_category=no_category,navigation=nav, color=color, active_time=20, ending_note=ending_note)

@bot.command(name='ping',help='this command can bot s latency')
async def ping(ctx):  
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    embed = discord.Embed(title=f"Ping.. Pong ..latency is {round(bot.latency * 1000)} ms", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.set_thumbnail(url="https://i.postimg.cc/BnQyPrMx/tenor.gif")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(name='sum',help='this command will sums numbers what you insert')
async def sum(ctx, numOne: int, numTwo: int):
    output = (numOne + numTwo)
    embed = discord.Embed(title=f"Sum is {output}", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.set_thumbnail(url="https://i.postimg.cc/vBM5csvy/tenor.gif")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(name='serverinfo',help='you can get your server info with this')
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
  sender = ctx.author.name
  embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed) 




@bot.event
async def on_ready():
  while True:
     await bot.change_presence(activity=discord.Game(name="USE >help"))
     await asyncio.sleep(4)
     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="USE >help"))
     await asyncio.sleep(4)
     await bot.change_presence(activity=discord.Streaming(name="USE >help", url='https://www.twitch.tv/accountname'))
     await asyncio.sleep(4)
     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="USE >help"))
    




@bot.command(name='clear', help='this command will clear messages ask author for permission')
async def clear(ctx, amount:int,static=1):
 if ctx.author.id == 780400901553782824 :   
  
    await ctx.channel.purge(limit=amount)
    author = ctx.author.name
    await ctx.send(f"`CLEARED`{amount}`MESSAGES...BY `{author} ")
 else:
    await ctx.send('`You do not have permission to delete this messages`')      
    

@bot.command(name='print',help='echo what you types')
async def print(ctx, *, content:str):
    embed = discord.Embed(title=f"{content}", timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.green())
    sender = ctx.author.name
    embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command(name='slap',help='fun command to slap your friend')
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    embed = discord.Embed(title= ('{} `just got slapped for` {}'.format(slapped, reason)),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.red())
    sender = ctx.author.name
    embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(name='greet',help='greet your boss :smile:')
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
  emoji = '\N{THUMBS UP SIGN}'
  await message.add_reaction(emoji)









@bot.command(name='hack',help='hack the nasa babe!')
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
  emoji = '\N{THUMBS UP SIGN}'
  await message.add_reaction(emoji)


    
 
@bot.command(name='iptrack',help='tracks any ip instantly')
async def iptrack(ctx, ip: str):
 from requests import get
 track = get(f'https://ipapi.co/{ip}/json/')
 traced = (track.json())
 embed = discord.Embed(title=":small_red_triangle:IP TRACKER:small_red_triangle_down: ", description="**project on my github** :pirate_flag:", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
 embed.set_thumbnail(url="https://i.postimg.cc/XvWHrS3d/tenor.gif")
 sender = ctx.author.name
 embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
 embed.add_field(name=f"Results for ip - {ip} ", value=f"```py\n{traced}```")
 await ctx.send(embed=embed)
    
@bot.command(name='invite',help='invite this bot to your server')
async def invite(ctx):
    embed = discord.Embed(title=":red_circle: `INVITE ME TO YOUR SERVER` :red_circle:", description="**USE BELOW LINK**", timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
    embed.add_field(name="`INVITE LINK`", value="`Octa-bot`")
    embed.add_field(name='||https://discord.com/api/oauth2/authorize?client_id=827215454238015598&permissions=8&scope=bot||',value=":heart:  `from Octa-bot`")
    embed.set_thumbnail(url="https://i.postimg.cc/v82LkP8r/tenor.gif")
    sender = ctx.author.name
    embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed) 
    
@bot.command(name='angry',help='report command on Octa-bot')
async def angry(ctx, members: commands.Greedy[discord.Member], *, reason='bad personality'):
    slapped = ", ".join(x.name for x in members)
    embed = discord.Embed(title= ('{} was reported for {}'.format(slapped, reason)),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.red())
    embed.set_thumbnail(url="https://i.postimg.cc/8c7SrwMb/813436939738677267.gif")
    embed.set_footer(text=ctx.author.name , icon_url=ctx.author.avatar_url)
    embed.add_field(name="Pease ping @moderator to report this guy", value="```py\nDo not use this as a joke because if you unnecessary used this you will get kicked or banned by server owner/admin/mod {this command is for your safety and democracy!}```")
    await ctx.send(embed=embed)    
    
@bot.command(name='google',help='search it! :hehe:')
async def google(ctx,content:str): 
 message = await ctx.send("`if this didn't donot gives a output donot worry , it means there is no such wikis on you requested.`")
 await asyncio.sleep(5)
 await message.edit(content="`tip=try using same but different{synonyms}`")
  
 import wikipedia
 txt =  wikipedia.summary(f"{content}",sentences=2)
 embed = discord.Embed(title=":small_red_triangle:GOOGLE:small_red_triangle_down: ", description="**Just google it! but sometimes it doesn't give you output it means there i no wiki of you requested**" , timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
 embed.set_thumbnail(url="https://i.postimg.cc/437ZyXkS/tenor.gif")
 sender = ctx.author.name
 embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
 embed.add_field(name=f"Results for {content} ", value=f"```py\n{txt}```")
 await ctx.send(embed=embed)    
    
    

bot.run('ODI3MjE1NDU0MjM4MDE1NTk4.YGXybQ.fRp13Oxwr9iIolzwmevBVWBr4tg')
