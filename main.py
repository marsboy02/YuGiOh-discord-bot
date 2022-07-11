import os
import discord
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Selenium import *
from functions import backtick
from Handtrap import Urara, Warasi
from tier_deck_list.season5 import tier
from discord.ext import commands

# 크롤링 환경 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
URL = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action'

# 헤로쿠에서 토큰 값 받아오기
TOKEN = os.environ.get('TOKEN')

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
    embed.add_field(name="!와라시 가이드", value="와라시 명령어에 대한 가이드를 확인합니다.", inline=False)
    embed.add_field(name="!서치 [카드이름]", value="카드 이름을 입력하면 카드를 서치합니다.", inline=False)
    embed.set_footer(text="Summoned by 강형준#5876",
                     icon_url="https://uploads3.yugioh.com/card_images/3946/detail/5736.jpg?1385135416")
    await ctx.send(embed=embed)


# 카드 서칭 명령어
@bot.command()
async def 서치(ctx, arg):
    driver = webdriver.Chrome("CHROMEDRIVER_PATH")
    driver.get(url=URL)

    search_box = driver.find_element_by_id('keyword')
    search_box.send_keys(arg)
    search_box.send_keys(Keys.RETURN)

    time.sleep(1)
    string = ''
    # (driver.find_element_by_id('card_image_0_1').get_attribute("src")) 카드 이미지 링크

    string += '카드명:' + driver.find_element_by_id('card_image_0_1').get_attribute('alt') + '\n'
    string += '설명:' + driver.find_element_by_class_name("card_info_species_and_other_item").text + '\n'
    string += '속성:' + driver.find_element_by_class_name("box_card_attribute").text + '\n'
    string += '공격력:' + driver.find_element_by_class_name("atk_power").text + '\n'
    string += '수비력:' + driver.find_element_by_class_name("def_power").text + '\n'
    string += '효과:' + driver.find_element_by_xpath(
        "//dl[@class='flex_1']/dd[@class='box_card_text c_text flex_1']").text

    await ctx.send(string)


# 우라라 리스트 명령어
@bot.command()
async def 와라시(ctx, arg):
    string = ''
    if arg == '가이드':
        string += '!와라시 [조회하고 싶은 덱] : 와라시 타이밍을 조회, ex)!와라시 드라이트론\n' \
                  '!와라시 리스트 : 와라시를 사용할 수 있는 목록을 불러옵니다.'

    elif arg == '리스트':
        for k in Warasi.keys():
            string += k + ' '

    else:
        if not arg in list(Warasi.keys()):
            string += '다시 입력해 주세요!'
        else:
            Warasi_list = Warasi.get(arg)
            # 와라시는 순위가 없음
            for i in range(len(Warasi_list)):
                string += Warasi_list[i] + '\n'

    await ctx.send(backtick(string))


@bot.command()
async def 어드민(ctx):
    await ctx.send(backtick("서버의 어드민은 {} 입니다.".format(ctx.guild.owner)))


@bot.command()
async def 우라라(ctx, arg):
    if arg == '가이드':
        string = '!우라라 [조회하고 싶은 덱]' + ': 우라라 타이밍을 조회, ex)!우라라 스파이랄\n' +\
                 '!우라라 주의사항' + ': 하루 우라라를 사용할 때의 주의 사항\n' +\
                 '!우라라 리스트' + ': 우라라를 사용할 수 있는 목록을 불러옵니다.\n' \
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

        if not arg in list(Urara.keys()):
            string += '다시 입력해 주세요!'
        else:
            Urara_list = Urara.get(arg)

            for i in range(len(Urara_list)):
                # 우라라 타이밍 리스트가 3개가 넘어가면 부가 설명으로 전환
                if i >= 3:
                    string += '부가 설명 : ' + Urara_list[i] + '\n'
                else:
                    string += str((i + 1)) + '순위 : ' + Urara_list[i] + '\n'

    await ctx.send(backtick(string))


@bot.command()
async def 티어덱(ctx):
    string = ''
    for i in range(len(tier)):
        string += f'{i + 1}티어 : '
        for j in range(len(tier[i])):
            string += tier[i][j] + ' '
        string += '\n'

    await ctx.send(backtick(string))


bot.run(TOKEN)
