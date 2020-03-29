import discord
from discord.ext import commands
import random
import time

client = discord.Client()
bot = commands.Bot(command_prefix="&&")

#Prints to terminal when the bot is ready
@bot.event
async def on_ready():
    print("Gregg is connected and online")
    await bot.change_presence(activity=discord.Game(name="Euthanize me nyaa~ UwU"))

#Replies to a user with status
@bot.command(pass_context=True)
async def ping(ctx):
    #await message.delete(ctx.message)
    before = time.monotonic()
    message = await ctx.send("Cunt")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"My ping to discord is {int(ping)}ms")

@bot.command(pass_context=True)
async def status(ctx):
    await ctx.send("Beep boop, I'm alive and pulling cones")

#Calls somebody a nigg
@bot.command()
async def nigg(ctx, name):
    pasta = "███░░░░██░██░░██████░░░██████░░███████░██████░\n████░░░██░██░██░░░░░░░██░░░░░░░██░░░░░░██░░░██\n" \
            "██░██░░██░██░██░░░███░██░░░███░█████░░░██████░\n██░░██░██░██░██░░░░██░██░░░░██░██░░░░░░██░░░██\n" \
            "██░░░████░██░░██████░░░██████░░███████░██░░░██\n"
    await ctx.send("That " + name + " kid? What a fucken")
    await ctx.send(pasta)

#Calls a random image from e621
@bot.command()
async def e6(ctx):
    postNum = str(random.randint(1,1899693))
    await ctx.send("https://e621.net/post/show/" + postNum)


#Luke terror generator
@bot.command()
async def lukeSCP(ctx):
    path =  "C:/Users/Jono/Desktop/Gregg/"
    roll = random.randint(1,100)
    roll2 = 0
    state = " "
    if roll > 75:
        state = "Keter"
        roll2 = random.randint(1, 11)
    elif roll > 40:
        state = "Euclid"
        roll2 = random.randint(1, 10)
    else:
        state = "Safe"
        roll2 = random.randint(1, 15)
    finalPath = path + state + "/" + str(roll2) + ".png"
    await ctx.send("Object class: " + state)
    await ctx.send(file=discord.File(finalPath))

@bot.command()
async def creeper(ctx, count):
    path = "C:/Users/Jono/Desktop/Creeper/"
    for i in range(0, int(count)):
        tempPath = path + str(i + 1) + ".png"
        print(tempPath)
        await ctx.send(file=discord.File(tempPath))

@bot.command()
async def clown(ctx):
    await ctx.send("AppleSkies: My account is still on there with too many details. You will easily find me as I was head of an Rp club with a very popular girlfriend. Pretty renown. I even knew the game makers. Kinda been my secret for weeks. So no")

@bot.command()
async def lexi(ctx):
    await ctx.send("Oi you broke my legs you fat cunt")
    await ctx.send("Shutting down")
    exit()

'''
@bot.command()
async def prime(ctx):
    #time.sleep(120)
    await ctx.send('"<@Twalaght#6063>" faggot lmao')
'''

bot.run("NTQyMzU2NzI3OTU0NDA3NDQ0.XP5xKQ.seKkUgj8O5u8qt5ycLqdPTxUnYk")


