import discord
#from data import Token
from HandTrap import Urara
from discord.ext import commands

# Intents 명시
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name}이 연결 되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command()
async def 안녕(ctx):
    await ctx.send('{}님, 반갑습니다.'.format(ctx.author.mention))


@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title="TG 하이퍼 라이브러리언 명렁어 목록", description="마스터 듀얼에 도움이 되는 명렁어들이 있습니다!", color=0x32A4FF)
    embed.set_thumbnail(url="https://uploads3.yugioh.com/card_images/3946/detail/5736.jpg?1385135416")
    embed.add_field(name="!안녕", value="TG 하이퍼 라이브러리언과 인사합니다", inline=False)
    embed.add_field(name="!티어덱", value="마스터듀얼 티어덱을 조회합니다.", inline=False)
    embed.add_field(name="!어드민", value="서버 어드민을 확인합니다.", inline=False)
    embed.add_field(name="!우라라 가이드", value="우라라 명령어에 대한 가이드를 확인합니다.", inline=False)
    embed.set_footer(text="Summoned by 강형준#5876",
                     icon_url="https://uploads3.yugioh.com/card_images/3946/detail/5736.jpg?1385135416")

    await ctx.send(embed=embed)


@bot.command()
async def 어드민(ctx):
    await ctx.send("서버의 어드민은 {} 입니다.".format(ctx.guild.owner))


@bot.command()
async def 우라라(ctx, arg):
    if arg == '가이드':
        string = '!우라라 [조회하고 싶은 덱] : 우라라 타이밍을 조회, ex)!우라라 스파이랄\n' \
                 '!우라라 주의사항 : 하루 우라라를 사용할 때의 주의 사항\n' \
                 '!우라라 리스트 : 우라라를 사용할 수 있는 목록을 불러옵니다.\n' \
                 '해당 명령어는 \'마스터듀얼 갤러리\'의 \'마스터듀얼정보글\' 님의 게시글을 참고했습니다!'

    elif arg == '주의사항':
        string = '여기 적혀져 있는 순위는 모든 상황에 국한된 것이 아닙니다!\n' \
                 '상대 덱의 용병 카드나 패 필드/묘지/제외 존에 있는 카드의 영향을 무시한\n' \
                 '보편적으로 효과가 있는 상황에서의 순위입니다! 그 점 참고 해 주세요!\n\n'

        string += '주의사항 : 1턴에 1번 제약이 없는 효과에 우라라 던지지 않기\n' \
                  '주의사항 : 하루 우라라의 효과를 무시할 수 있는 카드거나 효과 무효를 무시하는 카드가 있는데 우라라 던지지 않기'

    elif arg == '리스트':
        string = '우라라 타이밍 조회가 가능한 덱 리스트 :\n'
        for k in Urara.keys():
            string += k + ' '

    else:
        string = ''
        Urara_list = Urara.get(arg)
        for i in range(len(Urara_list)):
            string += str((i + 1)) + ' 순위 : ' + Urara_list[i] + '\n'

    await ctx.send(string)


@bot.command()
async def 티어덱(ctx):

    await ctx.send("티어덱 조회가 끝났습니다.")


bot.run(process.env.TOKEN)
