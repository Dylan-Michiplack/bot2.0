import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def calculadora(ctx,operacion:str,num1:int,num2:int):
    if operacion=="suma":
        resultado= num1 + num2
        await ctx.send(f"el resultado es,{resultado}")
    if operacion=="resta":
        resultado= num1 - num2
        await ctx.send(f"el resultado es,{resultado}")
    if operacion=="multiplicacion":
        resultado= num1 * num2
        await ctx.send(f"el resultado es,{resultado}")
    if operacion=="division":
        if num2!= 0:
            resultado= num1 * num2
            await ctx.send(f"el resultado es,{resultado}")
        else:
            await ctx.send("no seas pendejo , esudia mejor")

    else:
        await ctx.send("los parametros no son correctos")
