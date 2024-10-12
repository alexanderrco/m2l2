import discord 
from discord.ext import commands 


intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


residuos = {
    "papel": "Reciclaje (papel)",
    "plástico": "Reciclaje (plástico)",
    "vidrio": "Reciclaje (vidrio)",
    "orgánico": "Desecho (orgánico)",
    "metal": "Reciclaje (metal)",
    "residuos peligrosos": "Desecho (peligroso)",
    "ropa": "Reciclaje o donación",
}


@bot.command(name='clasificar')
async def clasificar(ctx, tipo_residuo: str):
    tipo_residuo = tipo_residuo.lower()
    respuesta = residuos.get(tipo_residuo, "Lo siento, no reconozco ese tipo de residuo.")
    await ctx.send(respuesta)


@bot.command(name='tipos')
async def tipos(ctx):
    tipos_residuos = ', '.join(residuos.keys())
    await ctx.send(f"Tipos de residuos que puedo clasificar: {tipos_residuos}")


@bot.event
async def on_ready():
    print(f'Bot {bot.user} ha iniciado sesión.')


bot.run('token')
