import discord
from discord.ext import commands
import youtube_dl
import time


def is_admin(ctx):
    allowed_roles = ["Admin"]    
    user_roles = [role.name for role in ctx.author.roles]
    return any(role in allowed_roles for role in user_roles)

intents = discord.Intents.default()
intents.messages = True  
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} olarak bağlandı!')
    await bot.change_presence(activity=discord.Game(name="!bilgi"))
    

@bot.command()
async def cal(ctx, url):
    channel = ctx.author.voice.channel
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name=channel.name)

    if not bot.voice_clients:
        vc = await voice_channel.connect()
    else:
        vc = bot.voice_clients[0]

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        vc.play(discord.FFmpegPCMAudio(url2), after=lambda e: print('done', e))

@bot.command()
async def ayril(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def merhaba(ctx):
    await ctx.send('Merhaba!')
    

@bot.command()
@commands.check(is_admin)
async def at(ctx, member: discord.Member, *, reason="Sebep belirtilmedi"):
    await member.kick(reason=reason)
    await ctx.send(f'{member.display_name} başarıyla atıldı. Sebep: {reason}')
    

@bot.command()
@commands.check(is_admin)
async def sustur(ctx, member: discord.Member, duration: int = None, *, reason="Sebep belirtilmedi"):
    muted_role = discord.utils.get(ctx.guild.roles, name="Susturulmuş")

    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Susturulmuş")

        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, send_messages=False)

    await member.add_roles(muted_role, reason=reason)

    if duration:
        await ctx.send(f'{member.display_name} başarıyla susturuldu. Sebep: {reason}, Süre: {duration} saniye')
        await time.sleep(duration)
        await member.remove_roles(muted_role, reason="Süre doldu")
    else:
        await ctx.send(f'{member.display_name} başarıyla susturuldu. Sebep: {reason}')
        

@bot.command()
@commands.check(is_admin)
async def yasakla(ctx, member: discord.Member, *, reason="Sebep belirtilmedi"):
    await member.ban(reason=reason)
    await ctx.send(f'{member.display_name} başarıyla yasaklandı. Sebep: {reason}')


@bot.command()
@commands.check(is_admin)
async def temizle(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'{amount} mesaj başarıyla temizlendi.')
    

@bot.command()
async def bilgi(ctx, member: discord.Member = None):
    member = member or ctx.author

    embed = discord.Embed(title=f'{member.display_name} Hakkında Bilgiler', color=member.color)
    embed.add_field(name='Katılım Tarihi', value=member.joined_at.strftime('%d.%m.%Y %H:%M:%S'))
    embed.add_field(name='Discord\'a Katılma Tarihi', value=member.created_at.strftime('%d.%m.%Y %H:%M:%S'))
    embed.add_field(name='Roller', value=', '.join([role.name for role in member.roles]))

    await ctx.send(embed=embed)


@bot.command()
async def yardim(ctx):
    embed = discord.Embed(title="Yardım Komutları", color=discord.Color.blue())

    embed.add_field(name="!merhaba", value="Merhaba mesajı atar.", inline=False)
    embed.add_field(name="!at <kullanıcı> [sebep]", value="Kullanıcıyı sunucudan atar.", inline=False)
    embed.add_field(name="!sustur <kullanıcı> [süre] [sebep]", value="Kullanıcıyı belirtilen süreyle susturur.", inline=False)
    embed.add_field(name="!yasakla <kullanıcı> [sebep]", value="Kullanıcıyı sunucudan yasaklar.", inline=False)
    embed.add_field(name="!temizle <mesaj sayısı>", value="Belirtilen miktarda mesajı temizler.", inline=False)
    embed.add_field(name="!bilgi [kullanıcı]", value="Belirtilen kullanıcının bilgilerini gösterir.", inline=False)
    embed.add_field(name="!ping", value="Botun gecikmesini ms cinsinden gösterir.", inline=False)
    embed.add_field(name="!avatar [kullanıcı]", value="Belirtilen kullanıcının avatarını gösterir.", inline=False)
    embed.add_field(name="!yaz [metin]", value="Girilen metini Botun yazmasını sağlar", inline=False)
    embed.add_field(name="!kullanıcılar", value="Sunucudaki tüm kullanıcıların adını gösterir.", inline=False)
    embed.add_field(name="!sesli [metin]", value="Girilen metini Botun sesli olarak okumasını sağlar", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Bot gecikmesi: {latency}ms')

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    user = member if member is not None else ctx.author
    await ctx.send(user.avatar_url)


@bot.command()
async def yaz(ctx, *, metin: str):
    await ctx.send(metin)


@bot.command()
async def kullanıcılar(ctx):
    members = ', '.join([member.name for member in ctx.guild.members])
    await ctx.send(f"Sunucudaki Kullanıcılar: {members}")


@bot.command()
async def sesli(ctx, *, metin: str):
    await ctx.send(f"{ctx.author.mention} sesli diyor: {metin}", tts=True)


# Botun token'ını ekleyin
bot.run('Token')
