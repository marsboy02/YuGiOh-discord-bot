from data import Token
from HandTrap import Urara
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

intro = open('YuGiOh-discord-bot/intro.txt', 'r', encoding="UTF8")
contents = intro.read()
@bot.event
async def on_ready():
    print(f'{bot.user.name}이 연결 되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command(name="안녕")
async def Hello(ctx):
    await ctx.send('{}, 안녕'.format(ctx.author.mention))


@bot.command(name="명령어")
async def Commands(ctx):
    embed = discord.Embed(title="명렁어 목록", description="포뮬러 싱크론", color=0x32A4FF)
    embed.set_thumbnail(url="https://uploads3.yugioh.com/card_images/3946/detail/5736.jpg?1385135416")
    embed.add_field(name="!안녕", value="TG 하이퍼 라이브러리언과 인사합니다", inline=False)
    embed.add_field(name="!우라라", value="우라라 타이밍을 조회합니다.", inline=False)
    embed.set_footer(text="Summoned by 강형준#5876", icon_url="https://uploads3.yugioh.com/card_images/3946/detail/5736.jpg?1385135416")

    await ctx.send(embed=embed)


@bot.command(name="우라라")
async def Handtrap(ctx):
    await ctx.send("끝!")

bot.run(Token)
