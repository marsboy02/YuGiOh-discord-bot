from data import Token
from HandTrap import Urara
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name}이 연결 되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command(name="안녕")
async def Hello(ctx):
    await ctx.send('{}님, 반갑습니다.'.format(ctx.author.mention))


@bot.event
async def on_message(message):
    if message.author.bot:
        return None

    await bot.process_commands(message)


@bot.command(name="명령어")
async def Commands(ctx):
    embed = discord.Embed(title="TG 하이퍼 라이브러리언 명렁어 목록", description="마스터 듀얼에 도움이 되는 명렁어들이 있습니다!", color=0x32A4FF)
    embed.set_thumbnail(url="https://uploads3.yugioh.com/card_images/3946/detail/5736.jpg?1385135416")
    embed.add_field(name="!안녕", value="TG 하이퍼 라이브러리언과 인사합니다", inline=False)
    embed.add_field(name="!우라라", value="우라라 타이밍을 조회합니다.", inline=False)
    embed.add_field(name="!티어덱", value="티어덱을 조회합니다.", inline=False)
    embed.set_footer(text="Summoned by 강형준#5876", icon_url="https://uploads3.yugioh.com/card_images/3946/detail/5736.jpg?1385135416")

    await ctx.send(embed=embed)


@bot.command(name="우라라 목록")
async def UraraList(ctx):
    await ctx.send(list(Urara.keys()))


@bot.command(name="우라라")
async def Urara(ctx, args):
    await ctx.send(list(Urara[args]))


@bot.command(name="티어덱")
async def Tier(ctx):
    await ctx.send("티어덱 조회가 끝났습니다.")

bot.run(Token)
