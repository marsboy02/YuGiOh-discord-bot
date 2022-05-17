from data import Token
import Haru
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

intro = open('YuGiOh-discord-bot/intro.txt', 'r', encoding="UTF8")
contents = intro.read()
@bot.event
async def on_ready():
    print(f'{bot.user.name}이 연결 되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command()
async def 안녕(ctx):
    await ctx.send('{}, 안녕'.format(ctx.author.mention))


@bot.command()
async def 명령어(ctx):
    await ctx.send(contents)


@bot.command()
async def 우라라(ctx, *, text):
    if text in Haru:
        deck = Haru.text
        await ctx.send("{}이 당신이 원하는 덱인가요?",deck)
    else:
        await ctx.send("{}이 발견되지 않았습니다!", text)
    await ctx.send(text)

bot.run(Token)
