import discord
from discord.ext import commands
import random

# Bot token'inizi buraya ekleyin
TOKEN = 'TOKEN GİR'

# Intents ayarını yapıyoruz
intents = discord.Intents.default()
intents.message_content = True

# Botu oluşturuyoruz
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yaptım')

@bot.command(name='yazıtura')
async def yazitura(ctx):
    sonuc = random.choice(["Yazı", "Tura"])
    await ctx.send(f'{ctx.author.mention}, Sonuç: **{sonuc}**!')

@bot.command(name='tahmin')
async def tahmin(ctx, tahmin: int):
    if tahmin < 1 or tahmin > 10:
        await ctx.send(f'{ctx.author.mention}, lütfen 1 ile 10 arasında bir sayı tahmin edin.')
    else:
        dogru_sayi = random.randint(1, 10)
        if tahmin == dogru_sayi:
            await ctx.send(f'{ctx.author.mention}, Tebrikler! Doğru tahmin ettiniz: **{dogru_sayi}** 🎉')
        else:
            await ctx.send(f'{ctx.author.mention}, Maalesef yanlış. Doğru cevap: **{dogru_sayi}**.')

bot.run(TOKEN)
